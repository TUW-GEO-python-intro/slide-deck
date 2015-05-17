class Human(object):
    """
    Class represents a human being.
    """
    population = 0

    def __init__(self, name, age):
        """
        Initialise.
        """
        self.name = name
        self.__age = age
        print '(Initializing %s)' % self.name

        Human.population += 1

    def sayHi(self):
        """
        Greeting by the person.
        """
        print 'Hi, my name is %s.' % self.name

    # define as static method either with a decorator:
    @staticmethod
    def howMany():
        """
        Prints the current population.
        """
        if Human.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Human.population
    # or this way:
    # howMany = staticmethod(howMany)

jack = Human("Jack", 32)
jack.sayHi()
jack.howMany()

jane = Human("Jane", 44)
jane.sayHi()
jane.howMany()

jane.name = "Julia"
print jane.name
print jane._Human__age
print dir(jane)

# this won't work:
# jane.__age