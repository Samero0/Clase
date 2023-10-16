#programa para validar entrada de nuemros enteros

valor = input("Ingrese un numero: ")
if valor.isnumeric(): #pregunta si se puede pasar a número
    valor = int(valor)
    if valor > 0:
        print("El numero es positivo")
    elif valor < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")
