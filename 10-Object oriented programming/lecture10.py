class Human_1(object):
     
    # definition of a class variable
    population = 0 
     
    def __init__(self, name):
        # definition of an instance variable
        self.name = name
        Human_1.population += 1
    
    def say_hi(self):
        print("Hi, my name is {:}.".format(self.name))

# make an instance of a class
jason = Human_1("Jason")
jason.say_hi()

class Human_2(object):
     
    def __init__(self, name):
        self.name = name
        print("I can see the light!")
    
    def say_hi(self):
        print("Hi, my name is {:}.".format(self.name))
    
    def __del__(self):
        print("Bye bye!")

jason = Human_2("Jason")
jason.say_hi()
del jason

class Human_3(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

jason = Human_3("Jason", 33)
print("Name: {:}".format(jason.name))
print("Age: {:}".format(jason._Human_3__age))
# print("Age {:}".format(jason.age))

class Human_4(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self):
        print("Hi, my name is {:}".format(self.name))

class Student(Human_4):
    def say_hi(self):
        print("Hey, I'm {:} and {:}".format(self.name, self.age))

class Teacher(Human_4):
    def say_bye(self):
        print("Bye")

jason = Student("Jason", 22)
jason.say_hi()
betty = Teacher("Betty", 44)
betty.say_hi()
betty.say_bye()

import math

class Pizza(object):
    def __init__(self, radius):
        self.radius = radius
    def cf(self):
        return 2 * math.pi * self.radius
    def __str__(self):
        return "CF={:4.2f}".format(self.cf())

class Calzone(Pizza):
    def cf(self):
        c = super(Calzone, self).cf()
        return c / 2. + 2 * self.radius

p = Pizza(10)
print(p)
p2 = Calzone(10)
print(p2)

import math

class Vector(object):

    def __init__(self, *args):
        self.coords = args

    def __str__(self):
        return str(self.coords)

    def __add__(self, other):
        coords = tuple(map(sum, zip(self.coords, other.coords)))
        return Vector(*coords)

    def __getitem__(self, index):
        return self.coords[index]

v1, v2 = Vector(2, 10), Vector(5, -2)
print v1 + v2
print v2[1], v2.coords[1]

class Human_5(object):
     
    population = 0 
      
    def __init__(self, name):
        self.name = name
        Human_5.population += 1
     
    @staticmethod
    def how_many():
        print("Population: {:}".format(Human_5.population))
     
    def __del__(self):
        type(self).population -= 1

jason = Human_5("Jason")
betty = Human_5("Betty")
jason.how_many()
robin = Human_5("Robin")
Human_5.how_many()

class Duck(object):
    def quack(self):
        print "Quack, quack!"
    def fly(self):
        print "Flap, Flap!"
 
class Person(object):
    def quack(self):
        print "I'm Quackin'!"
    def fly(self):
        print "I'm Flyin'!"

def in_the_forest(mallard):
    mallard.quack()
    mallard.fly()
 
in_the_forest(Duck())
in_the_forest(Person())

class Employee(object):
    """
    Class docstring.
    """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__: ", Employee.__dict__)
