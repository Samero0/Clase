# lista = [1,2,3,4,5,'a',6,7,8,9]

# pos = 0
# longitud = len(lista)

# while pos < longitud:
#     print(lista[pos])
#     pos += 1


# lista = [1,2,3,4,5,6,7,8,9]

# pos = 0
# longitud = len(lista)

# while pos < longitud:
#     if type(lista[pos]) != int:
#         print('la lista tiene un valor no entero')
#         break
#     pos += 1
# if pos == longitud:
#         print('la lista tiene valor entero')



#imprimir todos los valores que no son enteros
# lista = [1,2,'a',3,4,5,'b',6,7,8,9]

# pos = 0
# longitud = len(lista)

# while pos < longitud:
#     if type(lista[pos]) == int:
#         pos += 1
#         continue
#     else:
#          print (lista[pos])
#          pos += 1





lista = [1,2,'a',3,4,5,'b',6,7,8,9]

pos = 0
longitud = len(lista)

while pos < longitud:
    if type(lista[pos]) == int:
        print('la lista tiene valor no entero')
        break
    pos += 1
       
else:
    print ('la lista tiene valor entero') if longitud !=0\
        else print('la lista esta vacia')
         
         
 