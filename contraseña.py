validacion=False
while not validacion:
    contra=input('cree una contraseña: ')
    validacion=True
    if len(contra)<8:
        print('-Deben ser minimo 8 caracteres')
        validacion=False
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
    if not validacion:
        print('Contraseña invalida, vuelva a intentarlo')
print('Contraseña valida')