import pulp


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
shifts = ["Morning", "Evening"]
smurfs = ["Papa", "Smurfette", "Brainy", "Grouchy", "Clumsy"]

x = pulp.LpVariable.dicts(name="x", indices=(days, shifts, smurfs), cat="Binary")

myModel = pulp.LpProblem(name="Smurf_Scheduling", sense=pulp.LpMinimize)

# Objective: Minimize number of smurfs
myModel += pulp.lpSum(x[day][shift][smurf] 
                      for day in days 
                      for shift in shifts 
                      for smurf in smurfs), "Total_Smurfs"


print(myModel)