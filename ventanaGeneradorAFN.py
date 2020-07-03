import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from AlgoritmoLex import AlgoritmoLex
import FuncionesGeneradorAFN as Fun

# Clase para crear la pantalla **********************************************************************************
class ventanaGeneradorAFN(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.DiccionarioObjetos = {}
        self.AFD = ""
        self.master.geometry("400x700")
        self.master.title("Generador AFN")
        self.master.config(bg="navy")
        self.ListaAFNs = []
        self.pack()

    def create_widgets(self):

        tk.Button(self, text="AFN Basico", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("AFN Simple",self.master)).pack()
        tk.Button(self, text="Union", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Union",self.master)).pack()
        tk.Button(self, text="Concatenacion", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold" ,command = lambda: self.create_second_window("Concatenacion",self.master)).pack()
        tk.Button(self, text="Cerradura Positiva", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold" ,command = lambda: self.create_second_window("Cerradura+",self.master)).pack()
        tk.Button(self, text="Cerradura Kleene", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Cerradura*",self.master)).pack()
        tk.Button(self, text="Opcional", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Opcional",self.master)).pack()
        tk.Button(self, text="Realizar Union Especial", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: Fun.CrearUnionEspecial(self.DiccionarioObjetos,self.ListaAFNs)).pack()
        tk.Button(self, text="ImprimirTransiciones", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Mostrar",self.master)).pack()
        tk.Button(self, text="Convertir AFN  a AFD", height = 3, width = 20, activebackground = "blue", activeforeground = "White",font = "bold",command = lambda: self.create_second_window("Analizador",self.master)).pack()
        self.quit = tk.Button(self, text="Cerrar" , fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_second_window(self,tipo_ventana,root):
        ventana = tk.Toplevel(root)
        ventana.geometry("500x300")
        ventana.title("Operación "+tipo_ventana)
          

        if tipo_ventana == "AFN Simple":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/AFNSimple.jpeg")
            aux = aux.resize((250, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)
            
            tk.Label(ventana, text="Por favor, Ingrese el caracter del AFN Simple: ").place(x = 50, y = 50)
            Entrada = tk.Entry(ventana,width = 10)
            Entrada.place(x = 330, y = 50 )

            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: Fun.CreacionAFNSimple(self.DiccionarioObjetos,lista,Entrada,ventana)).place( x = 420, y = 46)
            lista = tk.Listbox(ventana)
            

            lista.insert(tk.END,*Elementos)
            lista.place(x = 50, y = 80)
            
            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 220 , y = 100)

        if tipo_ventana == "Union":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Union.jpeg")
            aux = aux.resize((320, 170), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)
            
            tk.Label(ventana, text="Union entre: ").place(x = 50, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 135, y = 50)
            
            AFN_b = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_b.place(x = 275, y = 50)

            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: Fun.CreacionUnion(self.DiccionarioObjetos,AFN_a,AFN_b,ventana)).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 90 , y = 75)

        if tipo_ventana == "Concatenacion":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Concatenacion.jpeg")
            aux = aux.resize((350, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)
            
            tk.Label(ventana, text="Concatenacion entre: ").place(x = 25, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 12)
            AFN_a.place(x = 160, y = 50)
            
            AFN_b = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 12)
            AFN_b.place(x = 290, y = 50)

            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: Fun.CreacionConcatenacion(self.DiccionarioObjetos,AFN_a,AFN_b,ventana)).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 70 , y = 120)

        if tipo_ventana == "Cerradura+":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/CerraduraPositiva.jpeg")
            aux = aux.resize((350, 125), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)

            tk.Label(ventana, text="Cerradura Positiva a: ").place(x = 100, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 250, y = 50)
            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: Fun.CreacionCerraduraPositiva(self.DiccionarioObjetos,AFN_a,ventana)).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 70 , y = 100)

        if tipo_ventana == "Cerradura*":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/CerraduraAsterisco.jpeg")
            aux = aux.resize((350, 125), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)

            tk.Label(ventana, text="Cerradura de Kleene a: ").place(x = 100, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 250, y = 50)
            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: Fun.CreacionCerraduraKleene(self.DiccionarioObjetos,AFN_a,ventana)).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 70 , y = 100)

        if tipo_ventana == "Opcional":
            Elementos = list(self.DiccionarioObjetos.keys())
            aux = Image.open("./Imagenes/Opcional.jpeg")
            aux = aux.resize((350, 125), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(aux)

            tk.Label(ventana, text="Cerradura Opcional a: ").place(x = 100, y = 50)
            AFN_a = ttk.Combobox(ventana,state = "readonly",values = Elementos , width = 15)
            AFN_a.place(x = 250, y = 50)
            tk.Button(ventana, text="Crear", height = 1, width = 5, activebackground = "blue", activeforeground = "White", command = lambda: Fun.CreacionCerraduraOpcional(self.DiccionarioObjetos,AFN_a,ventana)).place( x = 410, y = 46)

            EtiquetaImagen = tk.Label(ventana,image = img)
            EtiquetaImagen.image = img
            EtiquetaImagen.place(x = 70 , y = 100)

        if tipo_ventana == "Mostrar":
            Elementos = list(self.DiccionarioObjetos.keys())
            AuxTexto = []

            for i in Elementos:
                cadenaAux = "AFN: " + i
                AuxTexto.append(cadenaAux)
                for key in range(len(list(self.DiccionarioObjetos[i].estados.keys()))):
                    AuxTexto.append("  Estado: "+str(key)+" -->  "+str(self.DiccionarioObjetos[i].estados.get(key).transiciones))
                
                AuxTexto.append("")

            tk.Label(ventana, text="Trasiciones de los AFN actuales: ").place(x = 20, y = 20)

            texto = tk.Listbox(ventana, height = 12 , width = 55 )
            texto.insert(tk.END,*AuxTexto)
            texto.place(x = 20, y = 40)

        if tipo_ventana == "Analizador":
            Elementos = list(self.DiccionarioObjetos.keys())
            self.AFD = self.DiccionarioObjetos[Elementos[0]].ir_a()

            print("AFD-------------------------")
            print(self.AFD.estados)
            print(self.AFD.finales)
            print(self.AFD.transiciones)
            print(self.ListaAFNs)
             
            messagebox.showinfo(message="La conversion AFN --> AFD fue Exitosa", title="Confirmacion", parent = ventana)

            tk.Label(ventana, text="Cadena: ").place(x = 20, y = 20)

            Cadena = tk.Entry(ventana,width = 40)
            Cadena.place(x = 80, y = 20 )

            tk.Button(ventana, text="Analizar", height = 1, width = 5, activebackground = "blue", activeforeground = "White",command = lambda: AlgoritmoLex(Cadena.get(),Resultados,self.AFD)).place( x = 415, y = 15)

            tk.Label(ventana, text="Tabla del AFD ").place(x = 80, y = 45)
            listaTablaReglas = tk.Listbox(ventana,height = 11 , width = 26)
            listaTablaReglas.place(x = 20, y = 60)

            Fun.ObtencionTablaAFD(self.AFD,listaTablaReglas,self.ListaAFNs)

            tk.Label(ventana, text="Resultado Analisis ").place(x = 300, y = 45)
            Resultados = tk.Listbox(ventana,height = 11 , width = 26)
            Resultados.place(x = 260, y = 60)

        tk.Button(ventana, text="Cerrar" , fg="red", command = ventana.destroy).place(x = 225, y = 250)

    def Mostrar(self):
        Elementos = list(self.DiccionarioObjetos.keys())

        for i in Elementos:
            Objeto = self.DiccionarioObjetos[i]
            Objeto.imprimir_transiciones()
