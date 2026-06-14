class Chai:
    temperature = "hot"
    strength = "Strong"
    

cutting = Chai()
print(cutting.temperature)
cutting.temperature ="Mild"
# cutting.cup = "small"
# print("cup size is",cutting.cup)
print("After changing",cutting.temperature)
print("Direct look into the class",Chai.temperature)

del cutting.temperature
print(cutting.temperature)
# del cutting.cup
# print(cutting.cup)
