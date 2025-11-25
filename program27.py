from dataclasses import dataclass

nums = list(map(float, input("Enter numbers: ").split()))


@dataclass
class showAscending:
    nums: list

    @property
    def compute(self) -> list:
        return sorted(self.nums)


if __name__ == "__main__":
    result = showAscending(nums)
    print(result.compute)
    print(__name__)


"""
Ye raha **short and easy Hindi note** on `__name__` aur `__main__`:

---

# 📝 **Short Note in Hindi**

Python har file ko ek special variable `__name__` deta hai, jisme us file ka naam store hota hai.
Agar file **seedha run** ki jaati hai, to Python `__name__` ko `"__main__"` set karta hai.
Lekin agar file **import** ki jaati hai, to `__name__` us file ka asli naam hota hai.

Iska use hum isliye karte hain taaki kuch code sirf tab chale jab file directly run ho, import karne par na chale.

```python
if __name__ == "__main__":
    # yeh code sirf direct run par chalega
```

---

Agar chaho to mai 2-line version bhi de sakta hoon.
"""
