import json

with open("benchmarks.json", "r") as f:
    data = json.load(f)

strategy_a_better = 0
strategy_b_better = 0
equal_count = 0

for key, strategies in data.items():

    avg_a = sum(item["score"] for item in strategies["strategy_a"]) / len(strategies["strategy_a"])
    avg_b = sum(item["score"] for item in strategies["strategy_b"]) / len(strategies["strategy_b"])

    print(f"\nKey: {key}")
    print(f"Strategy A Average = {avg_a:.2f}")
    print(f"Strategy B Average = {avg_b:.2f}")

    if avg_a < avg_b:
        print("Better Strategy: strategy_a")
        strategy_a_better += 1
    elif avg_b < avg_a:
        print("Better Strategy: strategy_b")
        strategy_b_better += 1
    else:
        print("Both strategies are equal")
        equal_count += 1

print("\n=== Summary ===")
print(f"strategy_a better: {strategy_a_better}")
print(f"strategy_b better: {strategy_b_better}")
print(f"equal: {equal_count}")