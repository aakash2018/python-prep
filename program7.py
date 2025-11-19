import math

radius = float(input("Enter the radius of Circle"))

class radiusCircle:
    def __init__(self,radius):
        self.radius = radius
    def compute(self):
        return math.pi * self.radius ** 2
   
area = radiusCircle(radius)
print(f"the area of circle {area.compute():.2f}")

