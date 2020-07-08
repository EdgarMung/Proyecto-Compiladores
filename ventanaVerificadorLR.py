import tkinter as tk

class ventanaLR(tk.Frame):
    def __init__(self,master=None,Objeto=None,Objeto_Extra = None):
        super().__init__(master)
        self.master = master
        self.master.geometry("450x400")
        self.master.title("Analizador")
        self.master.config(background = "dodger blue")
        self.Objeto = Objeto
        self.Objeto_Extra = Objeto_Extra
    
    def widges(self):
        tk.Label(self.master, text="Analizador Cadena ",font = ("Arial Black",12),background = "dodger blue",fg = "black").grid(column = 0,columnspan = 2,row = 0,padx = 5, pady = 5)
        Entrada = tk.Entry(self.master,width = 50,background = "white",fg = "black",justify = tk.CENTER)
        Entrada.grid(column = 0,row = 1,padx = 15, pady = 5)
        tk.Button(self.master, text="Analizar", height = 1, width = 10, activebackground = "blue", activeforeground = "White",command = lambda: self.Verificar(Entrada.get(),Salida)).grid(column = 1, row = 1,padx = 5, pady = 5)
        tk.Label(self.master, text="Resultado:",font = ("Arial Black",9),background = "dodger blue",fg = "black").grid(column = 0,row = 2,padx = 5, pady = 5)
        Salida = tk.Listbox(self.master,height = 15 , width = 70)
        Salida.grid(column = 0,row = 3,columnspan = 2,padx = 10, pady = 5)

    def Verificar(self,Cadena,Salida):
        Solucion = []
        Salida.delete(0, tk.END)
        r=self.Objeto.convertir_cadena(Cadena)
        self.Objeto_Extra.evaluar(r,Solucion)
        Salida.insert(tk.END,*Solucion)
#"(sors)+grados*grados"