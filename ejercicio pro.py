print('bienvenidos a estructuras')
print('1. Tuplas')
print('2. Listas')
print('3. Diccionarios')
print('0. Salir')
opc=int(input('Ingrese una opcion: '))
while opc!= 0:
    match opc:
        case 1:
            tupla=('kevin','samuel','angela')
            print('Tuplas')
            print('A. Agregar elemento')
            print('B. Eliminar elemento')
            print('0. Salir')
            res=input('ingrese una opcion: ').upper()
            while res!= '0':
                match res:
                    case 'A':
                        print(f"La tupla antigua es {tupla}")
                        c=list(tupla)
                        elem=input('ingrese elemento para añadir: ')
                        c.append(elem)
                        tupla=tuple(c)
                        print(f'La tupla nueva es {tupla}')
                    case 'B':
                        print(f'La tupla antigua es {tupla}')
                        c=list(tupla)
                        elem=input('ingrese elemento para eliminar: ')
                        c.remove(elem)
                        tupla=(tuple(c)) 
                        print(f'La tupla nueva es {tupla}')
                    case _:
                        print('Opcion incorrecta')  
                print('A. Agregar elemento')
                print('B. Eliminar elemento')
                print('0. Salir')
                res=input('ingrese otra opcion: ').upper()
            print('volviendo al menu inicial')
        case 2:
            mylist=['samuel','kevin','angela','jose']
            print('Listas')
            print('A. Agregar elemento')
            print('B. Eliminar elemento')
            print('0. Salir')
            res=input('ingrese una opcion: ').upper()
            while res!= '0':
                match res:
                    case 'A':
                        print(f'La lista antigua es {mylist}')
                        add=input('ingrese elemento a añadir: ')
                        mylist.append(add)
                        print(f'La lista nueva es {mylist}')
                    case 'B':
                        print(f'La lista antigua es {mylist}')
                        remo=input('Ingrese elemento a eliminar: ')
                        mylist.remove(remo)
                        print(f'La lista nueva es {mylist}')
                    case _:
                        print('opcion incorrecta')
                print('A. Agregar elemento')
                print('B. Eliminar elemento')
                print('0. Salir')
                res=input('ingrese otra opcion: ').upper()        
            print('volviendo al menu inicial')        
        case 3:
            dic={'Nombre':'Samuel', 'Edad':18,'Altura':1.80}       
            print(f'El diccionario es {dic}')
        case _: 
            print('opcion incorrecta')   
    print('1. Tuplas')
    print('2. Listas')
    print('3. Diccionarios')
    print('0. Salir')       
    opc=int(input('Ingrese otra opcion: '))    
print('Hasta luego')                