# pip3 install pillow --break-system-packages
from PIL import Image

imagen = Image.open("imagen.jpg")

anchura, altura = imagen.size				

for x in range(0, anchura):					
	for y in range(0, altura)				
		pixel = imagen.getpixel((0, 0))	
		# Primero leo los componentes de color
		rojo = pixel[0]
		verde = pixel[1]
		azul = pixel[2]
		
		# Ahora le subo el tono de color (aclaro)
		rojo += 255 - rojo								# Rojo a negativo
		verde += 255 - verde 							# Verde a negativo
		azul += 255 - azul								# Azul a negativo
		
		# Y sobreescribo el valor
		pixel = (rojo, verde, azul)					
		
imagen.save('modificado.jpg')
