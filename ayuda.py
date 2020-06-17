import tkinter as tk
from ventanaCalculadora import Crear_VentanaCalculadora


ventanaSecundaria = tk.Tk()
Calculadora = Crear_VentanaCalculadora(master=ventanaSecundaria)
Calculadora.widges()
ventanaSecundaria.mainloop()