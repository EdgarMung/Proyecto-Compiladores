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