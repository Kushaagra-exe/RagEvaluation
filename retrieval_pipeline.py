from rag import RAGPipeline
import json
import warnings
warnings.filterwarnings("ignore")

pipeline = RAGPipeline('Quantum computing.txt')


with open("validation.json", "r", encoding="utf-8") as f:
    data = json.load(f)

queries = [item["question"] for item in data]
print("No. of queries:", len(queries))
# print(queries)

# benchmark_results = {}

# for i, query in enumerate(queries, start=1):
#     print("working on Vector retreival")
#     print("working on query:", i)

#     benchmark_results[query] = {

#         "strategy_a":
#             pipeline.strategy_a(query),

#         "strategy_b":
#             pipeline.strategy_b(query)
#     }

# with open('benchmarks.json', 'w') as f:
#     f.write(json.dumps(
#         benchmark_results,
#         indent=2
#     ))


answer_result = {}

for i, query in enumerate(queries, start=1):
    print("working on Aanwer Generation")
    print("working on query:", i)

    answer_result = pipeline.combine_rag_strategies(query)

with open('answers.json', 'w') as f:
    f.write(json.dumps(
        answer_result,
        indent=2
    ))