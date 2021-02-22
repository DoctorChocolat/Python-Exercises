#Eureka! - Archimedes and King Hiero's Crown - www.101computing.net/eureka-and-king-hieros-crown/

mass = float(input("Intro the mass of the crown in kg: "))
volume = float(input("Intro the volume of the crown in cubic meter, m3: "))

#Code here to calculate the density and compare it with the density of a range of differen metals
# Densidad = Masa / Volumen
d = mass/volume
if d >2400 and d <2700:
    print ("La corona es de Aluminio")
elif d >8100 and d <8300:
    print ("La corona es de Bronce")
elif d >10400 and d <10600:
    print ("La corona es de Plata")
elif d >11200 and d <11400:
    print ("La corona es de Plomo")
elif d >17100 and d < 17500:
    print ("La corona es de Oro")
elif d >21000 and d <21500:
    print ("La corona es de Platino")
