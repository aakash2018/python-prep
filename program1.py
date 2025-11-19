print("ram")

print(1,2,3,sep='---')

print("hello","world",sep='***')

print("apple","banana","cherry",sep=' | ')

print("Python","Java","C++",sep=' <> ')

print("red","green","blue",sep=' ~ ')

print(21.5, 42.7, 3.14, sep=' -- ')

print(ord('A'), ord('B'), ord('C'), sep=' ++ ')

print("Monday","Tuesday","Wednesday",sep=' /// ')

print("cat","dog","mouse",sep=' *** ')

x=int(input("enter a value of a: "))
y=int(input("enter a value of b: "))

# print("the value of a and b is:",x,y,sep=' + ',end='=',x+y)
#   File "D:\python_prep\program1.py", line 24
#     print("the value of a and b is:",x,y,sep=' + ',end='=',x+y)
#                                                               ^
# SyntaxError: positional argument follows keyword argument

print(f'the value of a and b is: {x} + {y} = {x+y}')
print("the value of a and b is:",x,"+",y,"=",x+y)