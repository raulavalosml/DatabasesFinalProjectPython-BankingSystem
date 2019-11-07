from tkinter import *
#from BancoAD import *
from BancoADjdbc import *

class ClienteGUI1:
	# Atributos
	frame = Tk()
	#bancoad = BancoAD()
	bancoad=BancoADjdbc()

	# Constructor
	def __init__(self):
		# 1. Definir Atributos y crear los objetos de tales atributos
		self.frame.title("Bancomer: Gestión de Clientes")
		self.frame.geometry("500x400")

		# Labels
		self.lbNocta 	= Label(self.frame, text="NO. DE CUENTA:    ")
		self.lbNombre	= Label(self.frame, text="NOMBRE:    ")
		self.lbTipo		= Label(self.frame, text="TIPO DE CUENTA:   ")
		self.lbSaldo	= Label(self.frame, text="SALDO:    ")

		# TextFields
		self.tfNocta	= Entry(self.frame, width=20)
		self.tfNombre	= Entry(self.frame, width=20)
		self.tfTipo		= Entry(self.frame, width=20)
		self.tfSaldo	= Entry(self.frame, width=20)

		# Buttons
		self.bCapturar 		= Button(self.frame, text="Capturar Datos", command=self.bCapturarEvent)
		self.bConsultar 	= Button(self.frame, text="Consultar Clientes", command=self.bConsultarEvent)
		self.bConsultarTipo	= Button(self.frame, text="Consultar tipo de cuenta", command=self.bConsultarTipoEvent)
		self.bConsultarNcta = Button(self.frame, text="Consultar No. de cuenta", command=self.bConsultarNctaEvent)


		# TextArea
		self.taDatos = Text(self.frame, width=40, height=10)

		# 2. Colocar los atributos en un layout
		self.lbNocta.grid(row=0, column=0)
		self.tfNocta.grid(row=0, column=1)

		self.lbNombre.grid(row=1, column=0)
		self.tfNombre.grid(row=1, column=1)

		self.lbTipo.grid(row=2, column=0)
		self.tfTipo.grid(row=2, column=1)

		self.lbSaldo.grid(row=3, column=0)
		self.tfSaldo.grid(row=3, column=1)

		self.bCapturar.grid(row=4, column=0)
		self.bConsultar.grid(row=4, column=1)

		self.bConsultarTipo.grid(row=5, column=0)
		self.bConsultarNcta.grid(row=5, column=1)

		self.taDatos.grid(row=6, column=0)
		# 3. Hacer visible el frame
		self.frame.mainloop() #setVisible(true)

	# Métodos

	def obtenerDatos(self):
		ncta = self.tfNocta.get()
		nombre = self.tfNombre.get()
		tipo = self.tfTipo.get()
		saldo = self.tfSaldo.get()

		if(ncta == "" or nombre == "" or tipo == "" or saldo == ""):
			datos = "VACIO"
		else:
			try:
				nsaldo = float(saldo)
				datos = ncta+"_"+nombre+"_"+tipo+"_"+saldo
			except:
				datos = "NO_NUMERICO"

		

		return datos

	def bCapturarEvent(self):
		datos = self.obtenerDatos()


		if(datos == "VACIO"):
			respuesta = "Algún dato está vacío..."
		else:
			if(datos == "NO_NUMERICO"):
				respuesta = "Saldo debe ser numérico..."
			else:
				respuesta = self.bancoad.capturar(datos)

		self.taDatos.delete("1.0",END)
		self.taDatos.insert(END, respuesta)

	def bConsultarEvent(self):
		datos = self.bancoad.consultarClientes()

		self.taDatos.delete("1.0", END)
		self.taDatos.insert(END,datos)

	def bConsultarTipoEvent(self):
		tcta = self.tfTipo.get()
		datos = self.bancoad.consultarTipo(tcta)

		self.taDatos.delete("1.0", END)
		self.taDatos.insert(END,datos)

	def bConsultarNctaEvent(self):
		ncta = self.tfNocta.get()
		datos = self.bancoad.consultarNcta(ncta)

		self.taDatos.delete("1.0", END)
		self.taDatos.insert(END,datos)
		
# main()
cliente = ClienteGUI1()