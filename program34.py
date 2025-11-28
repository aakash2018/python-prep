age = int(input("Enter your age"))


class Age:
    def __init__(self):
        self.age = age

    @staticmethod
    def category(age) -> str:
        if age <= 12:
            return "Child"
        elif age <= 17:
            return "Teenager"
        elif age <= 59:
            return "Adult"
        else:
            return "Elderly"


if __name__ == "__main__":
    result = Age()
    print(result.category(result.age))
