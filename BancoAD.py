
class BancoAD:

	def capturar(self, datos):
		# 1. Abrir el archivo
		archivo = open("Clientes.txt","a")

		# 2. Escribir, guardar o almacenar los datos en el archivo
		archivo.write(datos+"\n")

		# 3. Cerrar el archivo
		archivo.close()

		return "Captura exitosa: "+datos

	def consultarClientes(self):

		datos=""
		cliente=""
		try:
			# 1. Abrir el archivo
			archivo = open("Clientes.txt", "r")

			# 2. Procesar datos
			cliente= archivo.readline()

			while(cliente != ""):
				datos = datos + cliente
				cliente = archivo.readline()

			# 3. Cerrar el archivo
			archivo.close()

		except:
			datos = "Error al abrir el archivo..."

		return datos

	def consultarTipo(self,tcta):
		
		datos=""
		cliente=""
		encontrado = False

		try:
			# 1. Abrir el archivo
			archivo = open("Clientes.txt", "r")

			# 2. Procesar datos
			cliente= archivo.readline()

			while(cliente != ""):
				st = cliente.split("_")
				tipo = st[2]
				if(tipo == tcta):
					datos = datos + cliente
					encontrado = True

				cliente = archivo.readline()

			# 3. Cerrar el archivo
			archivo.close()

			if(not encontrado):
				datos = "No se localizó el tipo: "+tcta

		except:
			datos = "Error al abrir el archivo..."

		return datos

	def consultarNcta(self,ncta):
		
		datos=""
		cliente=""
		encontrado = False

		try:
			# 1. Abrir el archivo
			archivo = open("Clientes.txt", "r")

			# 2. Procesar datos
			cliente= archivo.readline()

			while(cliente != ""):
				st = cliente.split("_")
				numero = st[0]
				if(numero==ncta):
					datos = datos + cliente
					encontrado = True

				cliente = archivo.readline()

			# 3. Cerrar el archivo
			archivo.close()

			if(not encontrado):
				datos = "No se localizó la cuenta: "+ncta

		except:
			datos = "Error al abrir el archivo..."

		return datos