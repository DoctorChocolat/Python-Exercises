'''How many lego bricks would be needed to build planet Earth - www.101computing/what-if-planet-earth-was-made-of-lego/'''

radio_tierra = 6371 #km
ancho = 16 #mm
largo = 16 #mm
alto = 10 #mm
#Convertirlo todo a la misma unidad de medida, mm

#Convertir el radio de la tierra a mm
radio_tierra_en_mm = radio_tierra * 1000000
print("El radio del planeta es ", radio_tierra_en_mm, "mm")

#Calcular y sacar el volumen del planeta en mm3. El volumen de una esfera es 4/3*Pi*r3
volumen_tierra = 4 * 3.14 * (radio_tierra_en_mm**3)/3
print("El volumen de la tierra es ", volumen_tierra)


#Calcular el volumen de una pieza lego v=alto*ancho*largo
vol_pieza = ancho * largo * alto
print("El volumen de la pieza de lego es ", vol_pieza, "mm")

#Calcula el numero de piezas de lego que se necesitan para construir una planeta tierra.
n = volumen_tierra / vol_pieza
print("Se necesitan ", n,"piezas")

'''Lo que da aprox.
≈ 4.229 x 10**26 redondeando....
≈ 423,000,000,000,000,000,000,000,000 bloques de lego'''
