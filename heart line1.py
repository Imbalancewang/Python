
"""
'(x^2+y^2+y)^2 = x^2 + y^2'
"""
import numpy as np
import matplotlib.pyplot as plt
 
X = np.arange(-2.0, 2.0, 0.05)
Y = np.arange(-2.0, 2.0, 0.05)
 
x, y = np.meshgrid(X, Y)
f = (x ** 2 + y ** 2 + y) ** 2 - x ** 2 - y ** 2
 
fig = plt.figure()
cs = plt.contour(x, y, f, 0, colors = 'r')
plt.show()
 
