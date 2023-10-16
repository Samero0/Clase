jugador1 = input('indica tu jugada: ')
jugador2 = input('indica tu jugada: ')

# if jugador1 == 'piedra' or \
#     jugador1 == 'papel' or \
#     jugador1 == 'tijera' and \
#     jugador2 == 'piedra' or \
#     jugador2 == 'papel' or \
#     jugador2 == 'tijera':

if jugador1 in ('piedra', 'papel', 'tijera') and\
    jugador2 in ('piedra', 'papel', 'tijera'):
    
    if jugador1 == 'piedra' and jugador2 == 'tijera' \
        or jugador1 == 'papel' and jugador2 == 'piedra'\
        or jugador1 == 'tijera' and jugador2 == 'papel':
        print('gana jugador 1')

    elif jugador2 == 'piedra' and jugador1 == 'tijera' \
        or jugador2 == 'papel' and jugador1 == 'piedra'\
        or jugador2 == 'tijera' and jugador1 == 'papel':
        print('gana jugador 2')

    elif jugador1 == jugador2:
        print('empate')



else: print('error en los valores de la jugada')
    



