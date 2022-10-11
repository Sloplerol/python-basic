Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def add(x,y):
    return x+y

import functools
functools.reduce(add,[1,2,3,4,5])
15
add(add(add(add(1,2),3),4),5)
15
functools.reduce(lambda x,y:x*y ,range(1,11))
3628800
cube = functools.partial(pow,2)
cube(3)
8
cube(5)
32
square = functools.partial(pow,ex=3)
square(3)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    square(3)
TypeError: pow() missing required argument 'exp' (pos 2)
help(exp)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    help(exp)
NameError: name 'exp' is not defined
help(pow)
Help on built-in function pow in module builtins:

pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

square = functools.partial(pow,exp = 2)
square(3)
9
