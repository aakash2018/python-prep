from dataclasses import dataclass

height = float(input("Enter Your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))


@dataclass
class calculateBmi:
    @classmethod
    def calculate(cls) -> float:
        return weight / (height**2)

    @staticmethod
    def checkBmi(bmi: float) -> str:
        if bmi < 18.5:
            return "UnderWeight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        elif bmi < 35:
            return "Obese"
        else:
            return "Severely obese"

    @property
    def compute(self) -> float:
        return self.calculate()


if __name__ == "__main__":
    result = calculateBmi()
    print(result.calculate())
    print("Your BMI is:", result.compute)
    print("Category:", result.checkBmi(result.compute))
