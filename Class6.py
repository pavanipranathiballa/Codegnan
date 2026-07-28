''' 
In the usexase (mini- proj, we will make use of control block statements
BMI --> Body Mass Index -->bmi = (weight (kg) / (height ** 2) (meters)
'''

'''
name = input("Enter user name: ")
user = int(input("Enter no.of iterations: "))
for i in range(user):
    weight = int(input("Enter the weight in kgs: "))
    height = float(input("Enter the height in meters: "))

    #print(bmi)
    #we want to make it dynamic nd build calci

    if weight > 0 and height >0:
        bmi = (weight) / ((height) ** 2)
        if bmi < 18.5:
            print(f'{name}--> Underweight and bmi is {bmi}')
        elif 18.5<=bmi<24.9:
            print(f'{name}--> Normal weight and bmi is {bmi}')
        elif 25<=bmi<29:
            print(f'{name}--> overweight and bmi is {bmi}')
        else:
            print(f'{name}--> Obesity and bmi is {bmi}')
    else:
        print("Enter positive values")


'''
#task: for same bmi calci store the details in a  dictionary.
#out should be like: bmi_results = {'name': [user1, user2, user3],
#                                    'BMI_values': [bmi1, bmi2, bmi3]}
#user height--> inches,cm, feet to meters


#Exception handling --> Try and expect, finally
'''
try:
    statements...
except ErrorName:
    debugging
finally:
    result storage
'''
'''
while True:
    try:
        n = int(input())
        name = input("Enter user name: ")
        user = int(input("Enter no.of iterations: "))
        for i in range (n):
            
            weight = int(input("Enter the weight in kgs: "))
            height = float(input("Enter the height in meters: "))
            if weight > 0 and height > 0:
                bmi = bmi = (weight) / ((height) ** 2)
                if bmi < 18.5:
                    print(f'{name}--> Underweight and bmi is {bmi}')
                    break
                elif 18.5<=bmi<24.9:
                    print(f'{name}--> Normal weight and bmi is {bmi}')
                    break
                elif 25<=bmi<29:
                    print(f'{name}--> overweight and bmi is {bmi}')
                    break
                else:
                    print(f'{name}--> Obesity and bmi is {bmi}')
                    break
            elif weight <0 and height < 0:
                print("Put valid number")
                break
            else:
                print("enter Valid number")
                break
    except ValueError:
        print("Make sure to enter +ve number")
'''
'''
while True:
    try:
        weight = int(input("Enter the weight in kgs: "))
        height = float(input("Enter the height in meters: "))
        if weight > 0 and height > 0:
            break
        else:
            print(f'Make sure to enter only +ve')
    except ValueError:
        print(f'Invalid only integer weight in int and height in float')
    except ZeroDivisionError:
        print(f'Both zeros r not allowed')
bmi = (weight) / ((height) ** 2)
if bmi < 18.5:
    print(f'Underweight and bmi is {bmi}')
elif 18.5<=bmi<24.9:
    print(f'Normal weight and bmi is {bmi}')
elif 25<=bmi<29:
    print(f'overweight and bmi is {bmi}')
else:
    print(f'Obesity and bmi is {bmi}')

'''

'''
while True:
    try:
        weight = int(input("Enter the weight in kgs: "))
        height = float(input("Enter the height in meters: "))
        bmi = (weight) / ((height) ** 2)
        if weight < 0 and height < 0:
            print(f'Make sure to enter only +ve')
        break
    except ValueError:
        print(f'Invalid only integer weight in int and height in float')
    except ZeroDivisionError:
        print(f'Both zeros r not allowed')

if bmi < 18.5:
    print(f'Underweight and bmi is {bmi}')
elif 18.5<=bmi<24.9:
    print(f'Normal weight and bmi is {bmi}')
elif 25<=bmi<29:
    print(f'overweight and bmi is {bmi}')
else:
    print(f'Obesity and bmi is {bmi}')

'''
#task2-->try to have ZeroDivisionError include
#task3--> bmi calci did just like. In 2nd usecase build an ATM calci--> user acct --> pin verification --> balance checck --> wuthdraaw-->deposit --> transaction --> limit the valid pin(if 3 times incorrect should print account locked for 24hrs)


    #Functions:
