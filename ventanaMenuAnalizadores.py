import tkinter as tk

class ventanaMenuAnalizadores(tk.Frame):
    def __init__(self,Grama,master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x500")
        self.master.title("Verificador Gramaticas")
        self.master.config(background = "dodger blue")
        self.Gramatica = Grama
        self.ConjuntoReglas = None
        self.Inicializacion()
    
    def Inicializacion(self):
        print(self.Gramatica)
        self.ConjuntoReglas = self.Gramatica.split(';')
        self.ConjuntoReglas.pop()
        


Menu = ventanaMenuAnalizadores(master=tk.Tk(),Grama="S->E;E->EorT|T;T->T&C|C;C->C*|C+|F;F->(E)|a;") 
        