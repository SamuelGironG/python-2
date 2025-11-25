 
valida=False
while not valida:
    contra=input('cree una contraseña: ')
    valida=True
    if len(contra)<8:
        print('-Deben ser minimo 8 caracteres')
        valida=False
    mayus = False
    Lower= False
    digitos= False
    simbo= False
    for a in contra:
        if a.isupper():
            mayus=True
        elif a.isdigit():
            digitos=True
        elif a.islower():
            lower=True
        else:
            simbo=True
    if not mayus:
        print('-Debe contener al menos una mayuscula')
        valida=False
    if not lower:
        print('-Debe contener al menos una minuscula')
        valida=False
    if not digitos:
        print('-Debe contener al menos un digito numerico')
        valida=False
    if not simbo:
        print('-Debe contener al menos un simbolo') 
        valida=False   
    if not valida:
        print('Contraseña invalida, vuelva a intentarlo')
print('Contraseña valida')
inten=input('Ingrese su contraseña: ')
while inten!=contra:
    print('Contraseña incorrecta, vuelva a intentar')
    inten=input('Ingrese su cotraseña de nuevo: ')
print('Menu') 
print('1. Diccionario')
print('2. Lista')
print('0. Salir')
opc=int(input('Seleccione alguna de las opciones: '))
while opc!=0:
    match opc:
        case 1:
            dicc={}
            print('1. Añadir elemento')
            print('2. Eliminar elemento')
            print('3. Volver al menu principal')
            res=int(input('Ingrese una de las opciones: '))
            while res !=3:
                match opc:
                    case 1:
                        elem=input('Ingrese algun elemento: ')
                        dicc['Nuevo']={elem}
                        print(dicc)
                    case 2:
                        elem=input('Ingrese elememto que desea eliminar: ')
                        if elem in dicc:
                            del dicc['Nuevo'][elem]
                        else:
                            print('Elemento no encontrado')
                print('1. Añadir elemento')
                print('2. Eliminar elemento')
                print('3. Volver al menu principal')
                res=int(input('Ingrese otra opcion: '))
        case 2:
            lista=[]
            print('1. Añadir elemento')
            print('2. Eliminar elemento')
            print('3. Volver al menu principal')
            res=int(input('Ingrese una de las opciones: '))
            while res!=3:
                    match opc:
                        case 1:
                            print