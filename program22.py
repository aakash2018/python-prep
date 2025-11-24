from dataclasses import dataclass

PASSING_MARKS = 6

score1 = int(input("Enter the score1 "))
score2 = int(input("Enter the score2 "))


@dataclass
class reportCard:
    score1: int
    score2: int

    def checkReport(self) -> str:
        if score1 >= PASSING_MARKS:
            print("The student passed the first test.")
        else:
            print("The student failed the first test.")

        if score2 >= PASSING_MARKS:
            print("The student passed the second test.")
        else:
            print("The student failed the second test.")


result = reportCard(score1, score2)
result.checkReport()
