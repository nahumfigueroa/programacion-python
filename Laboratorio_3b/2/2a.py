#Ramiro Nahum Figueroa Castro
#Laboratorio 3b

import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,4*math.pi,100)
y=np.cos(2*x)+np.sin(3*x)
b=-2*np.sin(2*x)+3*np.cos(3*x)
plt.plot(x,y,linewidth=7,color='b',label='$S(x)=cos(2x)+sen(3x)$')
plt.plot(x,b,linewidth=3,color='y',label='$V(x)=-2sen(2x)+3cos(3x)$')
plt.legend()
plt.title('Ejercicio 2.a')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
