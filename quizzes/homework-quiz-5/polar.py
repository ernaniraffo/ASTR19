import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0,2*np.pi,100)
x = np.cos(theta)
y = np.sin(theta)

r = (x**2 + y**2)**0.5

ax = plt.subplot(1,1,1,projection='polar')
ax.plot(theta,r)

plt.show()
