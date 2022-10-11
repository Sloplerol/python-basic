Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = 3
print(x)
3
43422fpad
SyntaxError: invalid decimal literal
x = "基操勿6"
print(x)
基操勿6
x = y =5
x
5
y
5
x = 3
y = 5
x = y
x
5
y
5
x = 3
y = 5
z = x
x = y
y = z
x
5
y
3
x,y = y,x
print(x,y)
3 5
print('Let's go')
      
SyntaxError: unterminated string literal (detected at line 1)
print("Let's go")
      
Let's go
print(Let's go)
      
SyntaxError: unterminated string literal (detected at line 1)
print('"Let's go"')
      
SyntaxError: unterminated string literal (detected at line 1)
print('"Let\'s go"')
      
"Let's go"
print("Let's\n,go")
      
Let's
,go
print("User:\Applications\table")
      
User:\Applications	able
print("User:\\Applications\\table")
      
User:\Applications\table
print("whan\table\nan\")
      
SyntaxError: unterminated string literal (detected at line 1)
print("User:\\Applications\\table")
      
User:\Applications\table
print(r"User:\Applications\table")
      
User:\Applications\table
i love \
      
SyntaxError: unexpected EOF while parsing
i love\
      
SyntaxError: unexpected EOF while parsing
print(i love\)
      
SyntaxError: unexpected character after line continuation character
print(i love\
      
SyntaxError: '(' was never closed
print("i love\")
      
SyntaxError: unterminated string literal (detected at line 1)
i love \n\
      
SyntaxError: unexpected character after line continuation character
poet = """666
askdkas
sadnjkdmka
asndnkds
"""
      
print(poet)
      
666
askdkas
sadnjkdmka
asndnkds

print("
      
SyntaxError: unterminated string literal (detected at line 1)
print("\
dawdawdw
      
SyntaxError: unterminated string literal (detected at line 2)
print("sdhajd\
admsaddk\
sdmad\
ksadka")
      
sdhajdadmsaddksdmadksadka
print("asfj\n\
fakfsk\n\
afsjfja\n\
fsanfjs")
      
asfj
fakfsk
afsjfja
fsanfjs
5+1
      
6
'5'+'1'
      
'51'
print("真的C"*10)
      
真的C真的C真的C真的C真的C真的C真的C真的C真的C真的C
print("真的C\n"*10)
      
真的C
真的C
真的C
真的C
真的C
真的C
真的C
真的C
真的C
真的C

tmp = input("你是谁:")
      
你是谁:your father
print(tmp)
      
your father
tmp = input("请输入一个数字")
      
请输入一个数字8
guess = int(tmp)
      
print(guess)
      
8
guess
      
8
count = 3
      
while count > 0:
    print("666")
    count = count - 1

    
666
666
666
import random
random.randint(1,10)
6
random.randint(1,10)
3
random.randint(1,10)
1
random.randint(1,10)
6
random.randint(1,10)
8
x=random.getstate()
random.getstate(x)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    random.getstate(x)
TypeError: Random.getstate() takes 1 positional argument but 2 were given
random.setstate(x)
rnadom.randint(1,10)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    rnadom.randint(1,10)
NameError: name 'rnadom' is not defined. Did you mean: 'random'?
random.randint(1,10)
4
random.randint(1,10)
1
random.randint(1,10)
3
random.randint(1,10)
10
random.randint(1,10)
8
x = getstate()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    x = getstate()
NameError: name 'getstate' is not defined. Did you mean: 'getattr'?
x = random.getstate()
print(x)

random.setstate(x)
random.randint(1,10)
7
random.randint(1,10)
5
random.randint(1,10)
5
random.randint(1,10)
2
x=random.getstate()
random.randint(1,10)
10
x=random.getstate()
random.randint(x)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    random.randint(x)
TypeError: Random.randint() missing 1 required positional argument: 'b'
random.randint(1,10)
7
random.randint(1,10)
8
random.randint(1,10)
8
random.randint(1,10)
5
random.randint(1,10)
5
random.setstate(x)
random.randint(1,10)
7
random.randint(1,10)
8
random.randint(1,10)
8
random.randint(1,10)
5
6/2
3.0
0.1+0.2 = 0.3
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
0.1+0.2 == 0.3
False
import decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
a + b
Decimal('0.3')
print(a+b)
0.3
0.00005
5e-05
1 + 2j
(1+2j)
x = 1+2j
x.real
1.0
x.imagine
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    x.imagine
AttributeError: 'complex' object has no attribute 'imagine'
x.imag
2.0
3 // 2
1
-3 // 2
-2
divmod(3,2)
(1, 1)
divmod(-3,2)
(-2, 1)
abs(-2)
2
abs(-6)
6
abs(1+2j)
2.23606797749979
int('520')
520
int(3.14)
3
float('520')
520.0
float(2)
2.0
float('+1E6')
1000000.0
float(+1E6)
1000000.0
complex(1+2j)
(1+2j)
complex(1 + 2j)
(1+2j)
complex('1 + 2j')
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    complex('1 + 2j')
ValueError: complex() arg is a malformed string
complex('1+2j')
(1+2j)
pow(2,3)
8
pow(2,3,5)
3
bool("25")
True
bool(False)
False
bool("")
False
bool(" ")
True
bool(0)
False
bool(0.0)
False
if bool(268):
    print("555")
else:
    print("444")

    
555
1 == True
True
0 == False
True
True + False
1
3>4 and 4>5
False
4>3 and 5>4
True
3>4 and 4>3
False
3>4 or 4>3
True
not True
False
3 and 4
4
4 or 3
4
0 or not 3 and 5 or 6
6
