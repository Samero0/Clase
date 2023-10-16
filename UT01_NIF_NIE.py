#programa para saber letra de DNI y NIE

NIE = ("trwagmyfpdxbnjzsqvhlcke")
DNI_NIE = (input("Por favor, ingresa tu número de DNI o NIE (sin letra): "))

if DNI_NIE[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
    DNI_NIE= int(DNI_NIE)
    resto = DNI_NIE % 23 # Calculamos el resto de la división por 23
    letra= NIE[resto]
    print(f'Para el DNI {DNI_NIE} la letra que corresponde es: {letra} ')

elif DNI_NIE[0] in ['X', 'Y', 'Z',]:
    
    if DNI_NIE[0] == 'Y':
        DNI_NIE= '1' + DNI_NIE[1:]
        DNI_NIE= int(DNI_NIE)
        resto = DNI_NIE % 23 # Calculamos el resto de la división por 23
        letra = NIE[resto]
        (f'Para el NIE {DNI_NIE} la letra que corresponde es: {letra} ')
    
    elif DNI_NIE[0] == 'Z':
        DNI_NIE= '2' + DNI_NIE[1:]
        DNI_NIE= int(DNI_NIE)
        resto = DNI_NIE % 23 # Calculamos el resto de la división por 23
        letra = NIE[resto]
        print(f'Para el NIE {DNI_NIE} la letra que corresponde es: {letra} ')
    
    elif  DNI_NIE[0] == 'X':
         DNI_NIE= '0' + DNI_NIE[1:]
         DNI_NIE= int(DNI_NIE)
    resto = DNI_NIE % 23 # Calculamos el resto de la división por 23
    letra = NIE[resto]
    print(f'Para el NIE {DNI_NIE} la letra que corresponde es: {letra} ')

        





    