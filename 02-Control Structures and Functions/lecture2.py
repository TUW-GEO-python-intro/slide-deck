if 3 < 5:
    print("Three is less than 5")

if 5 <= 3:
    print("Five is less or equal to three")

name = "Rick"
if name in ["Rick", "Morty"]:
    print("Name is in list")

key = 1
if key in {1: "one", 2: "two"}:
    print("key is in dict")

if key in {"one": 1, "two": 2}:
    print("Comparison of dicts is against keys by default")

if key in {"one": 1, "two": 2}.values():
    print("value is in dict")

var = "test"
if 5 > 3 and var == "test":
    print("both statements are true")

if 5 > 3 or 8 > 2:
    print("at least one statement is true")

name = 2
assert type(name) == str, "name should be a string"
if type(name) != str:
    pass # can be useful when planning program structure

i = 0
data = [8, 4.5]

# the len function gets the length of a list
print("Length of the list is:", len(data)) 

while i < len(data):
    print(data[i])
    i += 1

data = [ 1.73, 2.4122, 80, -4 ]

# iterate over elements, using keyword 'in'
for elem in data:
    print(elem)

data = [ 1.73, 2.4122, 80, -4 ]
datanames = ["number 1", "number 2", "number 3", "number 4"]
for number, name in zip(data, datanames):
    print(name, number)

d = {"key1": 1, "key2": 2, "key3": 3}
for key in d:
    print(key)

d = {"key1": 1, "key2": 2, "key3": 3}
for key, item in d.iteritems():
    print(key, item)

print("range")
for i in range(1, 10, 2):
    print(i)

l = ["a", "b", "c", "d"]
for i, item in enumerate(l):
    print(i, item)

dataset1 = [ 1.73, 2.4122, 80, -4 ]
# if/else blocks
for d in dataset1:
    if d > 3:
        res = ">3"
    else:
        res = "<=3"
    print(res)

for n in range(2, 8): # lets debug through this
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break # breaks out of (ends) current loop
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 8):
    if num % 2 == 0: # percent sign is modulo
        print("Found an even number", num)
        continue # continue with the next iteration of the loop
    print("Found a number", num)

def classify(dataset, threshold):
    """
    classifies dataset into small and large class using the 
    threshold

    Parameters
    ----------
    dataset: list
        list to classify
    threshold: float
        threshold to use for classification

    Returns
    -------
    results: list
        containing True or False
    """
    results = []  # create an empty list
    for data in dataset:
        results.append(data > threshold)
    return results

dataset1 = [1.73, 80, 2.4122, -4]
res = classify(dataset1, 2)
print(res)
print(classify(dataset1, 1))

def classifydefault(dataset, threshold=2.5):
    """
    classifies dataset into small and large class using the 
    threshold

    Parameters
    ----------
    dataset: list
        list to classify
    threshold: float, optional
        threshold to use for classification

    Returns
    -------
    results: list
        containing True or False
    """
    results = []  # create an empty list
    for data in dataset:
        results.append(data > threshold)
    return results

dataset2 = [1.73, 80, 2.4122, -4, 2.6]
print(classifydefault(dataset2))

variable = "I am Global"
var = "I'm also Global"
def func():
    variable = "I am Local"
    print(variable)
    print(var)

print(variable)
func()

l = [1, 2, 3]
def func(ls):
    ls.append(4)

print(l)
func(l)
print(l)

# String Formatting
# handy for any kind of logging, etc.
# mark replacement fields with curly braces
arg = 'world'
res = "hello {}".format(arg)
print(res)

res = "{} and {}".format("a pear", "a tree")
print(res)

# refer to arguments by index; possibly re-use them
res = "{0} and {1}, {1} and {0}".format("a pear", "a tree")
print(res)

# refer to arguments by name; possibly re-use them
res = "{good} is better than {bad}".format(good="some", bad="nothing")
print(res)

# practically anything can be an argument to format(.)
value = 3.429188
res = "value is: {}".format(value)
print(res)

# custom formatting using format specifiers:
# format specifiers follow a colon inside the curly braces
# format as fixed point, with 3 digits after comma
res = "value is: {:.3f}".format(value)
print(res)

# format left-aligned, centered, and right-aligned 
# with the given minimum width,
# and a trailing line-break
# prepare the template-string
tpl = "{:<15} {:^5} {:>10}\n"
# provide empty string to match all replacement fields
res = tpl.format("Carl Friedrich", "", "Gauss")
# re-use the template-string
res += tpl.format("Alexander", "von",  "Humboldt")
res += tpl.format("Gerhard", "", "Mercator")
print(res)

# multi-line strings can be formatted just as well.
res = """# This might be a {}-file-header,
# created by {}
# on {}""".format("text", "me", "2014-02-18")
print(res)
