Interview Preparation 



Python Interpreted language 
Execute and compile	
Line by line compile 
Stops at first error
O/p will display line by line 

What are the benefits of using Python?
Ans: The benefits of using python are-
    1. Easy to use– Python is a high-level programming language that is easy to use, read, write and learn.
    2. Interpreted language– Since python is interpreted language, it executes the code line by line and stops if an error occurs in any line.
    3. Dynamically typed– the developer does not assign data types to variables at the time of coding. It automatically gets assigned during execution.
    4. Free and open-source– Python is free to use and distribute. It is open source.
    5. Extensive support for libraries– Python has vast libraries that contain almost any function needed. It also further provides the facility to import other packages using Python Package Manager(pip).
    6. Portable– Python programs can run on any platform without requiring any change.
    7. The data structures used in python are user friendly.
    8. It provides more functionality with less coding.


Python Memory Manager 

Its stored python private heap space 
We can’t access 

python build-in modules?
* os
* sys
* math
* random
* data time
* JSON

Types conversion
int()str()

Pep 8 ==>  python enhancement proposal 
set of rules to Python  code 

Pip = Pip Installs Packages

Namespace
*************
Namespace is a naming system
Makesure name are unique

__init__
*********
This Method is automatically called to allocate memory when a new object/instance of a class

Self in python?
Self is a instance or an object of a class
Local variable  and  instance variable differentiates 


Python Jira, GitHub, gitlab, docker, shell scripting, postman, teleantapi, vscode PyCharm, google-colab, ngrok, putty, Filezile,


Python ALL Important 
************************

Python Indentation
*********************
Most of the programming languages like C, C++, and Java use braces { } to define a block of code. Python, however, uses indentation

For x in range():
	ghgh        ====>> syndex 

Literals
*********

String | numeric  | Booleans | special 

Recursion
***********
Function calling its self

Def bfjd():
	print(“dodged”)
	return bfjd

With Statement
*****************
File handing close()

map()
In to interable in function 


Python Document
  								Python latest version 3.10.4

https://pythonexamples.org/python-json-to-dict/
https://pythonbasics.org/
       

Why We Want to Learn?
* Data Analysis and Processing
* Artificial Intelligence
* Games
* Hardware/Sensor/Robots
* Desktop Applications

Desktop GUI Applications?

* Tkinter or Tk
* wxWidgetM
* Kivy (used for writing multitouch applications )
* PyQt or Pyside

Python Variables?
	Variable is a name that is used to refer to memory location. Python variable is also known as an identifier and used to hold value.
Camel Case
	For example - nameOfStudent, valueOfVaraible, etc
Pascal Case
	For example - NameOfStudent, etc
Snake Case
	For example - name_of_student, etc


Python copy types

* Deep copy
* Shallow copy


Python Variable Types?
	 Local variable and Global variable

Python Data Types?
str
int, float, complex
list, tuple, range
dict
set, frozenset
bool
bytes, bytearray, memoryview
NoneType

Python Strings?

	Strings indexing 
	a = “Hello”
	print(a[0])    ==> H        ==>   indexing  

	splitting
	strf = "JAVATPOINT"  
	print(strf[:]) or print(strf)  == print all,    print(strf[3:])   ===>  I don’t need first 3 char,  print(strf[:3])  ===>  I need first 3 char  print(strf[-1:])  ==> I need that last char,  print(strf[:-1])  ===> I don’t need last char
	
	Modify Strings
	a = "Hello, World!"
	print(a.upper())
	
	strip And Split
	strip only removes whitespace
	X="  Hello World!   ”
	print(x.strip())        ==     Hello World!
	Split
	# Splitting at ':'  word = 'geeks:for:geeks'  print(word.split(':'))  ==>  [‘geeks', 'for', 'geeks’]         | # Splitting at t   word = 'CatBatSatFatOr'  print(word.split('t'))  ==> ['Ca', 'Ba', 'Sa', 'Fa', 'Or']

	The format() method
		print("{} and {} both are the best friend".format("Devansh","Abhishek"))  
		print("{1} and {0} best players ".format("Virat","Rohit"))  
		print(”{a},{b},{c}”.format(a = "James", b = "Peter", c = "Ricky"))  
		print(f”sjzjsbz{asd}nscbhsbc”)

