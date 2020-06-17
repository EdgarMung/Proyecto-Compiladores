from Clases import AFN
import tkinter as tk
from tkinter import messagebox

def ObtencionTablaAFD(AFD,Lista,ListaAFNs):
    Aux = []
    AFD.tokens = AFD.finales

    tokensModificados = OrdenamientoTokens(AFD.tokens)

    Elementos = list(AFD.transiciones.keys())

    Aux.append("Transiciones del AFD")
    for i in Elementos:
        auxTransicion = AFD.transiciones.get(i)
        Aux.append("    Estado " + str(i) + ": " +str(auxTransicion))
        
    Aux.append("")
    Aux.append("Tokens")

    num = 0
    for i in ListaAFNs:
        Aux.append("    "+str(i)+ " -> "+str(tokensModificados[num]))
        num += 1
        
    Lista.insert(tk.END,*Aux)

def CreacionAFNSimple(Diccionario,Lista,Entrada,root):
    print(Diccionario)
    caract = Entrada.get()
    if caract != "":
        if Diccionario.get(caract) == None:
            Diccionario[caract] = AFN(simbolo=caract)
        else:
            llave = caract + " "
            Diccionario[llave] = AFN(simbolo=caract)

        Lista.delete(0,tk.END)
        Elementos = list(Diccionario.keys())
        Lista.insert(tk.END,*Elementos)
        messagebox.showinfo(message="La Creacion del AFN '"+ caract +"' fue Exitosa", title="Confirmacion",parent = root)  
        
        Entrada.delete(0, tk.END)
    else:
        messagebox.showerror(message="No se ha detectado ningun caracter, por favor ingrese alguno.",title="Entrada Vacia",parent = root)
    print(Diccionario)

def CreacionUnion(Diccionario,Lista_a,Lista_b,root):
    print(Diccionario)

    Elemento_a = Lista_a.get()
    Elemento_b = Lista_b.get()
    if Elemento_a != "" and Elemento_b != "": 
        Objeto_A = Diccionario.get(Elemento_a)
        Objeto_B = Diccionario.get(Elemento_b)

        Objeto_A.union(Objeto_B)

        KeyAux = "("+Elemento_a + "|" +Elemento_b+")" 
        ObjetoAux = Objeto_A

        Diccionario.pop(Elemento_a)
        Diccionario.pop(Elemento_b)
        Diccionario[KeyAux] = ObjetoAux
        messagebox.showinfo(message="La Union entre '"+ Elemento_a +" y "+ Elemento_b+"' fue Exitosa", title="Confirmacion",parent = root)
    else:
        messagebox.showerror(message="No se ha seleccionado uno de los dos AFN, por favor revise.",title="Lista Vacia",parent = root)
    
    Lista_a.set("")
    Lista_b.set("")
    Elementos = list(Diccionario.keys())
    Lista_a ["values"] = Elementos
    Lista_b ["values"] = Elementos
    print(Diccionario)

def CreacionConcatenacion(Diccionario,Lista_a,Lista_b,root):
    print(Diccionario)
    Elemento_a = Lista_a.get()
    Elemento_b = Lista_b.get()

    if Elemento_a != "" and Elemento_b != "": 
        if Elemento_a != Elemento_b:
            Objeto_A = Diccionario.get(Elemento_a)
            Objeto_B = Diccionario.get(Elemento_b)

            Objeto_A.concatenacion(Objeto_B)

            KeyAux = "("+Elemento_a + "°" +Elemento_b+")" 
            ObjetoAux = Objeto_A

            Diccionario.pop(Elemento_a)
            Diccionario.pop(Elemento_b)
            Diccionario[KeyAux] = ObjetoAux
            messagebox.showinfo(message="La Concatenacion entre '"+ Elemento_a +" y "+ Elemento_b+"' fue Exitosa", title="Confirmacion",parent = root)
        else:
            messagebox.showerror(message="Se ha seleccionado el mismo AFN para la concatenación, por favor revise.",title="Mismo AFN",parent = root)
    else:
        messagebox.showerror(message="No se ha seleccionado uno de los dos AFN, por favor revise.",title="Lista Vacia",parent = root)
    
    Lista_a.set("")
    Lista_b.set("")
    Elementos = list(Diccionario.keys())
    Lista_a ["values"] = Elementos
    Lista_b ["values"] = Elementos
    print(Diccionario)

