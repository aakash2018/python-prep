from dataclasses import dataclass


@dataclass
class seperateWord:
    word: str

    @staticmethod
    def checkSeperate(word):
        for letter in word:
            print(letter)


if __name__ == "__main__":
    word = input("Enter a word: ")
    obj = seperateWord(word)
    seperateWord.checkSeperate(obj.word)
