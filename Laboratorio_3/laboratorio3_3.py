#Laboratorio 3
#Ramiro Nahum Figueroa Castro

print "Escribe el primer numero"
x = int(raw_input())
print "Escribe el segundo numero"
y = int(raw_input())
print "Escribe tu ultimo numero"
z = int(raw_input())
print "Los numeros que escribiste ordenados de menor a mayor: "
if x >= y >= z:
	print z,y,x
elif x >= z >= y:
	print y,z,x
elif y >= x >= z:
	print z,x,y
elif y >= z >= x:
	print x,z,y
elif z >= x >= y:
	print y,x,z
elif z >= y >= x:
	print x,y,z
