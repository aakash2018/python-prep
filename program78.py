from dataclasses import dataclass


@dataclass
class diaplayAmountBlankSpace:
    sentence: str

    def counting(self):
        count = 0

        for char in sentence:
            if char == " ":
                count += 1
        print("Number of blank spaces:", count)


if __name__ == "__main__":
    sentence = input("Enter a sentence")
    obj = diaplayAmountBlankSpace(sentence)
    obj.counting()
