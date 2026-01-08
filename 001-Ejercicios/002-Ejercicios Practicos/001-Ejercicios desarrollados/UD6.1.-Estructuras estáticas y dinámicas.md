En este ejercicio nos ponemos en el papel de un aficionado al deporte que desea digitalizar sus registros. Para ello, utilizamos una de las estructuras más potentes en Python: la lista de diccionarios.

Hasta ahora hemos trabajado con listas (colecciones ordenadas) y diccionarios (colecciones de pares clave-valor) por separado. Al combinarlas, podemos crear estructuras de datos complejas que simulan una base de datos sencilla: la lista actúa como la "tabla" y cada diccionario como una "fila" o registro con campos específicos (equipo_local, resultado, etc.). Este concepto es fundamental antes de abordar la Programación Orientada a Objetos (POO), ya que nos enseña a encapsular datos relacionados en una única entidad lógica.

---

El código comienza definiendo una lista llamada partidos. Dentro de esta lista, en lugar de almacenar datos simples (como números o cadenas), almacenamos tres diccionarios. Cada diccionario representa un partido específico y tiene las mismas claves para mantener la coherencia:

- equipo_local
- equipo_visitante
- resultado
- estadio

Posteriormente, el programa intenta realizar dos operaciones de lectura:

1. Acceso directo: Se intenta imprimir el nombre del equipo local del primer partido accediendo al índice 0 de la lista y luego a la clave correspondiente.

2. Recorrido: Se intenta recorrer la lista para mostrar la información de todos los partidos mediante bucles.
