Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = [1,2,3]
y = x
x[1] = 1
x
[1, 1, 3]
y
[1, 1, 3]
x = [1,2,3]
y = x.copy()
x[1] = 1
x
[1, 1, 3]
y
[1, 2, 3]
x = [1,2,3]
y = x[:]
x[1]=1
x
[1, 1, 3]
y
[1, 2, 3]
x = [[1,2,3],[4,5,6],[7,8,9]]
y = x
x[1][1]=0
x
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
y
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
import copy
x = [[1,2,3],[4,5,6],[7,8,9]]
y = copy.copy(x)
x[1][1]=0
x
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
y
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
x = [[1,2,3],[4,5,6],[7,8,9]]
y = copy.deepcopy(x)
x[1][1]=0
x
[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
y
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
swl = [1,2,3]
swl = 2*swl
swl
[1, 2, 3, 1, 2, 3]
swl = [2]*swl
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    swl = [2]*swl
TypeError: can't multiply sequence by non-int of type 'list'
swl = [2*swl]
swl
[[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]]
sml = [1,2,3]
for i in range(len(sml)):
    sml = sml[i] *2

    
Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    sml = sml[i] *2
TypeError: 'int' object is not subscriptable
for i in range(len(sml)):
    sml = sml[i]*2

    
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    for i in range(len(sml)):
TypeError: object of type 'int' has no len()
for i in range(len(sml)):
    sml[i] = sml[i]*2

    
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    for i in range(len(sml)):
TypeError: object of type 'int' has no len()
i
1
sml
2
sml = [1,2,3]
for i in range(len(sml)):
    sml[i]=sml[i]*2

    
sml
[2, 4, 6]
sml = [1,2,3]
sml = [i*2 for i in sml]
sml
[2, 4, 6]
hero = "111" "222"
hero.append("333")
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    hero.append("333")
AttributeError: 'str' object has no attribute 'append'
hero.append("333")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    hero.append("333")
AttributeError: 'str' object has no attribute 'append'
i = [1,2,3]
i = [i for i in range(10)]
i
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = []
for i in range(10):
    x.append = i+1

    
Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    x.append = i+1
AttributeError: 'list' object attribute 'append' is read-only
for i in range(10):
    x.append(i+1)

    
i
9
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = ["Miracle"]
y = [i*2 for i in y]
y
['MiracleMiracle']
y = [i*2 for i in "Miracle"]
y
['MM', 'ii', 'rr', 'aa', 'cc', 'll', 'ee']
y = [[1,2,3],
     [4,5,6],
     [7,8,9]]
clone = [row[2] for row in y]
clone
[3, 6, 9]
diag = [y[i][i] for i in y]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    diag = [y[i][i] for i in y]
  File "<pyshell#80>", line 1, in <listcomp>
    diag = [y[i][i] for i in y]
TypeError: list indices must be integers or slices, not list
diag = [y[i][i] for i in range(len(y))]
diag
[1, 5, 9]
c = [ord[c] for c in "Miracle"]
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    c = [ord[c] for c in "Miracle"]
  File "<pyshell#83>", line 1, in <listcomp>
    c = [ord[c] for c in "Miracle"]
TypeError: 'builtin_function_or_method' object is not subscriptable
c = [ord(c) for c in "Miracle"]
c
[77, 105, 114, 97, 99, 108, 101]
diag = [y[i]y[2-i] for i in range(len(y))]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
y = [[1,2,3],
     [4,5,6],
     [7,8,9]]
diag = [y[i]y[2-i] for i in range(len(y))]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
diag = [y[i][2-i] for i in range(len(y))]
diag
[3, 5, 7]
B = [[0]*3]*3
B
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B[1][1] = 1
B
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
for i in range(3):
    A[i]=[0]*3

    
Traceback (most recent call last):
  File "<pyshell#97>", line 2, in <module>
    A[i]=[0]*3
NameError: name 'A' is not defined
A = [0]*3
for i in range(3):
    A[i]=A

    
A
[[...], [...], [...]]
for i in range(3):
    A[i]=[0]*3

    
A
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
A[1][1]= 1
A
[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
S = [[0]*3 for i in range(3)]
S
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
S[1][1] = 1
S
[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
self = [i for i in range(10) if i%2==0]
self
[0, 2, 4, 6, 8]
self = [i+1 for i in range(10) if i%2==0]
self
[1, 3, 5, 7, 9]
hyber = ["sad","satellite","word"]
hello = [i for i in hyber if h[0]=='s']
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    hello = [i for i in hyber if h[0]=='s']
  File "<pyshell#117>", line 1, in <listcomp>
    hello = [i for i in hyber if h[0]=='s']
NameError: name 'h' is not defined
hello = [i for i in hyber if h[0] == 's']
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    hello = [i for i in hyber if h[0] == 's']
  File "<pyshell#118>", line 1, in <listcomp>
    hello = [i for i in hyber if h[0] == 's']
NameError: name 'h' is not defined
hello = [i for i in hyber if hyber[0] == 's']
hello
[]
wit = ["sad","swd","dfa"]
had = [w for w in wit if w[0]=='s']
had
['sad', 'swd']
wit = ['sajdj','asd','sdac']
sad = [s for s in wit if s[0]=='s']
sad
['sajdj', 'sdac']
flat = []
media = [[1,2,3],[4,5,6].[7,8,9]]
SyntaxError: invalid syntax
media = [[1,2,3],[4,5,6],[7,8,9]]
for i in media:
    for media in flat:
        flat.append[media]

        
flat
[]
for i in media:
    for m in i:
        flat.append(m)

        
falt
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    falt
NameError: name 'falt' is not defined
flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
flat = [m for i in media for m in i]
flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
hed = [x+y for x in "what" for y in "shit"]
hed
['ws', 'wh', 'wi', 'wt', 'hs', 'hh', 'hi', 'ht', 'as', 'ah', 'ai', 'at', 'ts', 'th', 'ti', 'tt']
hed = [[x,y] for x in range(10) if x%2==0 for y in range(10) if y % 3==0]
hed
[[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6], [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]
