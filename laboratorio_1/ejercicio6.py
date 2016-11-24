#laboratorio 1
#ramiro nahum figueroa castro
#24/11/2016
print( '===calcular IMC - Massa corporal====')

peso = raw_input (' Peso actual: ')
altura = raw_input ('Altura actual: ')
imc = (float(peso)/(float(altura)*float(altura)))*10000

print 'Su IMC es : ', imc
if imc <16:
    raw_input ('delgadez severa')
if imc <16.99 and imc >16:
    raw_input ('delgadez moderada')
if imc <24.99 and imc >18.5:
    raw_input ('normal')
if imc >25:
    raw_input ('sobrepeso')
