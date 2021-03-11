Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("5+2=",5+2, ,7+2)
SyntaxError: invalid syntax
>>> print("5+2=",5+2)
5+2= 7
>>> print("5-2=",5-2)
5-2= 3
>>> print("5*2=",5*2)
5*2= 10
>>> print("5/2=",5/2)
5/2= 2.5
>>> print("5//2=",5//2)
5//2= 2
>>> print("5%2=",5%2)
5%2= 1
>>> print("5**2=",5**2)
5**2= 25
>>> quote="zia"
>>> print("%s",quote)
%s zia
>>> print("%s"%quote)
zia
>>> print(quote)
zia
>>> print("%s"+quote)
%szia
>>> print("%s" quote)
SyntaxError: invalid syntax
>>> print("do you know",quote)
do you know zia
>>> print("do you know "+quote)
do you know zia
>>> quote="\"always remember you are unique"
>>> multi_line_quote='''just
know u r not a man u r a brave and bold...
u r hillarious'''
>>> quotr="\"do
SyntaxError: EOL while scanning string literal
>>> quotr="\"do
SyntaxError: EOL while scanning string literal
>>> 
>>> quotr="\do u knno the
SyntaxError: EOL while scanning string literal
>>> 
>>> print("%s"%quote)
"always remember you are unique
>>> print("%s %s %s"%('i like the quote' qoute multi_line_quote)
      
SyntaxError: invalid syntax
>>> print("%s %s %s"%('i like the quote',qoute,multi_line_quote)
      print("%s %s %s"%('i like the quote',quote,multi_line_quote)
	    
SyntaxError: invalid syntax
>>> print(multi_line_quote)
just
know u r not a man u r a brave and bold...
u r hillarious
>>> print("%s %s %s"%('i m lover boy',quote,multi_line_quote))
i m lover boy "always remember you are unique just
know u r not a man u r a brave and bold...
u r hillarious
>>> print("\n"*5)






>>> print("\n")


>>> print("\n",quote)

 "always remember you are unique
>>> print("\n",quote,"\n")

 "always remember you are unique 

>>> print(quote,"\n")
"always remember you are unique 

>>> print("i m always",=end(''))
SyntaxError: invalid syntax
>>> print("i m always",end="")
i m always
>>> print("happy")
happy
>>> print("i m always",end="")
i m always
>>> print("i m always",end="happy")
i m alwayshappy
>>> print("i m always ",end="goen to shop")
i m always goen to shop
>>> list=['mal','lungi','gamsa',50]
>>> print("4 th item is ",list[3])
4 th item is  50
>>> print("4 th item is",list[3])
4 th item is 50
>>> list[3]="balish"
>>> i=0
>>> for i<4:
	
SyntaxError: invalid syntax
>>> list2=['genji','uw']
>>> list1=list+list2
>>> print(list1)
['mal', 'lungi', 'gamsa', 'balish', 'genji', 'uw']
>>> print(list1[2:])
['gamsa', 'balish', 'genji', 'uw']
>>> rint(list1[2:1])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    rint(list1[2:1])
NameError: name 'rint' is not defined
>>> 
KeyboardInterrupt
>>> rint(list1[2:2])
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    rint(list1[2:2])
NameError: name 'rint' is not defined
>>> rint(list1[2:5])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    rint(list1[2:5])
NameError: name 'rint' is not defined
>>> print(list1[2:2])
[]
>>> print(list1[2:1])
[]
>>> print(list1[2:0])
[]
>>> print(list1[2:7])
['gamsa', 'balish', 'genji', 'uw']
>>> print(list1[:-1])
['mal', 'lungi', 'gamsa', 'balish', 'genji']
>>> print(list1[-1])
uw
>>> print(list1[-1:])
['uw']
>>> print(list1[:-1])
['mal', 'lungi', 'gamsa', 'balish', 'genji']
>>> 
==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

Traceback (most recent call last):
  File "C:/Users/HP/Desktop/fact.py", line 3, in <module>
    a=int(a)
ValueError: invalid literal for int() with base 10: ''
>>> 
==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5
120
120
>>> 120
120
>>> 5
5
>>> 
==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

Traceback (most recent call last):
  File "C:/Users/HP/Desktop/fact.py", line 3, in <module>
    a=int(a)
ValueError: invalid literal for int() with base 10: ''
>>> a
''
>>> 
==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5
 
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/fact.py", line 3, in <module>
    a=int(a)
ValueError: invalid literal for int() with base 10: ' '
>>> a=input()
2
>>> a=int(a)
>>> print(a)
2
>>> 
==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

Traceback (most recent call last):
  File "C:/Users/HP/Desktop/fact.py", line 7, in <module>
    a=int(a)
ValueError: invalid literal for int() with base 10: ''
>>> 
==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
5
5
>>>  5
 
SyntaxError: unexpected indent
>>> 5
5
>>> 
==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/fact.py", line 6, in <module>
    a=input("enter a num: ",a)
NameError: name 'a' is not defined
>>> 5
5
>>> 
[DEBUG ON]
>>> 
==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
[DEBUG OFF]
>>> 
>>> 5
5
>>> 
=============================== RESTART: Shell ===============================
>>> 
==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
Enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
enter a num:5

==================== RESTART: C:/Users/HP/Desktop/fact.py ====================
enter a num:1

Traceback (most recent call last):
  File "C:/Users/HP/Desktop/fact.py", line 3, in <module>
    a=int(a)
ValueError: invalid literal for int() with base 10: ''
>>> list1=['water','oil','firnish']
>>> list2['abba','amma','dada']
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    list2['abba','amma','dada']
NameError: name 'list2' is not defined
>>> list2=['abba','amma','dada']
>>> list=[list1,list2]
>>> print(list)
[['water', 'oil', 'firnish'], ['abba', 'amma', 'dada']]
>>> print(list[1][1:3])
['amma', 'dada']
>>> print(list[1][1:3],list[0][2])
['amma', 'dada'] firnish
>>> print(list[1][2])
dada
>>> list3=list[1][1:3]
>>> print(list3)
['amma', 'dada']
>>> list3.append("moon")
>>> print(list3)
['amma', 'dada', 'moon']
>>> list3.insert(1,"chandu")
>>> print(list3)
['amma', 'chandu', 'dada', 'moon']
>>> list3.remove('dada')
>>> print(list3)
['amma', 'chandu', 'moon']
>>> list3.sort()
>>> print(list3)
['amma', 'chandu', 'moon']
>>> list3.reverse()
>>> print(list3)
['moon', 'chandu', 'amma']
>>> del list3[0]
>>> print(list3)
['chandu', 'amma']
>>> list4=list1+list2
>>> print(len(list4))
6
>>> print(list4)
['water', 'oil', 'firnish', 'abba', 'amma', 'dada']
>>> print(max(list4))
water
>>> print(min(list4))
abba
>>> pi_tuple=(3,2,1,14,5,6,8,7,9)
>>> new=list(pi_tuple)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    new=list(pi_tuple)
TypeError: 'list' object is not callable
>>> new=list[pi_tuple]
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    new=list[pi_tuple]
TypeError: list indices must be integers or slices, not tuple
>>> pi_tuple=(3,1,4,1,5,9)
>>> new_tuple=list(pi_tuple)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    new_tuple=list(pi_tuple)
TypeError: 'list' object is not callable
>>> new_tuple=list1(pi_tuple)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    new_tuple=list1(pi_tuple)
TypeError: 'list' object is not callable
>>> print(pi_tuple)
(3, 1, 4, 1, 5, 9)
>>> print(pi_tuple(2))
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    print(pi_tuple(2))
TypeError: 'tuple' object is not callable
>>> min(pi_tuple)
1
>>> max(pi_tuple)
9
>>> new_list=tuple(pi_tuple)
>>> list1=list(new_list)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    list1=list(new_list)
TypeError: 'list' object is not callable
>>> print(new_list)
(3, 1, 4, 1, 5, 9)
>>> list(new_tuple)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    list(new_tuple)
NameError: name 'new_tuple' is not defined
>>> 
