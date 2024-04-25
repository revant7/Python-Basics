Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fwc=["Italy",'"Argentina',"Germany","Brazil","France","Brazil","Italy","Spain","Germany","France"]
>>> fwc("Brazil")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    fwc("Brazil")
TypeError: 'list' object is not callable
>>> fwc["Brazil"]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fwc["Brazil"]
TypeError: list indices must be integers or slices, not str
>>> fwc
['Italy', '"Argentina', 'Germany', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany', 'France']
>>> fwc.index("Brazil")
3
>>> fwc.index("Germany") + 7
9
>>> "Brazil" in fwc
True
>>> "" in fwc
False
>>> for i in fwc:
	" ".join(i)
	print(i)

'I t a l y'
Italy
'" A r g e n t i n a'
"Argentina
'G e r m a n y'
Germany
'B r a z i l'
Brazil
'F r a n c e'
France
'B r a z i l'
Brazil
'I t a l y'
Italy
'S p a i n'
Spain
'G e r m a n y'
Germany
'F r a n c e'
France
>>> fwc
['Italy', '"Argentina', 'Germany', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany', 'France']
>>> for i in fwc:
	i = " ".join(i)
	print(i)

I t a l y
" A r g e n t i n a
G e r m a n y
B r a z i l
F r a n c e
B r a z i l
I t a l y
S p a i n
G e r m a n y
F r a n c e
>>> fwc[1]
'"Argentina'
>>> fwc[1] = "India"
>>> fwc[1]
'India'
>>> fwc
['Italy', 'India', 'Germany', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany', 'France']
>>> fwc.extend([1,2,3])
>>> fwc
['Italy', 'India', 'Germany', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany', 'France', 1, 2, 3]
>>> fwc.pop()
3
>>> i = fwc.pop()
>>> i
2
>>> fwc.remove()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fwc.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> fwc.pop(-1)
1
>>> fwc.pop(4)
'France'
>>> fwc.remove(5)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    fwc.remove(5)
ValueError: list.remove(x): x not in list
>>> fwc.remove("France")
>>> fwc
['Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany']
>>> fwc is True
False
>>> type(fwc)
<class 'list'>
>>> True is False
False
>>> is fwc False
SyntaxError: invalid syntax
>>> fwc is False
False
>>> " " in fwc
False
>>> fwc.append(1)
>>> fwc[-1]
1
>>> fwc[-1:-5]
[]
>>> fwc[-5:-1]
['Brazil', 'Italy', 'Spain', 'Germany']
>>> fwc[-1:-2]
[]
>>> fwc[-1:4]
[]
>>> fwc[-1:0]
[]
>>> fwc[2:-2]
['Germany', 'Brazil', 'Brazil', 'Italy', 'Spain']
>>> fwc[5:2]
[]
>>> fwc[-1:-5:-1]
[1, 'Germany', 'Spain', 'Italy']
>>> fwc
['Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany', 1]
>>> fwc[8] = 10
>>> fwc
['Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany', 10]
>>> fwc[12] = 15
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    fwc[12] = 15
IndexError: list assignment index out of range
>>> l = [i for i in range(1,100) if i%2 == 0]
>>> l
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> l = list(list(list([[fwc]])))
>>> l
[[['Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany', 10]]]
>>> list(l)
[[['Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany', 10]]]
>>> l[1] = 10
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    l[1] = 10
IndexError: list assignment index out of range
>>> l[0][1] = 10
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    l[0][1] = 10
IndexError: list assignment index out of range
>>> l[0]
[['Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany', 10]]
>>> l[0][0][0]
'Italy'
>>> list(tuple(fwc))
['Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany', 10]
>>> tuple(list(fwc))
('Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany', 10)
>>> len(fwc)
9
>>> type(fwc)
<class 'list'>
>>> fwc
['Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany', 10]
>>> fwc(len+1)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    fwc(len+1)
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'int'
>>> len(fwc)+1
10
>>> fwc
['Italy', 'India', 'Germany', 'Brazil', 'Brazil', 'Italy', 'Spain', 'Germany', 10]
>>> fwc[::-2]
[10, 'Spain', 'Brazil', 'Germany', 'Italy']
>>> fwc[::2]
['Italy', 'Germany', 'Brazil', 'Spain', 10]
>>> fwc[::3]
['Italy', 'Brazil', 'Spain']
>>> 