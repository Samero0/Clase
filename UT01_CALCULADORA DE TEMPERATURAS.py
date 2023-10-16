menu = """
1. ºc > ºf
2. ºf > ºc"""

print(menu)
opcion = int(input('escribe una opcion (1,2): '))
if opcion == 1:
    temp_cent = float(input('escribe temperatura en grados centigrados): '))
    temp_fahr = (temp_cent * 9/5 + 32)
    print('la temperatura en fahrenheit es: ', temp_fahr)
else:
    temp_fahr = float(input('escribe temperatura en grados fahrenheit: '))
    temp_cent = (temp_fahr -32 * 5/9)
    print('la temperatura en celcius es: ', temp_cent)


#ejemplo 2 de celcius a farenheit
# temp_cent = float(input('escribe temperatura en grados centigrados): '))
# temp_fahr = (temp_cent * 9/5 + 32)
# print(f'la temperatura en ºC es {temp_cent} y en ºF es {temp_fahr:.1f}')