Python Operators
* Arithmetic operators.             + - / * %
* Comparison operators.          ==  != <= >=  < >
* Assignment Operators           =  +=  -=  *=
* Logical Operators                  and  or not
* Bitwise Operators                   &  | 
* Membership Operators          in  not in
* Identity Operators                  is  is not 
Difference Between List, Tuple Set and Dictionary 
Collection VS Features	Mutable	Ordered	Indexing	Duplicate Data
List	✔	✔	✔	✔
Tuple	𐄂	✔	✔	✔
Set	✔	𐄂	𐄂	𐄂
Dictionary	✔	✔	✔	𐄂

LIST VS TUPLES
*******************
Tuples are immutable	
Implication of iterations is Time-consuming	The implication of iterations is comparatively Faster
The list is better for performing operations, such as insertion and deletion.	Tuple data type is appropriate for accessing the elements
Lists consume more memory	Tuple consume less memory as compared to the list
Lists have several built-in methods	Tuple does not have many built-in methods.
The unexpected changes and errors are more likely to occur	In tuple, it is hard to take place.

Ordered means how many times we print that it will print only order 
A = [1 , 2, 'abc', 3, 'def']
Print(A)     ===>  use this print every time print the same order but set some times the order will differed

Mutable we can able to change the index posiction 
tuple1 = (0, 1, 2, 3)     tuple1[0] = 4      print(tuple1)     ====> error
list = [0,2,3,5]  list[0]= 8    print(list)  ===> [8,2,3,5]

Indexing
tuples, list, dictionary ==> a = [1, 2, 4, 6]     print(a[0]) ===>  1
set      ==> error

Duplicate Data
List and tuples = [1,2,3,2,4,1]      its working print(a) ===> [1,2,3,2,4,1]
Set	= {1,2,4,5,1,2,4}      ====> its print(a)    ===> {1,2,4,5}
Dict     ===>    Ordered collection in Python version 3.7, unordered in Python Version=3.6

List	
New Items in a list can be added using the append() method

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

Tuples
No
Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
Set	

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
Dist

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

Function 

A function is a block of code which is executed only when it is called. To define a Python function, the def keyword is used

Types of arguments
1. Required arguments
2. Keyword arguments
3. Default arguments
4. Variable-length arguments

Required Arguments
**********************
def func(name):        #name is Required Arguments
    message = "Hi "+name  
    return message  
name = input("Enter the name:")    
print(func(name))    

Dafault arguments
********************
def printme(name,age=22):     # We give the value age =22 Dafault arguments
    print("My name is",name,"and age is",age)    
printme(name = "john") 

Variable-length Arguments (*args)
*************************************
def printme(*names):     We using *name mean multiple value Variable-length Arguments
    print("printing the passed arguments...")    
    for name in names:    
        print(name)    
printme("john","David","smith","nick")    

Keyword arguments
**********************
def func(name,message):    
    print("printing the message with",name,"and ",message)    
    func(name = "John",message="hello")   #  we give key and value Keyword arguments

*args and **kwargs in Python
https://www.geeksforgeeks.org/args-kwargs-python/?ref=lbp

*args multiple Arguments 
****************************
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

**kwargs multiple key and value
**********************************
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


Python Built-in Functions
****************************
s = sum([1, 2,2 ])   5
Len() Float() list() open() print() reversed()  range() round() str() tuple() type() dir() enumerate()
Dict() min() set() slice() sorted() input() int() help()
eval()
x = 5  
print(eval('x + 1'))  

Python Lambda Functions
************************
An anonymous function is known as a lambda function. This function can have any number of parameters but, can have just one statement

lambda arguments: expression  

x = lambda a:a+10 
print(x(20))  

Give Another Way
df = (lambda x: x*4)(3)
print(df)

Python Lambda function is known as the anonymous function that is defined without a name

showing difference between def() and lambda()

def()
def cube(y):
	return y*y*y
print(cube(5))
Lamda
lambda_cube = lambda y: y*y*y
print(lambda_cube(5))
EX:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
Function with lama
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

