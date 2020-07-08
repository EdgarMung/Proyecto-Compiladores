class lector:
	#Atributos de la clase:
	conjunto_reglas=[]
	diccionario={}
	lt=[] #Lista de terminales.
	ln=[] #Lista de NO terminales.
	#Constructor de la clase:
	def __init__(self):
		self.procesar_txt()
	#Procesar el txt para obtener las reglas:
	def obtener_reglas(self,txt):
		archivo=open(txt,'r')

		for linea in archivo.readlines():
			print(linea,end='')
			self.conjunto_reglas.append(linea)

		archivo.close()
	#Obtener los terminales de las reglas:
	def obtener_no_terminales(self):
		#print("OBTENIENDO NO TERMINALES")
		for regla in self.conjunto_reglas:
			self.ln.append(self.obtener_subcadena(regla,'->'))
	#Obtener los no terminales de las reglas:
	def obtener_terminales(self):
		l_aux=[]
		#print("OBTENIENDO TERMINALES")
		for regla in self.conjunto_reglas:
			posicion=regla.find("->")
			cad_aux=regla[posicion+2:]
			#cad_aux=cad_aux.replace(" ","")
			cad_aux=cad_aux.replace("\n","")
			#Quitando uno por uno los terminales:
			for terminal in self.ln:
				cad_aux=cad_aux.replace(terminal," ")
			l_aux.append(cad_aux)
		#l_aux es una lista que contiene todas las cadenas sin terminales.
		nt=[]
		for r_nt in l_aux:
			nt+=r_nt.split('|')

		l_aux=nt
		nt=[]
		for elemento in l_aux:
			if elemento.split() != []:
				nt+=elemento.split()

		nt=list(set(nt))
		self.lt=nt
	#Obtener el siguiente pedazo de cadena antes de un símbolo:
	def obtener_subcadena(self,cadena,simbolo):
		posicion=cadena.find(simbolo)
		temporal=cadena[:posicion]
		return temporal.replace(" ","")
	#Cambiando las reglas a una estructura de datos:
	def convertir_reglas(self):
		#print("CONVIRTIENDO REGLAS")
		reglas_finales=[]

		for regla in self.conjunto_reglas:
			posicion=regla.find('->')

			no_terminal=(regla[:posicion]).replace(" ","")
			terminal=((regla[posicion+2:]).replace(" ","")).replace("\n","")
			terminal=terminal.split("|")
			conjunto_reglas=[no_terminal]
			for regla in terminal:

				reglas=[]
				cadena=''
				posicion=0

				while posicion < len(regla):
					cadena+=regla[posicion]
					if cadena in self.lt:
						reglas.append(cadena)
						cadena=''
					elif cadena in self.ln:
						reglas.append(cadena)
						cadena=''
					posicion+=1

				conjunto_reglas.append(reglas)
			reglas_finales.append(conjunto_reglas)
		self.conjunto_reglas=reglas_finales
	#Conversión de las listas a un diccionario:
	def conversion_diccionario(self):
		#print("CONVERSION A DICCIONARIO")
		self.diccionario={}
		for regla in self.conjunto_reglas:
			li=regla[0]
			ld=regla[1:]
			self.diccionario.setdefault(li,ld)
	#Funcion para llamar a las funciones en orden:
	def procesar_txt(self):
		self.obtener_reglas('txt')
		self.obtener_no_terminales()
		self.obtener_terminales()
		self.convertir_reglas()
		self.conversion_diccionario()
		self.codigo()
	#Cambiar las letras por numeros:
	def codigo(self):
		c=0
		d_cod={}
		for terminal in self.ln:
			d_cod.setdefault(terminal,c)
			c+=1
		for no_terminal in self.lt:
			d_cod.setdefault(no_terminal,c)
			c+=1

		d_cod.setdefault('$',-1)

		d_aux=self.diccionario.copy()

		for key in d_aux.keys():
			for regla in d_aux.get(key):
				for p in range(len(regla)):
					regla[p]=d_cod.get(regla[p])

		l_keys=list(d_aux.keys())

		for key in l_keys:
			d_aux[d_cod.get(key)]=d_aux.pop(key)

		for p in range(len(self.lt)):
			self.lt[p]=d_cod.get(self.lt[p])
		for p in range(len(self.ln)):
			self.ln[p]=d_cod.get(self.ln[p])
		self.conjunto_reglas=d_cod
		self.diccionario=d_aux
	def convertir_cadena(self,cadena):
		s=[]
		aux=""
		for p in range(len(cadena)):
			aux+=cadena[p]
			#print(aux,s)
			if aux in self.conjunto_reglas:
				s.append(self.conjunto_reglas.get(aux))
				aux=""
		s.append(-1)

		print(s)
		return s