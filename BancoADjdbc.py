import mysql.connector
from ClienteDP import ClienteDP

class BancoADjdbc:

	def capturar(self, datos):
		try:
			# 1. Abrir el archivo
			conexion=mysql.connector.connect(user="root",database="Bancomer")
			print("Conexion exitosa a la base de datos...\n")

			#1.5 Preparar el INSERT a ejecutar
			clientedp=ClienteDP(datos)
			insertCliente = "INSERT INTO Cliente VALUES ("+clientedp.toStringSql()+")"


			# # 2. Escribir, guardar o almacenar los datos en el archivo
			# archivo.write(datos+"\n")
			statement=conexion.cursor()
			statement.execute(insertCliente)#aqui esta en el buffer
			conexion.commit() #Cuando tenemos bases de datos grandes necesitamos un commit. para asegurarnos de que esta guardado en la tabla

			# # 3. Cerrar el archivo
			# archivo.close()
			statement.close
			conexion.close
			resultado="Captura exitosa: "+datos
		except:
			resultado="Error en la captura de datos: "+datos+"..."

		return resultado

	def consultarClientes(self):

		datos=""
		cliente=""
		try:
			# 1. Abrir el archivo
			#archivo = open("Clientes.txt", "r")
			conexion = mysql.connector.connect(user="root", database="Bancomer")
			print("Conexion exitosa a la BD...")

			# 1.1 Preparar el Query y ejecutarlo
			query = "SELECT * FROM Cliente"
			statement = conexion.cursor()
			statement.execute(query)

			# 2. Procesar datos
			#cliente= archivo.readline()

			#while(cliente != ""):
			#	datos = datos + cliente
			#	cliente = archivo.readline()
			clientedp = ClienteDP(datos)
			cliente = statement.fetchone()
			while(cliente != None):
				clientedp.setNocta(cliente[0])
				clientedp.setNombre(cliente[1])
				clientedp.setTipo(cliente[2])
				clientedp.setSaldo(cliente[3])

				datos = datos + clientedp.toString() + "\n"
				cliente = statement.fetchone()
			# 3. Cerrar el archivo
			#archivo.close()
			statement.close()
			conexion.close

		except:
			datos = "Error al consultar la base de datos..."

		return datos

	def consultarTipo(self,tcta):
		
		datos=""
		cliente=""
		encontrado=False
		try:
			# 1. Abrir el archivo
			#archivo = open("Clientes.txt", "r")
			conexion = mysql.connector.connect(user="root", database="Bancomer")
			print("Conexion exitosa a la BD...")

			# 1.1 Preparar el Query y ejecutarlo
			query = "SELECT * FROM Cliente WHERE tipo='"+tcta+"'"
			statement = conexion.cursor()
			statement.execute(query)

			# 2. Procesar datos
			#cliente= archivo.readline()

			#while(cliente != ""):
			#	datos = datos + cliente
			#	cliente = archivo.readline()
			clientedp = ClienteDP(datos)
			cliente = statement.fetchone()
			while(cliente != None):
				clientedp.setNocta(cliente[0])
				clientedp.setNombre(cliente[1])
				clientedp.setTipo(cliente[2])
				clientedp.setSaldo(cliente[3])

				encontrado=True;

				datos = datos + clientedp.toString() + "\n"
				cliente = statement.fetchone()
			# 3. Cerrar el archivo
			#archivo.close()
			statement.close()
			conexion.close

			if(not encontrado):
				datos="No se localizo el tipo de cuenta: "+tcta

		except:
			datos = "Error al consultar al base de datos..."

		return datos

	def consultarNcta(self,ncta):
		
		datos=""
		cliente=""
		try:
			# 1. Abrir el archivo
			#archivo = open("Clientes.txt", "r")
			conexion = mysql.connector.connect(user="root", database="Bancomer")
			print("Conexion exitosa a la BD...")

			# 1.1 Preparar el Query y ejecutarlo
			query = "SELECT * FROM Cliente WHERE nocta='"+ncta+"'"
			statement = conexion.cursor()
			statement.execute(query)

			# 2. Procesar datos
			clientedp = ClienteDP(datos)
			cliente = statement.fetchone()
			if(cliente != None):
				clientedp.setNocta(cliente[0])
				clientedp.setNombre(cliente[1])
				clientedp.setTipo(cliente[2])
				clientedp.setSaldo(cliente[3])

				datos = datos + clientedp.toString() + "\n"
				cliente = statement.fetchone()
			else:
				datos="No se localizo el tipo de cuenta: "+tcta
			# 3. Cerrar el archivo
			#archivo.close()
			statement.close()
			conexion.close

		except:
			datos = "Error al consultar la base de datos..."

		return datos