If else
vm = 78
nwe = (lambda v: "biggest" if (v > 80) else "yes")(vm)
print(nwe)


without using for loop we using lama filter and map function 
Sample code  for filter (normal syntax)
new =[]
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
for x in mylist:
    if x %2 == 0:
        new.append(x)
    else:
        continue
print(new)

Filter with Lamda
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

Sample code  for map (normal syntax)
new =[]
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
for x in mylist:
    	x *2 
        new.append(x)
print(new)

Filter with Map
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)

Python Filters Functions
***************************
filter (function, iterable)  

def fun(variable):
	letters = ['a', 'e', 'i', 'o', 'u']
	if (variable in letters):
		return True
	else:
		return False
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence)
for s in filtered:
	print(s)
Lamda
seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

Python Map Functions
************************
def addition(n):
	return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
Lamda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

Python difference between filter() and map()
*********************************************

print(list(map(lambda num: "Even" if(num % 2 == 0) else "Add", num_list)))
print(list(filter(lambda num: num % 2 == 0 , num_list)))


As per my understanding below are the difference between map and filter:	
def even(num):
    if(num % 2 == 0):
        return 'Even'
num_list = [1,2,3,4,5]
print(list(filter(even,num_list))) ->>>>>>>output: [2, 4]
print(list(map(even,num_list))) ->>>>>>> output: [None, 'Even', None, 'Even', None]

Python File Handling
**********************
* Open a file
* Read or write - Performing operation
* Close the file

Python Modules
*********************
                                                       Code reusable 

A python module can be defined as a python program file which contains a python code including python functions, class, or variables. In other words, we can say that our python code file saved with the extension (.py) is treated as the module. We may have a runnable code inside the python module

Ex:
calculation.py
def summation(a,b):  
    return a+b  
Main.py
from calculation import summation    
a = int(input("Enter the first number"))  
b = int(input("Enter the second number"))  
print("Sum = ",summation(a,b))

from <module> import *   
import <module-name> as <specific-name>   


