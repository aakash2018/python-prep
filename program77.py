from dataclasses import dataclass


@dataclass
class splitFullName:
    names: str

    def breakName(self):
        name = self.names.split()
        first_name = name[0]

        print("First name:", first_name)


if __name__ == "__main__":
    full_name = input("Enter your full name:")
    obj = splitFullName(full_name)
    obj.breakName()
