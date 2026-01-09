Este ejercicio plantea un escenario sencillo relacionado con el fútbol, en el que se desea mantener un registro de varios partidos disputados. Cada partido contiene información básica como el equipo local, el equipo visitante, el resultado final y el estadio donde se ha jugado.  

El objetivo principal es practicar el uso de estructuras de datos vistas en clase, concretamente listas y diccionarios, para almacenar información relacionada y recorrerla posteriormente para mostrarla por pantalla. Este tipo de estructura es muy habitual cuando se trabaja con conjuntos de datos organizados.

---

El programa comienza con un comentario de cabecera donde se indica el nombre del ejercicio, la versión y una breve descripción de su funcionalidad. Este tipo de comentarios es útil para documentar el código y facilitar su comprensión.

A continuación, se define una lista llamada `partidos`, que contiene varios diccionarios. Cada diccionario representa un partido de fútbol y almacena sus características utilizando pares clave–valor:

```
partidos = [
    {
        'equipo_local':'Real Madrid',
        'equipo_visitante':'FC Barcelona',
        'resultado':'0-4',
        'estadio':'Santiago Bernabeu'
    }
]
```

En este caso, las claves del diccionario (equipo_local, equipo_visitante, resultado y estadio) permiten identificar claramente la información que se guarda en cada partido. Al utilizar una lista, se pueden almacenar múltiples diccionarios, cada uno representando un encuentro diferente.

Una vez definida la estructura de datos, el programa accede a un elemento concreto de la lista para mostrar el equipo local del primer partido. Esto se hace utilizando el índice 0 de la lista y la clave correspondiente del diccionario:

```
	print(partidos[0]['equipo_local'])
```

Este acceso directo permite obtener un dato específico sin necesidad de recorrer toda la estructura.

Posteriormente, se utiliza un bucle for para recorrer la lista de partidos:

```
	for partido in partidos:
```

En cada iteración, la variable partido contiene uno de los diccionarios de la lista. Dentro de este bucle, se incluye otro bucle que intenta recorrer los elementos del diccionario para mostrar su contenido por pantalla. De esta forma, el programa trata de imprimir la información almacenada en cada partido.

Finalmente, se utiliza la función print() para mostrar los datos en consola, permitiendo visualizar la información completa de los partidos registrados.

---

```
	'''
		Diccionario de partidos
		v1.0 Daniel Oliveira Vidal
		Este programa tiene un diccionario que almacena una serie de partidos y sus caracteristicas
	'''

	partidos = [
		{
			'equipo_local':'Real Madrid',
			'equipo_visitante':'FC Barcelona',
			'resultado':'0-4',
			'estadio':'Santiago Bernabeu'
		},{
			'equipo_local':'Manchester City',
			'equipo_visitante':'Liverpool',
			'resultado':'3-0',
			'estadio':'Etihad Stadium'
		},{
			'equipo_local':'Real Sociedad',
			'equipo_visitante':'Atletico de Madrid',
			'resultado':'1-1',
			'estadio':'Estadio de Anoeta'
		}
	]

	print('Equipo local primer equipo: 'partidos[0]['equipo_local'])

	for partido in partidos:
		for i in partidos:
			print(partido[i])
```

**Notas:**

- Se utiliza una lista para almacenar varios partidos de fútbol.
- Cada partido se representa mediante un diccionario con claves descriptivas.
- Se accede a un elemento concreto de la lista usando su índice.
- Se emplean bucles for para recorrer los datos almacenados.
- El programa muestra información por pantalla utilizando la función print().

---

Este ejercicio permite reforzar el uso combinado de listas y diccionarios para organizar información relacionada. A través de un ejemplo cercano como los partidos de fútbol, se practican conceptos fundamentales como el acceso a elementos concretos, el recorrido de estructuras dinámicas y la impresión de datos en consola. Este tipo de prácticas resulta esencial para entender cómo manejar conjuntos de datos más complejos en futuros programas.


		