'''Approach of POP(procedure oriented programming) ---> the entire divided into blocks which is functions
Functions --> A function is a block of code (statements) which performs a specific task
it is a reusable code --> readbility, resuability and easy to maintain
reccursive, anonymus(next days)
User defined Functions --> def
Built-in function --> python by default
Anonymous functions --> lamda (map,filter,reduce)
Recursive function(factorial, fibanocci)

Syntax --> user defined function
def fname(parameters):  #Functon Header
"""Doc string (description of function"""
statements   #Body of function
return value(s)
fname(arguments)  #Function call
'''
'''
def add(a,b):
    """Sample Add Function"""
    c = a + b
    print(f'Value of c is {c}')
add([2,3], [4,5])
add('code','gnan')
add(2,3)


def add(a,b):
    """Sample Add Function"""
    c = a + b
#    print(f'Value of c is {c}')
    return c
print(add([2,3], [4,5]))
print(add('code','gnan'))


def add(a,b):
    """Sample Add Function"""
    c = a + b
#    print(f'Value of c is {c}')
    return c
results = add([2,3], [4,5])
result = add('code','gnan')
print(results, result)
'''
'''
#Parameters --> Below categories
#Positional Arguments --> count of arguments to be matched
#Default arguments --> we can make arguments as default
#Keyword arguments --> order/keyword name to be matched
#Variable length arguments (*args) --> we can pass any number of positional arguments can be given (gonna see in next class)
#Keyword variable length arguments (**kwargs) --> we can pass any number of keyword arguments


#Grocery purchase
#def grocery(item, price):
#def grocery(item = "jam", price): #nondefault always follow default error (if we put grocery(item, 45))
#def grocery(item, price = 45): #Default
def grocery(item = "Choco", price = 45):
    """Usage of Positional, Default and Keyword Arguments"""
    print(f'Value of item is {item}')
    print(f'Value of price is {price}')
grocery('Milk', 30)
grocery('Bread') #typeerror if no default price
grocery()
grocery(price = 45, item = "Milk") #can't write grocery(45, milk) get keyboard error
'''
'''
#Variable length arguments

def sample(*args):
    """Usage of Variable length arguments"""
    print(args)
    print(type(args))
sample()
sample(1,2,3)


def add(*a):
    """Summation of given objects"""
    result = 0 #Output objects
    #print(a)
    for i in a:
        #print(i)
        if type(i) in (int,float):
            result = result + i
    return result
add()
print(add(1,3,5))
print(add(1,2,3,3.4,"pp",2+4j   ))


#Keyword variable length arguments --> Any number of keywork arguments can be passed a function
#Data is stored in dictionary format where we use ** format

def sample(**kwargs):
    """Usage of keyword variable length arguments"""
    print(kwargs)
    print(type(kwargs))
sample()
sample(name = "pp", age = 21, course = "AAI")
'''
'''
def grocery(**items):
    """Groceries list"""
    print(items)
    for keys in items:
        print(keys)
    for values in items.values():
        print(values)
    for keys, values in items.items():
        print(f'keys is {keys} and value is {values}')
grocery(name = "Milk", price = 30, brand = "Heritage")
'''

'''
name = input("Enter user name: ")
user = int(input("Enter no.of iterations: "))
for i in range(user):
    weight = int(input("Enter the weight in kgs: "))
    height = float(input("Enter the height in meters: "))

    #print(bmi)
    #we want to make it dynamic nd build calci

    if weight > 0 and height >0:
        bmi = (weight) / ((height) ** 2)
        if bmi < 18.5:
            print(f'{name}--> Underweight and bmi is {bmi}')
        elif 18.5<=bmi<24.9:
            print(f'{name}--> Normal weight and bmi is {bmi}')
        elif 25<=bmi<29:
            print(f'{name}--> overweight and bmi is {bmi}')
        else:
            print(f'{name}--> Obesity and bmi is {bmi}')
    else:
        print("Enter positive values")
'''
'''
def bmicalci(**details):
    """BMI Calculator"""
    for i in details:
        weight = int(input("Enter the weight in kgs: "))
        height = float(input("Enter the height in meters: "))
        if weight > 0 and height >0:
            bmi = (weight) / ((height) ** 2)
            if bmi < 18.5:
                print(f'Underweight and bmi is {bmi}')
            elif 18.5<=bmi<24.9:
                print(f'Normal weight and bmi is {bmi}')
            elif 25<=bmi<29:
                print(f'overweight and bmi is {bmi}')
            else:
                print(f'Obesity and bmi is {bmi}')
        #print(i)
    for i in details.values():
        print(i)
        """
    for i, j in details.details():
        print(f'{i}, {j}')
        """
#bmicalci()
bmicalci(weight = 50, height = 1.4)

'''


