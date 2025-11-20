import math

radius = float(input("Enter the radius of the sphere:"))

class volumeOfSphere:
    def __init__(self,radius):
        self.radius = radius
    def calculate(self):
        return (4/3) * math.pi * radius ** 3
    def compute(self):
            return {
                "volume":round(self.calculate(),3)
            }
result = volumeOfSphere(radius)
print("The volume of the sphere is:", result.compute())