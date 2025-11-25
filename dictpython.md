Create a dictionary: my_dict = {'a': 1, 'b': 2, 'c': 3}
Create dict from list: my_dict = dict(a=1, b=2, c=3)
Create dict from list of tuples: my_dict = dict([('a', 1), ('b', 2), ('c', 3)])
Access value by key: value = my_dict['a']
Get value with default: value = my_dict.get('d', 0)
Add/update item: my_dict['d'] = 4
Update multiple items: my_dict.update({'e': 5, 'f': 6})
Remove item: del my_dict['b']
Pop item: value = my_dict.pop('c')
Pop item with default: value = my_dict.pop('e', None)
Remove and return item: item = my_dict.popitem()
Clear dictionary: my_dict.clear()
Get all keys: keys = my_dict.keys()
Get all values: values = my_dict.values()
Get all items: items = my_dict.items()
Copy dictionary: new_dict = my_dict.copy()
Shallow copy: import copy; shallow_copy = copy.copy(my_dict)
Deep copy: import copy; deep_copy = copy.deepcopy(my_dict)
Check if key exists: exists = 'a' in my_dict
Check if key not exists: not_exists = 'z' not in my_dict
Dictionary comprehension: squared = {x: x**2 for x in range(5)}
Conditional dict comprehension: even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
Merge dictionaries (Python 3.9+): merged = dict1 | dict2
Merge dictionaries (Python 3.5+): merged = {**dict1, **dict2}
Get length: length = len(my_dict)
Create dict from keys: new_dict = dict.fromkeys(['a', 'b', 'c'], 0)
Set default value: my_dict.setdefault('g', 7)
Get value or set default: value = my_dict.setdefault('h', 8)
OrderedDict: from collections import OrderedDict; ordered = OrderedDict()
Defaultdict: from collections import defaultdict; dd = defaultdict(int)
Invert dictionary: inverted = {v: k for k, v in my_dict.items()}
Sort by key: sorted_dict = dict(sorted(my_dict.items()))
Sort by value: sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
Filter dict: filtered = {k: v for k, v in my_dict.items() if v > 2}