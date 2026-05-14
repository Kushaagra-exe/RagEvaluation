from synthetic_generation import Queries
from helper import ingest
import json 

class GenerateQueries:

    def __init__(self , path) -> None:
        
        self.generator = Queries()

        self.chunks = ingest(path=path, chunk_size=500, overlap_size=10)

        self.generated = []
    
    def generate(self):
        for chunk in self.chunks:
            qna = self.generator.generate(chunk.page_content)
            self.generated.append({
                'question':qna.question,
                'answer': qna.answer
            })

        gen = json.dumps(
                self.generated,
                indent=2
            )
        with open('validation.json', 'w') as f:
            f.write(gen)


if __name__ == '__main__':
    g = GenerateQueries('Quantum computing.txt')
    g.generate()