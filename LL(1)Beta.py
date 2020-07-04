import pandas as pd

#Variables que se recibirán
DiccionarioConjuntoReglas = {}
ConjuntoReglas = ['E->E+T|E-T|T','T->T*F|T/F|F','F->(E)|num']
NoTerminales =  ['S','E','T','C','F']
Terminales = ['or','&','*','+','']

def QuitarRecursividad(Regla):
    A = Regla[0]
    Beta = Regla[1][-1]
    New = A+'p'
    Regla1 = [A,Beta+New]
    ArregloAux = []
    for Elemento in Regla[1]:
        if(A in Elemento):
            ArregloAux.append(Elemento.replace(A,'')+New)
    ArregloAux.append('epcilon')
    Regla2=[New,ArregloAux]
    
    return Regla1,Regla2

def ObtencionDiccionario():
    for Elemento in ConjuntoReglas:
        Regla = Elemento.split("->")
        Regla[1]=Regla[1].split('|')
        if(Elemento[0] == Regla[1][0][0]):
            Regla1,Regla2 = QuitarRecursividad(Regla)
            DiccionarioConjuntoReglas[Regla1[0]]=Regla1[1]
            DiccionarioConjuntoReglas[Regla2[0]]=Regla2[1]
            NoTerminales.append(Regla1[1])
        else:
            DiccionarioConjuntoReglas[Regla[0]]=Regla[1]
def ObtencionFisrt(Diccionario):
    

def Algoritmo():
    DiccionarioFisrt = {}
    ObtencionFisrt(DiccionarioFisrt)

def ObtenerTabla():
    data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}
    df = pd.DataFrame(data, columns = ['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
    df.to_csv('example.csv')


#ObtencionDiccionario()
ObtenerTabla()