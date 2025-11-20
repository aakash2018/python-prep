applied_force = float(input("Enter the applied force:"))
distance = float(input("Enter the distance traveled:"))

class workDone:
    def __init__(self,applied_force,distance):
        self.applied_force = applied_force
        self.distance = distance
    def compute(self):
        return self.applied_force * self.distance
        
result = workDone(applied_force,distance)
print("The work done by the force is:",result.compute())