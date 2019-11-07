
class ClienteDP:

	#Atributos

	#Constructores
	def __init__(self):
		self.nocta=""
		self.nombre=""
		self.tipo=""
		self.saldo=0

	def __init__(self, datos):
		if(datos==""):
			self.nocta=""
			self.nombre=""
			self.tipo=""
			self.saldo=0
		else:

			st=datos.split("_")

			self.nocta=st[0]
			self.nombre=st[1]
			self.tipo=st[2]
			self.saldo=int(st[3])

	#Accesors(getters)
	def getNocta(self):
		return self.nocta

	def getNombre(self):
		return self.nombre

	def getTipo(self):
		return self.tipo

	def getSaldo(self):
		return self.saldo

	#Mutators(seters)
	def setNocta(self,ncta):
		self.nocta=ncta

	def setNombre(self,name):
		self.nombre=name

	def setTipo(self,tcta):
		self.tipo=tcta

	def setSaldo(self,cantidad):
		self.saldo=cantidad

	#Metodos
	def toString(self):
		return self.nocta+"_"+self.nombre+"_"+self.tipo+"_"+str(self.saldo)

	def toStringSql(self):
		return "'"+self.nocta+"','"+self.nombre+"','"+self.tipo+"','"+str(self.saldo)+"'"


#clientedp=ClienteDP("1144_Guille_Ahorro_700")
#print (clientedp.toString())
#print (clientedp.toStringSql())
