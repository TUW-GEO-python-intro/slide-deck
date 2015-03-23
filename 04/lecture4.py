dataset1 = [1.73, 80, 2.4122, -4]
threshold = 2.
result = [x > threshold for x in dataset1]
print(result)

cl = {True: 'larger', False: 'smaller'}
result = {k: cl[k>threshold] for k in dataset1}
print result

data = ['a', 'b', 'c', 'd']
result = {i: x for i,x in enumerate(data)}
print result

########################################################
# Tiny Exercise

# Create a list that contains the square value of every
# element in dataset1 using list comprehension.
########################################################

def multi(a, b):
    """Documentation does not fit on slide"""
    return a * b

print(multi(2,3))
numbers = [3, 4]
print(multi(*numbers))

print multi(numbers)

def multikw(arg1="dummy", arg2="text"):
    """Documentation does not fit on slide"""
    return " ".join([arg1, arg2])

kwargs = {'arg1': "this text comes from",
          'arg2': "a keyword dictionary"}

print(multikw())
print(multikw(**kwargs))

def multi(*args):
    """
    Multiplies all given numbers
    """
    print(type(args))
    print("{} Arguments to multiply".format(len(args)))
    res = 1
    for arg in args:
        res *= arg
    return res
print(multi(2,3,4,5,6))

def print_kw(**kwargs):
    """print keywords"""

    print(type(kwargs))
    for key in kwargs:
        print("{}: {}".format(key, kwargs[key]))

print_kw(argument1=45, argument2="string", test="hello")

def do(f, a, b):
   print f.__doc__ # this is the docstring of the function
   return f(a,b) 
def add(a, b):
   """addition"""
   return a+b
def sub(a, b):
   """subtraction"""
   return a-b

print(do(add, 2, 3))
print(do(sub, 3, 2))

name = 2
assert type(name) == str, "name should be a string"
def function():
    pass # can be useful when planning program structure

for n in range(2, 8): # lets debug through this
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n / x
            break # breaks out of (ends) current loop
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'

for num in range(2, 8):
    if num % 2 == 0: # percent sign is modulo
        print "Found an even number", num
        continue # continue with the next iteration of the loop
    print "Found a number", num

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"
divide(2, 1)
divide(2, 0)

########################################################
# Mini Exercise

# write a function that makes sure that the input is
# a number
########################################################
