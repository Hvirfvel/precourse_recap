ski_resort = input("Where do you want to go skiing? ")
input_days = input("How many days do you want to go skiing? ")

ski_rental = 35
ski_pass = 39

def skiingCost(cost1, cost2, days):
  total_cost = (cost1 + cost2) * days
  print("The cost of your ski trip to", ski_resort, "is £", total_cost)

skiingCost(ski_rental, ski_pass, int(input_days))