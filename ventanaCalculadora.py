from Clases import AFN,AFD,Calculadora
from AlgoritmoLexObjeto import Lexico
import tkinter as tk

class ventanaCalculadora(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("520x150")
        self.master.title("Calculadora")
        self.master.config(background = "dodger blue")
        self.Objeto = None
        self.InicializacionCalculadora()

    def widges(self):
        tk.Label(self.master, text="CADENA: ",font = ("Arial Black",12),background = "dodger blue",fg = "black").grid(column = 0,row = 0,padx = 5, pady = 5)
        Entrada = tk.Entry(self.master,width = 40,background = "white",fg = "black",justify = tk.CENTER)
        Entrada.grid(column = 1,row = 0,columnspan = 2,padx = 5, pady = 5)
        tk.Label(self.master, text="RESULTADO :",font = ("Arial Black",12),background = "dodger blue",fg = "black").grid(column = 1,row = 1,padx = 5, pady = 5)
        Salida = tk.Entry(self.master,width = 10,background = "white",fg = "black",state="readonly",justify = tk.CENTER)
        Salida.grid(column = 2,row = 1,padx = 5, pady = 5)
        tk.Button(self.master, text="Calcular", height = 1, width = 5, activebackground = "blue", activeforeground = "White",command = lambda: self.Calcular(Entrada.get(),Salida)).grid(column = 3, row = 0,padx = 5, pady = 5)
        tk.Button(self.master, text="Cerrar" , command = self.master.destroy).grid(column = 1, row = 2,padx = 5, pady = 5)
        
    def InicializacionCalculadora(self):
        digitos=AFN(simbolo='0')
        uno=AFN(simbolo='1')
        dos=AFN(simbolo='2')
        tres=AFN(simbolo='3')
        cuatro=AFN(simbolo='4')
        cinco=AFN(simbolo='5')
        seis=AFN(simbolo='6')
        siete=AFN(simbolo='7')
        ocho=AFN(simbolo='8')
        nueve=AFN(simbolo='9')

        digitos.union(uno)
        digitos.union(dos)
        digitos.union(tres)
        digitos.union(cuatro)
        digitos.union(cinco)
        digitos.union(seis)
        digitos.union(siete)
        digitos.union(ocho)
        digitos.union(nueve)

        digitos.cerradura_positiva()

        mas=AFN(simbolo='+')
        menos=AFN(simbolo='-')
        mult=AFN(simbolo='*')
        div=AFN(simbolo='/')
        pot=AFN(simbolo='^')
        i=AFN(simbolo='(')
        d=AFN(simbolo=')')

        sin=AFN(simbolo='s')
        sin.concatenacion(AFN(simbolo='i'))
        sin.concatenacion(AFN(simbolo='n'))

        cos=AFN(simbolo='c')
        cos.concatenacion(AFN(simbolo='o'))
        cos.concatenacion(AFN(simbolo='s'))

        tan=AFN(simbolo='t')
        tan.concatenacion(AFN(simbolo='a'))
        tan.concatenacion(AFN(simbolo='n'))

        mas.union_especial([menos,mult,div,pot,i,d,sin,cos,tan,digitos])
        AFDD=mas.ir_a()
        self.Objeto = Calculadora(AFDD)

    def Calcular(self,cadena,Salida):
        self.Objeto.InicioOperaciones(cadena)
        resultado = self.Objeto.ConsultaResultado()
        Salida.config(state = tk.NORMAL)
        Salida.delete(0)
        Salida.insert(tk.END,resultado)
        Salida.config(state="readonly")

        