#Ramiro Nahum Figueroa Castro
#Laboratorio 3b


import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(0,2*math.pi,100)
x=np.sin(3*t)
y=np.sin(4*t)
plt.plot(t,x,linewidth=4,color='steelblue',label='g(f)')
plt.plot(t,y,linewidth=2,color='magenta',label='f(g)')
plt.legend()
plt.title('Ejercicio 3.c)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
