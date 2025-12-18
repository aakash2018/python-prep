1. Generative an infinite fibonnaci series by using a generators

```def fibonacci():
	a,b =0,1
	while True:
		yield a
		a,b=b,a+b

f1 = fibonacci()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
```
2. Sort a list without Using a sort keyword
```
list1=[41,2,12,6,35,8,10,1,19]
n = len(list1)
for i in range(n):
	for j in range(i+1,n):
		if list1[i]>list1[j]:
		list1[i],list1[j] = list1[j],list[i]

print(list1)
```
3. Weite a code to check whether a string is palindrome or not ?

```
s="nitin"
if s == s[::-1]:
	print("yes palindrome")
else:
	print("No")

#Alternative
n=len(s)
x=0
for i in range(n):
	if s[i]!=s[n-i-1]:
		x=1
		break
if x==0:
	print("Yes Palindrome")
else:
	print("No")

```
4. sort a dictionary / bu using dict Comprehension
```
dict = { 575:"Apple",876:"Mongo",132:"Graphes",782:"Banana"}

d = sorted(dict1.keys())
dict2 = {}
for i in d:
	dict2[i] = dict1[i]
print(dict2)

#alternate method
dict2 = {key:value for key,value in sorted(dict1.items(),key=lambdax:x[1])}
```
5. Find the pair with given number in A list
```
list1 = [8,7,2,5,3,1]
n = len(list1)
k=10
for i in range(n):
	for j in range(i+1,n):
		if list1[i]+list1[j]==k:
			print(list1[i],list1[j])

```
6. create a fibonnaci series using recursion
```def recur_fibo(n):
 if n <= 1:
 	return n
 else:
   return(recur_fibo(n-1) + recur_fibo(n-2))

 nterms = int(input("How many terms? "))

 if nterms < =0:
   print("Please enter a positive integer")
 else:
   for i in range(nterms):
   	print(recur_fibo(i))

```
7. find the required output
```
s = "this sky is blue"
l = s.split()
l = l[::-1]
l = ' '.join(l)
print(l)

#another program
str1 = "/*apples are & found% only @red & green"
s = ''
for i in str1:
 if((i>='A' and i<='Z') | (i>='a' and i<='z') | (i=='')):
 	s=s+i
print(s)
```
8. find the maximum repeated character in a string without having On2 complexity
```
s= "itininiytnnhhn"
ch ={}
for i in s:
	if i in ch:
		ch[i]+=1
	else:
		ch[i]=1
max_char = max(ch,key=ch.get)
print(max_char)
```
9. find the maximum and minimum value from a list without using any predefined function
```
l =[9,11,0,370,55,40,2]
maximum = l[0]
minimum = l[0]

for i in l:
 if i > maximum:
 	maximum = i
 if i < minimum:
 	minimum = i
print("maximum:",maximum)
print('minimum:',minimum)
```
10. Write a code to raise an exception
```
l =[1,2,3,4]
sum =0
for i in l:
	if i==1:
	raise Exception("Exception: 1 is foun")
	else:
	 sum+=i
```
11. Find the difference between list,tuple and array 
12. what do yo mean by lambda function. explain with example
13. Explain list function - Append() and extend()
14. How Exception is handlrd in python ?
15. Explain decorator in detail
    - what do you mean by decorator
    - how you create customised decorator
    - how you create parameterized decorator
    - how you will add 2 number using decorator
    - example  of decorator
16. what do you mean by abstraction. How you define abstract class or function by using  abstraction
17. what do you mean by MRO ?
18. what do you mean by gil ?
19. what if we don't use "with" statement ?
20. what is the difference between static and class method ?


