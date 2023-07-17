# Importamos numpy
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sin(x)

def df(f, x):
	h = 0.000001
	return (f(x+h) - f(x))/h

x = np.linspace(-10, 10, num = 1000)
y = f(x)

plt.plot(x, y, 'b')
plt.plot(x, df(f, x), 'r')
plt.grid()

plt.show()