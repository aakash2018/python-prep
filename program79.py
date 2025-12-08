from dataclasses import dataclass


@dataclass
class countVowels:
    word: str
    vowels = ["a", "e", "i", "o", "u"]

    def counting(self):
        count = 0

        for char in self.word:
            if char.lower() in self.vowels:
                count += 1

        print("Number of vowels:", count)


if __name__ == "__main__":
    word = input("Enter a word: ")
    obj = countVowels(word)
    obj.counting()
