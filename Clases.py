from Estado import Estado
import math
import csv

class AFD:
	def __init__(self,estados,transiciones,finales,alfabeto):
		self.estados=estados
		self.transiciones=transiciones
		self.finales=finales
		self.tokens = []
		self.alfabeto = alfabeto

#----------------------------------------------------------------------------------------------------

class AFN:
	#Constructor de la clase.
	def __init__(self, simbolo = None):
		if simbolo == None:
			self.estado_inicial = 0
			self.estados_aceptacion = []
			self.alfabeto = []
			self.estados = {}
		else:
			self.estado_inicial = 0
			self.estados_aceptacion = [1]
			self.alfabeto = [simbolo]
			self.estados = {}
			self.agregar_estado(0)
			self.agregar_estado(1)
			self.anadir_transicion(0,simbolo,1)
	#Agregar un simbolo al lenguaje.
	def agregar_simbolo(self,simbolo):
		if simbolo in self.alfabeto:
			print("El simbolo |"+simbolo+"| ya se encuentra en el alfabeto.")
		else:
			#print("Insertando simbolo en el alfabeto.")
			self.alfabeto.append(simbolo)
			#print(self.alfabeto)
	#Agregar un estado al lenguaje.
	def agregar_estado(self,id):
		if self.estados.get(id) == None:
			#print("Ingresando un nuevo estado: "+str(id))
			self.estados.setdefault(id,Estado(id))
		else:
			print("El estado ya se encuentra en el conjunto")
	#Agregar una transicion a un estado existente:
	def anadir_transicion(self,id,simbolo,id_final):
		if self.estados.get(id) == None:
			print("El estado no existe")
		else:
			self.estados.get(id).anadir_transicion(simbolo,id_final)
	#Agregar un estado dd aceptacion a la lista:
	def anadir_estado_aceptacion(self,simbolo):
		self.estados_aceptacion.append(simbolo)
	#Hacer una union entre dos AFNs.
	def union(self,AFN2):
		for elemento in AFN2.alfabeto:
			if elemento not in self.alfabeto:
				self.alfabeto.append(elemento)
		self.estado_inicial = -1
		self.agregar_estado(-1)
		self.anadir_transicion(-1,'ε',0)
		numero_nodos_AFN1=len(list(self.estados))
		#Agregando la otra ruta de la union.
		self.anadir_transicion(self.estado_inicial,'ε',self.estado_inicial+numero_nodos_AFN1)
		#print("Generando una transicion del "+str(self.estado_inicial)+" e "+str(self.estado_inicial+numero_nodos_AFN1))
		#Actualizar los numeros de los nodos.
		self.estados=self.recorrer_estados(self.estados,1)
		for key in list(self.estados.keys()):
			#print("AFN1 "+str(key))
			self.estados.get(key).actualizar_transiciones(1)
			#print(self.estados.get(key).transiciones)
		#Actualizar los numeros de los nodos del segundo AFN.
		AFN2.estados=self.recorrer_estados(AFN2.estados,numero_nodos_AFN1)
		for key in list(AFN2.estados.keys()):
			#print("AFN2 "+str(key))
			AFN2.estados.get(key).actualizar_transiciones(numero_nodos_AFN1)
			#print(AFN2.estados.get(key).transiciones)
		numero_nodos_total=len(list(self.estados))+len(list(AFN2.estados))
		self.anadir_transicion(numero_nodos_AFN1-1,'ε',numero_nodos_total)
		self.estados_aceptacion=[numero_nodos_total]
		self.agregar_estado(numero_nodos_total)
		AFN2.anadir_transicion(numero_nodos_total-1,'ε',numero_nodos_total)
		self.estado_inicial=0
		self.estados.update(AFN2.estados)
	#Hacer una concatenacion de AFNs.
	def concatenacion(self,AFN2):
		for elemento in AFN2.alfabeto:
			if elemento not in self.alfabeto:
				self.alfabeto.append(elemento)
		numero_nodos_AFN1=len(list(self.estados))-1
		#Actualizar los numeros de los nodos del segundo AFN.
		AFN2.estados=self.recorrer_estados(AFN2.estados,numero_nodos_AFN1)
		for key in list(AFN2.estados.keys()):
			#print("AFN2 "+str(key))
			AFN2.estados.get(key).actualizar_transiciones(numero_nodos_AFN1)
			#print(AFN2.estados.get(key).transiciones)
		self.estados.update(AFN2.estados)
		#self.imprimir_transiciones()
		numero_nodos_total=len(list(self.estados))-1
		self.estados_aceptacion=[numero_nodos_total]
	#Actualizar los id de los estados al agregar nodos antes.
	def cerradura_positiva(self):
		self.estado_inicial = -1
		self.agregar_estado(-1)
		self.anadir_transicion(-1,'ε',0)
		#Recorrer los estados.
		self.estados=self.recorrer_estados(self.estados,1)
		for key in list(self.estados.keys()):
			self.estados.get(key).actualizar_transiciones(1)
		#Agregar el ultimo nodo y las transiciones para la cerradura positiva.
		numero_nodos_total=len(list(self.estados))
		self.anadir_transicion(numero_nodos_total-1,'ε',numero_nodos_total)
		self.estados_aceptacion=[numero_nodos_total]
		self.agregar_estado(numero_nodos_total)
		self.anadir_transicion(numero_nodos_total-1,'ε',1)
	#La cerradura de kleene se forma de una positiva mas una transicion epsilon.
	def cerradura_kleene(self):
		self.cerradura_positiva()
		self.anadir_transicion(0,'ε',len(list(self.estados))-1)
	#No se como se llama esta operacion.
	def interrogacion(self):
		self.estado_inicial = -1
		self.agregar_estado(-1)
		self.anadir_transicion(-1,'ε',0)
		#Recorrer los estados.
		self.estados=self.recorrer_estados(self.estados,1)
		for key in list(self.estados.keys()):
			self.estados.get(key).actualizar_transiciones(1)
		#Agregar el ultimo nodo y las transiciones para la cerradura positiva.
		numero_nodos_total=len(list(self.estados))
		self.anadir_transicion(numero_nodos_total-1,'ε',numero_nodos_total)
		self.estados_aceptacion=[numero_nodos_total]
		self.agregar_estado(numero_nodos_total)
		self.anadir_transicion(0,'ε',numero_nodos_total)
	#La funcion que reemplaza los numeros de estados viejos por los nuevos.
	def recorrer_estados(self,estados,no_posiciones):
		nuevos_estados={}
		for key in list(estados.keys()):
			nuevos_estados.setdefault(key+no_posiciones,estados.get(key))
		return nuevos_estados
	#Funcion para imprimimir los conjuntos de transiciones.
	def imprimir_transiciones(self):
		for key in range(len(list(self.estados.keys()))):
			print("FINAL "+str(key))
			print(self.estados.get(key).transiciones)
	#Funcion ir_a
	def ir_a(self):
		conjunto_conjuntos=[]
		cerraduras_revisadas=[]
		conjuntos_por_revisar=[]
		conjuntos_por_revisar.append([0])
		conjuntos_transiciones=[]
		while len(conjuntos_por_revisar)>0:
			s=[]
			#print("Conjuntos por revisar: ",end="")
			#print(conjuntos_por_revisar)
			#print("Cerraduras revisadas:",end="")
			#print(cerraduras_revisadas)
			e=conjuntos_por_revisar.pop()
			#print("e:")
			#print(e)
			#print("Cerradura epsilon")
			for var in e:
				s=list(set(s)|set(self.cerradura_e(var)))
			if s not in conjunto_conjuntos:
				conjunto_conjuntos.append(s)
				cerraduras_revisadas.append(e)
			#print("s:")
			#print(s)
			for simbolo in self.alfabeto:
				m=self.mover(s,simbolo)
				if m in cerraduras_revisadas or len(m) == 0:
					pass
				else:
					conjuntos_por_revisar.append(m)
					#print("\tm:")
					#print("\t"+str(m))
				if [e,simbolo,m] not in conjuntos_transiciones:
					conjuntos_transiciones.append([e,simbolo,m])
		lista_finales=[]

		#Asignar los tokens a los nuevos estados del AFN:
		for lista in conjunto_conjuntos:
			lista_finales.append(0)
			token=10
			for final in self.estados_aceptacion:
				if final in lista:
					lista_finales.pop()
					lista_finales.append(token)
				token+=10
		#print(lista_finales)
		return(self.crear_AFD(cerraduras_revisadas,conjuntos_transiciones,lista_finales,self.alfabeto))
	#Crear un nuevo AFD
	def crear_AFD(self,cerraduras,transiciones,finales,alfabeto):
		#print("CREANDO AFD")
	########################################################
		#Cambiando los indices de los conjuntos:
		lista_temp=[]
		indice_temp=0
		a=0
		b=0
		for x in range(len(finales)):
			for posicion in range(len(finales)-1):
				if cerraduras[posicion]>cerraduras[posicion+1]:
					a=cerraduras[posicion+1]
					cerraduras[posicion+1]=cerraduras[posicion]
					cerraduras[posicion]=a

					b=finales[posicion+1]
					finales[posicion+1]=finales[posicion]
					finales[posicion]=b
		for lista in cerraduras:
			lista_temp.append(indice_temp)
			for transicion in transiciones:
				if lista in transicion:
					if lista == transicion[0]:
						transicion.pop(0)
						transicion.insert(0,indice_temp)
					if lista == transicion[2]:
						transicion.pop(2)
						transicion.insert(2,indice_temp)
			indice_temp-=1
		for lista in transiciones:
			lista[0]*=-1
			lista[2]*=-1
		dic_AFD={}
		for lista in transiciones:
			if not isinstance(lista[2],list):
				if dic_AFD.get(lista[0]) == None:
					dic_AFD.setdefault(lista[0],[[lista[1],lista[2]]])
				else:
					conjunto_ids = dic_AFD.get(lista[0])
					conjunto_ids.append([lista[1],lista[2]])
		cerraduras=[]
		for elemento in lista_temp:
			cerraduras.append(elemento*-1)
		nuevo_AFD=AFD(cerraduras,dic_AFD,finales,self.alfabeto)


		return nuevo_AFD
	#Funcion mover
	def mover(self,conjunto_epsilon,simbolo):
		lista_resultado=[]
		for var in conjunto_epsilon:
			if(self.estados.get(var).transiciones.get(simbolo)!=None):
				for elemento in self.estados.get(var).transiciones.get(simbolo):
					lista_resultado.append(elemento)
		return lista_resultado
	#Funcion cerradura epsilon
	def cerradura_e(self,var):
		lista_temp=[]
		lista_temp.append(var)
		nueva_lista=[]
		nueva_lista2=[]
		while len(lista_temp) != 0:
			var=lista_temp.pop()
			if var not in nueva_lista:
				nueva_lista.append(var)
				if(self.estados.get(var).transiciones.get('ε')!=None):
					nueva_lista2=self.estados.get(var).transiciones.get('ε')
					for elemento in nueva_lista2:
						lista_temp.append(elemento)

		return nueva_lista
	#Recorrer los numeros de los estados finales.
	def recorrer_finales(self,posiciones):
		for posicion in range(len(self.estados_aceptacion)):
			#print("Cambiando el estado final de "+str(elemento)+" a "+str(elemento+posiciones))
			self.estados_aceptacion[posicion]+=posiciones
	#Unir varios AFN a un solo inicio:
	def union_especial(self,lista_AFN):
		for AFNx in lista_AFN:
			for simbolo in AFNx.alfabeto:
				if simbolo not in self.alfabeto:
					self.alfabeto.append(simbolo)
		posicion=0
		self.agregar_estado(-1)
		self.anadir_transicion(-1,'ε',0)
		self.estados=self.recorrer_estados(self.estados,1)
		self.recorrer_finales(1)
		for key in list(self.estados.keys()):
			self.estados.get(key).actualizar_transiciones(1)
		posicion+=len(list(self.estados))
		#print("Recorriendo "+str(posicion))
		for AFN in lista_AFN:
			self.anadir_transicion(0,'ε',posicion)
			AFN.estados=AFN.recorrer_estados(AFN.estados,posicion)
			AFN.recorrer_finales(posicion)
			for key in list(AFN.estados.keys()):
				AFN.estados.get(key).actualizar_transiciones(posicion)
			posicion+=len(list(AFN.estados))

		for AFN in lista_AFN:
			for estado in AFN.estados_aceptacion:
				self.estados_aceptacion.append(estado)
			self.estados.update(AFN.estados)

