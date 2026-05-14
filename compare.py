import json

with open("benchmarks.json", "r") as f:
    data = json.load(f)

strategy_a_better = 0
strategy_b_better = 0
equal_count = 0

md_lines = ["# Benchmark Results - shows avg Eucledian distance of retieved docs for each strategy\n"]

for key, strategies in data.items():

    avg_a = sum(item["score"] for item in strategies["strategy_a"]) / len(strategies["strategy_a"])
    avg_b = sum(item["score"] for item in strategies["strategy_b"]) / len(strategies["strategy_b"])

    print(f"\nKey: {key}")
    print(f"Strategy A Average = {avg_a:.2f}")
    print(f"Strategy B Average = {avg_b:.2f}")

    md_lines.append(f"## {key}")
    md_lines.append(f"- Strategy A Average: **{avg_a:.2f}**")
    md_lines.append(f"- Strategy B Average: **{avg_b:.2f}**")

    if avg_a < avg_b:
        print("Better Strategy: strategy_a")
        md_lines.append("- Better Strategy: **strategy_a**")
        strategy_a_better += 1

    elif avg_b < avg_a:
        print("Better Strategy: strategy_b")
        md_lines.append("- Better Strategy: **strategy_b**")
        strategy_b_better += 1

    else:
        print("Both strategies are equal")
        md_lines.append("- Both strategies are equal")
        equal_count += 1

    md_lines.append("")

print("\n=== Summary ===")
print(f"strategy_a better: {strategy_a_better}")
print(f"strategy_b better: {strategy_b_better}")
print(f"equal: {equal_count}")

md_lines.append("## Summary")
md_lines.append(f"- strategy_a better: **{strategy_a_better}**")
md_lines.append(f"- strategy_b better: **{strategy_b_better}**")
md_lines.append(f"- equal: **{equal_count}**")

with open("benchmark.md", "w") as f:
    f.write("\n".join(md_lines))

print("\nbenchmark.md file created successfully.")