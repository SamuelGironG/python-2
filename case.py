
print('METODOS DE ENVIO')
print('1.GET')
print('2.POST')
print('3.PUT')
print('4.DELETE')
print('5.SALIR')
method=int(input('ingrese una de las opciones: '))
while (method!= 5):
    match method:
        case 1:
            print('metodo de envio es GET')
        case 2:
            print('metodo de envio es POST')
        case 3:
            print('metodo de envio es PUT')
        case 4:
            print('metodo de envio es DELETE')
        case _:
            print('opcion incorrecta')  
    print('METODOS DE ENVIO')
    print('1.GET')
    print('2.POST')
    print('3.PUT')
    print('4.DELETE')
    print('5.SALIR')
    method=int(input('ingrese otra de las opciones: '))  
print('saliendo')
