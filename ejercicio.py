opc=input('desea ingresar al programa? (S. para salir): ').upper()
while opc!= 'S':
    lista_nom=[]
    lista_estatu=[]
    lista_edad=[]
    canti=int(input('ingrese cantidad de minimo 4 personas: '))
    while canti <4:
        print('error, cantidad minima son 4 personas')
        canti=int(input('ingrese cantidad de minimo 4 personas: '))
    for a in range (0,canti):
            nom= input('ingrese nombre de la personas: ').capitalize()
            lista_nom.append(nom)
            alt=float(input('ingrese altura de la persona: '))
            lista_estatu.append(alt)
            edad=int(input('ingrese edad de la persona: '))
            lista_edad.append(edad)
    print(f'lista de nombres {lista_nom}')
    print(f'lista de alturas {lista_estatu}')
    print(f'lista de edades {lista_edad}')
    print(f'la longitud de la lista de edades es {len(lista_edad)}')
    lista_edad.pop(2)
    lista_estatu.pop(2)    
    lista_nom.pop(2)
    lista_nom.append('Carlos')
    lista_edad.append(35)
    lista_estatu.append(1.89)
    samuel_giron=[]
    samuel_giron=lista_nom+lista_edad+lista_estatu
    print(samuel_giron)
    opc=input('desea continuar en el programa? (S. para salir): ').upper()
print('Hasta luego')
  
