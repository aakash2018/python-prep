from dataclasses import dataclass
import math

# try:
#     num1, num2, num3 = map(float, input("Enter the num1 num2 and num3 ").split())
# except ValueError:
#     print("Error: you must enter 3 numbers seperated by space")
# -----------------------------------------------
# values = input("Enter the value of num1, num2 and num3: ").split()

# if len(values) != 3:
#     print("Error: Please enter exactly 3 values")
# else:
#     num1, num2, num3 = map(float, values)
#     print("Values are:", num1, num2, num3)

# ----------------------------------------------
values = input("Enter the value of num1, num2 and num3: ").split()

# Fill missing values with 0
while len(values) < 3:
    values.append("0")

num1, num2, num3 = map(float, values[:3])
print("Values are:", num1, num2, num3)

# nums = list(map(float, input("Enter numbers: ").split()))


@dataclass
class isPositive:
    num1: int
    num2: int
    num3: int

    @property
    def compute(self) -> str:
        sum = self.num1 + self.num2 + self.num3
        nums = math.copysign(1, sum)
        return "Positive" if nums == 1 else "Negative"


# result = isPositive(nums[0], nums[1], nums[2])
# print(result.compute)

result = isPositive(num1, num2, num3)
print(result.compute)


"""
`@property` Python का एक **special decorator** है जो किसी method को **variable की तरह access** करने की सुविधा देता है।

मतलब:

👉 Method लिखते हो
👉 लेकिन उसे call ऐसे करते हो जैसे **attribute हो**, बिना `()` लगाए

---

# ⭐ `@property` kya karta hai?

`@property` kisi method ko **getter** बना देता है।

* Method **function की तरह चलता है**
* लेकिन दिखता **variable की तरह** है

---

# 🎯 Simple Example (Without @property)

```python
class Person:
    def get_age(self):
        return 25

p = Person()
print(p.get_age())   # function call
```

---

# ⭐ Same Example With @property

```python
class Person:
    @property
    def age(self):
        return 25

p = Person()
print(p.age)    # no brackets!
```

✔ Method run होता है
✔ लेकिन access ऐसे होता है जैसे variable `age`

---

# 💡 क्यों useful है?

* code clean दिखता है
* object का data calculate करके return करना हो
* future में logic बदले तो भी access pattern same रहता है
* Encapsulation maintain होता है

---

# ✔ Example — Computed Property

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area)
```

✔ area एक method है
✔ लेकिन हम इसे variable की तरह access करते हैं

---

# ⭐ Setter + Getter (Advanced)

`@property` सिर्फ getter है
Setter इस तरह बनता है:

```python
class Person:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

---

# 📌 Short Summary

| Concept       | Meaning                                 |
| ------------- | --------------------------------------- |
| `@property`   | Method को variable-like access बनाता है |
| No brackets   | `p.age` instead of `p.age()`            |
| Clean code    | बेहतर readability                       |
| Encapsulation | अंदर logic बदल सकते हैं, access same    |

---

अगर चाहो, मैं `@property` + dataclass वाला example या real-world use cases भी समझा दूँ।
"""
