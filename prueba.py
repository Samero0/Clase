cadena = "123456789"  # Tu cadena de dígitos

# Inicializa una lista para almacenar los números
numeros = []

# Convierte cada carácter de la cadena en un número
for caracter in cadena:
    numero = int(caracter)
    numeros.append(numero)

# Multiplica por 2 las posiciones impares
for i in range(len(numeros)):
    if i % 2 == 1:  # Comprueba si la posición es impar
        numeros[i] *= 2

# Imprime la lista resultante de números
print(numeros)





