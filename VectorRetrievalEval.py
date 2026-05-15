import json
from retievalmetrics import Metrics
import numpy as np

class VectorRetrievalEval:
    def __init__(self) -> None:
        with open('strategy_a.json', "r", encoding="utf-8") as f:
            self.data_stra = json.load(f)
        
        with open('strategy_b.json', "r", encoding="utf-8") as f:
            self.data_strb = json.load(f)
        
        self.metrics = Metrics()
    

    def compare_techniques(self, k: int = 3):

        
        print(f"\nDataset 1 size: {len(self.data_stra)} samples")
        print(f"Dataset 2 size: {len(self.data_strb)} samples")
        
        print(f"\n{'='*60}")
        print(f"EVALUATION RESULTS (K={k})")
        print(f"{'='*60}")
        
        metrics1 = self.metrics.evaluate_dataset(self.data_stra, k)
        metrics2 = self.metrics.evaluate_dataset(self.data_strb, k)
        
        print(f"\n{'Metric':<20} {'Technique 1':<15} {'Technique 2':<15} {'Difference':<15}")
        print(f"{'-'*65}")
        
        for metric in ['Recall@K', 'Precision@K', 'MRR', 'NDCG@K']:
            val1 = metrics1[metric]
            val2 = metrics2[metric]
            diff = val2 - val1
            diff_str = f"+{diff:.4f}" if diff > 0 else f"{diff:.4f}"
            winner = "✓" if diff > 0 else "✗"
            
            print(f"{metric:<20} {val1:<15.4f} {val2:<15.4f} {diff_str:<15} {winner}")
        
        avg_improvement = np.mean([
            metrics2['Recall@K'] - metrics1['Recall@K'],
            metrics2['Precision@K'] - metrics1['Precision@K'],
            metrics2['MRR'] - metrics1['MRR'],
            metrics2['NDCG@K'] - metrics1['NDCG@K']
        ])
        
        print(f"\n{'='*60}")
        if avg_improvement > 0:
            print("✓ Technique 2 performs BETTER overall")
        else:
            print("✓ Technique 1 performs BETTER overall")
        print(f"{'='*60}")
        
        return metrics1, metrics2

if __name__ == "__main__":
    
    a = VectorRetrievalEval()
    a.compare_techniques()
        
    
