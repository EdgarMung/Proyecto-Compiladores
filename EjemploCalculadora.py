from Clases import AFN
from Clases import AFD
from AlgoritmoLexObjeto import Lexico
import math

class Calculadora:
	def __init__(self,AFD,cadena):
		self.Lex=Lexico(cadena,AFD)
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



digitos=AFN(simbolo='0')
uno=AFN(simbolo='1')
dos=AFN(simbolo='2')
tres=AFN(simbolo='3')
cuatro=AFN(simbolo='4')
cinco=AFN(simbolo='5')
seis=AFN(simbolo='6')
siete=AFN(simbolo='7')
ocho=AFN(simbolo='8')
nueve=AFN(simbolo='9')

digitos.union(uno)
digitos.union(dos)
digitos.union(tres)
digitos.union(cuatro)
digitos.union(cinco)
digitos.union(seis)
digitos.union(siete)
digitos.union(ocho)
digitos.union(nueve)

digitos.cerradura_positiva()

mas=AFN(simbolo='+')
menos=AFN(simbolo='-')
mult=AFN(simbolo='*')
div=AFN(simbolo='/')
pot=AFN(simbolo='^')
i=AFN(simbolo='(')
d=AFN(simbolo=')')



sin=AFN(simbolo='s')
sin.concatenacion(AFN(simbolo='i'))
sin.concatenacion(AFN(simbolo='n'))

cos=AFN(simbolo='c')
cos.concatenacion(AFN(simbolo='o'))
cos.concatenacion(AFN(simbolo='s'))

tan=AFN(simbolo='t')
tan.concatenacion(AFN(simbolo='a'))
tan.concatenacion(AFN(simbolo='n'))

mas.union_especial([menos,mult,div,pot,i,d,sin,cos,tan,digitos])
AFDD=mas.ir_a()


MiCalculadora=Calculadora(AFDD,"1+2")
MiCalculadora.E()
#1+4*2+cos(1)*sin(2-1)-1