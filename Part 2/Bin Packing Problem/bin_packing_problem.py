import pulp

m = 1  # number of items
I = range(1, m + 1)  # Set of items
s_i = [] # size of item i for i in I
for i in Schwerin1_BPP1.txt

C = 1000
n = m  # number of bins (can be set to m in worst case)
B = range(1, n + 1)  # Set of bins

# Decision variable: =1 if item i is placed in bin b, =0 otherwise
x = pulp.LpVariable.dicts(name="x", indices=(I, B), cat="Binary")
myModel = pulp.LpProblem(name="Bin_Packing_Problem", sense=pulp.LpMinimize)

# Objective: Minimize number of bins used
y = pulp.LpVariable.dicts(name="y", indices=B, cat="Binary")
myModel += pulp.lpSum(y[b] for b in B), "Total_Bins_Used"

# Constraint: Each item must be placed in exactly one bin
for i in I:
    myModel += pulp.lpSum(x[i][b] for b in B) == 1, f"Item_{i}_Placement"

# Constraint: The total size of items in each bin cannot exceed its capacity
for b in B:
    myModel += pulp.lpSum(s_i[i] * x[i][b] for i in I) <= C * y[b], f"Bin_{b}_Capacity"    

myModel.solve()
print(myModel)