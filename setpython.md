Create set: my_set = {1, 2, 3, 4, 5}
Create set from list: my_set = set([1, 2, 3, 4, 5])
Create empty set: empty_set = set()
Add: my_set.add(6)
Update: my_set.update({7, 8, 9})
Remove: my_set.remove(3)
Discard: my_set.discard(10)
Pop: element = my_set.pop()
Clear: my_set.clear()
Copy: new_set = my_set.copy()
Shallow copy: import copy; shallow_copy = copy.copy(my_set)
Deep copy: import copy; deep_copy = copy.deepcopy(my_set)
Union: union_set = set1.union(set2)
Union operator: set1 | set2
Intersection: set1 & set2
Difference: set1 - set2
Symmetric difference: set1 ^ set2
Subset check: set1.issubset(set2)
Superset check: set1.issuperset(set2)
Disjoint: set1.isdisjoint(set2)
Frozen set: frozen = frozenset([1, 2, 3])
Set comprehension: even_set = {x for x in range(10) if x % 2 == 0}
Length: len(my_set)
Max/min: max(my_set) / min(my_set)
Sum: sum(my_set)