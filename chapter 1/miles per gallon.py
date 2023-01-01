import random

no_of_gallons = random.randint(10, 25)
miles = random.randint(200, 400)

MPG = miles // no_of_gallons
print("gallons of gas in the car's fuel tank",no_of_gallons,"\n miles it can travel on a full tank", miles)
print("MPG ", MPG)
