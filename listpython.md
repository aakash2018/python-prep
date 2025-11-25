Create a list: my_list = [1, 2, 3, 4, 5]
Create list from iterable: list(range(5))
Access element by index: element = my_list[0]
Access last element: last = my_list[-1]
Slicing: sub_list = my_list[1:4]
Slicing with step: every_second = my_list[::2]
Reverse list with slicing: reversed_list = my_list[::-1]
Append element: my_list.append(6)
Extend list: my_list.extend([7, 8, 9])
Insert element: my_list.insert(2, 10)
Remove element: my_list.remove(3)
Remove element at index: del my_list[2]
Pop element: popped = my_list.pop()
Pop element at index: popped = my_list.pop(2)
Clear list: my_list.clear()
Index of element: index = my_list.index(4)
Count occurrences: count = my_list.count(2)
Sort list in-place: my_list.sort()
Sort list descending: my_list.sort(reverse=True)
Sort list with key: my_list.sort(key=abs)
Reverse list in-place: my_list.reverse()
Copy list: new_list = my_list.copy()
Shallow copy: import copy; shallow_copy = copy.copy(my_list)
Deep copy: import copy; deep_copy = copy.deepcopy(my_list)
List comprehension: squares = [x**2 for x in range(10)]
Conditional list comprehension: evens = [x for x in my_list if x % 2 == 0]
Nested list comprehension: matrix = [[i*j for j in range(5)] for i in range(5)]
Map function to list: doubled = list(map(lambda x: x*2, my_list))
Filter list: evens = list(filter(lambda x: x % 2 == 0, my_list))
Check if item in list: is_present = 3 in my_list
Get length of list: length = len(my_list)
Get max value: max_val = max(my_list)
Get min value: min_val = min(my_list)
Sum of list: total = sum(my_list)
Join list of strings: joined = " ".join(["Hello", "World"])
Split string to list: my_list = "Hello World".split()
Zip lists: zipped = list(zip([1, 2, 3], ['a', 'b', 'c']))
Unzip lists: nums, letters = zip(*zipped)
Enumerate list: for index, value in enumerate(my_list):
List from enumerated: indexed = list(enumerate(my_list))
Flatten list of lists: flattened = [item for sublist in matrix for item in sublist]
Create list with repeated elements: repeated = [0] * 5