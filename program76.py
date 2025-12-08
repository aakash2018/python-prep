from dataclasses import dataclass


@dataclass
class Anagram:
    word1: str
    word2: str

    def isAnagram(self):
        self.word1 = word1.lower().replace(" ", "")
        self.word2 = word2.lower().replace(" ", "")

        if len(self.word1) != len(self.word2):
            print("The second word is not an Anagram of the first.")
        else:
            sorted_word1 = sorted(word1)
            sorted_word2 = sorted(word2)

            if sorted_word1 == sorted_word2:
                print("The second word is an anagram of the first")
            else:
                print("The second word is not an anagram of the first")


if __name__ == "__main__":
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word:")

    obj = Anagram(word1, word2)
    obj.isAnagram()
