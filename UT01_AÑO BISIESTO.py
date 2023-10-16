#programa para ver si un año es bisiesto
#si el resto de la division en todos los casos es 0, es bisiesto.
#

anio = int(input("Ingrese un año: "))

if anio % 4 == 0 and anio % 100!= 0 or anio % 400 == 0:
    print ('es bisiesto')
else:
    print ('no es bisiesto')