#-----------------------------------------------------------------------------------------------------

class Lexico:
	def __init__(self,cadena,AFD):
		self.cadena=cadena
		self.AFD=AFD

	def getToken(self):
		estados = self.AFD.estados
		tokens = self.AFD.finales
		transiciones = self.AFD.transiciones
		TamañoCadena = len(self.cadena)
		estado_Actual = 0
		antes_vista = 0

		if TamañoCadena == 0:
				return ("$",0)

		cadenaAux = ""

		while len(self.cadena) != 0:
			caracter = self.cadena[0:1]
			self.cadena=self.cadena[1:]

			if self.buscarTransicion(caracter,transiciones,estado_Actual) > -1:
				estado_Actual = self.buscarTransicion(caracter,transiciones,estado_Actual)
				cadenaAux+= caracter
				token = self.checarToken(estado_Actual,estados,tokens)
				if token > 0:
					antes_vista = 1
			else:
				if (antes_vista == 0):
					self.cadena=caracter+self.cadena
					return ("ERROR",-1)
				else:
					self.cadena=caracter+self.cadena
					return (cadenaAux,token)

		if (antes_vista == 0):
			self.cadena=caracter+self.cadena
			return ("ERROR",-1)
		if (antes_vista != 0):
			return (cadenaAux,token)


	def checarToken(self,estado,estados,tokens):
		indice = estados.index(estado)
		return tokens[indice]

	def buscarTransicion(self,caracter,transiciones,estado_Actual):
		transicionesDelEstado = transiciones.get(estado_Actual)

		if transicionesDelEstado != None:
			for i in transicionesDelEstado:
				if caracter == i[0]:
					return i[1]
		return -1
	def rewind(self,cadena):
		self.cadena=cadena+self.cadena

	def GetEstadoLexic(self,temp):
		temp[0] = self.cadena

	def SetEstadoLexic(self,temp):
		self.cadena = temp[0]

