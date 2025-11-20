mass = float(input("Enter the mass of the object:"))
velocity = float(input("Enter the velocity of the object:"))

class kineticEnergy:
	def __init__(self,mass,velocity):
		self.mass = mass
		self.velocity = velocity
	def kineticEnergy(self):
		return (mass * velocity ** 2) / 2
	def compute(self):
            return {
                "kineticEnergy":self.kineticEnergy()
            }
result = kineticEnergy(mass,velocity)
print("The kineticc energy of the object is:",result.compute())