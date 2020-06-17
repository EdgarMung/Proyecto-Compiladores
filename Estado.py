class Estado:

	def __init__(self,id):
		self.id = id
		self.transiciones = {}
	#Agrega transiciones al diccionario.
	def anadir_transicion(self,simbolo,id_final):
		if self.transiciones.get(simbolo) == None:
			#print("Hay un nuevo simbolo en el estado "+str(self.id))
			self.transiciones.setdefault(simbolo,[id_final])
			#print(self.transiciones)
		else:
			#print("Agregando transicion.")
			conjunto_ids = self.transiciones.get(simbolo)
			conjunto_ids.append(id_final)
			#print(self.transiciones)
	#Redefine los numeros de las transiciones a los nuevos nodos.
	def actualizar_transiciones(self,no_posiciones):
		self.id=self.id+no_posiciones
		for llave in list(self.transiciones.keys()):
			nuevas_transiciones=[]

			for transicion in self.transiciones.get(llave):
				nuevas_transiciones.append(transicion+no_posiciones)

			self.transiciones.pop(llave)
			self.transiciones.setdefault(llave,nuevas_transiciones)