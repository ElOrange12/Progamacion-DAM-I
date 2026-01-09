'''
	Mini CRUD menu
	v1.0 Daniel Oliveira Vidal
	Este programa añade platos, lee los platos actuales y guarda en memoria un menú
'''
import pickle

menu = ['Paella','Tacos','Lasaña']

while True:
	print('Opciones a elegir:\n1.-Añadir plato al menú\n2.-Listar menu\n3.-Guardar menú en archivo\n4.-Salir')
	respuesta = int(input('Escoje una opción: '))
	
	if respuesta == 1:
		plato_nuevo = input('¿Que plato quiere introducir al menú?: ')
		
		menu.append(plato_nuevo)
		
	elif respuesta == 2:
		for platos in menu:
			print(platos)
		
	elif respuesta == 3:
		archivo = open('datos.bin', 'w')
		archivo.write(menu)
		archivo.close
	
	elif repuesta == 4:
		break
		
	else:
		print('Eso no es una opción posible')
		
