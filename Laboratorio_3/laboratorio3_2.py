#Ramiro Nahum Figueroa Castro
#Laboratorio 3
n=int(input("Escriba un numero del que quiera la suma de sus digitos: "))
ahh=str(n)
ahh=map(int,ahh)

def suma(a):
	s=0
	for i in range(0,len(a)):
		s=s+a[i]
	return s

print suma(ahh)
