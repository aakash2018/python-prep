from dataclasses import dataclass


@dataclass
class palindrome:
    word: str

    def isReversed(self):
        self.reversed_word = self.word[::-1]

        if word == self.reversed_word:
            print("The word is a palindrome.")
        else:
            print("The word is not a palindrome.")


if __name__ == "__main__":
    word = input("Enter a word")
    obj = palindrome(word)
    obj.isReversed()
