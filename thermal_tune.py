################################################################################
##
##
##
##

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a*np.exp(-b*x) + c

x = np.linspace(0,4,50)
y = func(x, 2.5, 1.3, 0.5)
yn = y + 0.2*np.random.normal(size=len(x))

popt, pcov = curve_fit(func, x, yn)

print "popt = ", popt
print "pcov = ", pcov

plt.figure()
plt.plot(x, yn, 'r.')
plt.plot(x, func(x, popt[0], popt[1], popt[2]), 'b')

plt.show()