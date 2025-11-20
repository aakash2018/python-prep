space_variation = float(input("Enter the space variation (S):"))
time_variation = float(input("Enter the time variation (t):"))

class averageVelocity:
	def __init__(self,space,time):
		self.space = space
		self.time = time
	def calculateVelocity(self):
		 return self.space/self.time
	def compute(self):
          return {
            "averagevelocity":self.calculateVelocity()
            }
        
result = averageVelocity(space_variation,time_variation)
print("The average velocity is:",result.compute())