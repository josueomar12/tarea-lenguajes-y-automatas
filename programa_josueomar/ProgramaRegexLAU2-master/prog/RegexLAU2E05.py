# encoding: utf-8
import re
print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares|.\n\"Detección de direcciones IP\".")
archivo = open("archivo4.txt", "r")
for linea in archivo.readlines():
	print (linea)
splitValues =linea.split(" ")
print("Se encontraron las siguientes coincidencias:")
for i in range(len(splitValues)):
    if(re.search(".*(\d+\.\d+\.\d+).*",splitValues[i])):
        if(i==0):
            print("Se encontraron las siguientes coincidencias:")
        try:
            print(re.search(".*(\d+\.\d+\.\d+).*",splitValues[i]).group())
        except AttributeError:
            print(re.search(".*(\d+\.\d+\.\d+).*",splitValues[i]))
            archivo.close()