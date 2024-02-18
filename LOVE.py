import numpy as np
import matplotlib.pyplot as plt
import math

t = np.linspace(0, 2*math.pi)
x = 16*np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0, color='red')
ax.set(xlim=(-20, 20), xticks=np.arange(-20, 20),
       ylim=(-15, 15), yticks=np.arange(-20, 20))

plt.show()