Python __init__.py(https://www.youtube.com/watch?v=wMTO8K1kG7Y)
Tamil  (https://www.youtube.com/watch?v=HFDJF9IEoJc)
Folder name function 
In that folder we have new.py in that py we have def add()

Outside of the folder we create main.py in that py we import below method to access the folder

1  ==> from function.new import add              print(add())
2  ==> from function import new                     print(new.add())

Outside of the folder we need to access all files

import function as fd                    print(fd.new.add())              ==== not working

So we need to create a __init__.py file in that function folder  and we call all function in that directory 

from .new import add

Main.py file 

import function as fd          print(fd.add())          === now we can get 

Python 3.2.0 blow only we use this      The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach

1st ===>       We need to create	a folder name   Employee	
2nd ===>     in that Employee folder we create a two  python file  calculate.py      and      __init__.py
3rd ===>      create a functions link blow

In that  calculate.py
def getITNames():  
    List = ["John", "David", "Nick",    "Martin"]  
    return List;  

In that  __init__.py 
from  calculate  import getITNames  

Now, the directory Employees has become the package containing two python modules

Python Exception
*******************
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

Python Date and time
***********************
* date - It is a naive ideal date. It consists of the year, month, and day as attributes.
* time - It is a perfect time, assuming every day has precisely 24*60*60 seconds. It has hour, minute, second, microsecond, and tzinfo as attributes.
* datetime - It is a grouping of date and time, along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.
* timedelta - It represents the difference between two dates, time or datetime instances to microsecond resolution.
* tzinfo - It provides time zone information objects.
* timezone - It is included in the new version of Python. It is the class that implements the tzinfo abstract base class.

import time 
print(time.time())

import datetime  
print(datetime.datetime.now())    

import calendar;    
cal = calendar.month(2020,3)    
print(cal) 

import calendar    
s = calendar.prcal(2020)

Python Regular Expressions
******************************
Function	Description
match	This method matches the regex pattern in the string with the optional flag. It returns true if a match is found in the string otherwise it returns false.
search	This method returns the match object if there is a match found in the string.
findall	It returns a list that contains all the matches of a pattern in the string.
split	Returns a list in which the string has been split in each match.
sub	Replace one or many matches in the string.

import re  
str = "How are you. How is everything"  
matches = re.findall("How", str)  
print(matches)  

Python Sending Email using SMTP
  
import smtplib    
sender_mail = 'sender@fromdomain.com'    
receivers_mail = ['reciever@todomain.com']    
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receivers_mail)    
try:    
   smtpObj = smtplib.SMTP('localhost')    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")    

Python List Comprehension
Loop with list
sd = [x for x in range(4)]
print(sd)

newlist = [expression for item in iterable if condition == True] 

NORMAL
def for_loop(num):  
    l = []  
    for i in range(num):  
        l.append(i + 10)  
    return l 

Using list comprehension
def list_comprehension(num):  
    return [i + 10 for i in range(num)] 

Python OS Module

import os  
os.mkdir("d:\\newdir") 

import os     
print(os.getcwd())   

Python Random module
import random  
print (random.randrange(100, 500, 10))  

import random  
print (random.choice([50, 41, 84, 40, 31]))  

Python LIst vs Array
List	Array
Can consist of elements belonging to different data types	Only consists of elements belonging to the same data type
No import a module 	Need to explicitly import a module for declaration
Cannot directly handle arithmetic operations	Can directly handle arithmetic operations
Greater flexibility allows easy modification (addition, deletion) of data	Less flexibility since addition, deletion has to be done element wise
The entire list can be printed without any explicit looping	A loop has to be formed to print or access the components of array
Consume larger memory for easy addition of elements	Comparatively more compact in memory size


Python Stack and Queue
************************* Stack
A Stack is a data structure that follows the LIFO(Last In First Out) principle. To implement a stack, we need two simple operations
 Push and pop
x = ["Python", "C", "Android"]   
x.push("Java")   
print(x)  
print(x.pop()) 

Queue
A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front
import queue   
L = queue.Queue(maxsize=10)   
L.put(9) 
print(L.get())   

What is Web Scraping?
Web Scraping is a technique to extract a large amount of data from several websites

* Selenium- Selenium is an open-source automated testing library. It is used to check browser activities. To install this library, type the following command in your terminal.
* Pandas
Pandas library is used for data manipulation and analysis. It is used to extract the data and store it in the desired format.
* BeautifulSoup
BeautifulSoup is a Python library that is used to pull data of HTML and XML files. It is mainly designed for web scrapping. It works with the parser to provide a natural way of navigating, searching, and modifying the parse tree. The latest version of BeautifulSoup is 4.8.1
  
Python Multiprocessing $ Multithreading
******************************************

Multiprocessing is the ability of the system to run one or more processes in parallel. In simple words, multiprocessing uses the two or more CPU

within the single computer system

Python
provides the built-in package called multiprocessing which supports swapping processes. Before working with the multiprocessing, we must aware with the process object.

import multiprocessing

def print_cube(num):
	print("Cube: {}".format(num * num * num))
def print_square(num):
	print("Square: {}".format(num * num))
if __name__ == "__main__":
	# creating processes
	p1 = multiprocessing.Process(target=print_square, args=(10, ))
	p2 = multiprocessing.Process(target=print_cube, args=(10, ))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print("Done!")

What does the if __name__ == “__main__”: do? (https://www.youtube.com/watch?v=IeOi4lC_gN4&t=15s/)

Def nam(a, b):
	return a+ b

print(nam(2, 5)

This is our function we used to add two values so we print that 
We run this code our output link 7
Incase  we  want to use that function we import py like

From py_file_name import nam

Print(nam(5, 7)
Without  if  __name__==“__main__:
We print   7 and 12
We use if  __name__==“__main__:
We print 12

Python Decoraters

Python that allows a user to add new functionality to an existing object without modifying its structure.

Way 1
def div(a,b):
    return a/b

def new_cha(func):
    def inner(a,b):
        if a < b:
            new_a, new_b = b,a
            return func(new_a, new_b)
        else:
            return func(a, b)
    return inner

df = new_cha(div)
print(df(2,4))

Way 2
def new_cha(func):
    def inner(a,b):
        if a < b:
            new_a, new_b = b,a
            return func(new_a, new_b)
        else:
            return func(a, b)
    return inner

@new_cha
def div(a,b):
    return a/b

print(div(2,4))

Oops Python (https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming/)
*******************

Class
 A class is a collection of objects or you can say it is a blueprint of objects defining the common attributes and behaviour 
Class name.    ===> two things 
Attributes and behaviour ==> 
Attributes == variables
behaviour == Methods(functions)

Object	

Every thing is a objects ex: dog ,mouse, laptop, persons 

For example, a car can be an object. If we consider the car as an object then its properties would be – its colour, its model, its price, its brand, etc. And its behaviour/function would be acceleration, slowing down, gear change


Inheritance (https://www.youtube.com/watch?v=poMVuz0zndM)
Single, multiple, multilevel,  Hierarchical, hybrid 

Create a relationship between  parents class and child class called Inheritance
                                                (or)
Deriving the child the class from the parent class

class version1:
    def v1(self):
        print('Button')
        print('text box')
class version2(version1): # Inheritance
    def v2(self):
        print('Drop down list')
if __name__ == '__main__':
    app = version2()
    app.v1()
    app.v2()

Polymorphism (https://www.youtube.com/watch?v=Jp-RjCPx_vA)

Poly = many
Morphism =  different behaviour

class version1:
    def button (self):
       print("colour Red")
class version2(version1):
    def button (self):                                        Method over write.   Same function give different value
        print("colour yellow")
#instantiate objects
a=version2 ()
a.button()


Encapsulation in Python (https://www.youtube.com/watch?v=n5oPKHyJvrU&t=954s)
***********************************

A class is an example of encapsulation as it encapsulates all the data that is member functions,
variables, etc.

Public and private   ===>  use to secure the data

Public 
******
class Bank:
    def ram(self):             #public any one can access
        print("Name:Ram")
        print("A/C No:12345")
        print("Amount:10000")
        print("Address:Salem")
    def sam(self):		 #public any one can access
        print("Name:Sam")                
        print("A/C No:12346")
        print("Amount:15000")
        print("Address:Chennai")
obj=Bank()
obj.ram()

Private
*******
1.class Bank:
    def __init__(self):
        self.__value = 10
    def ram(self):
        print("Name:Ram")
        print("A/C No:12345")
        print("Amount:10000")
        print("Address:Salem")
    def sam(self):
        print("Name:Sam")
        print("A/C No:12346")
        print("Amount:15000")
        print("Address:Chennai")
obj=Bank()
obj.ram()
Print(“value”, obj.value)          # we cont access     so we to change

2.class Bank:
    def __init__(self):
        self.__value = 10
    def ram(self):
        print(self.__value)
        print("Name:Ram")
        print("A/C No:12345")
        print("Amount:10000")
        print("Address:Salem")
obj=Bank()
obj.ram()                                   # now you got that output

3.class Bank:
    def __ram(self):                #new change
        print("Name:Ram")
        print("A/C No:12345")
        print("Amount:10000")
        print("Address:Salem")
    def sam(self):
        print("Name:Sam")
        print("A/C No:12346")
        print("Amount:15000")
        print("Address:Chennai")
obj=Bank()
obj.ram()           # we cont acces

4.class Bank:
    def __init__(self):
        self.__value = 10
    def __ram(self):
        print(self.__value)
        print("Name:Ram")
        print("A/C No:12345")
        print("Amount:10000")
        print("Address:Salem")
    def sam(self):
        self.__ram()                         # now we can access
        print("Name:Sam")
        print("A/C No:12346")
        print("Amount:15000")
        print("Address:Chennai")
obj=Bank()
obj.sam()

Another Method
*****************
class Bank:
    def __ram(self):                        # private function
        print("Name:Ram")
        print("A/C No:12345")
        print("Amount:10000")
        print("Address:Salem")
    def sam(self):
        print("Name:Sam")
        print("A/C No:12346")
        print("Amount:15000")
        print("Address:Chennai")

obj=Bank()
obj._Bank__ram()

Python Abstraction(https://www.youtube.com/watch?v=g6nTTPgTCRI&t=28s)
****************************

Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user
Abstraction is used to hide the internal functionality of the function
from the users.
The users only interact with the basic implementation of the function,
but inner working is hidden

Internal (process)function ex:pandas is a package ex:Atm

Python __init__
*****************
__init__ is a method or constructor in Python. This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ method

The __init__ method is similar to constructors in C++ and Java. Constructors are used to initialize the object’s state 

# A Sample class with init method
class Person:
	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()


Python JSON

JSON stands for JavaScript Object Notation, which is a widely used data format for data interchange on the web

import json  
#Python  list conversion to JSON  Array   
print(json.dumps(['Welcome', "to", "javaTpoint"]))  
#Python  tuple conversion to JSON Array   
print(json.dumps(("Welcome", "to", "javaTpoint")))  
# Python string conversion to JSON String   
print(json.dumps("Hello"))  
# Python int conversion to JSON Number   
print(json.dumps(1234))  
# Python float conversion to JSON Number   
print(json.dumps(23.572))  
# Boolean conversion to their respective values   
print(json.dumps(True))  
print(json.dumps(False))  
# None value to null   
print(json.dumps(None))   

Python Iterable
***************
Iterators are objects which can be traversed though or iterated upon

(loop) another name
Ex:
d = { "one”, "two”, "three", "four", "five" }
iterator = iter(d)
print( next(iterator) )                 ===>> loop one by one
print( next(iterator) )
 

Types Of Method in Python

InstanceMethod $ classmethod $ staticmethod  (https://www.youtube.com/watch?v=XBQayMyMlb0)
**************************************************

classmethod:

class Fruit:
    name = 'Fruitas'
    @classmethod
    def printName(cls):
        print('The name is:', cls.name)
Fruit.printName()
classmethod :
class Fruit:
    name = 'Fruitas'
    def printName(cls):
            print('The name is:', cls.name)
Fruit.printAge = classmethod(Fruit.printName)                ====> avoid this line
Fruit.printAge()

staticmethod:
class Music:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")

Music.play()

obj = Music()
obj.stop()


Python Enumerate

# create a sequence
browsers = ['Chrome','Firefox','Opera','Vivaldi']

# create an enumeratable and convert to list
x = list(enumerate(browsers))
print(x)

fruits = [ "Apple","Berry","Cherry" ]
for i,j in enumerate(fruits):
	print(i,j)

for i,j in enumerate(fruit, start=2):         ====> start with 2

Python Pickel
Pickle can be used to serialize and deserialize objects. A seralized object can be saved and loaded from the disk. Pickling is a method to convert an object (list, dict, etc) to a file and vice versa

import pickle
exampleObj = {'Python':3,'KDE':5,'Windows':10}
fileObj = open('data.obj', 'wb')
pickle.dump(exampleObj,fileObj)                                =====>> dump
fileObj.close()

import pickle   
fileObj = open('data.obj', 'rb')
exampleObj = pickle.load(fileObj)                               =====>> load
fileObj.close()
print(exampleObj)

Python magic comments
*************************
https://www.educative.io/edpresso/what-is-the-str-method-in-python

Python list object and x range returns an xrange object
Range vs Xrange


Python namespace

Memory Management
Memory management in python is managed by Python private heap space
A namespace is a naming system used to make sure that names are unique to avoid naming conflicts

We dint mention size and type python memory management it will take care   

A = 10)
print(id(10), id(a))

Both address are same 

Literals
1. string literals– A string literal is created by assigning some text enclosed in single or double quotes to a variable. To create multiline literals, assign the multiline text enclosed in triple quotes. Eg.name=”Tanya”
2. A character literal– It is created by assigning a single character enclosed in double quotes. Eg. a=’t’
3. Numeric literals include numeric values that can be either integer, floating point value, or a complex number. Eg. a=50
4. Boolean literals– These can be 2 values- either True or False.
5. Literal Collections


python case sensitive?    Yes
 
How can you randomize the items of a list in place in Python?       from random import shuffle

How can you generate random numbers in Python?    Import random       random.radom

What are the generators in python?
https://www.youtube.com/watch?v=-2-omZ5j9_0
https://www.youtube.com/watch?v=mziIj4M_uwk

What are docstrings in Python?  “”””””

 datatypes in Python 

Ternary Operator in Python  [on_true] if [expression] else [on_false] 

How can files be deleted in Python?   Os.remove()

What are the built-in types of python?
* Integers
* Floating-point
* Complex numbers
* Strings
* Boolean
* Built-in functions

How to add values to a python array?
a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.append(3.4)
print(a)
a.extend([4.5,6.3,6.8])
print(a)
a.insert(2,3.8)
print(a)

 How to remove values to a python array?
Ans: Array elements can be removed using pop() or remove() 

What is split used for?
The split() method is used to separate a given String in Python
a="edureka python"
print(a.split())

How to import modules in python?
From py_namr import *        == import all
From py_namr import fction_name      === function 
Import folder_all as fd            ====  import full folder and using __init__.py

How are classes created in Python? 
Ans: Class in Python is created using the class keyword.
class Employee:
def __init__(self, name):
self.name = name
E1=Employee("abc")
print(E1.name)

Does python support multiple inheritance?
Ans: Multiple inheritance means that a class can be derived from more than one parent classes. Python does support multiple inheritance, unlike Java.

How to create an empty class in Python? 
class a:
  pass
obj=a()
obj.name="xyz"
print("Name = ",obj.name)

 Write a program in Python to execute the Bubble sort algorithm
def bs(a):
# a = name of list
   b=len(a)-1nbsp; 
# minus 1 because we always compare 2 adjacent values
   for x in range(b):
        for y in range(b-x):
              a[y]=a[y+1]
   
   a=[32,5,3,6,7,54,87]
   bs(a)

Write a program in Python to produce Star triangle
r =5
for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1)) 
Fibonacci series in Python. 
Write a program in Python to check if a number is prime  a%2==0 not prime
Write a program in Python to check if a sequence is a Palindrome   323   a[::-1]
Write a sorting algorithm for a numerical dataset in Python a.sort()   second large  a.sort()  a[-2]



Web framework 
*****************

Wsgi vs Asgi  (https://www.youtube.com/watch?v=LtpJup6vcS4)

API

API is the Application Programming Interface, which is a software intermediary that allows two applications to talk to each other
One of their jobs is to handle incoming requests from the client
Handle   File  ||  Form  || Text  || Json  ||  xml   ||  Html  ||   query-parameters

RESTAPI   Representational state transfer

REST API is an architectural style for building web services that interact via an HTTP protocol
Http Request get post put delete 
		GET request to retrieve a record,
		POST request to create one, 
		PUT request to update a record, 
		DELETE request to delete one. 

Flask   port:8000  
******************
* Built-in web server and debugger
* Web Server Gateway Interface(WSGI) compliance
* Flask is lightweight and modular
* It is very easy to deploy Flask in production as Flask comes with 100% WSGI 1.0 support
* Integrated support for unit testing
* Community Support large
* More Flexibility 
* RESTful request dispatching
* Jinja2 Templating

FastApi   port:5000
*********************
* ASGI (Asynchronous Server Gateway Interface)
* Asynchronous Framework 
* Data verification using Pydantic Basemodel
* Handle microservices 
* Faster Performance and very Speed
* Interactive Doc it’s have OpenApi (Swagger, Redoc)
* Development cost very low
* Community Support Small
* Automatic data model documentation with Json_Schema
* No inbuilt server Uvicorn is an ASGI web server implementation for Python

Flask vs Fastapi
￼
Api Token In FastApi using JWT (
￼
Securing FastAPI with JWT Token-based Authentication )
step1:
first we need to create a .env file in our env 
into the file we give

secret_key = hdbkjsdmjskbjhdjhjdhjdhfjdgjd
algorithm = HS256

Api Ratelimit
**************
fastapi-limiter - PyPI
Slowapi

 	1xx: Informational – Communicates transfer protocol-level information.
	2xx: Success – Indicates that the client’s request was accepted successfully.
	3xx: Redirection – Indicates that the client must take some additional action in order to complete their request.
	4xx: Client Error – This category of error status codes points the finger at clients.
	5xx: Server Error – The server takes responsibility for these error status codes.

      MAP Document
*************************

https://towardsdatascience.com/make-beautiful-spatial-visualizations-with-plotly-and-mapbox-fd5a638d6b3c

https://towardsdatascience.com/meet-plotly-mapbox-best-choice-for-geographic-data-visualization-599b514bcd9a

Many traces on same plot in plotly express


https://stackoverflow.com/questions/60910962/is-there-any-way-to-draw-india-map-in-plotly


https://discuss.streamlit.io/t/ann-streamlit-folium-a-component-for-rendering-folium-maps/4367

Need to learn 
*********************


1. TensorFlow 
2. Keras
3. PyTroch
  4. Scikit-learn Python
  5. Python Pandas
  6 . NumPy Python

frame = frame[500:700, 500:1300]


Poly Line 
*********

https://stackoverflow.com/questions/57312028/problem-with-using-cv2-pointpolygontest-and-cv2-polylines


CNN MODEL  *************

IMAGE Classification 

https://www.youtube.com/watch?v=ejkRh9obVjk

https://www.youtube.com/watch?v=7MceDfpnP8k

Data Augmentation
*********************

https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks


Method 

1. https://www.analyticsvidhya.com/blog/2021/08/image-classification-using-cnn-understanding-computer-vision/

2. https://www.analyticsvidhya.com/blog/2021/06/develop-your-first-image-classification-project-with-convolutional-neural-network/

3. https://www.analyticsvidhya.com/blog/2021/01/image-classification-using-convolutional-neural-networks-a-step-by-step-guide/



Pre-Training Model

https://www.analyticsvidhya.com/blog/2020/08/top-4-pre-trained-models-for-image-classification-with-python-code/

DevOps
https://www.edureka.co/blog/docker-commands/#run
      
      
AI projects Details


AI   VS    ML    VS    DL    vs    DATA-Science
*******************************************
https://www.youtube.com/watch?v=k2P_pHQDlp0
https://www.geeksforgeeks.org/8-best-topics-for-research-and-thesis-in-artificial-intelligence/

Machine Learning 
****************************
https://www.geeksforgeeks.org/machine-learning/
https://www.simplilearn.com/10-algorithms-machine-learning-engineers-need-to-know-article

￼
Supervised learning
*********************
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

regression-classification
**************************
https://www.geeksforgeeks.org/regression-classification-supervised-machine-learning/

Unsupervised Learning   in   clustering        
****************************************
https://www.geeksforgeeks.org/clustering-in-machine-learning/

Reinforcement Learning 
**************************
https://www.youtube.com/watch?v=Mut_u40Sqz4

Deep Learning 
***********************
Depp learning?
****************
https://www.youtube.com/watch?v=6M5VXKLf4D4

Deep learning CNN
*********************
https://www.simplilearn.com/tutorials/deep-learning-tutorial/convolutional-neural-network\

Deep learning RNN
*********************
https://www.simplilearn.com/tutorials/deep-learning-tutorial/rnn

Deep learning GANs
*********************
https://www.simplilearn.com/tutorials/deep-learning-tutorial/generative-adversarial-networks-gans


Face Recognition 
	
		Face detection Method 
		Liveness Detection
		Face to binary encoding 
		Face Matching 

Face Detection Method or Algorithms 
*****************************************
https://bleedai.com/5-easy-effective-face-detection-algorithms-in-python/
	
Haar Cascade Face Detection 
Dlip
CNN
DNN
MTCNN
Media-pipe

Liveness Detection
**********************
 https://github.com/ee09115/spoofing_detection

Face to binary encoding 
**************************

Face recognition
Arc face
Dlip
Face net 
Deep face
Face Matching 
****************


NLP
*****
https://www.analyticsvidhya.com/blog/2022/01/roadmap-to-master-nlp-in-2022/

https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/

Text Preprocessing
      



Chatbot
**************

We have Two Method 


First Method


1.  https://www.youtube.com/watch?v=9KZwRBg4-P0    
2. https://github.com/Sourabhhsethii/Building-a-simple-chatbot-in-python


Second Method 

1.  https://realpython.com/python-speech-recognition/


Video link
***********

https://www.youtube.com/watch?v=SCk7onPrrwk

				       
				       
				       
				       
