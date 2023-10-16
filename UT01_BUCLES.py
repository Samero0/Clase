#bucles

# i = 1
# while i <= 100: #condicion que si se cumple ejecuta los siguiente
#     print(i)
#     i += 1   #sumas 1 al valor de i pero como está en el while se ejecuta hasta el 100




i = 1
while i <= 100:
    print(f"{i:5}", end=" ")
    if i % 20 == 0: #si el resto de dividir un numero entre 10 es 0 imprime la siguiente linea debajo.
        print()
    i += 1


# n = int(input("Ingrese un numero: "))
# while n>= 0 and n<= 100:
#     print(n)
#     n = int(input("Ingrese un numero: "))



# n = int(input("Ingrese un numero: "))
# while True:
#     print(n)
#     n = int(input("Ingrese un numero: "))

# n = int(input("Ingrese un numero: "))
# while True:
#     if n%10 == 0:
#         break
#     print(n)


# n = 1
# while True:
#     if n%2 == 0:
#         print(n)
#     n += 1
#     if n == 10:
#         break



# i = 1
# while i <= 2:
#     j = 1
#     while j <= 2:
#         if i+j == 3:
#             break
#         print(i+j)
#         j += 1
#     i += 1



i = 1
while i <= 2:
    j = 1
    while j <= 2:
        if i+j == 3:
            j += 1
            continue
        print(i+j)
        j += 1
    i += 1



    
    
