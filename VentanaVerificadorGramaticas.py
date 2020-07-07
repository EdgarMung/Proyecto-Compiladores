from Clases import AFN,AFD,Verificador,AlgoritmoLL
from AlgoritmoLexObjeto import Lexico
import tkinter as tk
from tkinter import messagebox
from ventanaAnalisadorSintacticoCadena import ventanaAnalizadorSintactico

class ventanaVerificadorGramaticas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x350")
        self.master.title("Verificador Gramaticas")
        self.master.config(background = "dodger blue")
        self.Objeto = None
        self.Gramatica = None
        self.NoTerminales = []
        self.Terminales = []
        self.Inicializacion()

    def widges(self):
        tk.Label(self.master, text="GRAMATICA ",font = ("Arial Black",12),background = "dodger blue",fg = "black").grid(column = 0,columnspan = 3,row = 0,padx = 5, pady = 5)
        Entrada = tk.Text(self.master,width = 30,height = 10,background = "white",fg = "black")
        Entrada.grid(column = 0,columnspan = 3,row = 1,padx = 23, pady = 5)
        tk.Button(self.master, text="Verificar", height = 1, width = 10, activebackground = "blue", activeforeground = "White",command = lambda: self.Verificar(Entrada.get(1.0,tk.END))).grid(column = 1, row = 2,padx = 5, pady = 5)
        tk.Button(self.master, text="LL(1)", height = 1, width = 10, activebackground = "blue", activeforeground = "White",command = self.LL1).grid(column = 0, row = 3,padx = 10, pady = 5)
        tk.Button(self.master, text="LR(0)", height = 1, width = 10, activebackground = "blue", activeforeground = "White",command = self.LR0).grid(column = 1, row = 3,padx = 10, pady = 5)
        tk.Button(self.master, text="LR(1)", height = 1, width = 10, activebackground = "blue", activeforeground = "White",command = self.LR0).grid(column = 2, row = 3,padx = 10, pady = 5)
        tk.Button(self.master, text="Cerrar" , command = self.master.destroy).grid(column = 1, row = 4,padx = 5, pady = 5)
        
    def Inicializacion(self):
        NoTerminal = AFN(simbolo = 'A')
        NoTerminal.union(AFN(simbolo = 'B'))
        NoTerminal.union(AFN(simbolo = 'C'))
        NoTerminal.union(AFN(simbolo = 'D'))
        NoTerminal.union(AFN(simbolo = 'E'))
        NoTerminal.union(AFN(simbolo = 'F'))
        NoTerminal.union(AFN(simbolo = 'G'))
        NoTerminal.union(AFN(simbolo = 'H'))
        NoTerminal.union(AFN(simbolo = 'I'))
        NoTerminal.union(AFN(simbolo = 'J'))
        NoTerminal.union(AFN(simbolo = 'K'))
        NoTerminal.union(AFN(simbolo = 'L'))
        NoTerminal.union(AFN(simbolo = 'M'))
        NoTerminal.union(AFN(simbolo = 'N'))
        NoTerminal.union(AFN(simbolo = 'O'))
        NoTerminal.union(AFN(simbolo = 'P'))
        NoTerminal.union(AFN(simbolo = 'Q'))
        NoTerminal.union(AFN(simbolo = 'R'))
        NoTerminal.union(AFN(simbolo = 'S'))
        NoTerminal.union(AFN(simbolo = 'T'))
        NoTerminal.union(AFN(simbolo = 'U'))
        NoTerminal.union(AFN(simbolo = 'V'))
        NoTerminal.union(AFN(simbolo = 'W'))
        NoTerminal.union(AFN(simbolo = 'X'))
        NoTerminal.union(AFN(simbolo = 'Y'))
        NoTerminal.union(AFN(simbolo = 'Z'))

        Terminal=AFN(simbolo = 'a')
        Terminal.union(AFN(simbolo = 'b'))
        Terminal.union(AFN(simbolo = 'c'))
        Terminal.union(AFN(simbolo = 'd'))
        Terminal.union(AFN(simbolo = 'e'))
        Terminal.union(AFN(simbolo = 'f'))
        Terminal.union(AFN(simbolo = 'g'))
        Terminal.union(AFN(simbolo = 'h'))
        Terminal.union(AFN(simbolo = 'i'))
        Terminal.union(AFN(simbolo = 'j'))
        Terminal.union(AFN(simbolo = 'K'))
        Terminal.union(AFN(simbolo = 'l'))
        Terminal.union(AFN(simbolo = 'm'))
        Terminal.union(AFN(simbolo = 'n'))
        Terminal.union(AFN(simbolo = 'o'))
        Terminal.union(AFN(simbolo = 'p'))
        Terminal.union(AFN(simbolo = 'q'))
        Terminal.union(AFN(simbolo = 'r'))
        Terminal.union(AFN(simbolo = 's'))
        Terminal.union(AFN(simbolo = 't'))
        Terminal.union(AFN(simbolo = 'u'))
        Terminal.union(AFN(simbolo = 'v'))
        Terminal.union(AFN(simbolo = 'w'))
        Terminal.union(AFN(simbolo = 'x'))
        Terminal.union(AFN(simbolo = 'y'))
        Terminal.union(AFN(simbolo = 'z'))
        Terminal.union(AFN(simbolo = '/'))
        Terminal.union(AFN(simbolo = '*'))
        Terminal.union(AFN(simbolo = '-'))
        Terminal.union(AFN(simbolo = '+'))
        Terminal.union(AFN(simbolo = '^'))
        Terminal.union(AFN(simbolo = '('))
        Terminal.union(AFN(simbolo = ')'))
        Terminal.union(AFN(simbolo = '!'))
        Terminal.union(AFN(simbolo = '¡'))
        Terminal.union(AFN(simbolo = '"'))
        Terminal.union(AFN(simbolo = '#'))
        Terminal.union(AFN(simbolo = '%'))
        Terminal.union(AFN(simbolo = '?'))
        Terminal.union(AFN(simbolo = '¿'))
        Terminal.union(AFN(simbolo = '&'))
        Terminal.union(AFN(simbolo = '='))

        Terminal.cerradura_positiva()

        flecha = AFN(simbolo='-')
        flecha.concatenacion(AFN(simbolo='>'))

        PC = AFN(simbolo=';')

        Compuerta = AFN(simbolo='|')

        NoTerminal.union_especial([Terminal,flecha,PC,Compuerta])

        AFDD = NoTerminal.ir_a()
        self.Objeto = Verificador(AFDD)

    def Verificar(self,cadena):
        AuxNoTerminales = []
        AuxTerminales = []
        self.Gramatica = cadena.replace("\n","")
        if(self.Objeto.Verificar(self.Gramatica)):
            messagebox.showinfo(message="Gramatica Aceptada", title="Info",parent=self.master)  
            self.Objeto.ObtenerNoterminalesTerminales(AuxNoTerminales,AuxTerminales)
            self.NoTerminales = AuxNoTerminales[0]
            self.Terminales = AuxTerminales[0]
            
            print("No Terminales")
            print(self.NoTerminales)
            print("Terminales")
            print(self.Terminales)
        else:
            messagebox.showerror(message="Gramatica Erronea", title="Error",parent=self.master)

    def LL1(self):
        ConjuntoReglas = self.Gramatica.split(';')
        ConjuntoReglas.pop()
        Objeto = AlgoritmoLL(ConjuntoReglas,self.NoTerminales,self.Terminales)
        ventanaSecundaria = tk.Toplevel(self.master)
        ventana = ventanaAnalizadorSintactico(ventanaSecundaria,Objeto)
        ventana.widges()

    def LR0(self):
        pass

    def LR1(self):
        pass
        
#Ejemplo = ventanaVerificadorGramaticas(tk.Tk())
#Ejemplo.widges()
#Ejemplo.mainloop()