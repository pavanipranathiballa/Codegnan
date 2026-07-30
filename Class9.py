'''
List Comprehension --> In python its a precise/ easiest way to create lists

Syntax: [expression for item in iterable]
iterable --> list, tuple, set, dict or range()


#We need to append elements into list
list = []
for i in range(10):
    list.append(i)
    print(list)

#the same way above using list comprehension
list = [i for i in range(10)]
print(list)


#Get the square of numbers
data = []
for i in range(10):
    data.append(i * i)
    print(data)


data= [i**2 for i in range(10)]
print(data)

e = [i%2 ==1 for i in range(10)]
print(e)


#Converting strings to uppercase/lowercase

details = ['Pp', 'Ab', 'bc']
new = [i.upper() for i in details]
print(new)
print(*new)
low = [i.lower() for i in details]
print(low)
print(*low)


a, *name, c, alph = 1, 'pp', 'ab', 'bc', 90, 'ppp'
print(a)
print(name)
print(*name)
print(c)
print(alph)


a = [15,20,25,35]
#Update the list with each value by 5
a = [i+5 for i in a]
print(a)

#get the first letter of each object in collection
data = ['pp', 'ab', 'bc']
letter = [i[0] for i in data]
print(letter)

data = ['pp', 'ab', 'bc']
letter = [i[0].upper() for i in data]
print(*letter)


#List Comprehension with if usage
#[expression for item in iterable/range if condition]

#Even numbers from the collection
a = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(a)

b = list(map(int, input("Enter the number: ").split(',')))
a = ["Even" if i%2==0 else "Odd" for i in b]
print(a)

a = list(map(int, input("Enter the number: ").split(',')))
print(a)
result = [i for i in a if i%2 == 0]
print(result)


a = list(map(int, input("Enter the number: ").split(',')))
b = list(filter(lambda n: n%2 == 0, a))
print(b)


#Fetch desired values with condition satisfied
a = list(map(int, input("Enter the number: ").split(',')))
print(a)
final = [i for i in a if i > 10]
print(final)


#List Comprehension with if,  else condition
#[true_value if condition else false_value for i in iterable]

a = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(a)

#Nested Comprehension
#Nested is basically one inside another (one loop inside another loop)
#[expression for i in iterable1 for j in iterable2]

a = [(i,j) for i in range(5) for j in range(3)]
print(a)

b = [(i,j) for i in [1,3,5] for j in [4,5,6]]
print(b)

#Multiplication table pattern
c = [i*j for i in range(1,5) for j in range(1,5)]
print(c)

colors = ['red', 'blue', 'black']
sizes = ['s', 'm', 'l']
dress = [(i,j) for i in colors for j in sizes]
print(dress)

c = [i*j for i in range(1,5) for j in range(1,5)]
print(c)

c = [i*j for i in range(1,5) for j in range(1,5) if i != j]
print(c)


#Nested comprehension with if condition
#[expression for item1 in iterable1 for item2 in iterable2 if condition]

#Possible pairs
a = [(i,j) for i in range(5) for j in range(3) if i != j]
print(a)


#Nested comprehension with if-else

#[true_value if condition else error_value for item1 in iterable1 for item2 in iterable2]

a = [1,3,5,6,7]
b = [2,4,6,8,9]
c = [x+5 if x<y else x for x in a for y in b]
print(c)
'''

#In the above case if we replace [] brace with () we don't get tuple --> we get generator
#No tuple Comprehension -->Generator
#Generator --> Generator is a special function with produces one value at a time
#we use yield keyword
#Normal function
'''
def fname():
    """doc string"""
    return value(s)
fname()

def fname():
    """doc string"""
    yield value1
    yield value2
    yield value3
fname()


def fun():
    """Normal Function"""
    return [1,2,4,5,6]
print(fun())
a = fun()
for i in a:
    print(i)

def fun():
    """Generator function"""
    yield [1,2,4,5,6]
print(fun())
b = fun()
print(next(b))

def fun():
    """Generator function"""
    yield 1
    yield 2
    yield 3
#print(fun())
b = fun()
print(next(b))
print(next(b))
print(next(b))
print(next(b)) #Stop iteration Error
'''

def display():
    """Subject covered"""
    yield "Python"
    yield "GenAi"
    yield "RAG"
    yield "Agents"
print(display())
print(type(display()))
d = display()
print(next(d))
