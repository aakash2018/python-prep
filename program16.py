age = int(input("Enter your age."))


class validAge:
    def __init__(self, age):
        self.age = age

    def isValid(self):
        if age >= 18:
            print("you are of legal age.")
        else:
            print("you are not of legal age")


result = validAge(age)
result.isValid()
