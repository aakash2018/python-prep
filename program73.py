class replaceAandE:
    def __init__(self, sentence):
        self.sentence = sentence

        self.new_sentence = sentence.replace("a", "e")
        print("Modified sentence:", self.new_sentence)


if __name__ == "__main__":
    sentence = input("Enter a sentence")

    obj = replaceAandE(sentence)
