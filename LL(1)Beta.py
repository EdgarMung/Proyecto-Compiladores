import csv

ConjuntoReglas = ['E->E+T|E-T|T','T->T*F|T/F|F','F->(E)|num']
NoTerminales =  ['E','T','F']
Terminales = ['+','-','*','/','(',')','num']

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
                if(Elemento_Buscado in LadoDer):
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
        
        with open('students.csv', 'w', newline='') as csvfile:
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

        print("Empieza la Veridficacion")
        while (Bandera):
            Caracter = Entrada[0]
            Elemento_Pila = Pila[-1]

            print(Pila,end=" | ")
            print(Entrada,end=" | ")

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

            print(Accion)            

    def Inicializacion(self):
        self.ObtencionDiccionario()
        self.ObtencionFisrt(self.DiccionarioFisrt)
        self.ObtencionFollow(self.DiccionarioFollow)
        self.CreacionTabla()
        self.ObtenerTabla()
        
objeto = AlgoritmoLL(ConjuntoReglas,NoTerminales,Terminales)
objeto.Verificacion('num + num $')
