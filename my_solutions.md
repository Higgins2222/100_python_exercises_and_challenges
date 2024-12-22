**Question 1**

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

```python
print(', '.join([str(x) for x in range(2000, 3200) if x % 7 == 0 and not x % 5 == 0]))
```

**Question 2**

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

```python
def factorial(n):
    print(str(n) + "! = ", end='')
    result = n if n else 1           # To handle the 0 factorial case
    while n > 1:
        n -= 1
        result *= n
    print(str(result))

factorial(int(input('Enter a number to find its factorial: ')))
```

**Question 3**

With a given integral number n, write a program to generate a dictionary that contains (i, i\*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

```python
def square_dictionary(n):
    r = {}
    for i in range(1, n + 1):
        r[i] = i ** 2
    return r

print(square_dictionary(int(input('Enter a number to get a list of squuares up to and including that number: '))))
```

**Question 4**

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

```python
def gen_tuple_and_list(n: str):
    n = n.split(',')
    list_of_nums = n
    tuple_of_nums = tuple(n)

    print(list_of_nums)
    print(tuple_of_nums)

gen_tuple_and_list(input('Enter a sequence of numbers seperated by a comma with no space: '))
```

**Question 5**

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

```python
class ucasePrinter:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input('Enter a string: ')
    def printString(self):
        print(self.string.upper())

myinstance = ucasePrinter()
myinstance.getString()
myinstance.printString()
```

**Question 6**

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 \* C \* D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

```python
import math

values = input('Enter a comma seperated list of integers: ')
values = [int(x) for x in values.split(',')]

c = 50
h = 30
q = []

for d in values:
    q.append(round(math.sqrt(((2 * c * d)/h)), 0))

print(','.join([str(int(x)) for x in q]))
```

**Question 7**

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i\*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

```python
mylist = []

prompt = input('Enter two digits seperated by a comma:').split(',')
prompt = [int(x) for x in prompt]
assert(len(prompt)==2)
assert(prompt[0].isint() and prompt[1].isint())

for i in range(prompt[0]):
    mylist.append([])
    for j in range(prompt[1]):
        mylist[i].append(i*j)

print(mylist)
```
**Question 8**

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

```python
prompt = sort(input('Enter a comma seperated list of words'))

print(','.join(prompt))
```

**Question 9**

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

```python
messages = []
while True:
    next_msg = input('Provide a phrase: ')
    if next_msg:
        messages.append(next_msg)
    else:
        break

for s in messages:
    print(s.upper())
```

**Question 10**

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

```python
sorted_words = sorted(set(input('words: ').split(' ')))

print(sorted_words)
```

**Question 11**

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

```python
prompt = input('4 digit binary numbers (comma seperated): ').split(',')

for p in prompt:
    num = 0
    for i, c in enumerate(p):
        num += int(c) * 2 ** (3 - i)

value = []
for p in prompt:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))
```

**Question 12**

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

```python
from math import floor

result = []
for x in range(1000, 3000):
    if floor((x / 1000)) % 2 == 0:
        if floor((x / 100)) % 2 == 0:
            if floor((x / 10)) % 2 == 0:
                if x % 2 == 0:
                    result.append(str(x))
print(','.join(result))
```

**Question 13**

Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

```python
prompt = input('Enter text with numbers, letters, and characters: ')

letters, digits = 0, 0
for c in prompt:
    letters += 1 if c.isalpha() else 0
    digits += 1 if c.isdigit() else 0

print(f'{letters=}, {digits=}')
```

**Question 14**

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

```python
prompt = input().strip()
upper, lower = 0, 0

for char in prompt:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    else:
        pass

print("UPPER CASE " + str(upper))
print("LOWER CASE " + str(lower))
```

**Question 15**

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

```python
value = int(input('Enter a number: '))

expr = 'a+aa+aaa+aaaa'.replace('a', str(value))

print(eval(expr))
```

**Question 16**

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

```python
prompt = [int(x) for x in input('Enter a sequence of comma seperated numbers: ').split(',')]

squares = [n**2 for n in prompt if n % 2]

print(squares)
```
**Question 17**

Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

```python
account = 0
while True:
    next_msg = input('enter "D x" to deposit and "W x" to withdraw, where x is any positive integer: ')
    if next_msg.startswith('D'):
        account += int(next_msg[2:])
    elif next_msg.startswith('W'):
        account -= int(next_msg[2:])
    else:
        break

print(account)
```
**Question 18**

A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E\*,2We3345
Then, the output of the program should be:
ABd1234@1

```python
special_characters = ['$', '#', '@']


prompt = input('Enter a comma seperated list of passwords (no spaces): ').split(',')
valid_passwords = []
for p in prompt:
    req_lower, req_upper, req_number, req_special = False, False, False, False
    valid = False

    if not (len(p) >= 6 and len(p) <= 12):
        break

    for c in p:
        if c.isupper():
            req_upper = True
        elif c.islower():
            req_lower = True
        elif c.isdigit():
            req_number = True
        elif c in special_characters:
            req_special = True
        if req_upper and req_lower and req_number and req_special:
            valid = True
            valid_passwords.append(p)
            break
        print()

print(valid_passwords)
```
**Question 19**

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

```python
records = []

get_next = (msg for msg in ['mike,22,40', 'mike,30,50', 'mike,40,40', 'mike,23,40', 'mike,23,50', 'mike,30,40','april,12,15', 'april,1,15', 'april,30,15', ''])

while True:
    #prompt = input('Enter Name, Age, and height (comma seperated): ')
    prompt = next(get_next)
    if prompt == '':
        break
    else:
        records.append(tuple(prompt.split(',')))

records.sort(key=lambda x: x[2])
records.sort(key=lambda x: x[1])
records.sort(key=lambda x: x[0])

#gpt:
records.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))


print(records)
```

**Question 20**

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

```python
class nums_div_7:
    def __init__(self, maximum):
        self.num = 0
        self.max = maximum

    def __iter__(self):
        return self

    def __next__(self):
        self.num = self.num + 7
        if self.num > self.max:
            raise StopIteration
        return self.num

n = int(input('Enter a positive number: '))
for i in nums_div_7(n):
    print(i)
```

**Question 21**

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

```python
from math import sqrt

UP = 5
DOWN = 3
LEFT = 3
RIGHT = 2

y_dir = abs(UP - DOWN)
x_dir = abs(RIGHT - LEFT)

distance = sqrt(x_dir ** 2 + y_dir ** 2)

print("distance: " + str(round(distance)))
print("\n\n")
```

**Question 22**

Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

```python
words = {}
line = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

for word in line.split():
    words[word] = words.get(word,0) + 1

wordlist = sorted(words.keys())

for w in wordlist:
    print("%s:%d" % (w,words[w]))
```

**Question 23**

    Write a method which can calculate square value of number

```python
def square_num(n):
    return n ** 2
```

**Question 24**

    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function
    

```python
print(f'abs(num)\n{abs.__doc__}\n')
print(f'int(string)\n{int.__doc__}\n')
print(f'input(string)\n{input.__doc__}\n')
```

**Question 25**

    Define a class, which have a class parameter and have a same instance parameter.

```python
class MyClass:
    param = "Class" # Class parameter

    def __init__(self, param):
        self.param = param # Instance Parameter

myobject = MyClass("Instance")
print(MyClass.param) # Output: Class
print(myobject.param) # Output: Instance
```

**Question 26**

Define a function which can compute the sum of two numbers.

```python
def sum(a, b):
    return a+b
```

**Question 27**

Define a function that can convert a integer into a string and print it in console.

```python
def convert_and_print(n):
    print(str(n))
```

**Question 28**

Define a function that can convert a integer into a string and print it in console.

```python
def convert_and_print(n):
    print(str(n))
```

**Question 29**

Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

```python
def sum(a_string, b_string):
    return int(a_string) + int(b_string)
```

**Question 30**

Define a function that can accept two strings as input and concatenate them and then print it in console.

```python
def cat(a_string, b_string)
    print(str(a_string) + str(b_string))
```

**Question 31**

Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

```python
def print_longest_or_both(string1, string2):
    print(string1 if len(string1) >= len(string2) else string2)
    print(string2+'\n' if len(string1) == len(string2) else '', end='')
```

**Question 32**

Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

```python
def print_oddoreven(n)
    print('It is an even number' if not n % 2 else 'It is an odd number.'
```

**Question 33**

Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.


```python
def dictionary_print():
    mydict = {x: x*x for x in range(1, 4)}
    print(mydict)
```

**Question 34**

Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

```python
def dictionary_print():
    mydict = {x: x*x for x in range(1, 21)}
    print(mydict)
```

**Question 35**

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

```python
def dictionary_print():
    mydict = {x: x*x for x in range(1, 21)}
    values = [str(x) for x in list(mydict.values())]
    print(' '.join(values))
```

**Question 36**

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

```python
def dictionary_print():
    mydict = {x: x*x for x in range(1, 21)}
    values = [str(x) for x in list(mydict.keys())]
    print(' '.join(values))
```

**Question 37**

Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

```python
def list_print():
    li = [x for x in range(1, 21)]
    print(li)
```

**Question 38**

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

```python
def list_print():
    li = [x*x for x in range(1, 21)]
    print(li[0:5])
```

**Question 39**

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

```python
def list_print():
    li = [x*x for x in range(1, 21)]
    print(li[-5::])
```

**Question 40**

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

```python
def list_print():
    li = [x*x for x in range(1, 21)]
    print(li[5::])
```

**Question 41**

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

```python
def tuple_gen():
    t = tuple(x*x for x in range(1, 21))
```

**Question 42**

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

```python
# If len of prompt is odd we will choose not to print the middle value, as the problem doesn't specify but that's the best guess for 'half'
prompt = (1,2,3,4,5,6,7,8,9,10)
print(prompt[0:len(prompt) // 2])
print(prompt[len(prompt) // 2 + len(prompt) % 2::])
```

**Question 43**

Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

```python
prompt = (1,2,3,4,5,6,7,8,9,10)
t = tuple(x for x in prompt if x % 2 == 0)
print(t)
```

**Question 44**

Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

```python
prompt = input('Enter yes, Yes, or YES: ')
print('Yes' if prompt == 'yes' or prompt == 'Yes' or prompt == 'YES' else 'No')
```

**Question 45**

Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

```python
prompt = [1,2,3,4,5,6,7,8,9,10]

li = list(filter(lambda x: x % 2 == 0, prompt))
```

**Question 46**

Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

```python
prompt = [1,2,3,4,5,6,7,8,9,10]

result = list(map(lambda x: x*x, prompt))
```

**Question 47**

Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

```python
prompt = [1,2,3,4,5,6,7,8,9,10]

result = filter(lambda x: x % 2 == 0, prompt)
result = list(map(lambda x: x*x, li))
```

**Question 48**

Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

```python
prompt = [x for x in range(1, 21)]

result = list(filter(lambda x: x % 2 == 0, prompt))
```

**Question 49**

Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

```python
prompt = [x for x in range(1, 21)]

result = list(map(lambda x: x*x, prompt))
```

**Question 50**

Define a class named American which has a static method called printNationality.

```python
class American:
    def printNationality(self):
        print(type(self))
```

**Question 51**

Define a class named American and its subclass NewYorker. 

```python
class American:
    def printNationality(self):
        print(type(self))

class NewYorker(American):
    def printNationality(self):
        print('Get Outta Here!')
```

**Question 52**

Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

```python
class Circle:
    def __init__(self, r):
        self.radius = r
```

**Question 53**

Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
```

**Question 54**

Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

```python
class Shape:
    def __init__(self):
        self.area = 0

    def print_area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        self.__length = length
        self.__width = length
        self.__area = self.length * self.width
```

**Question 55**

Please raise a RuntimeError exception.

```python
raise(RuntimeError)
```

**Question 56**

Write a function to compute 5/0 and use try/except to catch the exceptions.

```python
a, b = 5, 0
try:
    print(a / b)
except ZeroDivisionError:
    print('Division by zero is not advised.')
except:
    print('basic maths broke.')
```

**Question 57**

Define a custom exception class which takes a string message as attribute.

```python
class myexception(Exception):
    def __init__(self, msg):
        print(msg)

raise myexception('ohno!')
```

**Question 58**


Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

```python
import re

prompt = input('Enter an email address: ')
pattern = r"(.*)@+(.*)\.+(.*)"

match = re.search(pattern, prompt, re.DOTALL)

print(match[1] if match else 'Email format not recognized')
```

**Question 59**


Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

```python
import re

prompt = input('Enter an email address: ')
pattern = r"(.*)@+(.*)\.+(.*)"

match = re.search(pattern, prompt, re.DOTALL)

print(match[2] if match else 'Email format not recognized')
```

**Question 60**


Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be a console input.

```python
prompt = input('Enter a sequence of words separated by whitespace: ').split( )
result = []

for word in prompt:
    if word.isdigit():
        result.append(word)

print(result)
```

**Question 61**



Print a unicode string "hello world".

```python
print("hello world") # Python 3 is unicode by default
```

**Question 62**

Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

```python
# Will throw an exception if non-ascii chars are present
prompt = input('Enter some ascii text: ').encode('ascii')

result = prompt.encode('utf-8')
```

**Question 63**


Write a special comment to indicate a Python source code file is in unicode.

```python
# -*- coding: utf-8 -*-
```
**Question 64**


Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.

```python
prompt = int(input('Enter an integer:'))
result = 0.0

for i in range(1, prompt + 1):
    result += i / (i+1)

print(f'{result:1.3}')
```

**Question 65**


Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

```python
prompt = int(input('Enter a positive integer: '))
def func(n):
    if n == 0:
        return 1
    else:
        return func(n-1) + 100

print(func(prompt))
```

**Question 66**



The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

13

In case of input data being supplied to the question, it should be assumed to be a console input.

```python
prompt = int(input('Enter a positive integer: '))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(prompt))
```

**Question 67**


The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

```python
prompt = int(input('Enter a positive integer: '))
def fibonacci_sequence(n):
    sequence = []
    def fibonacci(n):
        if n == 0:
            sequence.append(0)
            return 1
        elif n == 1:
            fibonacci(n-1)
            sequence.append(1)
            return 1
        else:
            fibonacci(n-1)
            sequence.append(sequence[n-2] + sequence[n-1])
    fibonacci(n)
    return sequence

