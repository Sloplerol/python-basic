Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
x = "我爱study"
x.startswith("我")
True
x.startswith("你")
False
x.endswith("y")
True
x.endswith("study")
True
x.startswith("我",0)
True
x.stratswith("我",0,3)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x.stratswith("我",0,3)
AttributeError: 'str' object has no attribute 'stratswith'. Did you mean: 'startswith'?
x.endswith("st",0,4)
True
x.endswith("st",0,3)
False
x.endswith("dy")
True
x.startswith("我爱")
True
x = "他很强"
if x.startswith("我","你","他"):
    print("6666")

    
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    if x.startswith("我","你","他"):
TypeError: slice indices must be integers or None or have an __index__ method
if x.startswith(("我","你","他")):
    print("6666")

    
6666
x = "I love Python"
x.istitle()
False
x = "I Love Python"
x.istitle()
True
x.isupper()
False
x.upper().isupper()
True
x.isalpha()
False
"Ilovepython".isalpha()
True
"     \n".isspace()
True
"i love this".isprintable()
True
"i love this\n".isprintable()
False
x = "12345"
x.isdecimal()
True
x.isdigit()
True
x.isnumeric()
True
"I am handsome".isidentifier()
False
"I_am_handsome".isidentifier()
True
"你是250".isidentifier()
True
"250是你".isidentifier()
False
import keyword
keyword.iskeyword("if")
True
keyword.iskeyword("else")
True
keyword.iskeyword("py")
False
"   左侧不留空白".lstrip()
'左侧不留空白'
"右侧不留空白   ".rstrip()
'右侧不留空白'
"  左右侧都没有空白   ".strip()
'左右侧都没有空白'
"welcome to my shop".lstrip("we.op")
'lcome to my shop'
"welcome to my shop".rstrip("we.op")
'welcome to my sh'
"welcome to my shop".strip("we.op")
'lcome to my sh'
"welcome to my shop".removeprefix("welcome")
' to my shop'
"welcome to my shop".removesuffix("welcome")
'welcome to my shop'
"welcome to my shop".removesuffix("shop")
'welcome to my '
"welcome to my shop".partition("t")
('welcome ', 't', 'o my shop')
"welcome to my shop".rpartition("t")
('welcome ', 't', 'o my shop')
"welcome.to.my.shop".rpartition("t")
('welcome.', 't', 'o.my.shop')
"welcome.to.my.shop".rpartition(".")
('welcome.to.my', '.', 'shop')
"welcome.to.my.shop".partition(".")
('welcome', '.', 'to.my.shop')
"666,777,888".spilt(',')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    "666,777,888".spilt(',')
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
"666,777,888".split(',')
['666', '777', '888']
"666,777,888".split(',',1)
['666', '777,888']
"666,777,888".rsplit(',',1)
['666,777', '888']
"666777 888".rsplit(',')
['666777 888']
"666 777 888".split(',')
['666 777 888']
"666 777 888".split()
['666', '777', '888']
"666\n777\n888\n".split("\n")
['666', '777', '888', '']
"666\r777\r888\r".split("\r")
['666', '777', '888', '']
"666\r777\r888".split("\r")
['666', '777', '888']
"666\r777\n888".splitlines()
['666', '777', '888']
"666\r777\r\n888".splitlines()
['666', '777', '888']
".".join(("www","apple","com"))
'www.apple.com'
a = "666"
a+="666"
a
'666666'
"".join(("666","666"))
'666666'
"".join(("666"*2))
'666666'
year = 2022
"今年是{}年".format(year)
'今年是2022年'
"二的平方是{},三的立方是{}".format(2*2,3*3*3)
'二的平方是4,三的立方是27'
"{0}{0}{1}{1}".format("是","非")
'是是非非'
"我是{name},我爱{word}".format(name="god",word="python")
'我是god,我爱python'
"我很{},你很{}".format("帅","丑")
'我很帅,你很丑'
"我很{1},你很{0}".format("帅","丑")
'我很丑,你很帅'
"我叫{},我喜欢{0},喜欢{0}的人都很牛逼".format("python",name="你爹")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    "我叫{},我喜欢{0},喜欢{0}的人都很牛逼".format("python",name="你爹")
ValueError: cannot switch from automatic field numbering to manual field specification
"我叫{name},我喜欢{0},喜欢{0}的人都很牛逼".format("python",name="你爹")
'我叫你爹,我喜欢python,喜欢python的人都很牛逼'
"{}{}{}".format("6","{}","8")
'6{}8'
"{} {{}} {}".format("6", "8")
'6 {} 8'
"{:^10}".format(520)
'   520    '
"{1:<10,0:>10}".format("520","250")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    "{1:<10,0:>10}".format("520","250")
ValueError: Invalid format specifier
"{1:<10}{0:>10}".format("520","250")
'250              520'
"{1:<10}{0:>10}".format(520,250)
'250              520'
"{1:>10}{0:<10}".format(520,250)
'       250520       '
"{left:>10}{right:<10}".format(left="520",right="250")
'       520250       '
"{left:<10}{right:>10}".format(left="520",right="250")
'520              250'
"{left:>10}{right:<10}".format(left="250",right="520")
'       250520       '
"{:010}".format(520)
'0000000520'
"{:010}".format(-520)
'-000000520'
"{:010}".format("333")
'3330000000'
"{:010}".format("-333")
'-333000000'
"{:010}".format("你真牛")
'你真牛0000000'
"{:010}".format("magic")
'magic00000'
"{:100}".format("magic")
'magic                                                                                               '
"{1:%10}{0:%10}".format(520,250)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    "{1:%10}{0:%10}".format(520,250)
ValueError: Invalid format specifier
"{1:>%10}{0:<%10}".format(520,250)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    "{1:>%10}{0:<%10}".format(520,250)
ValueError: Invalid format specifier
"{1:%>10}{0:%<10}".format(520,250)
'%%%%%%%250520%%%%%%%'
"{:+}".format(249)
'+249'
"{:-}".format(249)
'249'
"{:+}{:-}".format(421,38)
'+42138'
"{:+}{:-}".format(421,-38)
'+421-38'
"{:_}".format(12345)
'12_345'
"{:,}".format(12345)
'12,345'
"{:,}".format(1234567)
'1,234,567'
"{:,}".format(12)
'12'
"{:.2f}".format(3.1421)
'3.14'
"{:.2g}".format(3.1421)
'3.1'
"{:.3}".format(3.1421)
'3.14'
"{:.3}".format("我 很 牛")
'我 很'
"{:.3}".format(520)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    "{:.3}".format(520)
ValueError: Precision not allowed in integer format specifier
"{:b}".format(80)
'1010000'
"{:#b}".format(80)
'0b1010000'
"{:#c}".format(80)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    "{:#c}".format(80)
ValueError: Alternate form (#) not allowed with integer format specifier 'c'
"{:c}".format(80)
'P'
"{:d}".format(80)
'80'
"{:o}".format(80)
'120'
"{:#o}".format(80)
'0o120'
"{:x}".format(80)
'50'
"{:e}".format(3.21)
'3.210000e+00'
"{:E}".format(3.21)
'3.210000E+00'
"{:f}".format(3.21)
'3.210000'
"{:g}".format(3.21)
'3.21'
"{:g}".format(1234556)
'1.23456e+06'
"{:%}".format(0.21)
'21.000000%'
"{:.2%}".format(0.21)
'21.00%'
"{:{prec}%}".format(0.21,prec=.2)
'21.00%'
year = 2022
F"今年是year年".format(year)
'今年是year年'
F"今年是year年"
'今年是year年'
F"今年是{}年"
SyntaxError: f-string: empty expression not allowed
F"今年是{year}年"
'今年是2022年'
f"{-520:010}"
'-000000520'
"{:{fill}{fod}{wsd}.{rid}{red}}".format(3.123,fill=0,fod='^',wsd=10,rid=3,red='g')
'0003.12000'
fill = 3,123
fill = 0
wsd = 10
rid = 3
fod = '^'
red = 'g'
f"{3.123:{fill}{fod}{wsd}.{rid}{red}}"
'0003.12000'


