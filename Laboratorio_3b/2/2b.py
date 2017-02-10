#Ramiro Nahum Figueroa Castro
#Laboratorio 3b

import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,2,120)

y=x*math.e**(-3*x)
b=math.e**(-3*x)
plt.plot(x,y,linewidth=6,color='black',label='f(x)')
plt.plot(x,b,linewidth=4,color='pink',label='g(x)')
plt.legend("NH")
plt.title('Ejercicio 2.b')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