result = fibonacci_sequence(prompt)
print(','.join([str(x) for x in result]))
```

**Question 68**


Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

```python
prompt = int(input('Enter a positive integer: '))

def even_gen(n):
    i = 0
    while i <= n:
        yield i
        i += 2
result = []
for i in even_gen(prompt):
    result.append(i)
print(','.join([str(x) for x in result]))
```

**Question 69**


Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

```python
prompt = int(input('Enter a positive integer: '))

def div35_gen(n):
    i = 0
    while i < n:
        yield i
        i += 35
result = []
for i in div35_gen(prompt):
    result.append(i)
print(','.join([str(x) for x in result]))
```

**Question 70**



Please write assert statements to verify that every number in the list [2,4,6,8] is even.

```python
prompt = [2,4,6,8]
assert(all([x % 2 == 0 for x in prompt]))
```


**Question 71**


Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

```python
prompt = input('Enter an expresion (ex. 35+3): ')
print(eval(prompt))
```

**Question 72**


Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


```python
def mid(x, y):
    return (x + y) // 2

def binary_search(num_to_find, prompt):
    breadth = [0, len(prompt) - 1]
    index = mid(*(breadth))
    found = True
    while num_to_find != prompt[index]:
        if breadth[0] == breadth[1]:
            # value not in list, this index was just checked
            found = False
            break
        if num_to_find < prompt[index]:
            difference = breadth[1] - breadth[0]
            breadth[1] = breadth[0] + max(difference // 2, 1)
        else: 
            difference = breadth[1] - breadth[0]
            breadth[0] = breadth[0] + max(difference // 2, 1)
        index = mid(*(breadth))
        print(index)
        print(f'{num_to_find=} {prompt[index]=}')

    return found, index
```

**Question 73**


Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

```python
def mid(x, y):
    return (x + y) // 2

def binary_search(num_to_find, prompt):
    breadth = [0, len(prompt) - 1]
    index = mid(*(breadth))
    found = True
    while num_to_find != prompt[index]:
        if breadth[0] == breadth[1]:
            # value not in list, this index was just checked
            found = False
            break
        if num_to_find < prompt[index]:
            difference = breadth[1] - breadth[0]
            breadth[1] = breadth[0] + max(difference // 2, 1)
        else: 
            difference = breadth[1] - breadth[0]
            breadth[0] = breadth[0] + max(difference // 2, 1)
        index = mid(*(breadth))
        print(index)
        print(f'{num_to_find=} {prompt[index]=}')

    return found, index
```

**Question 74**


Please generate a random float where the value is between 10 and 100 using Python math module.


```python
import random

result = random.random()*80+10
```

**Question 75**


Please generate a random float where the value is between 5 and 95 using Python math module.

```python
import random

result = random.random()*90+5
```

**Question 76**


Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

```python
import random

print(random.choice([x*2 for x in range(0, 6)]))
```


**Question 77**


Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

```python
print(0)
```

**Question 78**


Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

```python
import random

result = [random.randint(100, 200) for x in range(5)]
```


**Question 79**


Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

```python
import random

result = [random.randint(50, 100) * 2 for x in range(5)]
```


**Question 80**


Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

```python
import random

result = [random.randint(0, 1000 // 35) * 35 for x in range(5)]
```


**Question 81**


Please write a program to randomly print a integer number between 7 and 15 inclusive.

```python
import random

print(random.randint(7, 15))
```


**Question 82**


Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".


```python
import zlib

def compress_string(s):
    return zlib.compress(s.encode('utf-8'))

def decompress_string(s):
    return zlib.decompress(s).decode('utf-8')

prompt = "hello world!hello world!hello world!hello world!"
prompt = compress_string(prompt)
prompt = decompress_string(prompt)
```

**Question 83**


Please write a program to print the running time of execution of "1+1" for 100 times.

```python
import timeit

execution_time = timeit.timeit(stmt='1+1', number=100)
print(execution_time)
```


**Question 84**


Please write a program to shuffle and print the list [3,6,7,8].

```python
import random

prompt = [3,6,7,8]
random.shuffle(prompt)
print(prompt)
```


**Question 85**


Please write a program to shuffle and print the list [3,6,7,8].

```python
import random

prompt = [3,6,7,8]
random.shuffle(prompt)
print(prompt)
```


**Question 86**


Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

```python
subject = ['I', 'You']
verb = ['Play', 'Love']
obj = ['Hockey', 'Football']

result = []
for s in subject:
    for t in verb:
        for u in obj:
            result.append(s+' '+ t +' '+ u +'.')
```

**Question 87**

Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

```python
prompt = [5,6,77,45,22,12,24]
print([x for x in prompt if x % 2 == 1])
```

**Question 88**


By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

```python
prompt = [12,24,35,70,88,120,155]
print([x for x in prompt if x % 35 == 0])
```

**Question 89**


By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].


```python
prompt = [12,24,35,70,88,120,155]
print([x for i, x in enumerate(prompt) if i not in [0,2,4,6]])
```

**Question 90**


By using list comprehension, please write a program generate a 3\*5\*8 3D array whose each element is 0.

```python
result = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]
```

**Question 91**


By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

```python
prompt = [12,24,35,70,88,120,155]
print([x for i, x in enumerate(prompt) if i not in [0,4,5]])
```

**Question 92**


By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

```python
prompt = [12,24,35,70,88,120,155]
print([x for x in prompt if x != 24])
```

**Question 93**


With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

```python
prompt1 = [1,3,6,78,35,55]
prompt2 = [12,24,35,24,88,120,155]

print(set(prompt1) & set(prompt2))
```

**Question 94**

With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

```python
prompt = [12,24,35,24,88,120,155,88,120,155]
li = prompt[::-1] # reverse the list, we will unreverse it after the loop

pointer = 0
while pointer < len(li):
    if li[pointer] in li[(pointer + 1):]:
        li.remove(li[pointer])
    else:
        pointer += 1

print(li)
```

**Question 95**


Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

```python
class Person:
    getGender(self):
        return None

class Male(Person):
    getGender(self):
        print('Male')

class Female(Person):
    getGender(self):
        print('Female')
```

**Question 96**


Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

```python
from collections import defaultdict

prompt = input('Enter some words: ')
result = defaultdict(int)
for c in prompt:
    if c.isalpha():
        result[c] += 1
for k, v in result.items():
    print(f'{k},{v}')
```

**Question 97**


Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

```python
prompt = input('Enter a string: ')
print(''.join(list(prompt[::-1])))
```

**Question 98**


Please write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

```python
s = input('Enter a string: ')
s = s[::2]
print(s)
```

**Question 99**


Please write a program which prints all permutations of [1,2,3]

```python
import itertools

prompt = [1, 2, 3]
combinations = itertools.permutations(mylist)

print(list(combinations))
```

**Question 100**


Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?


```python
# Given variables (constants)
heads, legs = 35, 94

# Verify that there is a solution
assert(legs % 2 == 0)
assert(legs >= heads * 2 and legs <= heads * 4)

# Assume all are chickens
chickens, rabbits = heads, 0

# Calculation for number of legs
get_legs = lambda chickens, rabbits: chickens * 2 + (rabbits * 4)

# Remove a chicen and add a rabbit until given # of legs == calculated # legs
while get_legs(chickens, rabbits) < legs:
    chickens -= 1
    rabbits += 1

print(f'{chickens} chickens, {rabbits} rabbits.')
print(f'heads = {chickens + rabbits}, legs = {get_legs(chickens, rabbits)}')
```