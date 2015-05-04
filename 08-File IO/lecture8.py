import os
import struct
import pickle

import numpy as np
import netCDF4
import h5py
import pandas as pd
from scipy.io import loadmat, savemat, whosmat

f_dir = os.path.join('.', 'files')
if not os.path.exists(f_dir):
    try:
        os.mkdir(f_dir)
        print("Created files folder")
    except OSError:
        f_dir = ''
        print("Failed creating files folder")

filename = os.path.join(f_dir, 'example1.txt')

f = open(filename, 'w')
f.write("Hello World!")
f.close()

# Using the context manager
with open(filename) as f:
    print(f.read())

filename = os.path.join(f_dir, 'example1.csv')

with open(filename, 'w') as f:
    f.write("lon,lat,temperature\n")
    data = [[16, 48, 20], [17, 48, 21], [18, 48, 18]]
    for record in data:
        f.writelines(','.join(map(str, record)))
        f.write("\n")

with open(filename) as f:
    for record in f.readlines():
        print(record)


filename = os.path.join(f_dir, 'example2.csv')
data = np.tile(np.arange(0, 5), (3, 1)).T

# save data
np.savetxt(filename, data, header='x,y,z', delimiter=',')

# load data
x, y, z = np.loadtxt(filename, skiprows=1,
                     delimiter=',', unpack=True)
print(x, y, z)


filename = os.path.join(f_dir, 'example1.bin')
points = [(1, 2), (3, 4), (9, 10), (23, 14), (50, 90)]

msg = bytearray()
msg.extend(struct.pack('I', len(points)))

for x, y in points:
    msg.extend(struct.pack('II', x, y))

# write data
with open(filename, 'wb') as f:
    f.write(msg)

# read data
with open(filename, 'rb') as f:
    n_points = struct.unpack('I', f.read(4))[0]
    print(n_points)

filename = os.path.join(f_dir, 'example2.bin')

points = np.array([(1, 2), (3, 4), (9, 10), (23, 14), (50, 90)],
                  dtype=np.int32)
points.tofile(filename)

data = np.fromfile(filename, dtype=[('x', np.int32),
                                    ('y', np.int32)])
print(data['x'], data['y'])

filename = os.path.join(f_dir, 'example1.npy')
x = np.arange(10)

# save data
np.save(filename, x)

# load data
data = np.load(filename)
print(data)

filename = os.path.join(f_dir, 'example2.npz')
x = np.arange(4).reshape(2, 2)
y = np.sin(x)

# save data
np.savez(filename, x, y=y)

# load data
data = np.load(filename)

print(data)
print('x:', data['arr_0'])
print('y:', data['y'])


filename = os.path.join(f_dir, 'example1.mat')
x = np.arange(10)

# save data
savemat(filename, {'var1': x})

# load data
data = loadmat(filename)

print(data['var1'])

filename = os.path.join(f_dir, 'example2.mat')
x = np.arange(4).reshape(2, 2)
y = np.sin(x)

# save data
savemat(filename, {'var1': x, 'y': y})

# show variables
print(whosmat(filename))

# load data
data = loadmat(filename)

print(data['y'])


filename = os.path.join(f_dir, 'example1.nc')

f = netCDF4.Dataset(filename, 'w', format='NETCDF4')
grp_temp = f.createGroup("temperature")
subgrp_air = grp_temp.createGroup("air")
subgrp_soil = grp_temp.createGroup("soil")

print(grp_temp.groups)

# Create Dimension
lat = f.createDimension('lat', 50)
lon = f.createDimension('lon', 50)
time = f.createDimension('time', None)
print(f.dimensions)

# Datasets and Attributes
soil_temp = np.ones((50, 50))
soil_dset = subgrp_soil.createVariable("Soil Temperature",
                                       soil_temp.dtype.name, ('lat', 'lon'))
soil_dset[:] = soil_temp

# http://docs.python.org/2/library/functions.html#setattr
# setattr(x, 'foobar', 123) is equivalent to x.foobar = 123
setattr(soil_dset, 'unit', 'degree celsius')
soil_dset.scaling = 1
f.close()

with netCDF4.Dataset(filename) as f:
    print(f.dimensions)
    print(f.groups['temperature'].groups['soil'].variables['Soil Temperature'])

with netCDF4.Dataset(filename) as f:
    print(f.groups['temperature'].groups['soil'].
          variables['Soil Temperature'][:])
    print(f.groups['temperature'].groups['soil'].
          variables['Soil Temperature'].unit)

filename = os.path.join(f_dir, 'example1.hdf5')

with h5py.File(filename, 'w') as f:
    grp_temp = f.create_group("temp")
    subgrp_soil = grp_temp.create_group("soil")
    soil_temp = np.arange(400)
    soil_dset = subgrp_soil.create_dataset("Soil Temperature",
                                           data=soil_temp)
    soil_dset.attrs['unit'] = 'degree celsius'
    print(soil_dset)

filename = os.path.join(f_dir, 'example1.hdf5')

with h5py.File(filename) as f:
    print(f['temp/soil'].keys())
    print(f['temp/soil/Soil Temperature'])
    print(f['temp/soil/Soil Temperature'][20:40])

# filename = os.path.join(f_dir, 'example1.xlsx')

# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# df.to_excel(filename)

# data = pd.io.excel.read_excel(filename)
# print(type(data), data)


filename = os.path.join(f_dir, 'example1.pickle')

data = {'a': [1, 2.0, 3, 4 + 6j],
        'b': ('string', u'Unicode string'),
        'c': None}

with open(filename, 'wb') as f:
    pickle.dump(data, f)

with open(filename, 'rb') as f:
    print(pickle.load(f))
