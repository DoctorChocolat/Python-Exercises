'''Jack y las judias mágicas....
Cada hora crece 150% y gana un extra de 30cm
Primera hora                100cms
2 hora	100 x 1.5 + 30 =	180
3 hora	180 x 1.5 + 30 =	300
4 hora 	300 x 1.5 + 30 =    480...etc
El programa debe pedir el numero de horas que han pasado y mostrar cuanto ha crecido la judia mágica. Pasarlo a metros'''

print("Jack y las judias mágicas")
altura = 100
horas = int(input("Introduce en el número de horas que han pasado: "))

print("La primera hora tras plantarlo el tallo medía 100 cms")
for i in range (1,horas):
    altura = altura*1.5+30
print("Tras ",horas, " horas, la judia mágica mide ", altura/100, "metros") 
    
print("Y todavia creciendo...")
