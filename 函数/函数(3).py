Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def myfuc():
    x = 10
    print(x)

    
myfuc(x)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    myfuc(x)
NameError: name 'x' is not defined
myfuc()
10
print(x)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
x = 20
def myfuc():
    print(x)

    
myfuc()
20
print(x)
20
x = 20
def myfuc():
    x = 30
    print(x)

    
myfuc()
30
print(x)
20
x = 20
id(x)
4371530576
def myfuc():
    print(id(x))

    
myfuc()
4371530576
def myfuc():
    x = 10
    print(id(x))

    
myfuc()
4371530256
id(x)
4371530576
x = 42
def myfuc():
    global x
    x = 20
    print(x)

    
myfuc()
20
print(x)
20
def fun1():
    x = 20
    def fun2():
        x = 10
        print("在fun2里,x=",x)
    fun2()
    print("在fun1里,x=",x)

    
fun1()
在fun2里,x= 10
在fun1里,x= 20
fun2()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    fun2()
NameError: name 'fun2' is not defined. Did you mean: 'fun1'?
def fun1():
    x = 20
    def fun2():
        nonlocal x
        x = 10
        print("在fun2里,x=",x)
    fun2()
    print("在fun1里,x=",x)

    
fun1()
在fun2里,x= 10
在fun1里,x= 10
str = "666"
str(259)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    str(259)
TypeError: 'str' object is not callable
str
'666'
def funA:
    
SyntaxError: invalid syntax
def funA():
    def funB()"
    
SyntaxError: unterminated string literal (detected at line 2)
def funA():
    x = 80
    def funB():
        print(x)
    return funB

funA()
<function funA.<locals>.funB at 0x107607520>
funA()()
80
mad = funA()
mad()
80
def outer(exe):
    def inner(ece):
        return ece**exe
    return inner

fid = outer()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    fid = outer()
TypeError: outer() missing 1 required positional argument: 'exe'
fid = outer(exe)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    fid = outer(exe)
NameError: name 'exe' is not defined. Did you mean: 'exec'?
fid = outer(2)
rub = outer(3)
fid(3)
9
rub(3)
27
def outer():
    x = 0
    y = 0
    def inner(n,m):
        x+=n
        y+=m
        print(F"现在x={x},y={y}")
    return inner

move = outer()
move(1,2)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    move(1,2)
  File "<pyshell#89>", line 5, in inner
    x+=n
UnboundLocalError: local variable 'x' referenced before assignment
move
<function outer.<locals>.inner at 0x1076075b0>
def outer():
    x = 0
    y = 0
    def inner(n,m):
        nonlocal x,y
        x+=n
        y+=m
        print(F"现在x={x},y={y}")
    return inner

move = outer()
move(1,4)
现在x=1,y=4
move(2,1)
现在x=3,y=5
