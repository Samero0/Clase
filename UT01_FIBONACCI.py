#imprimir los 50 primeros numeros de fibonacci


# fibn2= 0
# fibn1= 1
# print(fibn2,fibn1)
# cont = 2
# while cont < 12:
#     fibn = fibn2 + fibn1
#     print(fibn)
#     cont += 1
#     fibn2 = fibn1
#     fibn1 = fibn

#averiguar si un numero es de fibonacci

numero = int(input('Numero: '))


fibn2 = 0
fibn1 = 1
fibn = 1
if numero == fibn2 or numero == fibn1:
    print (f"{numero} es de fibonacci")
else:
    while fibn < numero:
        fibn = fibn2 + fibn1
        if fibn == numero:
            print (f"{numero} es de fibonacci")
            break
        elif fibn > numero:
            print (f"{numero} no es de fibonacci")
            break
        fibn2 = fibn1
        fibn1 = fibn