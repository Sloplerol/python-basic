Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a = {}
type(a)
<class 'dict'>
a = {"ok"}
type(a)
<class 'set'>
a = {"ok":"yes"}
type(a)
<class 'dict'>
{"666","77u7"}
{'666', '77u7'}
[s for s in {"Fish"}]
['Fish']
{s for s in "Fish"}
{'F', 'h', 'i', 's'}
set("Fish")
{'F', 'h', 'i', 's'}
s = set("Fish")
s[0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
'F' in s
True
'f' not in s
True
for each in s:
    print(each)

    
F
h
i
s
s = {1,1,2,3,4}
set(s)
{1, 2, 3, 4}
set(s) is s
False
len(set(s)) is len(s)
True
s = [1,1,2,3,4]
len(s) is len(set(s))
False
s
[1, 1, 2, 3, 4]
set(s)
{1, 2, 3, 4}
s
[1, 1, 2, 3, 4]
s is set(s)
False
a = "python"
a
'python'
a = {"python"}
a
{'python'}
set(a)
{'python'}
a = set("python")
a
{'y', 'h', 'p', 't', 'n', 'o'}
a.isdisjoint(set("pig"))
False
a.isdisjoint("pig")
False
a.issubset("pythonist")
True
a.issuperset("pythonist")
False
a.issuperset("pyth")
True
a.union("123")
{'y', 'h', 'n', 'o', '2', 'p', '3', 't', '1'}
a.intersection("pyth")
{'y', 'h', 't', 'p'}
a.union("2","3")
{'3', 't', 'y', 'h', 'o', '2', 'n', 'p'}
a.intersection("po","ph")
{'p'}
a.summetric_different("fishc")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.summetric_different("fishc")
AttributeError: 'set' object has no attribute 'summetric_different'. Did you mean: 'symmetric_difference'?
a.symmetric_different("fishc")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.symmetric_different("fishc")
AttributeError: 'set' object has no attribute 'symmetric_different'. Did you mean: 'symmetric_difference'?
a.symmetric_difference("fishc")
{'y', 'f', 'c', 'i', 'p', 's', 't', 'n', 'o'}
s.difference("fish")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.difference("fish")
AttributeError: 'list' object has no attribute 'difference'
s.difference("fish","what")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.difference("fish","what")
AttributeError: 'list' object has no attribute 'difference'
a.difference("fish")
{'t', 'y', 'o', 'n', 'p'}
a <= set("python")
True
a < set("python")
False
a > set("py")
True
a >= set("py")
True
a | {1,2,3} | "fuck"
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a | {1,2,3} | "fuck"
TypeError: unsupported operand type(s) for |: 'set' and 'str'
a | {1,2,3} | set("fuck")
{1, 2, 3, 'y', 'f', 'c', 'h', 'p', 'k', 't', 'n', 'u', 'o'}
a & set("Fish")
{'h'}
a - set("Fish")
{'y', 'p', 't', 'n', 'o'}
a ^ set("Fish")
{'y', 'i', 'p', 'F', 's', 't', 'n', 'o'}
t = frozenset("python")
t
frozenset({'y', 'h', 'p', 't', 'n', 'o'})
s = set("python")
s
{'y', 'h', 'p', 't', 'n', 'o'}
s.update([1,3,1],"42")
s
{1, 3, '4', 'y', 'h', '2', 'p', 't', 'n', 'o'}
t.update([1,2,1],"42")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    t.update([1,2,1],"42")
AttributeError: 'frozenset' object has no attribute 'update'
s.difference_update("pol")
s
{1, 3, '4', 'y', 'h', '2', 't', 'n'}
s.symmetric_difference_update("pyl")
s
{1, 3, '4', 'h', '2', 'p', 'l', 't', 'n'}
s
{1, 3, '4', 'h', '2', 'p', 'l', 't', 'n'}
s.add"43"
SyntaxError: invalid syntax
s.add "43"
SyntaxError: invalid syntax
s.add "90"
SyntaxError: invalid syntax
s.add("43")
s
{1, 3, '4', 'h', '2', 'p', 'l', 't', 'n', '43'}
s.remove("pi")
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.remove("pi")
KeyError: 'pi'
s.discard("pi")
s
{1, 3, '4', 'h', '2', 'p', 'l', 't', 'n', '43'}
s.pop()
1
s.pop()
3
s.pop()
'4'
s
{'h', '2', 'p', 'l', 't', 'n', '43'}
s.clear()
s
set()
hash(1)
1
hash(1.0)
1
hash(1.9323)
2149737437489926657
hash("666")
469797969611647681
hash((214))
214
hash([1,2,3])
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    hash([1,2,3])
TypeError: unhashable type: 'list'
{"555":333,"222":6666}
{'555': 333, '222': 6666}
{[1,2,3]:22}
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    {[1,2,3]:22}
TypeError: unhashable type: 'list'
{1,2,3,"222","222"}
{1, 2, 3, '222'}
{1,2,3,[1,2]}
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    {1,2,3,[1,2]}
TypeError: unhashable type: 'list'
x = {1,2,3}
y = {x,2,1}
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    y = {x,2,1}
TypeError: unhashable type: 'set'
frozenset(x)
frozenset({1, 2, 3})
y = {x,2,3}
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    y = {x,2,3}
TypeError: unhashable type: 'set'
x = frozenset(x)
y = {x,2,1}
y
{frozenset({1, 2, 3}), 1, 2}