# -----------------------------------------------------------------------------------------------------
class Calculadora:
	def __init__(self,AFDD):
		#self.Lex=Lexico(cadena,AFD)
		self.AFDD = AFDD
		self.Lex = None
		self.MAS=10
		self.MENOS=20
		self.MULT=30
		self.DIV=40
		self.POT=50
		self.PAR_I=60
		self.PAR_D=70
		self.SIN=80
		self.COS=90
		self.TAN=100
		self.NUM=110
		self.contador=0
		self.v2=[]
	#----------------------------------------------------
	def ConsultaResultado(self):
		resultado = str(self.v2[0])
		self.v2 = []
		self.contador = 0
		return resultado


	#----------------------------------------------------
	def InicioOperaciones(self,cadena):
		self.Lex = Lexico(cadena,self.AFDD)
		self.E()


	# ---------------------------------------------------
	def E(self):
		print('E:',end='')
		print(self.Lex.cadena,end=" ")
		print(self.v2,end=" ")
		print(self.contador)
		if self.T():
			if self.Ep():
			 return True
		return False
	#----------------------------------------------------
	def Ep(self):
		print('Ep:',end='')
		print(self.Lex.cadena,end=" ")
		print(self.v2,end=" ")
		print(self.contador)
		tupla=self.Lex.getToken()
		token=tupla[1]
		print(tupla[0],token)
		if token==self.MAS:
			if self.T():
				self.v2[self.contador-2]+=self.v2[self.contador-1]
				self.v2.pop()
				self.contador-=1
				if self.Ep():
					return True
			return False
		elif token==self.MENOS:
			if self.T():
				self.v2[self.contador-2]-=self.v2[self.contador-1]
				self.v2.pop()
				self.contador-=1
				if self.Ep():
					return True
			return False
		if tupla[0] != "$":
			print("Se regreso ",tupla[0])
			self.Lex.rewind(tupla[0])
		return True
	#----------------------------------------------------
	def T(self):
		print('T:',end='')
		print(self.Lex.cadena,end=" ")
		print(self.v2,end=" ")
		print(self.contador)
		if self.P():
			if self.Tp():
			 return True
		return False
	#----------------------------------------------------
	def Tp(self):
		print('Tp:',end='')
		print(self.Lex.cadena,end=" ")
		print(self.v2,end=" ")
		print(self.contador)
		tupla=self.Lex.getToken()
		token=tupla[1]
		print(tupla[0],token)
		if token==self.MULT:
			if self.P():
				self.contador-=1
				self.v2[self.contador-1]*=self.v2[self.contador]
				self.v2.pop()
				if self.Tp():
					return True
			return False
		if token==self.DIV:
			if self.P():
				self.contador-=1
				self.v2[self.contador-1]/=self.v2[self.contador]
				self.v2.pop()
				if self.Tp():
					return True
			return False
		if tupla[0] != "$":
			print("Se regreso ",tupla[0])
			self.Lex.rewind(tupla[0])
		return True
	#----------------------------------------------------
	def P(self):
		print('P:',end='')
		print(self.Lex.cadena,end=" ")
		print(self.v2,end=" ")
		print(self.contador)
		if self.F():
			if self.Pp():
			 return True
		return False
	#----------------------------------------------------
	def Pp(self):
		print('Pp:',end='')
		print(self.Lex.cadena,end=" ")
		print(self.v2,end=" ")
		print(self.contador)
		tupla=self.Lex.getToken()
		token=tupla[1]
		print(tupla[0],token)
		if token==self.POT:
			if self.F():
				if self.Pp():
					return True
			return False
		if tupla[0] != "$":
			print("Se regreso ",tupla[0])
			self.Lex.rewind(tupla[0])
		return True
	#----------------------------------------------------
	def F(self):
		print('F:',end='')
		print(self.Lex.cadena,end=" ")
		print(self.v2,end=" ")
		print(self.contador)
		tupla=self.Lex.getToken()
		token=tupla[1]
		print(tupla[0],token)
		if token==self.PAR_I:
			if self.E():
				tupla=self.Lex.getToken()
				token=tupla[1]
				if token==self.PAR_D:
					return True
				return False
		if token==self.SIN:
			tupla=self.Lex.getToken()
			token=tupla[1]
			if token==self.PAR_I:
				if self.E():
					self.v2[self.contador-1]=math.sin(self.v2[self.contador-1])
					tupla=self.Lex.getToken()
					token=tupla[1]
					if token==self.PAR_D:
						return True
					return False
		if token==self.COS:
			tupla=self.Lex.getToken()
			token=tupla[1]
			if token==self.PAR_I:
				if self.E():
					self.v2[self.contador-1]=math.cos(self.v2[self.contador-1])
					tupla=self.Lex.getToken()
					token=tupla[1]
					if token==self.PAR_D:
						return True
					return False
		if token==self.TAN:
			tupla=self.Lex.getToken()
			token=tupla[1]
			if token==self.PAR_I:
				if self.E():
					self.v2[self.contador-1]=math.tan(self.v2[self.contador-1])
					tupla=self.Lex.getToken()
					token=tupla[1]
					if token==self.PAR_D:
						return True
					return False
		if token==self.NUM:
			self.v2.append(0)
			self.v2[self.contador]=int(tupla[0])
			self.contador+=1
			return True
		return False

