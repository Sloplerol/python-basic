Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def funA():
    print("666")

    
def funB():
    funA()

    
funB()
666
def funC():
    print("6666")
    funC()

    
funC()
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666
6666Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    funC()
  File "<pyshell#10>", line 3, in funC
    funC()
  File "<pyshell#10>", line 3, in funC
    funC()
  File "<pyshell#10>", line 3, in funC
    funC()
  [Previous line repeated 128 more times]
  File "<pyshell#10>", line 2, in funC
    print("6666")
KeyboardInterrupt
def funC(i):
    if i<10:
        print("666")
        funC()
        i-=1

        
def funC(i):
    if i>0:
        print("666")
        funC()
        i-=1

        
funC(10)
666
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    funC(10)
  File "<pyshell#20>", line 4, in funC
    funC()
TypeError: funC() missing 1 required positional argument: 'i'
def funC(i):
    if i>0:
        print("666")
        funC(i)
        i-=1

        
funC(10)
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
666
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    funC(10)
  File "<pyshell#23>", line 4, in funC
    funC(i)
  File "<pyshell#23>", line 4, in funC
    funC(i)
  File "<pyshell#23>", line 4, in funC
    funC(i)
  [Previous line repeated 170 more times]
  File "<pyshell#23>", line 3, in funC
    print("666")
KeyboardInterrupt
def funC(i):
    if i>0:
        print("666")
        i-=1
        funC(i)

        
funC(10)
666
666
666
666
666
666
666
666
666
666
def factorial(n)
SyntaxError: expected ':'
def factorial(n):
    polly=n
    for i in n:
        polly*=i
    return polly

factorial(5)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    factorial(5)
  File "<pyshell#35>", line 3, in factorial
    for i in n:
TypeError: 'int' object is not iterable
def factorial(n):
    polly=n
    for i in range(1,n):
        polly*=i
    return polly

factorial(5)
120
def factorial(n):
    for i in n:
        n*=i
    return n

factorial(5)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    factorial(5)
  File "<pyshell#41>", line 2, in factorial
    for i in n:
TypeError: 'int' object is not iterable
def factorial(n):
    for i in range(1,n):
        n*=i
    return n

factorial(5)
120
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

    
factorial(5)
120
def fibonacci(n):
    a = 1
    b = 1
    c = 1
    while n>2:
        c = a+b
        a = b
        b = c
        n-=1
    return c

fibonacci(5)
5
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return factorial(n-1)+factorial(n-2)

    
fibonacci(5)
5
fibonacci(120)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    factorial(120)
  File "<pyshell#70>", line 5, in factorial
    return factorial(n-1)+factorial(n-2)
  File "<pyshell#70>", line 5, in factorial
    return factorial(n-1)+factorial(n-2)
  File "<pyshell#70>", line 5, in factorial
    return factorial(n-1)+factorial(n-2)
  [Previous line repeated 107 more times]
KeyboardInterrupt
def fibonacci(n):
    a = 1
    b = 1
    c = 1
    while n>2:
        c = a+b
        a = b
        b = c
        n-=1
    return c


fibonacci(120)
5358359254990966640871840
