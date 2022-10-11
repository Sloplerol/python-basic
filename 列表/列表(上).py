Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
[1,2,3,4,5]
[1, 2, 3, 4, 5]
rhy = [1,2,3,4,5]
print(rhy)
[1, 2, 3, 4, 5]
for i in rhy:
    print(i)

    
1
2
3
4
5
rhy[1]
2
rhy[-1]
5
length = len(rhy)
rhy[length-1]
5
rhy[0:3]
[1, 2, 3]
rhy[:3]
[1, 2, 3]
rhy[:]
[1, 2, 3, 4, 5]
rhy[0:4:2]
[1, 3]
rhy[::2]
[1, 3, 5]
rhy[::-1]
[5, 4, 3, 2, 1]
lines = [1,2,3]
lines.append(4)
lines
[1, 2, 3, 4]
lines.extend([5,6])
lines
[1, 2, 3, 4, 5, 6]
lines[len(lines)] = [7]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    lines[len(lines)] = [7]
IndexError: list assignment index out of range
lines[len(lines):] = [7]
lines
[1, 2, 3, 4, 5, 6, 7]
a =[1,3,4,5]
a.insert(1,2)
a
[1, 2, 3, 4, 5]
a.insert(0,0)
a
[0, 1, 2, 3, 4, 5]
a.insert(len(a),6)
a
[0, 1, 2, 3, 4, 5, 6]
a.remove(2)
a
[0, 1, 3, 4, 5, 6]
a.pop(2)
3
a
[0, 1, 4, 5, 6]
a.clear()
a
[]
num = [1,2,3,4,5]
num[2:]=[5,6,7]
num
[1, 2, 5, 6, 7]
num = [3,1,5,1,3]
num.sort()
num
[1, 1, 3, 3, 5]
num.reverse()
num
[5, 3, 3, 1, 1]
num = [3,1,5,1,3]
num.sort(reverse())
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    num.sort(reverse())
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
num.sort(reverse=True)
num
[5, 3, 3, 1, 1]
num.count(1)
2
num.index(1)
3
num.index(2,2,4)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    num.index(2,2,4)
ValueError: 2 is not in list
num.index(3,2,4)
2
num_copy1 = num.copy()
xum_copy1
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    xum_copy1
NameError: name 'xum_copy1' is not defined. Did you mean: 'num_copy1'?
num_copy1
[5, 3, 3, 1, 1]
num_copy2 = num[:]
num_copy2
[5, 3, 3, 1, 1]
s = [1,2,3]
t = [4,5,6]
s+t
[1, 2, 3, 4, 5, 6]
h = [[1,2,3],[4,5,6],[7,8,9]]
for i in h:
    for e in i:
        print(e)

        
1
2
3
4
5
6
7
8
9
for i in h:
    for e in i:
        print(e,end = " ")
    print()

    
1 2 3 
4 5 6 
7 8 9 
h[1][1]
5
A = [0]*3
A
[0, 0, 0]
for i in range(3):
    A[i] = [0]*3

    
print(i)
2
A
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0]*3]
B
[[0, 0, 0]]
B = [[0]*3]*3
B
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
A[0] is A[1]
False
A[1] is A[2]
False
B[1] is B[2]
True
B[1] is B[0]
True
A[1][1]=1
A
[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
B[1][1] = 1
B
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
