datos= "hola, mundo"
print(datos[-5:])
print(datos[-7:-6])
print(datos[::-1])
print(datos[::-2])
print(datos[::-3])

proverb="Más vale malo conocido que bueno por conocer"
print('malo' in proverb)

if 'malo' in proverb:
    print('si está')

proverb = "no hay mal que por bien no venga" #funcion para separar los caracteres de un string
print(proverb.split()) #devuelve una lista de strings
print(proverb.split('hay')) #
print(proverb.split(' ')[0])
   