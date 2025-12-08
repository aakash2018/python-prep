from dataclasses import dataclass


@dataclass
class ConcatWords:
    word1: str
    word2: str

    def getStringValue(self):
        result = self.word1 + self.word2
        print("Concatenated word:", result)


if __name__ == "__main__":
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    obj = ConcatWords(word1, word2)
    obj.getStringValue()
