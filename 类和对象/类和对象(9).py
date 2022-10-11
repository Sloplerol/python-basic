Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
2&3
2
3&4
0
bin(3)
'0b11'
bin(4)
'0b100'
3|2
3
3|4
7
~4
-5
~6
-7
3^2
1
3^4
7
4<<2
16
4>>2
1
4//pow(2,2)
1
4*pow(2,2)
16
4>>-2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    4>>-2
ValueError: negative shift count
import math
0.1+0.2==0.3+math.ulp(0.3)
True
class C:
    def __index__(self:)
    
SyntaxError: invalid syntax
class C:
    def __index__(self):
        print("666")
        return 3

    
s = "我就是天地"
c = C()
s[c]
666
'天'
