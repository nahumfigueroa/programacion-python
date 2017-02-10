#Ramiro Nahum Figueroa Castro
#Laboratorio 3b


import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(0,2*math.pi,99)
x=np.cos(t)**3
y=np.sin(t)**3
plt.plot(t,x,linewidth=3,color='orange',label='f(x)')
plt.plot(t,y,linewidth=3,color='cyan',label='f(a)')
plt.legend()
plt.title('Ejercicio 3.a)')
plt.xlabel('eje X')
plt.ylabel('eje Y')
plt.grid(True)
plt.show()
