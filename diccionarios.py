#dictionary={'nombres': 'Samuel', 'apellidos': 'Giron', 'edad':18,'Zapatos': ['Nike','Adidas']}
#dictionary['edad']=20
#dictionary['saludo']='Hola'
#print(dictionary.get('edad'))
#print(dictionary['nombres'])
#print(dictionary)
#print(dictionary['Zapatos'][0])
#print(dictionary['Zapatos'][0][1])



datos={9:{'name':'pepito','lastname':'tovar','pasw':'contrasñ1'}}
last=datos[9]['pasw']

for a in last:
    print(a)

busc=input('Ingrese la contraseña: ')
while busc in last:
    print(busc)
    break