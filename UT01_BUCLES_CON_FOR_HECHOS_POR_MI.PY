for i in range(1, 10):
    print(i)


nombres = ["Ana", "Juan", "María", "Pedro", "Luis"]
for nombre in nombres:
    print(nombre)


suma = 0
for i in range(1, 11):
    suma += i
print("La suma de los primeros 10 números naturales es:", suma)


#imprime numeros pares del 2 hasta el 11
for i in range(2, 11, 2):
    print(i)

#+= actualiza el valor de una variable sumandole un valor

#el segundo valor dentro de la función range se refiere al valor de "parada" o "stop" de la secuencia que se va a generar.

"""El tercer número, especificado como step en la función range, controla el incremento o decremento entre los valores en la secuencia generada. 
Si no se especifica, el valor predeterminado es 1, lo que significa que la secuencia avanzará de uno en uno."""

#tener en cuenta que el bucle para en el numero anterior al que especificaste el valor de stop.
#por ejemplo aqui multiplica por 2 desde el 1 hasta el 10, el ultimo resultado deberia ser 20.
for i in range(1, 11):
    i*=2
    print(i)