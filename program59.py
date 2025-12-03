import math

x = float(input("Enter the value of x: "))
term = 1.0
sum = 1.0
n = 1

while abs(term) >= 0.001:
    term *= x / n
    sum += term
    n += 1

math_result = math.exp(x)

print("Result (custom calculation):", sum)
print("Result (math.exp): ", math_result)
