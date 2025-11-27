from dataclasses import dataclass
import datetime

birth = int(input("Enter the year of birth: "))


@dataclass
class ableToVote:
    year_of_birth: int  # instance variable

    @classmethod
    def isCheck(cls) -> int:
        current_year = datetime.datetime.now().year
        age = current_year - birth
        return age

    @property
    def compute(self) -> str:
        checkAge = self.isCheck()
        print(checkAge)
        if checkAge >= 16:
            return "You are eligible to vote!"
        else:
            return "You are not eligible to vote yet."


if __name__ == "__main__":
    result = ableToVote(birth)
    print(result.compute)
