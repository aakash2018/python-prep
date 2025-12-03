import math

angle = float(input("Enter the angle in radius: "))
term = angle
sum = angle
n = 3

while abs(term) >= 0.0001:
    term *= -(angle**2) / ((n - 1) * n)
    sum += term
    n += 2

math_result = math.sin(angle)
print("Result (Custom Calculation):", sum)
print("Result (math.sin):", math_result)
