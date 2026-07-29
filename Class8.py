#Recursive Functions, Anonymous Functions
#Recursive Function --> A function calling itself, where it makes the smaller problem is broken into multiple times
#Depends on two cases --> 1. Base case( it indicates when to stop the base condition),
#                         2. Recursive case (it makes the problem to be repeated)

'''
Syntax:
def function():
    if base_condition:
        return
    function() #we write our recursive
function()


def test():
    """Withour base condition"""
    return test()
print(test())  #here it gives error, cuz there is no base condition it just test recursively 


#Factorial approach using recursion

def factorial(n):
    """Recursive approach"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter the number: "))
print(factorial(n))


def factorial(n):
    """Recursive approach"""
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Enter only +ve numbers"
    else:
        return n * factorial(n-1)
n = int(input("Enter the number: "))
print(factorial(n))


#Find the sum of natural numbers till 10

def sum(n):
    """Sum using recursive"""
    if n == 0:
        return 0
    elif n > 0 and n < 11:
        return n + sum(n-1)
    else:
        return "Enter only natural numbers"
n = int(input("Enter number: "))
print(sum(n))

#Task: Build a simple choice chooser
#1. recursive logic for factorial (like if option 1 it should open recursive of the number)
#2. Sum of numbers
#3. BMI calculate
#4. fibonacci series
#5. ATM usecase
#6. if other option he choose should get choose from the above

#5 --> 0, 1, 1, 2, 3

def fibonacci(n):
    """fibonacci in recursive"""
    if n == 0 and n == 1:
        return n
    elif n > 0:
        return fibonacci(n-1) + fibonacci (n -2)
    else:
        return "Enter +ve numbers"
n = int(input("Enter number: "))
print(fibonacci(n))



#Anonymous Function --> Nameless functions, we define them by using lambda keyword
#filter(), map()

#Create a function to return the area of rectangle

def area():
    
    area = l * b
    return area
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print(area())


#Syntax: --> var_name = lambda parameters: expression

b = lambda l,b : l*b
print(type(b))
print(b(2,3))


#Find the area of square

a = lambda a : a * a
print(a(4))


#User registration in a web page --> name
#First name --> input
#Last name --> input
#full name
#Write user defined then anonymous function

def web(a, b):
    return a.title() + " "+ b.title()
a = input("Enter First name: ")
b = input("Enter second name: ")
print(web(a, b))


name = lambda a,b : a.title() + " " + b.title()
a = input("Enter first name: ")
b = input("Enter last name: ")
print(name(a,b))


#to get even nnumber from user input
n = int(input("Enter the number: "))
result = lambda n : "Even" if n %2 ==0 else "Odd"
#result = lambda n : n if n %2 ==0 else "Odd"
print(result(n))


#length of sequence
n = input("Enter name: ")
seq = lambda n : len(n)
print(seq(n))

#Filter(), map()
#Filter(function, iterable) --> returns the filtered values by satisfying the condition
#yielding the value from iterable

#List of integers
a = list(map(int, input("Enter the number: ").split(',')))
print(a)
#Filter only even numbers
b = list(filter(lambda n: n%2 == 0, a))
print(b)

#names = ['pavan', 'abhiram', 'nihanth', 'saikiran', 'roshan', 'vasanthi', 'manimala'].... output should get who's length is more than 6

a = list(map(str, input("Enter the number: ").split(',')))
b = list(filter(lambda n: len(n) > 6, a))
print(b)


#map() --> it will apply for every value from multiple iterable

a = list(map(int, input("Enter the number: ").split(',')))
print(a)

names = ['ab', 'bc', 'cd']
result = list(map(lambda name: name.upper(), names))
print(result)


prices = [1000, 2500, 3500, 4500]
final_price = list(map(lambda prices : prices * 0.9, prices))
final_price = list(map(lambda prices : (prices - prices * 0.1), prices))
print(final_price)
'''
#reduce() --> this makes complete iterable to be a single value --> functools
#module creation
from functools import reduce
numbers = [1,2,3,4,7,8]
result = reduce(lambda a,b: a+b, numbers)
print(result)
result = reduce(lambda a,b: a*b, numbers)
print(result)
