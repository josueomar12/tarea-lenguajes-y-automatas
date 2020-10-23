import re
print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares|\n\"###PROGRAMAS###\".")
def UNO():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Las palabras que tengan una longitud de 7 letras o más\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
	splitValues = linea.split(" ")
	print("Se encontraron las siguientes coincidencias:")
	for i in range(len(splitValues)):
		if(re.search("\D[\w]{7,}",splitValues[i])):
			if(i==0):
				print("Se encontraron las siguientes coincidencias:")
			try:
				print(re.search("\D[\w]{7,}",splitValues[i]).group())
			except AttributeError:
				print(re.search("\D[\w]{7,}",splitValues[i]))
				archivo.close()
def DOS():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Detección de direcciones IP\".")
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
def TRES():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Expresiones que NO finalicen con una vocal\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search(".*([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z])+$",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					print(re.search(".*([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z])+$",splitValues[i]).group())
				except AttributeError:
					print(re.search(".*([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z])+$",splitValues[i]))
					archivo.close()
def CUATRO():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Las palabras que inicien con \"M\" donde la segunda letra NO sea una vocal\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search("^[Mm]([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z]).*",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					print(re.search("^[Mm]([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z]).*",splitValues[i]).group())
				except AttributeError:
					print(re.search("^[Mm]([B-D]|[b-d]|[F-H]|[f-h]|[J-N]|[j-n]|[P-T]|[p-t]|[V-Z]|[v-z]).*",splitValues[i]))
					archivo.close()
def CINCO():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Expresiones encerradas entre comillas\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		for i in range(len(splitValues)):
			if(re.search("('.*')|(\".*\")*",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					print(re.search("('.*')|(\".*\")*",splitValues[i]).group())
				except AttributeError:
					print(re.search("('.*')|(\".*\")*",splitValues[i]))
					archivo.close()
def SEIS():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Detección de fechas\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search(".*([0-3][0-9].[0-1][0-9].\d).*",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					print(re.search(".*([0-3][0-9].[0-1][0-9].\d).*",splitValues[i]).group())
				except AttributeError:
					print(re.search(".*([0-3][0-9].[0-1][0-9].\d).*",splitValues[i]))
					archivo.close()
def SIETE():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Detección de números de teléfono en México\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search("(^9[0-9]{9})",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					print(re.search("(^9[0-9]{9})",splitValues[i]).group())
				except AttributeError:
					print(re.search("(^9[0-9]{9})",splitValues[i]))
					archivo.close()
def OCHO():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Detección de correos electrónicos\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search("^[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}$",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					print(re.search("^[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}$",splitValues[i]).group())
				except AttributeError:
					print(re.search("^[a-zA-Z0-9_\-\.~]{2,}@[a-zA-Z0-9_\-\.~]{2,}\.[a-zA-Z]{2,4}$",splitValues[i]))
					archivo.close()
def NUEVE():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Detección de URL's\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					print(re.search("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$",splitValues[i]).group())
				except AttributeError:
					print(re.search("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$",splitValues[i]))
					archivo.close()
def DIEZ():
	print("Lenguajes y Autómatas U2|Ejercicios Exp. Regulares\n\"Detección de códigos postales\".")
	archivo = open("archivo4.txt", "r")
	for linea in archivo.readlines():
		print (linea)
		splitValues = linea.split(" ")
		print("Se encontraron las siguientes coincidencias:")
		for i in range(len(splitValues)):
			if(re.search("[0-9]{5}",splitValues[i])):
				if(i==0):
					print("Se encontraron las siguientes coincidencias:")
				try:
					print(re.search("[0-9]{5}",splitValues[i]).group())
				except AttributeError:
					print(re.search("[0-9]{5}",splitValues[i]))
					archivo.close()
while True:
	print("1.-PALABRAS MAYORES A 7")
	print("2.-DIRECCIONES IP")
	print("3.-EXPRECIONES QUE NO FINALICEN CON VOCAL")
	print("4.-PALABRAS CON M Y QUE NO SEA VOCAL")
	print("5.-ENTRE COMILLAS")
	print("6.-FECHAS")
	print("7.-TELEFONOS")
	print("8.-CORREOS ELECTRONICOS")
	print("9.-URL´S")
	print("10.-CODIGOS POSTALES")
	Opcion = input("Elige una opcion:")
	if Opcion.strip() == '1':
		UNO()
	if Opcion.strip() == '2':
		DOS()
	if Opcion.strip() == '3':
		TRES()
	if Opcion.strip() == '4':
		CUATRO()
	if Opcion.strip() == '5':
		CINCO()
	if Opcion.strip() == '6':
		SEIS()
	if Opcion.strip() == '7':
		SIETE()
	if Opcion.strip() == '8':
		OCHO()
	if Opcion.strip() == '9':
		NUEVE()
	if Opcion.strip() == '10':
		DIEZ()