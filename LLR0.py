from Lector import lector

#Clase para crear la tabla LLR0:
class LLRO:
	#Constructor de la clase
	#lt = lista de terminales
	#ln = lista de no terminales
	#dc = diccionario de terminales-reglas
	def __init__(self,lt,ln,dc,cod):
		self.lt=lt
		self.ln=ln
		self.dc=dc
		self.cod=cod
		self.inv_cod()
		#print("\nTERMINALES:",self.lt)
		#print("\nNO TERMINALES:",self.ln)
		#print("\nDICCIONARIO DE REGLAS:")
		print("TERMINALES:",lt)
		print("NO TERMINALES:",ln)
		for key in self.dc.keys():
			print(key,"\t",self.dc.get(key))
	#Función para crear las cerraduras:
	#C_E = Conjunto de reglas externo a la función.
	def cerradura(self,c_e):
		c_final=[]
		p_final=0
		for x in c_e:
			if x not in c_final:
				c_final.append(x)

			while p_final < len(c_final):
				c=c_final[p_final]
				p=c.index(0)
				#print("Lista",c,"en posicion",p)

				if p+1 < len(c):
					sig=c[p+1]
					#print("La siguiente va a ser cerradura de",sig)
					l_aux=self.dc.get(sig)

					if l_aux is not None:

						for e in l_aux:
							e_c=e.copy()
							e_c.insert(0,0)
							if e_c not in c_final:
								c_final.append(e_c)
				p_final+=1
				#print(c_final)
		#print("\t\tCerradura:",c_final)
		return c_final
	#Función para mover el punto:
	#c = Conjunto de reglas externo a la función.
	#s = Símbolo para mover()
	#p_s = posición del símbolo.
	def mover(self,c,s):
		#print("moviendo",c,"con",s)
		c_f=[]
		for r in c:
			if s in r:
				p_s=r.index(s)
				#print("entro",r.index(0),r.index(s))
				if r.index(s) > 0 and r.index(0) == r.index(s)-1:
					c_c=r.copy()
					p=c_c.index(0)
					#print("0 en posición",p)
					if p != len(c_c) -1:
						c_c.pop(p)
						c_c.insert(p+1,0)
						c_f.append(c_c)
					else:
						c_f.append([])
		#print("Resultado:",c_f)
		return(c_f)
	#Funcion ir_a:
	def ir_a(self,c,s):
		return self.cerradura(self.mover(c,s))
	#Función para obtener los símbolos antes del punto:
	#c = conjunto de reglas.
	def posteriores(self,c):
		post=[]
		for r in c:
			if r.index(0) < len(r)-1 and r[r.index(0)+1] not in post:
				post.append(r[r.index(0)+1])
		return post
	#Función para calcular el follow de un simbolo:
	#s = simbolo
	#c = conjunto
	#p = posicion
	def follow(self,s,resultado):
		if s == 0 and -1 not in resultado:
			resultado.append(-1)
			return resultado
		for key in self.dc.keys():
			for c in self.dc.get(key):
				if s in c:
					p=c.index(s)

					if p == len(c)-1:
						self.follow(key,resultado)
					elif c[p+1] not in resultado:

						resultado.append(c[p+1])
		return resultado
	def inv_cod(self):
		inv_map = {v: k for k, v in self.cod.items()}
		self.inv_cod=inv_map
	#Función para utilizar ir_a en los diferentes conjuntos:
	#self.pool = donde se guardan todos los conjuntos resultantes i(x)
	#p = posicion
	#s = simbolo
	#c = conjunto simple
	#d_r = diccionario de relaciones contiene los conjuntos que salieron de otro conjunto.
	#r = relaciones
	def crear(self):
		self.pool=[]
		d_r={}
		self.pool.append(self.cerradura([[0,1]]))
		p=0

		while p < len(self.pool):
			#print("Analizando el conjunto I("+str(p)+"):")
			for s in self.posteriores(self.pool[p]):
			#	print("\tBuscando el símbolo",s,":")
				c=self.ir_a(self.pool[p],s)
				if c not in self.pool:
					self.pool.append(c)
				print(p,"\t",self.inv_cod.get(s),"\t",self.pool.index(c))
				r=(p,s)
				d_r.setdefault(r,self.pool.index(c))
			p+=1

		print("POOL DE CONJUNTOS:")
		for conjunto in self.pool:
			print("[",end="")
			for regla in conjunto:
				print("[",end="")
				for p in range(len(regla)):
					if regla[p] == 0:
						print(".",end="")
					else:
						print(self.inv_cod.get(regla[p]), end="")
				print("]",end="")
			print("]")

		print("DICCIONARIO DE DESPLAZAMIENTO:")
		for key in d_r.keys():
			print("[",key[0],self.inv_cod.get(key[1]),d_r.get(key),"]",end="\t")
		print("TOTAL",len(d_r))
		self.diccionario_desplazamiento=d_r
	#Función para obtener las reglas que necesitan first y follow
	#l_r = lista de reglas originales por posición
	#p = posición
	#c = conjunto
	#r = regla
	def reglas(self):
		d=self.inv_dc()
		l_r=self.val_list()
		dic={}
		#print(l_r)
		for p in range(len(self.pool)):
			c=self.pool[p]
			for r in c:
				if r[len(r)-1] == 0:
					r_c=r.copy()
					r_c.pop()
					print(p,l_r.index(r_c),end=" ")
					self.p_lista(self.follow(d.get(tuple(r_c)),[]))
					print("")

					for simb in self.follow(d.get(tuple(r_c)),[]):
						dic.setdefault((p,simb),l_r.index(r_c))

		print("DICCIONARIO DE REDUCCIÓN:\n")
		for key in dic.keys():
			print("[",key[0],self.inv_cod.get(key[1]),dic.get(key),"]",end="\t")
		print("TOTAL",len(dic))
		print("TOTAL",len(dic))
		self.diccionario_reduccion=dic
	#Función que invierte las llaves y los valores del diccionario dc:
	def inv_dc(self):
		inv={}
		for key in self.dc.keys():
			for r in self.dc.get(key):
				inv.setdefault(tuple(r),key)

		return inv
	#Fución que regresa una lista de los valores del diccionario:
	def val_list(self):
		l_r=[]
		for key in self.dc.keys():
			for l in self.dc.get(key):
				l_r.append(l)
		return l_r
	#Función para evaluar la cadena:
	def evaluar(self,l):
		print("CADENA",l)
		reglas=self.val_list()
		busqueda=self.inv_dc()
		print("REGLAS:",reglas)
		pila=[-1,0]
		error=0

		while not error:
			self.p_operaciones(pila)
			self.p_lista(l)
			s=l.pop(0)

			if (pila[-1],s) in self.diccionario_desplazamiento:
				print("DESPLAZAMIENTO",self.diccionario_desplazamiento.get((pila[-1],s)))
				pila.append(s)
				pila.append(self.diccionario_desplazamiento.get((pila[-2],s)))

			elif (pila[-1],s) in self.diccionario_reduccion:
				print("REDUCCION",self.diccionario_reduccion.get((pila[-1],s)))
				if (pila[-1],s) == (1,-1):
					print("Cadena aceptada.")
					return
				pos=self.diccionario_reduccion.get((pila[-1],s))
				cardinalidad=len(reglas[pos])*2

				for n in range(cardinalidad):
					pila.pop()

				pila.append(busqueda.get(tuple(reglas[pos])))

				if (pila[-2],pila[-1]) in self.diccionario_desplazamiento:
					pila.append(self.diccionario_desplazamiento.get((pila[-2],pila[-1])))

				elif (pila[-2],pila[-1]) in self.diccionario_reduccion:
					pila.append(self.diccionario_reduccion.get((pila[-2],pila[-1])))

				l.insert(0,s)
			else:
				print("ERROR")
				return
	def p_lista(self,l):
		print("[",end="")
		for e in l:
			print(self.inv_cod.get(e),end=" ")
		print("]",end="")
	def p_operaciones(self,l):

		print("[",end="")
		for p in range(0,len(l),2):
			print(self.inv_cod.get(l[p]),l[p+1],end=" ")
		print("]",end="")


#Menú----------------------------------
reglas=lector()
tabla=LLRO(reglas.lt,reglas.ln,reglas.diccionario,reglas.conjunto_reglas)
print(tabla.cod)
tabla.crear()
tabla.reglas()
r=reglas.convertir_cadena("(aora)*&a+")
tabla.evaluar(r)