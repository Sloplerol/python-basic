Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class A(str):
    def __add__(self,other):
        return len(self)+len(other)

    
a = A("德爱","施恩")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = A("德爱","施恩")
TypeError: decoding str is not supported
a1 = A("德爱")
a2 = A("施恩")
a1 + a2
4
a1.__add__(a2)
4
a1+"666"
5
"666"+a2
'666施恩'
class A(str):
    def __add__(self,other):
        return NotImplemented

class B(str):
    def __radd__(self,other):
        return len(self)+len(other)

    
a = A("德爱")
b = B("施恩")
a+b
4
class A(str):
    def __iadd__(self,other):
        return len(self)+len(other)

    
a = A("德爱")
a+=b
a
4
type(a)
<class 'int'>
b = B("banana")
b+=b
b
'bananabanana'
type(b)
<class 'str'>
