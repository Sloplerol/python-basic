Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = 1,2,3,4
x = 12321
x[-1]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x[-1]
TypeError: 'int' object is not subscriptable
x = "12321"
if x == x[::-1]:
    print("yes")
else:
    print("no")

    
yes
x = "I Love You"
x.capitalize()
'I love you'
x
'I Love You'
x.casefold()
'i love you'
x
'I Love You'
x,title()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x,title()
NameError: name 'title' is not defined. Did you mean: 'tuple'?
x.title
<built-in method title of str object at 0x103be3570>
x.title()
'I Love You'
x.swapcase()
'i lOVE yOU'
x.upper()
'I LOVE YOU'
x.lower()
'i love you'
x = "1,2,3,4,5"
x.center(5)
'1,2,3,4,5'
x.center(15)
'   1,2,3,4,5   '
x.ljust(15)
'1,2,3,4,5      '
x.rjust(15)
'      1,2,3,4,5'
x.zjust(15)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x.zjust(15)
AttributeError: 'str' object has no attribute 'zjust'. Did you mean: 'ljust'?
x.zfill(15)
'0000001,2,3,4,5'
"520".zfill(5)
'00520'
"-520".zfill(5)
'-0520'
x.ljust(15,尕)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x.ljust(15,尕)
NameError: name '尕' is not defined
x.ljust(15, 666)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x.ljust(15, 666)
TypeError: The fill character must be a unicode character, not int
x.ljust(15, "尕娃")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x.ljust(15, "尕娃")
TypeError: The fill character must be exactly one character long
x = "1,2,3,4"
x.ljust(15, "555")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x.ljust(15, "555")
TypeError: The fill character must be exactly one character long
x.center()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x.center()
TypeError: center expected at least 1 argument, got 0
x.center(15)
'    1,2,3,4    '
x.center(15, "asdj")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    x.center(15, "asdj")
TypeError: The fill character must be exactly one character long
x = "有点东西"
x.center(15)
'      有点东西     '
x.center(15, "尕娃")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x.center(15, "尕娃")
TypeError: The fill character must be exactly one character long
x.center(15, "干")
'干干干干干干有点东西干干干干干'
x.center(15,"干")
'干干干干干干有点东西干干干干干'
x.ljust(15, "6")
'有点东西66666666666'
x.rjust(15, "6")
'66666666666有点东西'
x = 1,2,3,4,3,2
x.count(2)
2
x.count(2,0,3)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x.count(2,0,3)
TypeError: tuple.count() takes exactly one argument (3 given)
x = "你真的你真的"
x.count("你",0,3)
1
x.find("你")
0
x.rfind("你")
3
x.find("牛")
-1
x.rfind("牛")
-1
code = """
    print("666")
    print("666")
    """
code
'\n    print("666")\n    print("666")\n    '
code = """
        print("666")
    print("666")
    """
code
'\n        print("666")\n    print("666")\n    '
new code = ode.expandtabs(4)
SyntaxError: invalid syntax
new_code = ode.expandtabs(4)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    new_code = ode.expandtabs(4)
NameError: name 'ode' is not defined. Did you mean: 'code'?
new_code = code.expandtabs(4)
print(new_code)

        print("666")
    print("666")
    
code = """
    print("666")
    print("666")"""
print(code)

    print("666")
    print("666")
"我去，你是ikun".replace("我去","你去")
'你去，你是ikun'
label = str.maketrans("ABCDE","12345")
"Abandon Dead".translate(label)
'1bandon 4ead'
label = str.maketrans("ABCDE","12345","Dread")
"Anandon Dread".translate(label)
'1nnon '
