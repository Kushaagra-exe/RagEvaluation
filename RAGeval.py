from rag import RAGPipeline
from langchain_core.prompts import PromptTemplate
import json
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
    answer_correctness
)

from datasets import Dataset
from helper import EmbeddingModel, get_llm
class Evaluator:
    def __init__(self) -> None:
        # self.rag_pipeline = RAGPipeline()
        self.embed = EmbeddingModel(model='baai').get()

        self.llm = get_llm(model='oss')
        
        
    
    def Ragasready(self, groundtruth='validation.json', retrieveddocs='benchmarks.json', answers='answers.json'):

        with open(groundtruth, "r", encoding="utf-8") as f:
            validation = json.load(f)

        with open(retrieveddocs, "r", encoding="utf-8") as f:
            benchmark = json.load(f)

        with open(answers, "r", encoding="utf-8") as f:
            answers = json.load(f)

        ground_truth_lookup = {
            item["question"]: item["answer"]
            for item in validation
        }

        strategies = set()

        for q_data in answers.values():
            strategies.update(q_data.keys())

        for strategy in strategies:
            output = []

            for query, strategy_answers in answers.items():

                ground_truth = ground_truth_lookup.get(query, "")

                contexts = []

                if query in benchmark and strategy in benchmark[query]:
                    contexts = [
                        item["document"]
                        for item in benchmark[query][strategy]
                    ]

                answer = strategy_answers.get(strategy, "")

                output.append({
                    "user_input": query,
                    "ground_truth": ground_truth,
                    "contexts": contexts,
                    "answer": answer
                })

            with open(f"{strategy}.json", "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2, ensure_ascii=False)

            print(f"Saved {strategy}.json")

    def useRagas(self, path):
        with open(path, "r") as f:
            data = json.load(f)

        dataset = Dataset.from_list(data)

        result = evaluate(
            dataset=dataset,
            metrics=[
                faithfulness,
                answer_relevancy,
                context_precision,
                context_recall,
                answer_correctness
            ],
            embeddings=self.embed,
            llm = self.llm
        )
        return result.to_pandas()
    

    def evaluation(self):
        # self.Ragasready()
        eval1 = self.useRagas('strategy_a.json')
        eval2 = self.useRagas('strategy_b.json')

        with open('benchmark.md', "a") as f:
            f.write("# First DataFrame\n\n")
            f.write(eval1.to_markdown(index=False))
            f.write("\n\n")

            f.write("# Second DataFrame\n\n")
            f.write(eval2.to_markdown(index=False))
            f.write("\n\n")




if __name__ == '__main__':
    a = Evaluator()
    a.evaluation()
    # def check_correctness(self, query, answer):
    #     pass
    


    # def check_correctness(self, query, answer):
    #     pass


    # def check_correctness(self, query, answer):
    #     pass


    # def check_correctness(self, query, answer):
    #     pass
    
    


