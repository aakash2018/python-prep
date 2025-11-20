import math

x1 = float(input("Enter the x-coordinate of point 1:"))
y1 = float(input("Enter the y-coordinate of point 1:"))

x2 = float(input("Enter the x-coordinate of point 2:"))
y2 = float(input("Enter the y-coordinate of point 2:"))

class distance:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def calculate(self):
        return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    def compute(self):
            return {
                "distance":round(self.calculate(),2)
            }
result = distance(x1,y1,x2,y2)
print("The distance between the two point is:",result.compute())