#----------------------------------------------------

class Verificador:
    def __init__(self,AFDd):
        #self.Lex = Lexico(cadena,AFD)
        self.AFDD = AFDd
        self.NoTerminal = 10
        self.Terminal = 20
        self.FLECHA = 30
        self.PC = 40
        self.OR = 50
        self.NoTerminales = None
        self.Terminales = None

    def ObtenerNoterminalesTerminales(self,NoTerm,Term):
        NoTerm.append(self.NoTerminales)
        Term.append( self.Terminales)

    def Verificar(self,cadena):
        self.Lex = Lexico(cadena,self.AFDD)
        self.NoTerminales = []
        self.Terminales = []
        return self.G()
        
    def G(self):
        print("G:", end = " ")
        print(self.Lex.cadena)
        if(self.ListaReglas()):
            tupla = self.Lex.getToken()
            token = tupla[1]
            print(tupla)
            if(token == 0):
                return True
        return False

    def ListaReglas(self):
        print("ListaReglas:", end = " ")
        print(self.Lex.cadena)
        temp = [0]
        if(self.Regla()):
            self.Lex.GetEstadoLexic(temp)
            if (self.ListaReglas()):
                return True
            self.Lex.SetEstadoLexic(temp)
            return True
        return False

    def Regla(self):
        print("Regla:", end = " ")
        print(self.Lex.cadena)
        if(self.LadoIzq()):
            tupla=self.Lex.getToken()
            token = tupla[1]
            print(tupla)
            if(token == self.FLECHA):
                if(self.ListaLadosDer()):
                    tupla=self.Lex.getToken()
                    token = tupla[1]
                    print(tupla)
                    if(token == self.PC):
                        return True
        return False

    def LadoIzq(self):
        print("LadoIzq:", end = " ")
        print(self.Lex.cadena)
        tupla=self.Lex.getToken()
        token = tupla[1]
        print(tupla)
        if(token == self.NoTerminal):
            self.NoTerminales.append(tupla[0])
            return True
        return False

    def ListaLadosDer(self):
        print("ListaLadosDer:", end = " ")
        print(self.Lex.cadena)
        if(self.LadoDer()):
            tupla=self.Lex.getToken()
            token = tupla[1]
            print(tupla)
            if(token == self.OR):
                if(self.ListaLadosDer()):
                    return True
                return False
            self.Lex.rewind(tupla[0])
            return True
        return False

    def LadoDer(self):
        print("LadoDer:", end = " ")
        print(self.Lex.cadena)
        return self.ListaSimb()

    def ListaSimb(self):
        print("ListaSimb:", end = " ")
        print(self.Lex.cadena)
        temp = [0]
        tupla=self.Lex.getToken()
        token = tupla[1]
        print(tupla)
        if(token == self.NoTerminal or token== self.Terminal):
            if(token == self.Terminal):
                if(not(tupla[0] in self.Terminales)):
                    self.Terminales.append(tupla[0])
            self.Lex.GetEstadoLexic(temp)
            if(self.ListaSimb()):
                return True
            self.Lex.SetEstadoLexic(temp)
            return True
        return False

