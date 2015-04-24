import numpy as np
from numpy import random
from matplotlib import pyplot as plt

x_std = 2.52
x_mean = 5.4

# Draw 50 samples from the normal distribution defined by x_std and x_mean:
x = random.randn(50) * x_std + x_mean
y = random.randn(50) * 1.84 - 2.9

# Create a new figure each time this code is run.
# plt.figure()

# Create a plot in memory - not rendered yet
plt.scatter(x, y)

# Augment the existing plot using further commands, instead of re-writing it.
plt.hold(True)

# Plot the center of gravity, with 'x'-markers in red.
plt.scatter(x.mean(), y.mean(), c='r', marker='x')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Samples from normal distribution & their CoG")

# Save the plot to a file, rendering the plot on-demand.
# Opening the SVG-file in a recent browser, you may: zoom and pan.
plt.savefig("samples_cog.svg")

# Show the plot in a GUI-window.
# You may: zoom, pan, display pointer coordinates, edit.
# Interpreter will resume execution only after the window has been closed!
plt.show()

import ipdb
ipdb.set_trace()
print("script finished")
# No IDE supports interactive plotting while debugging :'(
# But IPython comes to the rescue, partly ...
