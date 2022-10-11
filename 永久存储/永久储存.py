Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
f = open("test.txt","w")
f
<_io.TextIOWrapper name='test.txt' mode='w' encoding='UTF-8'>
f = open("10086.txt","w")
f.write("i love python")
13
f.writelines("666666"\n"7777")
SyntaxError: unexpected character after line continuation character
f.writelines("666666\n","7777")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    f.writelines("666666\n","7777")
TypeError: _IOBase.writelines() takes exactly one argument (2 given)
f.writelines(["666666\n","7777"])
f.close
<built-in method close of _io.TextIOWrapper object at 0x1051b6e90>
f.close()
f = open("10086.txt","r+")
f.readable()
True
f.writable()
True
for each in f:
    print(i)

    
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    print(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
for each in f:
    print(each)

    
7777
f.read()
''
f.tell()
24
f.seek(0)
0
f.read()
'i love python666666\n7777'
f.tell()
24
f.seek()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    f.seek()
TypeError: seek expected at least 1 argument, got 0
f.seek(0)
0
f.readline()
'i love python666666\n'
f.write("i want to fly")
13
f.flush()
f.tell()
37
f.truncate(20)
20
f = open("10086",'w')
f.close
<built-in method close of _io.TextIOWrapper object at 0x1051b57d0>
f = open("10086.txt",'w')
f.close
<built-in method close of _io.TextIOWrapper object at 0x1051b6f60>
from pathlib import path
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    from pathlib import path
ImportError: cannot import name 'path' from 'pathlib' (/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/pathlib.py)
from pathlib import Path
cwd()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    cwd()
NameError: name 'cwd' is not defined
Path.cwd()
PosixPath('/Users/sivan/Documents')
p = Path('/Users/sivan/Documents')
p
PosixPath('/Users/sivan/Documents')
q  = p/"10086.txt"
q
PosixPath('/Users/sivan/Documents/10086.txt')
p.is_dir()
True
q.is_dir()
False
q.is_file()
True
q.exists()
True
Path('/Users/666').exists()
False
p.name
'Documents'
q.name
'10086.txt'
q.stem
'10086'
q.suffix
'.txt'
p.parent
PosixPath('/Users/sivan')
q.parent
PosixPath('/Users/sivan/Documents')
pc = q.parents
for each in pc:
    print(each)

    
/Users/sivan/Documents
/Users/sivan
/Users
/
pc[0]
PosixPath('/Users/sivan/Documents')
pc[1]
PosixPath('/Users/sivan')
p.parts
('/', 'Users', 'sivan', 'Documents')
p.stat()
os.stat_result(st_mode=16832, st_ino=246328, st_dev=16777231, st_nlink=8, st_uid=501, st_gid=20, st_size=256, st_atime=1659674739, st_mtime=1659674739, st_ctime=1659674739)
p.stat().st_size
256
q.stat()
os.stat_result(st_mode=33188, st_ino=8254058, st_dev=16777231, st_nlink=1, st_uid=501, st_gid=20, st_size=0, st_atime=1659678168, st_mtime=1659674777, st_ctime=1659674777)
Path(".10086")
PosixPath('.10086')
Path(".Playgrounds")
PosixPath('.Playgrounds')
Path("../10086")
PosixPath('../10086')
Path(."/10086".resolve())
SyntaxError: invalid syntax
Path("./10086").resolve()
PosixPath('/Users/sivan/Documents/10086')
Path("./Playgrounds").resolve()
PosixPath('/Users/sivan/Documents/Playgrounds')
Path("../10086").resolve()
PosixPath('/Users/sivan/10086')
Path("../10086").resolve().exesists
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    Path("../10086").resolve().exesists
AttributeError: 'PosixPath' object has no attribute 'exesists'. Did you mean: 'exists'?
Path("../10086").resolve().exists
<bound method Path.exists of PosixPath('/Users/sivan/10086')>
p.iterdir()
<generator object Path.iterdir at 0x1071b3d80>
for i in p.iterdir():
    print(i)

    
/Users/sivan/Documents/.DS_Store
/Users/sivan/Documents/.localized
/Users/sivan/Documents/10086.txt
/Users/sivan/Documents/Playgrounds
/Users/sivan/Documents/.UTSystemConfig
/Users/sivan/Documents/10086
[x for x in p.iterdir() if x.is_file()]
[PosixPath('/Users/sivan/Documents/.DS_Store'), PosixPath('/Users/sivan/Documents/.localized'), PosixPath('/Users/sivan/Documents/10086.txt'), PosixPath('/Users/sivan/Documents/10086')]
n = p/"真的牛"
n.mkdir()
n.mkdir(exist_ok = True)
n.mkdir()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    n.mkdir()
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
FileExistsError: [Errno 17] File exists: '/Users/sivan/Documents/真的牛'
n = p/"真的牛/A/B/C"
n.mkdir(exist_ok=True)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    n.mkdir(exist_ok=True)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/Users/sivan/Documents/真的牛/A/B/C'
n.mkdir(parents=True,exist_ok=True)
n = n/"牛逼"
n
PosixPath('/Users/sivan/Documents/真的牛/A/B/C/牛逼')
f = n.open('w')
f.write("代号008")
5
f.close
<built-in method close of _io.TextIOWrapper object at 0x1051b7440>
f.close()
n.rename("New project")
PosixPath('New project')
m = Path("new project")
m
PosixPath('new project')
n
PosixPath('/Users/sivan/Documents/真的牛/A/B/C/牛逼')
m.replace(n)
PosixPath('/Users/sivan/Documents/真的牛/A/B/C/牛逼')
n
PosixPath('/Users/sivan/Documents/真的牛/A/B/C/牛逼')
n.parent.rmdir()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    n.parent.rmdir()
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/pathlib.py", line 1215, in rmdir
    self._accessor.rmdir(self)
OSError: [Errno 66] Directory not empty: '/Users/sivan/Documents/真的牛/A/B/C'
n.unlink()
n.parent.rmdir()
p.Path('.')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    p.Path('.')
AttributeError: 'PosixPath' object has no attribute 'Path'. Did you mean: 'match'?
p = Path('.')
p
PosixPath('.')
p.glob("*.txt")
<generator object Path.glob at 0x1071b04a0>
list(p.glob("*.txt"))
[PosixPath('10086.txt')]
list(p.glob("*/*.py"))
[]
with open("10086.txt",'w') as f:
    f.write("我超勇的")

    
4
f.close()
with open("10086.txt",'w') as f:
    f.write("你看我迪奥吗")

    
6
