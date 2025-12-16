from PIL import Image

imagen = Image.open("imagen.jpg")

tamanyo = imagen.size
print(tamanyo)

pixel1 = imagen.getpixel((0, 0))

print(pixel1)
