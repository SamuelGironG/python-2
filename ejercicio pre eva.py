
colores={}
ing_color=input('Ingrese un color: ')
colores['color']=ing_color

print('Menu \n')
print('''1.ver
2.editar
3-eliminar
0.salir
    ''')
opc=int(input('seleccione una opcion: '))
match opc:
    case 1:
        print(colores)
    case 2:
        for m,a in colores.items():
            print(f'key {m} and values {a}')
            busque=input('Ingrese el color a cambiar: ')
            if busque in a:
                print(f'se en contro el color {busque}')
            else:
                print(f'No se encontro el color {busque}')
    case 3:
        p
    case _:
        p
    
        