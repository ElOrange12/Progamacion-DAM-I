ollama list

elorange12@Portatil-Dani:~$ ollama list
NAME                ID              SIZE      MODIFIED    
qwen2.5-coder:3b    f72c60cabf62    1.9 GB    2 weeks ago    
qwen2.5-coder:7b    dae161e27b0e    4.7 GB    3 weeks ago

elorange12@Portatil-Dani:~$ ollama run qwen2.5-coder:7b "crea una web en HTML, sin comentarios, solo el código"

```html
	<!DOCTYPE html>
	<html lang="es">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Mi Web</title>
			<style>
				body {
				    font-family: Arial, sans-serif;
				}
				header {
				    background-color: #f8f9fa;
				    padding: 1rem;
				    text-align: center;
				}
				nav {
				    display: flex;
				    justify-content: space-around;
				    background-color: #343a40;
				    padding: 0.5rem;
				}
				nav a {
				    color: white;
				    text-decoration: none;
				}
				section {
				    margin: 2rem;
				    padding: 1rem;
				    border: 1px solid #ddd;
				    border-radius: 5px;
				}
				footer {
				    background-color: #343a40;
				    color: white;
				    text-align: center;
				    padding: 1rem;
				    position: fixed;
				    bottom: 0;
				    width: 100%;
				}
			</style>
		</head>
		<body>
			<header>
				<h1>Bienvenido a Mi Web</h1>
			</header>
			<nav>
				<a href="#home">Inicio</a>
				<a href="#about">Acerca de</a>
				<a href="#services">Servicios</a>
				<a href="#contact">Contacto</a>
			</nav>
			<section id="home">
				<h2>Inicio</h2>
				<p>Bienvenido a nuestra web. Aquí encontrarás información sobre 
		nuestros servicios y productos.</p>
			</section>
			<section id="about">
				<h2>Acerca de</h2>
				<p>Somos una empresa dedicada a ofrecer soluciones innovadoras en 
		tecnología.</p>
			</section>
			<section id="services">
				<h2>Servicios</h2>
				<ul>
				    <li>Diseño web personalizado</li>
				    <li>Desarrollo de aplicaciones móviles</li>
				    <li>Mantenimiento y soporte técnico</li>
				</ul>
			</section>
			<section id="contact">
				<h2>Contacto</h2>
				<p>Puedes contactarnos a través del siguiente formulario:</p>
				<form action="#" method="post">
				    <label for="name">Nombre:</label>
				    <input type="text" id="name" name="name"><br><br>
				    <label for="email">Email:</label>
				    <input type="email" id="email" name="email"><br><br>
				    <label for="message">Mensaje:</label>
				    <textarea id="message" name="message"></textarea><br><br>
				    <input type="submit" value="Enviar">
				</form>
			</section>
			<footer>
				<p>&copy; 2023 Mi Web. Todos los derechos reservados.</p>
			</footer>
		</body>
	</html>
```

elorange12@Portatil-Dani:~$ ollama run qwen2.5-coder:7b "crea un programa en Python, que sume 4+3. Solo quiero el codigo, ningun comentario."

```python
	print(4 + 3)
```

