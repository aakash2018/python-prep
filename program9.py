width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))

class perimeterRectangle:
	def __init__(self,width,length):
		self.width = width
		self.length = length
	def perimeter(self):
		return 2 * (self.width + self.length)
	def area(self):
		return self.width * self.length

result = perimeterRectangle(width,length)

print("Perimeter of the rectangle:",result.perimeter())
print("Area of the rectangle:",result.area())