#----------------------------------------------

class Generador:
	def __init__(self, AFDD):
		self.AFD = AFDD
		self.CONC=10
		self.UNI=20
		self.C_P=30
		self.C_E=40
		self.S_I=50
		self.P_I=60
		self.P_D=70
		self.SIMB=80

	def Generar(self,cadena):
		self.Lex=Lexico(cadena,self.AFD)
		contenedor = []
		self.E(contenedor)
		return contenedor[0]
		
	def E (self,a):
		print('funcion E')
		if (self.T(a)):
			if(self.Ep(a)):
				return True
		return False

	def Ep (self,a):
		print('funcion Ep')
		tupla=self.Lex.getToken()
		print(tupla)
		token=tupla[1]
		if token==self.UNI:
			b=[]
			if (self.T(b)):
				print(a[0].alfabeto,'se une con:',b[0].alfabeto)#accion union f con f2
				a[0].union(b[0])
				if(self.Ep(a)):
					return True
			return False
		if tupla[0] != "$":
			print("Se regreso ",tupla[0])
			self.Lex.rewind(tupla[0])
		return True

	def T (self,a):
		print('funcion T')
		if (self.C(a)):
			if (self.Tp(a)):
				return True
		return False

	def Tp (self,a):
		print('funcion Tp')
		tupla=self.Lex.getToken()
		print(tupla)
		token=tupla[1]
		if token == self.CONC:
			b=[]
			if (self.C(b)):
				a[0].concatenacion(b[0])
				print ("se concatena con")#accion concatenar f con f2
				if (self.Tp(a)):
					return True
			return False
		if tupla[0] != "$":
			print("Se regreso ",tupla[0])
			self.Lex.rewind(tupla[0])
		return True

	def C (self,a):
		print('funcion C')
		if(self.F(a)):
			if(self.Cp(a)):
				return True
		return False

	def Cp (self,a):
		print('funcion Cp')
		tupla=self.Lex.getToken()
		print(tupla)
		token=tupla[1]
		if token==self.C_P:
			#f.cerr_pos()
			a[0].cerradura_positiva()
			print('cerradura posistiva')
			if (self.Cp(a)):
				return True
			return False
		elif token==self.C_E:
			#f.cerr_k()
			a[0].cerradura_kleene()
			print('cerradura estrella')
			if (self.Cp(a)):
				return True
			return False
		elif token==self.S_I:
			#f.opc()
			print('opcional')
			a[0].interrogacion()
			if (self.Cp(a)):
				return True
			return False
		if tupla[0] != "$":
			print("Se regreso ",tupla[0])
			self.Lex.rewind(tupla[0])
		return True

	def F (self,a):
		print('funcion F')
		tupla=self.Lex.getToken()
		print(tupla)
		token=tupla[1]
		if token==self.P_I:
			if (self.E(a)):
				tupla=self.Lex.getToken()
				print(tupla)
				token=tupla[1]
				if (token==self.P_D):
					return True
			return False
		elif token == self.SIMB:
			a.append(AFN(simbolo=tupla[0]))
			return True
		return False

