# Debugging
var1 = "test"
var2 = [1, 2, 3, 4]
var3 = {"key1": 1, "key2": 2}
print(var1, var2, var3) # set a breakpoint here, click on blue dot left of this line
var1 = "modified"
var3["key5"] = "a new value"

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

i = 0
data = [2, 4.5]
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

dataset1 = [ 1.73, 2.4122, 80, -4 ]
# if/else blocks
for d in dataset1:
    if d > 3:
        res = ">3"
    else:
        res = "<=3"
    print(res)

####################################################################
# Mini Exercise 

# Try to format and print only the positive numbers in 'dataset1',
# with 1 number on each line,
# and with 2 digits after the comma

####################################################################

def classify(dataset, threshold):
    """
    classifies dataset into small and large class using the threshold

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
    classifies dataset into small and large class using the threshold

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
def func():
    variable = "I am Local"
    print(variable)

print(variable)
func()

l = [1, 2, 3]
def func(ls):
    ls.append(4)

print(l)
func(l)
print(l)

####################################################################
# Mini Exercise 

# Write a function that classifies strings by length
# inputs should be a list of strings, and a threshold 
# specifying the number of characters
# The output should be a list containing the strings "shorter" or "longer"
# lets ignore strings of length = threshold for now
print(len("test")) # hint
# list of random strings
test_strings = ["faucal" ,"fiddling" ,"instil" ,"blake" ,"profanely" ,
                "bootblack" ,"decongest" ,"interest" ,"arrowy" ,"eponymic"]
####################################################################
