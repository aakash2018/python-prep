from dataclasses import dataclass


@dataclass
class splitFullName:
    names: str

    def breakName(self):
        name = self.names.split()
        last_name = name[1]

        print("First name:", last_name)


if __name__ == "__main__":
    full_name = input("Enter your full name:")
    obj = splitFullName(full_name)
    obj.breakName()
