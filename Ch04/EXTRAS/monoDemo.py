'''
Created on Oct 6, 2010
Shows montonocity of a function and the log of that function
@author: Peter
'''
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

t = np.arange(0.0, 0.5, 0.01)
s = np.sin(2*np.pi*t)
logS = np.log(s)

fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(t,s)
ax.set_ylabel('f(x)')
ax.set_xlabel('x')

ax = fig.add_subplot(212)
ax.plot(t,logS)
ax.set_ylabel('ln(f(x))')
ax.set_xlabel('x')
plt.show()
