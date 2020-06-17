import tkinter as tk
from ventanaGeneradorAFN import Crear_Ventana
from ventanaCalculadora import Crear_VentanaCalculadora

#Funcion Crear VEntana Calculadora
def abrirCalculadora():
    ventanaSecundaria = tk.Toplevel(ventana)
    Calculadora = Crear_VentanaCalculadora(master=ventanaSecundaria)
    Calculadora.widges()

#Funcion Crear Ventana Generador AFN  
def abrirMenuGeneradorAFN():
    ventanaSecundaria = tk.Toplevel(ventana)
    Menu = Crear_Ventana(master=ventanaSecundaria)
    Menu.create_widgets()

#Diseño de la pagina principal de todo el sistema ----------------------------------------------------------------
ventana = tk.Tk()
ventana.geometry("550x400")
ventana.title("Ventana Principal")
ventana.config(bg = "blue")

parteTitulo = tk.Frame(ventana,bd = 10,bg = "blue")
parteTitulo.pack()
tk.Label(parteTitulo,text="Menu Principal",padx = 15, pady = 20, font=("Cantarell Extra Bold",20),bg = "floral white",fg = "black").pack()
parteBotones = tk.Frame(ventana,bg = "blue")
parteBotones.pack()
tk.Button(parteBotones,text="Generador AFNś",font =("TSCu_Paranar",15),fg = "black",bg = "white",height = 2,width = 15 ,relief = "solid",activebackground = "cornflower blue",activeforeground = "white" ,bd = 3, command = abrirMenuGeneradorAFN).grid(column = 0, row = 0,pady = 10,padx = 5)
tk.Button(parteBotones,text="Calculadora",font =("TSCu_Paranar",15),fg = "black" ,bg = "white",height = 2,width = 15 ,relief = "solid",activebackground = "cornflower blue",activeforeground = "white" ,bd = 3, command = abrirCalculadora).grid(column = 1, row = 0,pady = 10,padx = 5)


ventana.mainloop()