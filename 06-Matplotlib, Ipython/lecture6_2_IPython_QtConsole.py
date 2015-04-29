# http://ipython.org/

# Run an IPython session within the (WinPython) command prompt,
# with interactive plotting enabled
# and numpy and matplotlib loaded into the global namespace:
#   python-course-dir>IPython --pylab

# Start an IPython session in the (WinPython) command prompt,
# run it in an IPython Qt console,
# again with interactive plotting enabled
# and numpy and matplotlib loaded into the global namespace:
#   python-course-dir>IPython qtconsole --pylab --paging=hsplit

# Enhanced help function:
#   array?
# Hit key 'q' to return from pager. Compare to help(array)

# IPython's "magic functions"
# ---------------------------
# http://ipython.org/ipython-doc/stable/interactive/tutorial.html#magic-functions

# Display and optionally change the working directory:
#   %cd

# Read a file and paste it into the console;
# use <tab> for auto-completion:
#   %load lecture6_1_PyScripter.py

# Open a file in a text editor:
#   %edit lecture6_1_PyScripter.py

# Execute a file as a Python script:
#   %run lecture6_1_PyScripter.py

# Print only the user-defined variables to the console:
# %whos # compare to built-in dir()

from scipy import stats

plt.figure()

# Having run lecture6_1_PyScripter.py,
# we can re-use variables defined in it: x, x_mean, x_std.
# plt.hist?
plt.hist(x, normed=True)

# np.linspace?
xPdf = np.linspace(x.min(), x.max(), 100)
rv = stats.norm(loc=x_mean, scale=x_std)
yPdf = rv.pdf(xPdf)

plt.plot(xPdf, yPdf, '-r')

plt.title('Normalized Histogram of x with underlying PDF')

# Variables defined in lecture6_1_PyScripter.py become available
# only in the interactive shell, but not to scripts executed with %run
# To make those variables available to %run, use:
#   %run -i lecture6_2_IPython_QtConsole.py
# To render the plot, call plt.show()
# plt.show()
