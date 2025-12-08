from dataclasses import dataclass


@dataclass
class letterStartWithA:
    name: str

    def checkName(self):
        if self.name.startswith("A"):
            print("The name starts with 'A'.")
        else:
            print("The name does not start with 'A'.")


if __name__ == "__main__":
    name = input("Enter a name")
    obj = letterStartWithA(name)
    obj.checkName()
