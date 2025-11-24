from dataclasses import dataclass

PASSING_MARKS = 6

grade1 = float(input("Enter the grade of the first test: "))
grade2 = float(input("Enter the grade of the first test: "))


@dataclass
class averageGrade:
    grade1: int
    grade2: int

    def calculate(self):
        self.average = (grade1 + grade2) / 2
        if self.average >= PASSING_MARKS:
            print("The student passed with an average of", self.average)
        else:
            print("The student failed with an average of", self.average)


result = averageGrade(grade1, grade2)
result.calculate()
