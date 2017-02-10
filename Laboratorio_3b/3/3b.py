#Ramiro Nahum Figueroa Castro
#Laboratorio 3b

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(-2*math.pi,2*math.pi,120)
x=t+2*np.sin(2*t)
y=t+2*np.cos(5*t)
plt.plot(t,x,linewidth=4,color='indigo',label='f(p)')
plt.plot(t,y,linewidth=4,color='tan',label='f(h)')
plt.legend()
plt.title('Ejercicio 3.b')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.show()
