from dataclasses import dataclass

values = input("Enter the persons age").split()

while len(values) < 3:
    values.append(0)

age1, age2, age3 = map(int, values[:3])
print("Values are:", age1, age2, age3)


@dataclass
class isLegalAge:
    @classmethod
    def checkAge(cls) -> int:
        count = 0
        if age1 >= 18:
            count += 1
        if age2 >= 18:
            count += 1
        if age3 >= 18:
            count += 1
        return count

    @property
    def compute(self):
        return isLegalAge.checkAge()


if __name__ == "__main__":
    result = isLegalAge()
    print(result.compute)


"""
समझ लो: classmethod क्यों?

classmethod object पर नहीं चलता, वह क्लास पर चलता है।

इसलिए:

self की जगह → cls

इसका काम है ऐसा लॉजिक करना जो instance पर depend न करे।


Bina self use kiye class ke variable use karne ke liye classmethod banate hai.
is me self ki place per cls(class) hoti hai

| Method Type     | `self`? | `cls`? | Instance Variables? |
| --------------- | ------- | ------ | ------------------- |
| instance method | ✔ yes   | ❌ no   | ✔ yes               |
| classmethod     | ❌ no    | ✔ yes  | ❌ no                |
| staticmethod    | ❌ no    | ❌ no   | ❌ no                |


Instance Variable क्या होता है?

जब आप किसी class से object बनाते हो, उस object के अंदर जो data store होता है, उसे instance variable कहते हैं।

ये variable:

self के साथ लिखे जाते हैं

हर object के लिए अलग value रखते हैं

एक object बदले तो दूसरे object पर असर नहीं पड़ता




`@staticmethod` Python में एक **method होता है जो class से bağlı होता है लेकिन object (instance) पर depend नहीं करता**.

इसे ऐसे समझो:

---

# ⭐ **Static Method क्या होता है?**

Static method वो function है जो **class के अंदर होता है**,
लेकिन:

* उसे `self` (instance) की ज़रूरत नहीं होती
* उसे `cls` (class) की ज़रूरत नहीं होती
* बस एक **normal function** जैसा behave करता है
* लेकिन logically class से related होता है

Static method को call करने के 2 तरीके हैं:

* `ClassName.method()`
* `object.method()` (possible है, लेकिन recommended नहीं)

---

# 🎯 Static Method का सही Use कब होता है?

जब function:

* ना instance variable use करे
* ना class variable use करे
* बस एक utility/helper काम करे

Example:

* age validate करना
* string format करना
* कोई calculation जो instance पर depend न हो

---

# ✔ Example 1 — Simple static method

```python
class MathOps:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOps.add(5, 7))
```

✔ कोई `self` नहीं
✔ कोई `cls` नहीं
✔ बस एक function है जो class के अंदर रखा गया है

---

# ✔ Example 2 — Static method inside dataclass

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    @staticmethod
    def is_adult(age):
        return age >= 18

p = Person("Aakash", 20)

print(Person.is_adult(p.age))
```

---

# 🔥 Classmethod vs Staticmethod vs Instance Method

| Type                | Access          | Uses `self`? | Uses `cls`? | Usage                 |
| ------------------- | --------------- | ------------ | ----------- | --------------------- |
| **Instance Method** | object instance | ✔ Yes        | ❌ No        | object-specific logic |
| **Class Method**    | class           | ❌ No         | ✔ Yes       | class-level logic     |
| **Static Method**   | class           | ❌ No         | ❌ No        | utility logic         |

---

# 📌 Quick Summary

`@staticmethod` एक ऐसा method है:

* जिसे class के अंदर रखा जाता है
* जो class/instance पर dependent नहीं होता
* जिसे बिना object बनाए भी call कर सकते हो
* बस एक **utility function** जैसा होता है

---

अगर चाहो, मैं static method में गलतियाँ और best practices भी examples से समझा सकता हूँ।


"""
