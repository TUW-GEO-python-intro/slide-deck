a = 1
b = 2.8
c = "text"
print("a is", a)
print("b is", a)
print("c is", c)
c = a
print("c is", c)

var1 = 5
Var1 = 6
print(var1, Var1)
import keyword
print(keyword.kwlist)

width = 20
height = 5 * 9
# calculate rectangular area
rect_area = width * height
print("Rectangular Area is", rect_area)

# calcualte area of square
square_area = width ** 2
print("Square area is", square_area)

print(1+4)
print(type(1+4))
print(type(1+4.)) # automatic conversion of resulting data type

# float and integer division
# this is different in Python 2
print("12 / 7 really is", 12/7.)
print(type(12/7.))
print("12 / 7 is", 12//7)
print(type(12//7))

#comparison
print("is 7 less than 5?" , 7<5)
print("is 5 less than 7?" , 7>5)
print("is 5 less or equal 5?" , 5<=5)

s1 = "Monthy"
s2 = 'Python' #single quotes are also fine
# joining string can be done in different ways
print(s1+s2, s1*3, ";".join([s1, s2]))

# sometimes double quotes are necessary
print("This wouldn't work with single quotes")
# or the ' has to be escaped using \
print('Escaping "wouldn\'t" also works')

s = "0123456789"
print(s[1:4])
print(s[3:8])
print(s[-1])
print(s[-6:-3])
print(s[0:5:2])
print("negative step reverts", s[::-1])

winter = ['jan', 'feb']
spring = ['apr', 'may', 'jun']
summer = ['jul', 'aug', 'sep']
autumn = ['oct', 'nov', 'dec']
# create one list containing all the elements
months = winter + spring + summer + autumn
print("List of months", months)
# create a nested list, list of seasons
seasons = [winter, spring, summer, autumn]
print("List of seasons", seasons)

winter.append('mar')
print("Winter is now:", winter)
print("List of months", months)
print("List of seasons", seasons)

months.insert(2, 'mar') # insert a element before index 2
print(months)
print(months[::2]) # slicing works the same as with strings
print(months[8:11])

li = [1, 4, 8.33, 3.6, 19, 12]
print(li.index(3.6))  # get the index of a element
print(li[li.index(3.6)])  # this index can be used to address the list
li.sort()  # sort the list
print(li)
#remove elements from list
del li[2]
print("removed index 2:", li)
li.pop(2)
print("removed index 2 again:", li)

m, p = set('mama'), set('papa')
print(m)
print(p)
print("Union, m or p", m | p)
print("Intersection, m and p", m & p)
print("Difference, m minus p", m - p)
print("Symetric Difference", m ^ p) # elements in either one but not both sets

d = {'integer': 7, 'string': "test", 1: [1, 2, 3]}
print(d)
print(d[1])
print(d['integer']) # get a value by the key
print(d.keys()) # list of the keys
print('integer' in d) # test for presence of key

# keys can be any hashable(unique) object
d1 = {(1, 2): "tuple with 1 and 2",
      (1, 3): "tuple with 1 and 3"}
print(d1[(1, 2)])

# add element to dictionary
d1['additional element'] = "I am new"
print(d1)
# delete it again
del d1['additional element']
print(d1)

d1 = {"one": 1, "two": 2}
d2 = {"two": "II", "three": "III"}
d1.update(d2)
print(d1)

answer_dict = {True: 'yes', False: 'no'}
print("is 7 less than 5?" , answer_dict[False])
print("is 7 less than 5?" , answer_dict[7<5])