'''
def bmicalci(*details):
    """BMI Calculator"""
    for i in details:
        """
        weight = int(input("Enter the weight in kgs: "))
        height = float(input("Enter the height in meters: "))
        """
        if weight > 0 and height >0:
            bmi = (weight) / ((height) ** 2)
            if bmi < 18.5:
                print(f'Underweight and bmi is {bmi}')
            elif 18.5<=bmi<24.9:
                print(f'Normal weight and bmi is {bmi}')
            elif 25<=bmi<29:
                print(f'overweight and bmi is {bmi}')
            else:
                print(f'Obesity and bmi is {bmi}')
        print(i)
        """
    for i in details.values():
        
        print(i)
    for i, j in details.details():
        print(f'{i}, {j}')
        """
#bmicalci()
weight = int(input("Enter the weight in kgs: "))
height = float(input("Enter the height in meters: "))
bmicalci(weight , height )
'''

'''

def bmicalci(*details):
    """BMI Calci"""
    while True:
        try:
            weight = int(input("Enter the weight in kgs: "))
            height = float(input("Enter the height in meters: "))
            bmi = (weight) / ((height) ** 2)
            if weight < 0 and height < 0:
                print(f'Make sure to enter only +ve')
            break
        except ValueError:
            print(f'Invalid only integer weight in int and height in float')
        except ZeroDivisionError:
            print(f'Both zeros r not allowed')
    if bmi < 18.5:
        print(f'Underweight and bmi is {bmi}')
    elif 18.5<=bmi<24.9:
        print(f'Normal weight and bmi is {bmi}')
    elif 25<=bmi<29:
        print(f'overweight and bmi is {bmi}')
    else:
        print(f'Obesity and bmi is {bmi}')

bmicalci()
'''

#BMI usecase -->Unit converter --->Function (*args/ **kwargs) -->Home task

#Scope of Variables --> Scope --> the field/place where we r defining the variables
'''
--> Local Variables
-->Global Variables
-->Global keyword usage
-->Enclosing variables (nonlocal keyword)
'''

#Local Variables: The variables defined inside the function

def fname():
    """USage of local variable"""
    name = "Codegnan" #Local variable
    return name
print(fname())
#print(name) #NameError


#Global Variable: It is defined and accessible in the entire module(entire python script)

name = "Codegnan"
def uname():
    """Global scope"""
    return name
print(uname())
print(name)
print(name + 'pp')


name = "Codegnan"
def uname():
    """Global scope"""
    name = "pp"
    return name
print(uname())
print(name)
print(name + 'pp')


#Global keyword: where we want to modiy global scope variable and use in function and update
#accordingly

count = 15
def update():
    """Usage of global keyword"""
    global count
    count = count + 10
    return count
print(update())
print(f'Count is {count}')


#Enclosing Scope --> non local keyword --> Nested function

def outer():
    """Outer function"""
    count = 10
    def inner():
        nonlocal count
        count = count + 5
        return count
    print(inner())
print(outer())

def outer():
    """Outer function"""
    count = 10
    def inner():
        nonlocal count
        count = count + 5
        return count
    print(inner())
    return count
print(outer())


#LEGB --> Local scope, Enclosing, Global, built-ins
#built in scope --> builtin functions can be used as variables but itt overrides its behaviours
#len = 34


count = 15
def update():
    """Usage of global keyword"""
    global count
    count1 = count + 10
    return count1
print(update())
print(f'Count is {count}')
