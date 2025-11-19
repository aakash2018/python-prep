print("enter the three quadratic point")

a = float(input("Enter the coefficient a:"))
b = float(input("Enter the coefficient b:"))
c = float(input("Enter the coefficient c:"))

class quadraticEquation:
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
	def compute(self):
		return b**2 - 4*a*c

result = quadraticEquation(a,b,c)

print("the delta of the quadratic equation is :", result.compute());