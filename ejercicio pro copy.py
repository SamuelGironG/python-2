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
                            print('seleccione tipo de dato que desea ingresar: ')
                            print('1. texto')
                            print('2. enteros')
                            print('3. decimales')
                            print('4. booleanos')
                            print('0.salir')
                            ter=int(input('ingrese una opcion: '))
                            while ter!= 0:
                                match ter:
                                    case 1:
                                        print(f"La tupla antigua es {tupla}")
                                        c=list(tupla)
                                        elem=input('ingrese elemento para añadir: ')
                                        c.append(elem)
                                        tupla=tuple(c)
                                        print(f'La tupla nueva es {tupla}')
                                    case 2:
                                        print(f"La tupla antigua es {tupla}")
                                        c=list(tupla)
                                        elem=int(input('ingrese elemento para añadir: '))
                                        c.append(elem)
                                        tupla=tuple(c)
                                        print(f'La tupla nueva es {tupla}')
                                    case 3:
                                        print(f"La tupla antigua es {tupla}")
                                        c=list(tupla)
                                        elem=float(input('ingrese elemento para añadir: '))
                                        c.append(elem)
                                        tupla=tuple(c)
                                        print(f'La tupla nueva es {tupla}')
                                    case 4:
                                        print(f"La tupla antigua es {tupla}")
                                        c=list(tupla)
                                        elem=bool(input('ingrese elemento para añadir: '))
                                        c.append(elem)
                                        tupla=tuple(c)
                                        print(f'La tupla nueva es {tupla}')
                                    case _:
                                        print('opcion invalida')
                                print('1. texto')
                                print('2. enteros')
                                print('3. decimales')
                                print('4. booleanos')
                                print('0.salir')
                                ter=int(input('ingrese otra opcion: '))
                            print('Tuplas')
                            print('A. Agregar elemento')
                            print('B. Eliminar elemento')
                            print('0. Salir')
                            res=input('ingrese una opcion: ').upper()      
                            print('volviendo al menu interior')         
                    case 'B':
                        print('seleccione tipo de dato que desea eliminar: ')
                        print('1. texto')
                        print('2. enteros')
                        print('3. decimales')
                        print('4. booleanos')
                        print('0.salir')
                        ter=int(input('ingrese una opcion: '))
                        while ter!= 0:
                            match ter :
                                case 1:
                                    print(f'La tupla antigua es {tupla}')
                                    c=list(tupla)
                                    remo=input('ingrese elemento para eliminar: ')
                                    c.remove(remo)
                                    tupla=(tuple(c)) 
                                    print(f'La tupla nueva es {tupla}')
                                case 2:
                                    print(f'La tupla antigua es {tupla}')
                                    c=list(tupla)
                                    remo=int(input('ingrese elemento para eliminar: '))
                                    c.remove(remo)
                                    tupla=(tuple(c)) 
                                    print(f'La tupla nueva es {tupla}')
                                case 3:
                                    print(f'La tupla antigua es {tupla}')
                                    c=list(tupla)
                                    remo=float(input('ingrese elemento para eliminar: '))
                                    c.remove(remo)
                                    tupla=(tuple(c)) 
                                    print(f'La tupla nueva es {tupla}')
                                case 4:
                                    print(f'La tupla antigua es {tupla}')
                                    c=list(tupla)
                                    remo=bool(input('ingrese elemento para eliminar: '))
                                    c.remove(remo)
                                    tupla=(tuple(c)) 
                                    print(f'La tupla nueva es {tupla}')
                                case _:
                                    print('opcion invalida')
                            print('1. texto')
                            print('2. enteros')
                            print('3. decimales')
                            print('4. booleanos')
                            print('0.salir')
                            ter=int(input('ingrese otra opcion: '))
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
                        print('seleccione tipo de dato que desea ingresar: ')
                        print('1. texto')
                        print('2. enteros')
                        print('3. decimales')
                        print('4. booleanos')
                        print('0.salir')
                        ter=int(input('ingrese una opcion: '))
                        while ter!= 0:
                            match ter:
                                case 1:
                                    print(f'La lista antigua es {mylist}')
                                    add=input('ingrese texto a añadir: ')
                                    mylist.append(add)
                                    print(f'La lista nueva es {mylist}')
                                case 2:
                                    print(f'La lista antigua es {mylist}')
                                    add=int(input('ingrese numero entero a añadir: '))
                                    mylist.append(add)
                                    print(f'La lista nueva es {mylist}')
                                case 3:
                                    print(f'La lista antigua es {mylist}')
                                    add=float(input('ingrese numero decimal a añadir: '))
                                    mylist.append(add)
                                    print(f'La lista nueva es {mylist}')
                                case 4:
                                    print(f'La lista antigua es {mylist}')
                                    add=bool(input('ingrese dato booleano a añadir: '))
                                    mylist.append(add)
                                    print(f'La lista nueva es {mylist}')
                                case _:
                                    print('Opcion invalida')
                            print('1. texto')
                            print('2. enteros')
                            print('3. decimales')
                            print('4. booleanos')
                            print('0.salir')
                            ter=int(input('ingrese otra opcion: '))
                    case 'B':
                        print('seleccione tipo de dato que desea eliminar: ')
                        print('1. texto')
                        print('2. enteros')
                        print('3. decimales')
                        print('4. booleanos')
                        print('0.salir')
                        ter=int(input('ingrese una opcion: '))
                        while ter!= 0:
                            match ter:
                                case 1:
                                    print(f'La lista antigua es {mylist}')
                                    remo=input('ingrese texto a añadir: ')
                                    mylist.remove(remo)
                                    print(f'La lista nueva es {mylist}')
                                case 2:
                                    print(f'La lista antigua es {mylist}')
                                    remo=int(input('ingrese numero entero a añadir: '))
                                    mylist.remove(remo)
                                    print(f'La lista nueva es {mylist}')
                                case 3:
                                    print(f'La lista antigua es {mylist}')
                                    remo=float(input('ingrese numero decimal a añadir: '))
                                    mylist.remove(remo)
                                    print(f'La lista nueva es {mylist}')
                                case 4:
                                    print(f'La lista antigua es {mylist}')
                                    remo=bool(input('ingrese dato booleano a añadir: '))
                                    mylist.remove(remo)
                                    print(f'La lista nueva es {mylist}')
                                case _:
                                    print('Opcion invalida')
                            print('1. texto')
                            print('2. enteros')
                            print('3. decimales')
                            print('4. booleanos')
                            print('0.salir')
                            ter=int(input('ingrese otra opcion: '))
                    case _:
                        print('opcion invalida')
                        print('Listas')
                        print('A. Agregar elemento')
                        print('B. Eliminar elemento')
                        print('0. Salir')
                        res=input('ingrese una opcion: ').upper()      
                        print('volviendo al menu interior')  
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