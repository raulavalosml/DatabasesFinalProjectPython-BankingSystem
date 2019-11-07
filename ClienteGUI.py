from tkinter import *

class ClienteGUI:
    #Atributos
    frame=Tk()
    
    #Constructor
    def __init__(self):
        
        #1. Definir atributos y crear objetos de tales atributos
        self.frame.title("Bancomer: Gestion de Clientes")
        self.frame.geometry("500x400")
        
        #Labels
        self.lbNocta = Label(self.frame, text="NO. DE CUENTA: ")
        self.lbNombre = Label(self.frame, text="NOMBRE: ")
        self.lbTipo = Label(self.frame, text="TIPO DE CUENTA: ")
        self.lbSaldo = Label(self.frame, text="SALDO: ")
        
        #TextFields
        self.tfNocta = Entry(self.frame, width=20)
        self.tfNombre = Entry(self.frame, width=20)
        self.tfTipo = Entry(self.frame, width=20)
        self.tfSaldo = Entry(self.frame, width=20)
        
        #Buttons
        self.bCapturar=Button(self.frame, text="Capturar Datos")
        self.bConsultar=Button(self.frame, text="Consultar Clientes")
        
        #TextArea
        self.taDatos=Text(self.frame,width=40, height=10)
        
        
        #2. Colocar los atributos en un Layout 
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
        
        self.taDatos.grid(row=5, column=0)
        
        
        
        
        #3.Hacer visible el frame 
        self.frame.mainloop()     #setVisible(true)

    
    #Metodos
    
#main()
cliente = ClienteGUI()