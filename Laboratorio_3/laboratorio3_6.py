#Ramiro Nahum Figueroa Castro
#Laboratorio 3

y=input("Ingresa tu edad")
while y<0:
    print "No hay edades negativas"
    y=input("Ingresa tu edad")
if y<2:
    x=y*10.5
if y>=2:
    x=((y-2)*4)+(21.0)
print y, "años equivale a", x, "años perro"
