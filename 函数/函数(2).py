Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def myfuc(a,b,c):
    return "".join(c,b,a)

myfuc("我","打","人")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    myfuc("我","打","人")
  File "<pyshell#2>", line 2, in myfuc
    return "".join(c,b,a)
TypeError: str.join() takes exactly one argument (3 given)
def myfuc(a,b,c):
    return "".join((c,b,a))

myfuc("我","打","他")
'他打我'
myfuc(a = "我",b = "打",c = "他")
'他打我'
myfuc(a = "他","打","我")
SyntaxError: positional argument follows keyword argument
myfuc("他","打",c = "我")
'我打他'
myfuc("他",b = "打",c = "我")
'我打他'
def myfuc(a,b,c = "我"):
    return "".join((c,b,a))

myfuc("他","打")
'我打他'
myfuc("他","打","你")
'你打他'
help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

abs(-1.9)
1.9
abs(x = -1.9)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    abs(x = -1.9)
TypeError: abs() takes no keyword arguments
help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

sum(1.9,4)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    sum(1.9,4)
TypeError: 'float' object is not iterable
sum(4,4)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    sum(4,4)
TypeError: 'int' object is not iterable
sum([1,2,3],4)
10
sum([1,2,3],x = 4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    sum([1,2,3],x = 4)
TypeError: 'x' is an invalid keyword argument for sum()
sum([1,2,3],strat = 4)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    sum([1,2,3],strat = 4)
TypeError: 'strat' is an invalid keyword argument for sum()
sum([1,2,3],strat=4)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sum([1,2,3],strat=4)
TypeError: 'strat' is an invalid keyword argument for sum()
sum([1,2,3],start=4)
10
sum(x = [1,2,3],4)
SyntaxError: positional argument follows keyword argument
def abc(a,/,b,c):
    print(a,b,c)

    
abc(1,2,3)
1 2 3
abc(a=1,2,3)
SyntaxError: positional argument follows keyword argument
abc(1,b=2,c=3)
1 2 3
def log(a,*,b,c):
    print(a,b,c)

    
log(4,b=1,c=2)
4 1 2
log(a=4,b=1,c=2)
4 1 2
def fuc(*arg):
    print("有{}个参数".format(len(arg)))
    print("第二个参数是{}".format(arg[1]))

    
fuc("德","爱","施恩")
有3个参数
第二个参数是爱
def fuc(*arg):
    print(arg)

    
fuc(1,2,3,4,5)
(1, 2, 3, 4, 5)
def fuc():
    return 1,2,3

fuc()
(1, 2, 3)
def fuc(*arg):
    print(type(arg))

    
fuc(1,2,3)
<class 'tuple'>
def myfuc(*arg,b,c):
    print(arg,b,c)

    
myfuc(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    myfuc(1,2,3,4,5)
TypeError: myfuc() missing 2 required keyword-only arguments: 'b' and 'c'
myfuc(1,2,3,b=4,c=5)
(1, 2, 3) 4 5
def fuc(**fuck):
    print(fuck)

    
def(a = 1,b = 2,c = 3)
SyntaxError: invalid syntax
fuc(a = 1,b = 2,c = 3)
{'a': 1, 'b': 2, 'c': 3}
def myfuc(a,*b,**c):
    print(a,b,c)

    
myfuc(1,2,3,4,x=5,y=6)
1 (2, 3, 4) {'x': 5, 'y': 6}
help(str.format)
Help on method_descriptor:

format(...)
    S.format(*args, **kwargs) -> str
    
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').

arg = (1,2,3,4,5)
def args(a,b,c,d,f):
    print(a,b,c,d,f)

    
args(arg)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    args(arg)
TypeError: args() missing 4 required positional arguments: 'b', 'c', 'd', and 'f'
args(*arg)
1 2 3 4 5
nall = {a:1,b:2,c:3}
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    nall = {a:1,b:2,c:3}
NameError: name 'a' is not defined
nall = {'a':1,'b':2,'c':3}
def nalls(a,b,c):
    print(a,b,c)

    
nalls(**nall)
1 2 3
