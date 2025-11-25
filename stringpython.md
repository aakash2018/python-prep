Create: my_string = "Hello, World!"
Multiline: """This is multiline"""
Raw: r"C:\Users\John"
F-string: f"Hello, {name}"
Access: char = my_string[1]
Slice: my_string[7:12]
Reverse: my_string[::-1]
Concat: "Hello" + " World"
Repeat: "Ha" * 3
Upper/lower: my_string.upper(), my_string.lower()
Capitalize/title/swapcase
Strip/lstrip/rstrip
Replace: my_string.replace("Hello", "Hi")
Split, splitlines
Join: "-".join(["a", "b", "c"])
Center/ljust/rjust
Starts/ends with
Find, rfind, index, rindex
Count: my_string.count("l")
Checks: isalpha, isdigit, islower, isupper, isspace, isprintable, isnumeric, isidentifier
Encode/decode
Remove prefix/suffix
Partition / rpartition
Translate: my_string.translate(str.maketrans('aeiou', '12345'))
Formatting: format(), f-string