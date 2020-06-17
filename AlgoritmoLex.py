import tkinter as tk

def AlgoritmoLex(cadena,Lista,AFD):
    estados = AFD.estados
    tokens = AFD.tokens
    Salida = []
    transiciones = AFD.transiciones
    Lista.delete(0,tk.END)
    TamañoCadena = len(cadena)
    estado_Actual = 0
    antes_vista = 0
    posicionCadena = 0
    posicionUltimoAceptado = 0

    if TamañoCadena == 0:
        token = ChecarToken(estado_Actual,estados,tokens)
        if token > -1:
            Salida.append(" "+" -> "+str(token))
    else:
        cadenaAux = ""
        while posicionCadena < len(cadena):
            caracter = cadena[posicionCadena]
            #if PertenceAlfabeto(caracter,alfabeto):
            if BuscarTransicion(caracter,transiciones,estado_Actual) > -1:
                estado_Actual = BuscarTransicion(caracter,transiciones,estado_Actual)
                posicionCadena += 1
                cadenaAux+= caracter
                
                token = ChecarToken(estado_Actual,estados,tokens)
                if token > 0:
                    antes_vista = 1
                    posicionUltimoAceptado = posicionCadena
            else:
                if (antes_vista == 0):
                    estado_Actual = 0
                    cadenaAux = ""
                else:
                    Salida.append(cadenaAux+" -> "+str(token))
                    antes_vista = 0
                    posicionCadena = posicionUltimoAceptado

            #else:
            #    cadenaAux = ""
            #    estado_Actual = 0
        if (antes_vista != 0):
            Salida.append(cadenaAux+" -> "+str(token))
            

            
    Lista.insert(tk.END,*Salida)

def ChecarToken(estado,estados,tokens):
    indice = estados.index(estado)

    return tokens[indice] 

def BuscarTransicion(caracter,transiciones,estado_Actual):
    transicionesDelEstado = transiciones.get(estado_Actual)

    if transicionesDelEstado != None:
        for i in transicionesDelEstado:
            if caracter == i[0]:
                return i[1]
    
    return -1
