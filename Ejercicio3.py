#3 Realice la suma y resta de dos imágenes cualquiera con openc (cv2)
# Función para cargar una imagen y convertirla en escala de grises
def CargarImagen(dir_imagen):
    image = cv2.imread(dir_imagen)
    return image

# Rutas de las imágenes en Google Drive
imagen_ruta1 =  '/content/drive/MyDrive/inf_lic_silva/leon1.jpg'
imagen_ruta2 =  '/content/drive/MyDrive/inf_lic_silva/leon2.jpg'

# Cargar dos imágenes
imagen1 = CargarImagen(imagen_ruta1)
imagen2 = CargarImagen(imagen_ruta2)

# verifica que sean el mismo tamañao
if imagen1.shape != imagen2.shape:
    print("Las imágenes no tienen el mismo tamaño. Redimensionando la segunda imagen para que coincida con la primera.")
    imagen2 = cv2.resize(imagen2, (imagen1.shape[1], imagen1.shape[0]))

# Realizar la suma de las dos imágenes
suma_de_imagen = cv2.add(imagen1, imagen2)

# Realizar la resta de las dos imágenes
resta_de_imagen = cv2.subtract(imagen1, imagen2)

# Mostrar las imágenes originales y las imágenes resultantes
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.title('Imagen 1')
plt.imshow(cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB))

plt.subplot(2, 2, 2)
plt.title('Imagen 2')
plt.imshow(cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB))

plt.subplot(2, 2, 3)
plt.title('Suma de Imágenes')
plt.imshow(cv2.cvtColor(suma_de_imagen, cv2.COLOR_BGR2RGB))

plt.subplot(2, 2, 4)
plt.title('Resta de Imágenes')
plt.imshow(cv2.cvtColor(resta_de_imagen, cv2.COLOR_BGR2RGB))

plt.show()