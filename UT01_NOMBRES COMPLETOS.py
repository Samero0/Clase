#leemos un nombre completo

nombre=input('Nombre completo: ')

lista_palabras=nombre.split()
print (lista_palabras)

if len(lista_palabras)>=2:
    if len(lista_palabras)==2:
        print(lista_palabras[1],', ',lista_palabras[0])
    elif len(lista_palabras)==3:
        nro_apellidos = int(input('¿Cuantos apellidos tienes? (1,2): '))
        if nro_apellidos==1:
            print(lista_palabras[2]+', '+lista_palabras[0]+ ' '+lista_palabras[1])
        else:
            print(lista_palabras[1]+' '+lista_palabras[2]+ ', '+lista_palabras[0])
    else:
        print(lista_palabras[2]+' '+lista_palabras[3]+ ', '+lista_palabras[0] + ' '+lista_palabras[1])

        
else:print('Error, escribe un nombre completo')

# apellidos=input('Apellidos: ')




# nombre=input('Nombre : ')
# apellidos=input('apellidos: ')

# if len(nombre) > 0 and len(apellidos) > 0:
#     print(apellidos+ ', '+nombre)   

# else:print('Error, nombre o apellidos no pueden estar en blanco')

# nombre01= input("Ingrese su nombre: ")
# nombre= input("Ingrese su segundo nombre: ")
# apellidos01= input('ingrese su apellido: ')
# apellidos02= input('ingrese su segundo apellido: ')

# a_escribir= ''
