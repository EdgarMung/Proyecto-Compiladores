from Clases import AFN
from Clases import AFN
from AlgoritmoLexObjeto import Lexico

class Verificador:
    def __init__(self,AFDd):
        #self.Lex = Lexico(cadena,AFD)
        self.AFDD = AFDd
        self.SIMB = 10
        self.FLECHA = 20
        self.PC = 30
        self.OR = 40

    def Verificar(self,cadena):
        self.Lex = Lexico(cadena,self.AFDD)
        return self.G()
        
    def G(self):
        print("G:", end = " ")
        print(self.Lex.cadena)
        if(self.ListaReglas()):
            tupla=self.Lex.getToken()
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
        if(token == self.SIMB):
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
        if(token == self.SIMB):
            self.Lex.GetEstadoLexic(temp)
            if(self.ListaSimb()):
                return True
            self.Lex.SetEstadoLexic(temp)
            return True
        return False

#-------------------------------------------------------------------------
sim = AFN(simbolo = 'A')
sim.union(AFN(simbolo = 'B'))
sim.union(AFN(simbolo = 'C'))
sim.union(AFN(simbolo = 'D'))
sim.union(AFN(simbolo = 'E'))
sim.union(AFN(simbolo = 'F'))
sim.union(AFN(simbolo = 'G'))
sim.union(AFN(simbolo = 'H'))
sim.union(AFN(simbolo = 'I'))
sim.union(AFN(simbolo = 'J'))
sim.union(AFN(simbolo = 'K'))
sim.union(AFN(simbolo = 'L'))
sim.union(AFN(simbolo = 'M'))
sim.union(AFN(simbolo = 'N'))
sim.union(AFN(simbolo = 'O'))
sim.union(AFN(simbolo = 'P'))
sim.union(AFN(simbolo = 'Q'))
sim.union(AFN(simbolo = 'R'))
sim.union(AFN(simbolo = 'S'))
sim.union(AFN(simbolo = 'T'))
sim.union(AFN(simbolo = 'U'))
sim.union(AFN(simbolo = 'V'))
sim.union(AFN(simbolo = 'W'))
sim.union(AFN(simbolo = 'X'))
sim.union(AFN(simbolo = 'Y'))
sim.union(AFN(simbolo = 'Z'))
sim.union(AFN(simbolo = 'a'))
sim.union(AFN(simbolo = 'b'))
sim.union(AFN(simbolo = 'c'))
sim.union(AFN(simbolo = 'd'))
sim.union(AFN(simbolo = 'e'))
sim.union(AFN(simbolo = 'f'))
sim.union(AFN(simbolo = 'g'))
sim.union(AFN(simbolo = 'h'))
sim.union(AFN(simbolo = 'i'))
sim.union(AFN(simbolo = 'j'))
sim.union(AFN(simbolo = 'K'))
sim.union(AFN(simbolo = 'l'))
sim.union(AFN(simbolo = 'm'))
sim.union(AFN(simbolo = 'n'))
sim.union(AFN(simbolo = 'o'))
sim.union(AFN(simbolo = 'p'))
sim.union(AFN(simbolo = 'q'))
sim.union(AFN(simbolo = 'r'))
sim.union(AFN(simbolo = 's'))
sim.union(AFN(simbolo = 't'))
sim.union(AFN(simbolo = 'u'))
sim.union(AFN(simbolo = 'v'))
sim.union(AFN(simbolo = 'w'))
sim.union(AFN(simbolo = 'x'))
sim.union(AFN(simbolo = 'y'))
sim.union(AFN(simbolo = 'z'))
sim.union(AFN(simbolo = '/'))
sim.union(AFN(simbolo = '*'))
sim.union(AFN(simbolo = '-'))
sim.union(AFN(simbolo = '+'))
sim.union(AFN(simbolo = '^'))
sim.union(AFN(simbolo = '('))
sim.union(AFN(simbolo = ')'))
sim.union(AFN(simbolo = '!'))
sim.union(AFN(simbolo = '¡'))
sim.union(AFN(simbolo = '"'))
sim.union(AFN(simbolo = '#'))
sim.union(AFN(simbolo = '%'))
sim.union(AFN(simbolo = '?'))
sim.union(AFN(simbolo = '¿'))

#sim.cerradura_positiva()

flecha = AFN(simbolo='-')
flecha.concatenacion(AFN(simbolo='>'))

PC = AFN(simbolo=';')

Compuerta = AFN(simbolo='|')

sim.union_especial([flecha,PC,Compuerta])

AFDD = sim.ir_a()

Herramienta = Verificador(AFDD)
print(Herramienta.Verificar("E->E+T|E-T|T;T->T*F|T/F|F;F->(E)|num;A"))
#E->E+T|E-T|T;T->T*F|T/F|F;F->(E)|num;