from dataclasses import dataclass

values = input("Enter the grade1,grade2,grade3").split()
grade1, grade2, grade3 = map(float, values)
print(grade1, grade2, grade3)


@dataclass
class finalGrades:
    @classmethod
    def averageGrade() -> float:
        return (grade1 + grade2 + grade3) / 3

    @staticmethod
    def check(self) -> str:
        average = self.averageGrade()
        if average >= 7:
            return "Pass"
        elif average < 4:
            return "Fail"
        else:
            return "Recovery"

    @property
    def compute(self):
        print(self.check(self))


if __name__ == "__main__":
    result = finalGrades()
    result.compute