#----------------------------------------------------------------------------------------------------------

class AlgoritmoLL():
    def __init__(self,ConjuntoReglas,NoTerminales,Terminales):
        self.ConjuntoReglas = ConjuntoReglas
        self.NoTerminales = NoTerminales
        self.Terminales = Terminales
        self.DiccionarioConjuntoReglas = {}
        self.DiccionarioFisrt = {}
        self.DiccionarioFollow = {}
        self.Columnas = []
        self.Filas = []
        self.tabla = []
        self.Mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.Inicializacion()

    def QuitarRecursividad(self,Regla):
        A = Regla[0]
        Beta = Regla[1][-1]
        New = A+'p'
        Regla1 = [A,[Beta+New]]
        ArregloAux = []
        for Elemento in Regla[1]:
            if(A in Elemento):
                ArregloAux.append(Elemento.replace(A,'')+New)
        ArregloAux.append('epsilon')
        Regla2=[New,ArregloAux]

        return Regla1,Regla2

    def ObtencionDiccionario(self):
        Bandera = False
        for Elemento in self.ConjuntoReglas:
            Regla = Elemento.split("->")
            Regla[1]=Regla[1].split('|')
            if(Elemento[0] == Regla[1][0][0]):
                Regla1,Regla2 = self.QuitarRecursividad(Regla)
                self.DiccionarioConjuntoReglas[Regla1[0]]=Regla1[1]
                self.DiccionarioConjuntoReglas[Regla2[0]]=Regla2[1]
                self.NoTerminales.append(Regla2[0])
                Bandera = True
            else:
                self.DiccionarioConjuntoReglas[Regla[0]]=Regla[1]

        if(Bandera):
            self.Terminales.append('epsilon')

    def Follow(self,NoTerminal):
        #Se obtienen todas las producciones donde se encuentre el No terminal del que se esta obteniendo el No Terminal
        Producciones_EncontradasFiltradas = []
        Producciones_Encontradas = []
        ListaAux = []
        for Elemento in self.NoTerminales:
            Producciones = self.DiccionarioConjuntoReglas.get(Elemento)
            for Produccion in Producciones:
                posicion = Produccion.find(NoTerminal)
                if( posicion != -1):
                    if(len(NoTerminal) == 1):
                        if(Produccion[posicion+1]!='p'):
                            Producciones_Encontradas.append([Elemento,Produccion])
                    else:
                        Producciones_Encontradas.append([Elemento,Produccion])
        
        #Checando que no haya producciones que vengan del mismo No Terminal 
        for Elemento in Producciones_Encontradas:
            if(Elemento[0] != NoTerminal):
                Producciones_EncontradasFiltradas.append(Elemento)

        #Checando si El No terminal es el comienzo de la gramatica
        if(NoTerminal == self.NoTerminales[0]):
            ListaAux.append('$')
        
        #Checando si existe cadena despues del No Terminal
        for Elemento in Producciones_EncontradasFiltradas:
            Division_Cadena = Elemento[1].partition(NoTerminal)
            if(Division_Cadena[2]==''):
                if(self.DiccionarioFollow.get(Elemento[0]) == None):
                    ListaAux+= self.Follow(Elemento[0])
                else:
                    ListaAux+= self.DiccionarioFollow.get(Elemento[0])
            else:
                if(self.DiccionarioFisrt.get(Division_Cadena[2]) == None):
                    Aux = self.First(Division_Cadena[2])
                else:
                    Aux = self.DiccionarioFisrt.get(Division_Cadena[2])

                if('epsilon' in Aux ):
                    Aux.remove('epsilon')
                    ListaAux+= Aux
                    if(self.DiccionarioFollow.get(Elemento[0]) == None):
                        ListaAux+= self.Follow(Elemento[0])
                    else:
                        ListaAux+= self.DiccionarioFollow.get(Elemento[0])
                else:
                    ListaAux+= Aux
        return ListaAux

    def First(self,NoTerminal):
        ListaAux = []

        if(NoTerminal in self.Terminales):
            return [NoTerminal]

        Producciones = self.DiccionarioConjuntoReglas.get(NoTerminal)
        for Produccion in Producciones:
            for Elemento in self.NoTerminales:
                if(Produccion.startswith(Elemento)):
                    if(self.DiccionarioFisrt.get(Elemento) == None):
                        ListaAux+= self.First(Elemento)
                    else:
                        ListaAux+= self.DiccionarioFisrt.get(Elemento)
                    break

            for Elemento in self.Terminales:
                if(Produccion.startswith(Elemento)):
                    ListaAux.append(Elemento)
                    break

        return ListaAux
        
    def ObtencionFisrt(self,Diccionario):
        for Elemento in self.NoTerminales:
            Diccionario[Elemento] = self.First(Elemento)
        print("Diccionario First")
        print(Diccionario)

    def ObtencionFollow(self,Diccionario):
        for Elemento in self.NoTerminales:
            ResultadoFiltrado = []
            Resultado = self.Follow(Elemento)
            
            for i in Resultado:
                if(not(i in ResultadoFiltrado)):
                    ResultadoFiltrado.append(i)
            
            Diccionario[Elemento] = ResultadoFiltrado 
        print("Diccionario Follow")
        print(Diccionario)

    def ObtenerProduccion(self,Elemento_Buscado,LadoIzq_Objetivo,Reglas,Regla_Objetivo):
        
        if(Elemento_Buscado in self.Terminales):
            for Elemento in Regla_Objetivo:
                if(Elemento_Buscado in Elemento):
                    return Elemento

        for Regla in Reglas:
            for LadoDer in Regla[1]:
                if((Elemento_Buscado in LadoDer) and LadoDer != 'epsilon'):
                    for Elemento in Regla_Objetivo:
                        if(Regla[0] in Elemento):
                            return Elemento
                    return self.ObtenerProduccion(Regla[0],LadoIzq_Objetivo,Reglas,Regla_Objetivo)

    def CreacionTabla(self):
        self.Columnas = self.Terminales[:] + ['$']
        self.Columnas.remove('epsilon')
        self.Filas = self.NoTerminales[:]
        Reglas = list(self.DiccionarioConjuntoReglas.items())
        self.tabla = []
    
        for Fila in self.Filas:
            Aux = []
            primeros = self.DiccionarioFisrt.get(Fila)
            for Columna in self.Columnas:
                if(Columna in primeros):
                    if(Columna != 'epsilon'):
                        Aux.append(self.ObtenerProduccion(Columna,Fila,Reglas,self.DiccionarioConjuntoReglas.get(Fila)))
                else:
                    Aux.append('')
            self.tabla.append(Aux)

        for Regla in Reglas:
            if('epsilon' in Regla[1]):
                Fila = self.Filas.index(Regla[0])
                Siguiente = self.DiccionarioFollow.get(Regla[0])
                for Elemento in Siguiente:
                    Columna = self.Columnas.index(Elemento)
                    self.tabla[Fila][Columna] = 'epsilon'

    def ObtenerTabla(self):
        i = 0
        
        with open('TablaLL1.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['']+self.Columnas)

            for Fila in self.Filas:
                writer.writerow([Fila]+self.tabla[i])
                i+= 1

    def Verificacion(self,cadena):
        Pila = ['$',self.NoTerminales[0]]
        Entrada = cadena.split(' ')
        Accion = 'Comienza'
        Bandera = True
        Solucion = []

        while (Bandera):
            AuxSolucion = ""
            Caracter = Entrada[0]
            Elemento_Pila = Pila[-1]

            for caracter in Pila:
                AuxSolucion += caracter
            AuxSolucion+= "  |  "
            for caracter in Entrada:
                AuxSolucion += caracter
            AuxSolucion+= "  |  "

            if(Elemento_Pila == Caracter):
                if(Elemento_Pila == '$' and Caracter == '$'):
                    Accion = 'Aceptada'
                    Bandera = False
                else:
                    Pila.pop()
                    Entrada.pop(0)
                    Accion = 'Avanzar'
            else:
                Accion = ''
                Columna = self.Columnas.index(Caracter)
                Fila = self.Filas.index(Pila[-1])
                Accion = self.tabla[Fila][Columna]
                if(Accion != ''):
                    Pila.pop()
                    if(Accion in self.Terminales):
                        if(Accion != 'epsilon'):
                            Pila.append(Accion)
                    else:
                        Aux = list(Accion)
                        while(len(Aux) != 0):    
                            if(Aux[-1] == 'p'):
                                Pila.append(Aux[-2]+Aux[-1])
                                Aux.pop()
                                Aux.pop()
                            else:
                                Pila.append(Aux.pop())	
                else:
                    Accion = 'ERROR'
                    Bandera = False

            AuxSolucion+= Accion
            Solucion.append(AuxSolucion)
        return  Solucion   

    def Inicializacion(self):
        self.ObtencionDiccionario()
        self.ObtencionFisrt(self.DiccionarioFisrt)
        self.ObtencionFollow(self.DiccionarioFollow)
        self.CreacionTabla()
        self.ObtenerTabla()
       
#----------------------------------------------------------------------------------------------------------------
'''
a=AFN(simbolo='a')
b=AFN(simbolo='b')
c=AFN(simbolo='c')
a.union(b)
a.cerradura_kleene()
c.cerradura_positiva()
a.concatenacion(c)

a=AFN(simbolo='a')
b=AFN(simbolo='b')
a.union_especial([b])

a.imprimir_transiciones()
print("ESTADOS ACEPTACION")
print(a.estados_aceptacion)
print("ALFABETO")
print(a.alfabeto)


AFDD=a.ir_a()
print("AFD-------------------------")
print(AFDD.estados)
print(AFDD.finales)
print(AFDD.transiciones)
'''