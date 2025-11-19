side_a = float(input("Enter the length of side a:"))
side_b = float(input("Enter the length of side b:"))
side_c = float(input("Enter the length of side c:"))
height = float(input("Enter the height relative to side b:"))

class perimeterOfTriangle:
    def __init__(self,side_a,side_b,side_c,height):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.height = height
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    def area(self):
        return (self.side_b * height) //2
    
result = perimeterOfTriangle(side_a,side_b,side_c,height)

print("Perimeter of the triangle:",result.perimeter())
print("Area of the triangle:",result.area())