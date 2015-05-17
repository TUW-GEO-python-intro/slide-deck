import math

class Pizza(object):
    """
    Representing a pizza.
    """
    def __init__(self, radius, ingredients=[]):
        self.radius = radius
        self.ingredients = ingredients

    def compute_circumference(self):
        """
        Compute circumference of Pizza.
        """
        return 2 * math.pi * self.radius


class Calzone(Pizza):
    """
    Representing a calzone.
    """
    def __init__(self, *args):
        ingredients = ['cheese', 'olives', 'tomatoes', 'ham']
        super(Calzone, self).__init__(*args, ingredients=ingredients)

    def compute_circumference(self):
        """
        Overload function circumference. Calzone is folded.
        """
        cf = super(Calzone, self).compute_circumference()
        return  cf / 2. + 2 * self.radius

p1 = Pizza(10, ["tomatoes", "cheese"])
print p1.compute_circumference()

c1 = Calzone(10)
print c1.compute_circumference()
print c1.ingredients

print hasattr(c1, 'ingredients')  # True if 'ingredients' attribute exists
print getattr(c1, 'ingredients')  # Returns 'ingredients' attribute
setattr(c1, 'radius', 6)  # Set attribute 'radius' at 6
delattr(c1, 'radius')  # Delete attribute 'radius'
print dir(c1)
