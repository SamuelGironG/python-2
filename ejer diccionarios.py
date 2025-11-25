#mis_companeros={1:['Angela',21,'ammartinezru@ut.edu.co'],2:['Kevin',17,'pradak512@gmail.com'],3:['Jose',20,'joselopezpava0403'],4:['Julian',21,'julianprado0812@gmail.com']}
#print(mis_companeros[1][2])
#print(mis_companeros[2])
#print(mis_companeros[3])
#print(mis_companeros[4])

#factura={'item':['Lapiz','Carpeta','Marcador'],'cantidad':[3,10,5],'valor':[3.50,4.25,7.85]}
#factura['item'].append('Borrador')
#factura['valor'].append(2.30)
#factura['cantidad'].append(15)
datos={1:18,2:'samuel',3:82.0,4:1.80}
datos2={'hola':123,45:32543,543:764}
for a in datos:
    print(a,datos[a])
#.clear()
print(datos.get(1,'No se encontro'))
datos.update(datos2)
print(datos)