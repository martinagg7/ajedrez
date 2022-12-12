from ajedrez import *
tablero = [
['♜',	'♞',	'♝',	'♛',	'♚',	'♝',	'♞',	'♜'],
['♟',	'♟',	'♟',	'♟',	'♟',	'♟',	'♟',	'♟'],
[' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
[' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
[' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
[' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
['♙',	'♙',	'♙',	'♙',	'♙',	'♙',	'♙',	'♙'],
['♖',	'♘',	'♗',	'♕',	'♔',	'♗',	'♘',	'♖'],
]



print('ESTE ES EL TABLERO DE LA PARTIDA:')
for k in tablero:
    print(k)
print('Desea hacer algun movimiento?')
respuesta=input('Si/No: ')
if respuesta == 'No':
    print('De acuerdo, su tablero se quedara asi:')
    for k in tablero:
        print(k)
elif respuesta == 'Si':
    print('I')
    print('La primera posicion es la fila y la segunda es la columna')
    print('LAS FILAS SON: 1,2,3,4,5,6,7,8 , la fila uno se encuentra en la parte suprior del tablero, es decir donde se encuntran las piezas blancas')

    
    

