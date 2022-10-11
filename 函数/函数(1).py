Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def myfuction():
    for i in range(3):
        print("6666")

        
myfuction()
6666
6666
6666
def myfuc(name):
    for i in range(3):
        print(f"i love (name)")

        
myfuc(you)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    myfuc(you)
NameError: name 'you' is not defined
def myfuc(name):
    for i in range(3):
        print(f"i love {name}")

        
myfuc("you")
i love you
i love you
i love you
myfuc(you)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    myfuc(you)
NameError: name 'you' is not defined
def myfuc(name,names):
    for i in range(times):
        print(f"i love {name}")

        
myfuc("you",5)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    myfuc("you",5)
  File "<pyshell#17>", line 2, in myfuc
    for i in range(times):
NameError: name 'times' is not defined. Did you mean: 'names'?
def myfuc(name,times):
    for i in range(times):
        print(f"i love {name}")

        
myfuc("you",5)
i love you
i love you
i love you
i love you
i love you
def div(x,y):
    z = x/y
    return z

div
<function div at 0x107a9ed40>
list(div)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list(div)
TypeError: 'function' object is not iterable
div(4/2)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    div(4/2)
TypeError: div() missing 1 required positional argument: 'y'
div(4,2)
2.0
def div(x,y):
    return x/y

div(4,2)
2.0
def div(x,y):
    if(y==0):
        print("除数不为零")
    return x/y

div(4/0)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    div(4/0)
ZeroDivisionError: division by zero
div(4,0)
除数不为零
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    div(4,0)
  File "<pyshell#38>", line 4, in div
    return x/y
ZeroDivisionError: division by zero
def dmg():
    pass

print(dmg())
None
