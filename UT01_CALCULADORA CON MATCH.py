menu= """
Menú Calculadora


1 suma
2 resta
3 multiplicación
4 división
5 división entera
6 potencia
7 calculo porcentaje 
9 salir """

print(menu)

opcion = int(input("Ingrese una opción:"))

match opcion: 
    case 1:
        a = float(input("Ingrese primer número: "))
        b = float(input("Ingrese segundo número: "))
        print(f"La suma da: {a+b}")

    case 2:
        a = float(input("Ingrese primer número: "))
        b = float(input("Ingrese segundo número:"))
        print(f"La resta da: {a-b}")
    
    case 3:
        a = float(input("Ingrese primer número:"))
        b = float(input("Ingrese segundo número:"))
        print(f"La multiplicación da: {a * b}")
    
    case 4:
        a = float(input("Ingrese primer número:"))
        b = float(input("Ingrese segundo número:"))
        print(f"La división da: {a / b}")

    case 5:
        a = float(input("Ingrese primer número:"))
        b = float(input("Ingrese segundo número:"))
        print(f"La división entera da: {int(a// b)} y el resto da: {int(a % b)}")

    case 6:
        a = float(input("Ingrese primer número:"))
        b = float(input("Ingrese segundo número:"))
        print(f"La potencia da: {a ** b}")

    case 7:
        a = float(input("Ingrese porcentaje a calcular:"))
        b = float(input("Ingrese segundo número:"))
        print(f"El porcentaje da: {(a * b) / 100}")
    
    case 9:
        print('\nopcion salida')

    case _: 
        print("Opción incorrecta")
