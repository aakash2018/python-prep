from dataclasses import dataclass

num1 = int(input("Enter num 1 "))
num2 = int(input("Enter num 2 "))
num3 = int(input("Enter num 3 "))


@dataclass
class largestNum:
    num1: int
    num2: int
    num3: int

    def getLargest(self):
        return max(self.num1, self.num2, self.num3)


result = largestNum(num1, num2, num3)
print(f"larget number is {result.getLargest()}")


"""Python में -> (arrow) sign का इस्तेमाल function या method की return type बताने के लिए किया जाता है। इसे type hinting कहते हैं, जिससे code पढ़ने वालों को यह पता चलता है कि यह function किस type का value return करेगा।[1][3]

## Arrow Sign का मतलब

- जब आप लिखते हैं:
  ```python
  def get_largest(self) -> int:
  ```
  इसका मतलब है कि यह function एक integer value return करेगा, यानी output integer होगा।[3]

## कहां-कहां इस्तेमाल कर सकते हैं

- Simple functions में:
  ```python
  def add(a: int, b: int) -> int:
      return a + b
  ```
- Class methods में:
  ```python
  class Example:
      def get_name(self) -> str:
          return self.name
  ```
- Constructor में भी:
  ```python
  def __init__(self) -> None:
      # initialization code
  ```
- कोई भी function या method जिसमें आप बताना चाहते हैं कि result किस type का होगा।[3]

इससे code ज्यादा साफ, readable और भविष्य में error कम हो जाते हैं, क्योंकि static type checkers इसका इस्तेमाल type errors पकड़ने में कर सकते हैं।[1][3]
"""

"""
Python में @dataclass एक class decorator है जिसका उपयोग डेटा-क्लासेस बनाने के लिए किया जाता है। इसका मुख्य उद्देश्य क्लास को आसान और साफ-सुथरा बनाना है, जिससे boilerplate code (जैसे __init__, __repr__, __eq__ आदि methods) अपने आप generate हो जाते हैं। 

## @dataclass कहाँ और क्यों उपयोग होती है

- जब आप किसी class को केवल data attributes (जैसे num1, num2, num3) रखने के लिए बनाना चाहते हैं, तो @dataclass इसे बहुत सरल बनाता है क्योंकि यह automatically init method और अन्य special methods जोड़ देता है।
- इसका उपयोग immutable classes (जिनमें फ़ील्ड्स को बदलना न हो, frozen=True option के साथ) बनाने के लिए भी किया जाता है।
- यह code को readable, maintainable और compact बनाता है, खासकर जब data को पास करना और compare करना होता है।
- बड़े प्रोजेक्ट्स में data models या value objects के लिए अक्सर उपयोग किया जाता है।

## उदाहरण
```python
from dataclasses import dataclass

@dataclass
class Numbers:
    num1: int
    num2: int
    num3: int
```
इस example में, class के लिए init, repr, eq आदि methods अपने आप बन जाएंगे, जिससे आप सीधे इस class का इस्तेमाल values को store, compare, या print करने के लिए कर सकते हैं।

इस प्रकार, @dataclass decorator classes को ज्यादा efficient और कम कोड के साथ define करने के लिए उपयोगी होता है.[2][3][6]

"""
