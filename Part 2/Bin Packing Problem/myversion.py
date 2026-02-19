import pulp
from pathlib import Path

here = Path(__file__).resolve().parent
file_path = here / "Schwerin1_BPP1.txt"

with open(file_path, "r") as file:
    lines = [line.strip() for line in file if line.strip()]

m = int(lines[0])                   # number of items
C = int(lines[1])                   # bin capacity
s = [int(x) for x in lines[2:]]     # item weights list

print("m =", m)
print("C =", C)
print("first 10 weights:", s[:10])

assert len(s) == m, f"Expected {m} weights, got {len(s)}"

I = range(m)   # items
B = range(m)   # bins (upper bound)

x = pulp.LpVariable.dicts("x", (I, B), cat="Binary")
y = pulp.LpVariable.dicts("y", B, cat="Binary")

model = pulp.LpProblem("Bin_Packing_Problem", pulp.LpMinimize)

model += pulp.lpSum(y[b] for b in B), "Total_Bins_Used"

for i in I:
    model += pulp.lpSum(x[i][b] for b in B) == 1, f"AssignItem_{i}"

for b in B:
    model += pulp.lpSum(s[i] * x[i][b] for i in I) <= C * y[b], f"CapacityBin_{b}"

solver = pulp.PULP_CBC_CMD(msg=True)
model.solve(solver)

print("Status:", pulp.LpStatus[model.status])
bins_used = sum(int(pulp.value(y[b])) for b in B)
print("Bins used:", bins_used)

for b in B:
    if pulp.value(y[b]) > 0.5:
        items_in_bin = [i for i in I if pulp.value(x[i][b]) > 0.5]
        load = sum(s[i] for i in items_in_bin)
        print(f"Bin {b}: load={load}/{C}, items={items_in_bin}")