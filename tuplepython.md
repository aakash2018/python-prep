Create: my_tuple = (1, 2, 3, 4, 5)
From list: tuple([1, 2, 3, 4, 5])
Single element: (42,)
Empty: ()
Access: element = my_tuple[0]
Negative index: last = my_tuple[-1]
Slice: sub_tuple = my_tuple[1:4]
Concat: new_tuple = my_tuple + (6, 7, 8)
Repeat: repeated = my_tuple * 3
Unpack: a, b, c = (1, 2, 3)
Unpack with *: a, *rest = (1, 2, 3, 4, 5)
Swap: a, b = b, a
Nested: nested = ((1, 2), (3, 4))
Count: my_tuple.count(2)
Index: my_tuple.index(3)
Length: len(my_tuple)
Max/min: max(my_tuple) / min(my_tuple)
Sum: sum(my_tuple)
Sort (returns list): sorted(my_tuple)
Map: mapped = tuple(map(lambda x: x * 2, my_tuple))
Any/all: any(my_tuple), all(my_tuple)