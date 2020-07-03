import tkinter as tk
from Clases import AFN,Generador
import FuncionesGeneradorAFN as Fun
from AlgoritmoLex import AlgoritmoLex

class ventanaAFN_Expresion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("450x350")
        self.master.title("Genereador desde Expresion")
        self.master.config(background = "dodger blue")
        self.Objeto = None
        self.DiccionarioObjetos = {}
        self.Inicializacion()

    def widges(self):
        tk.Label(self.master, text="EXPRESIONES",font = ("Arial Black",12),background = "dodger blue",fg = "black").grid(column = 0,row = 0,padx = 5, pady = 5)
        tk.Label(self.master, text="TRANSICIONES AFN",font = ("Arial Black",12),background = "dodger blue",fg = "black").grid(column = 1,row = 0,padx = 5, pady = 5)
        Entrada = tk.Text(self.master,width = 25,height = 10,background = "white",fg = "black")
        Entrada.grid(column = 0,row = 1,padx = 10, pady = 5)
        listaTablaReglas = tk.Listbox(self.master,height = 10 , width = 33)
        listaTablaReglas.grid(column = 1,row = 1,padx = 10, pady = 5)
        tk.Button(self.master, text="Generar", height = 1, width = 10, activebackground = "blue", activeforeground = "White",command = lambda: self.Generar(Entrada.get(1.0,tk.END),listaTablaReglas)).grid(column = 0, row = 2,padx = 5, pady = 5)
        tk.Button(self.master, text="Convertir AFD", height = 1, width = 15, activebackground = "blue", activeforeground = "White",command = lambda: self.RealizarConversionAFD()).grid(column = 1, row = 2,padx = 5, pady = 5)
        tk.Button(self.master, text="Cerrar" , command = self.master.destroy).grid(column = 0, row = 3,columnspan = 2,padx = 5, pady = 5)

    def Generar(self,Cadena,Salida):
        self.DiccionarioObjetos.clear()
        Entradas = Cadena.split("\n")
        Entradas.pop()
        for Elemento in Entradas:
            self.DiccionarioObjetos[Elemento]=self.Objeto.Generar(Elemento)

        self.Mostrar(Salida)

    def Mostrar(self,Salida):
        Salida.delete(0, tk.END)
        Elementos = list(self.DiccionarioObjetos.keys())
        AuxTexto = []

        for i in Elementos:
            cadenaAux = "AFN: " + i
            AuxTexto.append(cadenaAux)
            for key in range(len(list(self.DiccionarioObjetos[i].estados.keys()))):
                AuxTexto.append("  Estado: "+str(key)+" -->  "+str(self.DiccionarioObjetos[i].estados.get(key).transiciones))
                
            AuxTexto.append("")

        Salida.insert(tk.END,*AuxTexto)

    def Inicializacion(self):
        caracteres=AFN(simbolo='A')
        caracteres.union(AFN(simbolo = 'B'))
        caracteres.union(AFN(simbolo = 'C'))
        caracteres.union(AFN(simbolo = 'D'))
        caracteres.union(AFN(simbolo = 'E'))
        caracteres.union(AFN(simbolo = 'F'))
        caracteres.union(AFN(simbolo = 'G'))
        caracteres.union(AFN(simbolo = 'H'))
        caracteres.union(AFN(simbolo = 'I'))
        caracteres.union(AFN(simbolo = 'J'))
        caracteres.union(AFN(simbolo = 'K'))
        caracteres.union(AFN(simbolo = 'L'))
        caracteres.union(AFN(simbolo = 'M'))
        caracteres.union(AFN(simbolo = 'N'))
        caracteres.union(AFN(simbolo = 'O'))
        caracteres.union(AFN(simbolo = 'P'))
        caracteres.union(AFN(simbolo = 'Q'))
        caracteres.union(AFN(simbolo = 'R'))
        caracteres.union(AFN(simbolo = 'S'))
        caracteres.union(AFN(simbolo = 'T'))
        caracteres.union(AFN(simbolo = 'U'))
        caracteres.union(AFN(simbolo = 'V'))
        caracteres.union(AFN(simbolo = 'W'))
        caracteres.union(AFN(simbolo = 'X'))
        caracteres.union(AFN(simbolo = 'Y'))
        caracteres.union(AFN(simbolo = 'Z'))

        caracteres.cerradura_positiva()

        conc=AFN(simbolo='°')
        uni=AFN(simbolo='|')
        c_p=AFN(simbolo='+')
        c_e=AFN(simbolo='*')
        s_i=AFN(simbolo='?')

        p_i=AFN(simbolo='(')
        p_d=AFN(simbolo=')')

        conc.union_especial([uni,c_p,c_e,s_i,p_i,p_d,caracteres])
        AFDD=conc.ir_a()
        self.Objeto = Generador(AFDD)

    def RealizarConversionAFD(self):
        ventana = tk.Toplevel(self.master)
        ventana.geometry("500x300")
        ventana.title("Analizador AFD")

        ListaAFNs = []
        listaObjetos = []
        Elementos = list(self.DiccionarioObjetos.keys())
    
        for x in Elementos:
            ListaAFNs.append(x)

        ObjetoUnico = self.DiccionarioObjetos.get(Elementos[0])
        llave = Elementos.pop(0)

        for i in Elementos:
            listaObjetos.append(self.DiccionarioObjetos.get(i))
            self.DiccionarioObjetos.pop(i)

        ObjetoUnico.union_especial(listaObjetos)
        NuevaLlave = "Union_Especial"

        self.DiccionarioObjetos.pop(llave)

        self.DiccionarioObjetos[NuevaLlave] = ObjetoUnico

        tk.messagebox.showinfo(message="La Union especial entre los AFN fue Exitosa", title="Confirmacion",parent = self.master)

        Elementos = list(self.DiccionarioObjetos.keys())
        AFD = self.DiccionarioObjetos[Elementos[0]].ir_a()

        print("AFD-------------------------")
        print(AFD.estados)
        print(AFD.finales)
        print(AFD.transiciones)
        print(ListaAFNs)
             
        tk.messagebox.showinfo(message="La conversion AFN --> AFD fue Exitosa", title="Confirmacion", parent = ventana)

        tk.Label(ventana, text="Cadena: ").place(x = 20, y = 20)

        Cadena = tk.Entry(ventana,width = 40)
        Cadena.place(x = 80, y = 20 )

        tk.Button(ventana, text="Analizar", height = 1, width = 5, activebackground = "blue", activeforeground = "White",command = lambda: AlgoritmoLex(Cadena.get(),Resultados,AFD)).place( x = 415, y = 15)

        tk.Label(ventana, text="Tabla del AFD ").place(x = 80, y = 45)
        listaTablaReglas = tk.Listbox(ventana,height = 11 , width = 26)
        listaTablaReglas.place(x = 20, y = 60)

        Fun.ObtencionTablaAFD(AFD,listaTablaReglas,ListaAFNs)

        tk.Label(ventana, text="Resultado Analisis ").place(x = 300, y = 45)
        Resultados = tk.Listbox(ventana,height = 11 , width = 26)
        Resultados.place(x = 260, y = 60)

        tk.Button(ventana, text="Cerrar" , fg="red", command = ventana.destroy).place(x = 225, y = 250)
