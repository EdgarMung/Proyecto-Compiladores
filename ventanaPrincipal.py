import tkinter as tk
import ventanaGeneradorAFN, ventanaAFN_Expresion,ventanaCalculadora, VentanaVerificadorGramaticas

#Funcion Crear Ventana Verificador
def abrirVerificador():
    ventanaSecundaria = tk.Toplevel(ventana)
    verificador = VentanaVerificadorGramaticas.ventanaVerificadorGramaticas(master=ventanaSecundaria)
    verificador.widges()

#Funcion Crear Ventana Calculadora
def abrirCalculadora():
    ventanaSecundaria = tk.Toplevel(ventana)
    Calculadora = ventanaCalculadora.ventanaCalculadora(master=ventanaSecundaria)
    Calculadora.widges()

#Funcion Crear Ventana AFN_Expresion
def abrirGenerador_Expresion():
    ventanaSecundaria = tk.Toplevel(ventana)
    Generador = ventanaAFN_Expresion.ventanaAFN_Expresion(master=ventanaSecundaria)
    Generador.widges()

#Funcion Crear Ventana Generador AFN  
def abrirMenuGeneradorAFN():
    ventanaSecundaria = tk.Toplevel(ventana)
    Menu = ventanaGeneradorAFN.ventanaGeneradorAFN(master=ventanaSecundaria)
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
tk.Button(parteBotones,text="Generador AFN",font =("TSCu_Paranar",15),fg = "black",bg = "white",height = 2,width = 15 ,relief = "solid",activebackground = "cornflower blue",activeforeground = "white" ,bd = 3, command = abrirMenuGeneradorAFN).grid(column = 0, row = 0,pady = 10,padx = 5)
tk.Button(parteBotones,text="Generador AFN_Expresion",font =("TSCu_Paranar",15),fg = "black",bg = "white",height = 2,width = 25 ,relief = "solid",activebackground = "cornflower blue",activeforeground = "white" ,bd = 3, command = abrirGenerador_Expresion).grid(column = 1, row = 0,pady = 10,padx = 5)
tk.Button(parteBotones,text="Calculadora",font =("TSCu_Paranar",15),fg = "black" ,bg = "white",height = 2,width = 15 ,relief = "solid",activebackground = "cornflower blue",activeforeground = "white" ,bd = 3, command = abrirCalculadora).grid(column = 0, row = 1,pady = 10,padx = 5)
tk.Button(parteBotones,text="Analizadores Sintacticos",font =("TSCu_Paranar",15),fg = "black" ,bg = "white",height = 2,width = 25 ,relief = "solid",activebackground = "cornflower blue",activeforeground = "white" ,bd = 3, command = abrirVerificador).grid(column = 1, row = 1,pady = 10,padx = 5)

ventana.mainloop()