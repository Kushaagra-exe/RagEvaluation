from typing import List, Dict, Tuple
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np


class Metrics:
    def preprocess_text(self, text: str):
        stop_words = set(stopwords.words('english'))
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [
            token for token in tokens
            if token.isalnum() and token not in stop_words
        ]

        return set(tokens)

    def is_relevant(self, context: str, ground_truth: str, user_input: str,
                threshold: float = 0.5) -> bool:


        context_lower = context.lower()
        gt_lower = ground_truth.lower()

        if gt_lower in context_lower or context_lower in gt_lower:
            return True

        gt_words = self.preprocess_text(gt_lower)
        context_words = self.preprocess_text(context_lower)

        if len(gt_words) == 0 or len(context_words) == 0:
            return False

        overlap = len(gt_words & context_words) / len(gt_words)

        return overlap >= threshold
    

    def get_relevance_scores(self, contexts: List[str], ground_truth: str, user_input: str) -> List[int]:

        return [1 if self.is_relevant(ctx, ground_truth, user_input) else 0 
                for ctx in contexts]

    def recall_at_k(self, relevance_scores: List[int], k: int) -> float:

        if not relevance_scores:
            return 0.0
        
        total_relevant = sum(relevance_scores)
        if total_relevant == 0:
            return 0.0
        
        relevant_in_top_k = sum(relevance_scores[:k])
        return relevant_in_top_k / total_relevant

    def precision_at_k(self, relevance_scores: List[int], k: int) -> float:

        if k == 0 or not relevance_scores:
            return 0.0
        
        relevant_in_top_k = sum(relevance_scores[:k])
        return relevant_in_top_k / min(k, len(relevance_scores))

    def mrr(self, relevance_scores: List[int]) -> float:

        for i, score in enumerate(relevance_scores):
            if score == 1:
                return 1.0 / (i + 1)
        return 0.0

    def dcg_at_k(self, relevance_scores: List[int], k: int) -> float:

        dcg = 0.0
        for i in range(min(k, len(relevance_scores))):
            if relevance_scores[i] == 1:
                dcg += 1.0 / np.log2(i + 2)
        return dcg

    def idcg_at_k(self, relevance_scores: List[int], k: int) -> float:

        sorted_scores = sorted(relevance_scores, reverse=True)
        return self.dcg_at_k(sorted_scores, k)

    def ndcg_at_k(self, relevance_scores: List[int], k: int) -> float:

        idcg = self.idcg_at_k(relevance_scores, k)
        if idcg == 0:
            return 0.0
        return self.dcg_at_k(relevance_scores, k) / idcg

    def evaluate_dataset(self, dataset: List[Dict], k: int = 3) -> Dict[str, float]:
        metrics = {
            'recall': [],
            'precision': [],
            'mrr': [],
            'ndcg': []
        }
        for sample in dataset:
            contexts = sample['contexts']
            ground_truth = sample['ground_truth']
            user_input = sample['user_input']
            
            relevance_scores = self.get_relevance_scores(contexts, ground_truth, user_input)
            
            metrics['recall'].append(self.recall_at_k(relevance_scores, k))
            metrics['precision'].append(self.precision_at_k(relevance_scores, k))
            metrics['mrr'].append(self.mrr(relevance_scores))
            metrics['ndcg'].append(self.ndcg_at_k(relevance_scores, k))
        
        return {
            'Recall@K': np.mean(metrics['recall']),
            'Precision@K': np.mean(metrics['precision']),
            'MRR': np.mean(metrics['mrr']),
            'NDCG@K': np.mean(metrics['ndcg'])
        }