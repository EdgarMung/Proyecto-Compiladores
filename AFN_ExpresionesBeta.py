from Clases import AFN,AFD
from AlgoritmoLexObjeto import Lexico

class Generador:
	def __init__(self, AFD, cadena):
		self.Lex=Lexico(cadena,AFD)
		self.CONC=10
		self.UNI=20
		self.C_P=30
		self.C_E=40
		self.S_I=50
		self.P_I=60
		self.P_D=70
		self.SIMB=80

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

caracteres=AFN(simbolo='A')
B=AFN(simbolo='B')
C=AFN(simbolo='C')
D=AFN(simbolo='D')
E=AFN(simbolo='E')
F=AFN(simbolo='F')
G=AFN(simbolo='G')
H=AFN(simbolo='H')
I=AFN(simbolo='I')
J=AFN(simbolo='J')
K=AFN(simbolo='K')
L=AFN(simbolo='L')
M=AFN(simbolo='M')
N=AFN(simbolo='N')
#Ñ=AFN(simbolo='Ñ')
O=AFN(simbolo='O')
P=AFN(simbolo='P')
Q=AFN(simbolo='Q')
R=AFN(simbolo='R')
S=AFN(simbolo='S')
T=AFN(simbolo='T')
U=AFN(simbolo='U')
V=AFN(simbolo='V')
W=AFN(simbolo='W')
X=AFN(simbolo='X')
Y=AFN(simbolo='Y')
Z=AFN(simbolo='Z')
"""
a=AFN(simbolo='a')
b=AFN(simbolo='b')
c=AFN(simbolo='c')
d=AFN(simbolo='d')
e=AFN(simbolo='e')
f=AFN(simbolo='f')
g=AFN(simbolo='g')
h=AFN(simbolo='h')
i=AFN(simbolo='i')
j=AFN(simbolo='j')
k=AFN(simbolo='k')
l=AFN(simbolo='l')
m=AFN(simbolo='m')
n=AFN(simbolo='n')
#ñ=AFN(simbolo='ñ')
o=AFN(simbolo='o')
p=AFN(simbolo='p')
q=AFN(simbolo='q')
r=AFN(simbolo='r')
s=AFN(simbolo='s')
t=AFN(simbolo='t')
u=AFN(simbolo='u')
v=AFN(simbolo='v')
w=AFN(simbolo='w')
x=AFN(simbolo='x')
y=AFN(simbolo='y')
z=AFN(simbolo='z')
cero=AFN(simbolo='0')
uno=AFN(simbolo='1')
dos=AFN(simbolo='2')
tres=AFN(simbolo='3')
cuatro=AFN(simbolo='4')
cinco=AFN(simbolo='5')
seis=AFN(simbolo='6')
siete=AFN(simbolo='7')
ocho=AFN(simbolo='8')
nueve=AFN(simbolo='9')
"""

caracteres.union(B)
caracteres.union(C)
caracteres.union(D)
caracteres.union(E)
caracteres.union(F)
caracteres.union(G)
caracteres.union(H)
caracteres.union(I)
caracteres.union(J)
caracteres.union(K)
caracteres.union(L)
caracteres.union(M)
caracteres.union(N)
#caracteres.union(Ñ)
caracteres.union(O)
caracteres.union(P)
caracteres.union(Q)
caracteres.union(R)
caracteres.union(S)
caracteres.union(T)
caracteres.union(U)
caracteres.union(V)
caracteres.union(W)
caracteres.union(X)
caracteres.union(Y)
caracteres.union(Z)
"""
caracteres.union(a)
caracteres.union(b)
caracteres.union(c)
caracteres.union(d)
caracteres.union(e)
caracteres.union(f)
caracteres.union(g)
caracteres.union(h)
caracteres.union(i)
caracteres.union(j)
caracteres.union(k)
caracteres.union(l)
caracteres.union(m)
caracteres.union(n)
#caracteres.union(ñ)
caracteres.union(o)
caracteres.union(p)
caracteres.union(q)
caracteres.union(r)
caracteres.union(s)
caracteres.union(t)
caracteres.union(u)
caracteres.union(v)
caracteres.union(w)
caracteres.union(x)
caracteres.union(y)
caracteres.union(z)
caracteres.union(cero)
caracteres.union(uno)
caracteres.union(dos)
caracteres.union(tres)
caracteres.union(cuatro)
caracteres.union(cinco)
caracteres.union(seis)
caracteres.union(siete)
caracteres.union(ocho)
caracteres.union(nueve)
"""
#caracteres.union(digitos)


"""
simbolos=AFN(simbolo='.')
diagonal=AFN(simbolo='/')
menos=AFN(simbolo='-')
simb_+=AFN(simbolo='s')
simb_+.concatenacion(AFN(simbolo='i'))
simb_+.concatenacion(AFN(simbolo='m'))
simb_+.concatenacion(AFN(simbolo='b'))
simb_+.concatenacion(AFN(simbolo='_'))
simb_+.concatenacion(AFN(simbolo='+'))
simb_*=AFN(simbolo='s')
simb_*.concatenacion(AFN(simbolo='i'))
simb_*.concatenacion(AFN(simbolo='m'))
simb_*.concatenacion(AFN(simbolo='b'))
simb_*.concatenacion(AFN(simbolo='_'))
simb_*.concatenacion(AFN(simbolo='*'))
simbolos.union(diagonal)
simbolos.union(menos)
simbolos.union(simb_+)
simbolos.union(simb_*)
caracteres.union(simbolos)
"""

caracteres.cerradura_positiva()

conc=AFN(simbolo='°')
uni=AFN(simbolo='|')
c_p=AFN(simbolo='+')
c_e=AFN(simbolo='*')
s_i=AFN(simbolo='?')

p_i=AFN(simbolo='(')
p_d=AFN(simbolo=')')

conc.union_especial([uni,c_p,c_e,s_i,p_i,p_d,caracteres])
AFDD=conc.ir_a()


#l=Lexico('ASD-ASDF/ASD+',AFDD)
#print(l.getToken())

Asdf=Generador(AFDD,"(C|B)+")
r=[]
Asdf.E(r)
print("\nRESULTADO")
r[0].imprimir_transiciones()