def CreacionCerraduraPositiva(Diccionario,Lista,root):
    print(Diccionario)
    AFN = Lista.get()
    if AFN != "":
        Objeto = Diccionario.get(AFN)

        Objeto.cerradura_positiva()

        KeyAux = "("+AFN + ")+"
        ObjetoAux = Objeto

        Diccionario.pop(AFN)
        Diccionario[KeyAux] = ObjetoAux
        messagebox.showinfo(message="La Cerradura Positiva a '"+ AFN +"' fue Exitosa", title="Confirmacion",parent=root)
    else:
        messagebox.showerror(message="No se ha seleccionado algun AFN, por favor revise.",title="Lista Vacia",parent = root)
    Lista.set("")
    Elementos = list(Diccionario.keys())
    Lista["values"] = Elementos
    print(Diccionario)

def CreacionCerraduraKleene(Diccionario,Lista,root):
    print(Diccionario)
    AFN = Lista.get()
    if AFN != "":
        Objeto = Diccionario.get(AFN)

        Objeto.cerradura_kleene()

        KeyAux = "("+AFN + ")*"
        ObjetoAux = Objeto

        Diccionario.pop(AFN)
        Diccionario[KeyAux] = ObjetoAux
        messagebox.showinfo(message="La Cerradura de Kleene a '"+ AFN +"' fue Exitosa", title="Confirmacion",parent= root)
    else:
        messagebox.showerror(message="No se ha seleccionado algun AFN, por favor revise.",title="Lista Vacia",parent = root)
    Lista.set("")
    Elementos = list(Diccionario.keys())
    Lista["values"] = Elementos
    print(Diccionario)
    
def CreacionCerraduraOpcional(Diccionario,Lista,root):
    print(Diccionario)
    AFN = Lista.get()
    if AFN != "":
        Objeto = Diccionario.get(AFN)

        Objeto.interrogacion()

        KeyAux = "("+AFN + ")?"
        ObjetoAux = Objeto

        Diccionario.pop(AFN)
        Diccionario[KeyAux] = ObjetoAux
        messagebox.showinfo(message="La Cerradura Opcional a '"+ AFN +"' fue Exitosa", title="Confirmacion",parent = root)
    else:
        messagebox.showerror(message="No se ha seleccionado algun AFN, por favor revise.",title="Lista Vacia",parent = root)
    Lista.set("")
    Elementos = list(Diccionario.keys())
    Lista["values"] = Elementos
    print(Diccionario)

def CrearUnionEspecial(Diccionario,ListaAFNs):
    listaObjetos = []
    Elementos = list(Diccionario.keys())
    
    for x in Elementos:
        ListaAFNs.append(x)

    ObjetoUnico = Diccionario.get(Elementos[0])
    llave = Elementos.pop(0)

    for i in Elementos:
        listaObjetos.append(Diccionario.get(i))
        Diccionario.pop(i)

    ObjetoUnico.union_especial(listaObjetos)
    NuevaLlave = "Union_Especial"

    Diccionario.pop(llave)

    Diccionario[NuevaLlave] = ObjetoUnico

    messagebox.showinfo(message="La Union especial entre los AFN fue Exitosa", title="Confirmacion")

def OrdenamientoTokens(tokens):
    listaAux = []
    lista = sorted(tokens)
    aux = 0

    for i in lista:
        if i != aux:
            listaAux.append(i)
            aux = i
    
    print(listaAux)
    return listaAux

