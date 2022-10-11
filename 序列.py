Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
[1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
(1,2,3) + (4,5,6)
(1, 2, 3, 4, 5, 6)
"1,2,3"+"4,5,6"
'1,2,34,5,6'
"123"+"456"
'123456'
[1,2,3]*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
(1,2,3)*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
"123"*3
'123123123'
a = [1,2,3]
id(a)
4336412736
a*=2
a
[1, 2, 3, 1, 2, 3]
id(a)
4336412736
b = (1,2,3)
id(b)
4344055872
b*=2
b
(1, 2, 3, 1, 2, 3)
id(b)
4344007840
x = "See"
y = "See"
x i s y
SyntaxError: invalid syntax
x is y
True
x = [1,2,3]
y = [1,2,3]
x is y
False
x = (1,2,3)
y = (1,2,3)
x is y
False
"6" in "666"
True
"6" not in "666"
False
x = [1,2,3,4,5]
del x
x
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x
NameError: name 'x' is not defined
x = [1,2,3,4,5]
del x[1:4]
x
[1, 5]
x = [1,2,3,4,5]
x[1:4] = []
x
[1, 5]
y = [1,2,3,4,5]
del y[::2]
y
[2, 4]
y = [1,2,3,4,5]
y[::2]=[]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    y[::2]=[]
ValueError: attempt to assign sequence of size 0 to extended slice of size 3
x = [1,2,3,4]
x.clear()
x
[]
y = [1,2,3,4,5]
del y[0:5]
y
[]
y = [1,2,3]
del y[:]
y
[]
list "magic"
SyntaxError: invalid syntax
list("magic")
['m', 'a', 'g', 'i', 'c']
list((1,2,3,4,5))
[1, 2, 3, 4, 5]
tuple("magic")
('m', 'a', 'g', 'i', 'c')
tuple([1,2,3])
(1, 2, 3)
str((1,2,3,4))
'(1, 2, 3, 4)'
str([1,2,3])
'[1, 2, 3]'
a = [1,2,3]
a(min)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a(min)
TypeError: 'list' object is not callable
min(a)
1
a = ["magic"]
min(a)
'magic'
max(a)
'magic'
a = "magic"
min(a)
'a'
max(a)
'm'
min(1,2,3,4,5)
1
s = []
min(x)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    min(x)
ValueError: min() arg is an empty sequence
min(x,default="啥也没有")
'啥也没有'
len(range(2**100))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    len(range(2**100))
OverflowError: Python int too large to convert to C ssize_t
a = [1,2,3,4]
sum(a)
10
sum(a,strat=100)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sum(a,strat=100)
TypeError: 'strat' is an invalid keyword argument for sum()
sum(a,start=100)
110
s = [4,2,1,5,2]
sorted(s)
[1, 2, 2, 4, 5]
s
[4, 2, 1, 5, 2]
sorted(s,reverse=True)
[5, 4, 2, 2, 1]
t = ["Apple","Banana","Branch","Fake"]
sorted(t)
['Apple', 'Banana', 'Branch', 'Fake']
sorted(t,key=len)
['Fake', 'Apple', 'Banana', 'Branch']
a = ((3,1,4,2))
sorted(a)
[1, 2, 3, 4]
sorted("daskv")
['a', 'd', 'k', 's', 'v']
a = [1,2,3,4]
reverse(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    reverse(a)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
reversed(a)
<list_reverseiterator object at 0x10337ffd0>
list(reversed(a))
[4, 3, 2, 1]
a
[1, 2, 3, 4]
a.reverse()
a
[4, 3, 2, 1]
list(a.reverse())
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list(a.reverse())
TypeError: 'NoneType' object is not iterable
list(reversed("fucking"))
['g', 'n', 'i', 'k', 'c', 'u', 'f']
list(reversed(range(1,11)))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
t = ["Apple","Banana","Branch","Fake"]
t.sort(key=len)
t
['Fake', 'Apple', 'Banana', 'Branch']
x = [1,2,3]
y = [1,0,2]
all(x)
True
all(y)
False
any(x)
True
any(y)
True
season = ["spring","summer","autumn","winter"]
enumerate(season)
<enumerate object at 0x1006ff780>
list(enumerate(season))
[(0, 'spring'), (1, 'summer'), (2, 'autumn'), (3, 'winter')]
list(enumerate(season,10))
[(10, 'spring'), (11, 'summer'), (12, 'autumn'), (13, 'winter')]
x = [1,2,3]
y = [4,5,6]
zipped = zip(x,y)
list(zipped)
[(1, 4), (2, 5), (3, 6)]
z = ["Magic"]
zipped = zip(x,y,z)
list(zipped)
[(1, 4, 'Magic')]
z = [7,8,9]
list(x,y,z)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list(x,y,z)
TypeError: list expected at most 1 argument, got 3
zipped = zip(x,y,z)
list(zipped)
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
z = ["Magic"]
zipped=zip(x,y,z)
list(zipped)
[(1, 4, 'Magic')]
import itertools
zipped = itertools.zip_longest(x,y,z)
list(zipped)
[(1, 4, 'Magic'), (2, 5, None), (3, 6, None)]
mapped = map(ord,"Magic")
list(mapped)
[77, 97, 103, 105, 99]
mapped = map(pow,[2,3,4],[2,3,4])
list(mapped)
[4, 27, 256]
mapped = map(pow(2,2),pow(3,3),pow(4,4))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    mapped = map(pow(2,2),pow(3,3),pow(4,4))
TypeError: 'int' object is not iterable
[pow(2,2),pow(3,3),pow(4,4)]
[4, 27, 256]
mapped = map(max,[1,2,3],[4,5,6],[0,2,3,4])
list(mapped)
[4, 5, 6]
list(filter(str.islower,"Magic"))
['a', 'g', 'i', 'c']
list(filter(str.isupper,"Magic"))
['M']
x = [1,2,3,4,5]
y = iter(x)
type(x)
<class 'list'>
type(y)
<class 'list_iterator'>
next(y)
1
next(y)
2
next(y)
3
next(x)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    next(x)
TypeError: 'list' object is not an iterator
next(y)
4
next(y)
5
next(y)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    next(y)
StopIteration
z = iter(x)
next(z,"无了")
1
next(z,"无了")
2
next(z,"无了")
3
next(z,"无了")
4
next(z,"无了")
5
next(z,"无了")
'无了'
