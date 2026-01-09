En este ejercicio práctico se trabaja con la gestión de un menú de comidas utilizando una lista como estructura principal de almacenamiento. El programa permite al usuario interactuar con el menú a través de una interfaz sencilla por consola, ofreciendo distintas opciones para añadir platos, listar los existentes y guardar la información en un archivo binario.

Además, se introduce el uso del módulo `pickle`, que permite almacenar estructuras de datos complejas en archivos para que la información pueda conservarse incluso después de cerrar el programa. Este tipo de ejercicios resulta fundamental para comprender la persistencia de datos y la interacción entre memoria y almacenamiento.

---

El programa comienza con un comentario de cabecera que describe el nombre del ejercicio, la versión y su funcionalidad principal. Este comentario sirve como documentación inicial del código.

A continuación, se importa el módulo `pickle`, que se utilizará para trabajar con archivos binarios y guardar la información del menú:

```
	import pickle
```

Seguidamente, se define una lista llamada `menu`, que contiene inicialmente varios platos. Esta lista actúa como estructura dinámica donde se irán almacenando los datos introducidos por el usuario:

```
	menu = ['Paella','Tacos','Lasaña']
```

El núcleo del programa se basa en un bucle infinito `while True`, que permite mostrar de forma continua un menú de opciones hasta que el usuario decida salir del programa:

```
	while True:
```

Dentro de este bucle, se muestra por pantalla un menú con las distintas opciones disponibles y se solicita al usuario que introduzca una respuesta numérica:

```
	respuesta = int(input('Escoje una opción: '))
```

Si el usuario selecciona la opción 1, el programa solicita el nombre de un nuevo plato y lo añade a la lista `menu` utilizando el método `append`, lo que permite ampliar dinámicamente el contenido de la lista:

```
	menu.append(plato_nuevo)
```

Cuando se selecciona la opción 2, se recorre la lista `menu` mediante un bucle `for` y se imprime cada uno de los platos almacenados, mostrando así el contenido actual del menú:

```
	for platos in menu:
		print(platos)
```

En el caso de la opción 3, el programa abre un archivo binario llamado `datos.bin` con el objetivo de guardar el contenido del menú. Para ello, se crea o abre el archivo y se escribe la información de la lista en él, permitiendo almacenar los datos de forma persistente.

Por último, si el usuario selecciona la opción de salida, el bucle se interrumpe mediante la instrucción `break`, finalizando la ejecución del programa. Si la opción introducida no es válida, se muestra un mensaje de error por pantalla.

```
	'''
		CRUD menu
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
```

**Notas:**
- Se utiliza una lista para almacenar los platos del menú.
- El programa funciona mediante un bucle infinito con un menú de opciones.
- Se permite añadir y listar elementos de una estructura dinámica.
- Se trabaja con archivos binarios para guardar información.
- Se emplean condicionales para controlar el flujo del programa según la opción elegida.

---

Este ejercicio refuerza el uso de listas como estructura de datos dinámica y la creación de programas interactivos mediante menús por consola. Además, introduce el concepto de persistencia de datos a través de archivos binarios, una técnica muy utilizada en aplicaciones reales para conservar información. La combinación de bucles, condicionales y manejo de archivos permite consolidar conceptos fundamentales de programación en Python.
