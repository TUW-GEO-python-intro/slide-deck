from datetime import date
a = date(2015, 3, 1)
b = date.today()
print(a, b)
print(a.year, a.month, a.day) # attribute access
delta = b - a # difference are a datetime.timedelta object
print(delta)
print(type(delta))

from datetime import date, datetime, timedelta, time
a = date(2008, 5, 1)
b = time(12, 30, 15)
print(datetime.combine(a, b))
print(datetime(2008, 5, 1, 12, 30, 16))
# parsing and formatting
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))

import math
print(math.pi, math.e)
print(math.radians(180), math.degrees(2 * math.pi))
print(math.sin(math.pi / 4))

import os
p = os.path.join("test", "path", "to", "file.txt") # relative path
print(p)
print(os.path.abspath(p)) # absolute path
# split into path and filename with extension
path, fname_ext = os.path.split(p) 
# split filename and extension
fname, extension = os.path.splitext(fname_ext) 
print(path, fname_ext, fname, extension)
