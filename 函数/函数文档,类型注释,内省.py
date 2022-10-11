Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def exchange(dollar,rate = 7):
    """美元-->人民币
       rate = 7
       dollar*rate=人民币
    """
    return dollar*rate

exchange(6)
42
help(exchange)
Help on function exchange in module __main__:

exchange(dollar, rate=7)
    美元-->人民币
    rate = 7
    dollar*rate=人民币

def kill(s:str,t:int) -->str
SyntaxError: expected ':'
def kill(s:str,t:int): -->str
SyntaxError: invalid syntax
def kill(s:str,t:int) -->str:
    
SyntaxError: expected ':'
def kill(s:str,t:int)->str:
    return s*t

kill("line",3)
'linelineline'
kill(3,3)
9
def kill(s:str="666",t:int=5)->str:
    return s*t

kill()
'666666666666666'
def nain(s:list,t:int=3)->list:
    return s*t

nain([1,2,3,4])
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
def nail(s:list[int],int=3)->list:
    return s*t

nail([1,2,3])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    nail([1,2,3])
  File "<pyshell#27>", line 2, in nail
    return s*t
NameError: name 't' is not defined
def nail(s:list[int],t:int=3)->list:
    return s*t

nail([1,2,3])
[1, 2, 3, 1, 2, 3, 1, 2, 3]
def opo(s:dict(str,int),t:int=3)-->tuple:
    
SyntaxError: expected ':'
def opo(s:dict(str,int),t:int=3)->tuple:
    return (s.keys())*t

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    def opo(s:dict(str,int),t:int=3)->tuple:
TypeError: dict expected at most 1 argument, got 2
def opo(s:dict[str,int],t:int=3)->list:
    return (s.keys())*t

opo('A':3, 'B':4)
SyntaxError: invalid syntax
opo({'A':3, 'B':4})
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    opo({'A':3, 'B':4})
  File "<pyshell#37>", line 2, in opo
    return (s.keys())*t
TypeError: unsupported operand type(s) for *: 'dict_keys' and 'int'
def opo(s:dict[str,int],t:int=3)->list:
    return list((s.keys())*t)

opo({'A':3, 'B':3})
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    opo({'A':3, 'B':3})
  File "<pyshell#41>", line 2, in opo
    return list((s.keys())*t)
TypeError: unsupported operand type(s) for *: 'dict_keys' and 'int'
def opo(s:dict[str,int],t:int=3)->list:
    return list(s.keys())*t

opo({'A':3, 'B':3})
['A', 'B', 'A', 'B', 'A', 'B']
opo.__name__
'opo'
opo.__annotations__
{'s': dict[str, int], 't': <class 'int'>, 'return': <class 'list'>}
exechange.__doc__
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    exechange.__doc__
NameError: name 'exechange' is not defined. Did you mean: 'exchange'?
exchange.__doc__
'美元-->人民币\n       rate = 7\n       dollar*rate=人民币\n    '
print(exechange.__doc__)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(exechange.__doc__)
NameError: name 'exechange' is not defined. Did you mean: 'exchange'?
print(exchange.__doc__)
美元-->人民币
       rate = 7
       dollar*rate=人民币
    
