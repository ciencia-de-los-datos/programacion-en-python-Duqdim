"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from os import sep
from pickle import APPEND
from readline import append_history_file
with open("data.csv", newline='') as f:  
    datos= csv.reader(f, delimiter='\t')
    print(datos)
    colums = list(datos)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma=0
    for num in colums:
        suma += int(num[1])
    return suma

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    vocales = []
    valores = []
    for valor in colums:
            valores.append(valor[0])
    
    for i in valores:
            tupla=(i,valores.count(i))
            vocales.append(tupla)        
    return sorted(set(vocales))

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    x2=[]
    valores01=[]
    suma = 0
    sumas=[]
    valoress=('A',"B","C","D","E") 
    for x in valoress:
        suma=0
        for i in range(len(colums)):
            if colums[i][0]==x:
                suma += int(colums[i][1])      
        sumas.append(suma)
        x1=x 
        x2.append(x1)   
        tuplaa=(sumas+x2)
    for j in range (len(valoress)):       
        valores0=(tuplaa[5+j],tuplaa[j])
        valores01.append(valores0)

        #print(valores01)

    return(valores01)
    
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    
    """
    vocales = []
    valores = []
    vectorr =  []
    for valor in colums:
            valores.append(valor[2])
    for i in range(len(valores)):
        vector=(valores[i].split(sep='-'))
        vectorr.append(vector[1])
    for j in vectorr:   
        tupla=(j,vectorr.count(j))
        vocales.append(tupla)        
    return sorted(set(vocales))


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    x2=[]
    valores01=[]
    suma = 0
    sumas=[]
    sumast = []
    valoress=('A',"B","C","D","E") 
    for x in valoress:
        suma=0
        sumast=[]
        for i in range(len(colums)):
            if colums[i][0]==x:
                suma=(colums[i][1]) 
                sumast.append(suma)
        r=(x,int(max(sumast)),int(min(sumast)))
        x2.append(r)
        #print(x2)

    return(x2)

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    
    """
    vocales = []
    valores = []
    vectorr =  []
    vocali= []
    y = {}
    for valor in colums:
            valores.append(valor[4])
    for i in range(len(valores)):
        vector=(valores[i].split(sep=','))
        vectorr.append(vector)
    for j in vectorr:
        #print(j)
        for f in j:
            #print(f)
            voca=(f.split(sep=':'))
            voc=(voca[0],int(voca[1]))
            vocales.append(voc)
    for u in vocales:
        tupla=(u[0])
        vocali.append(tupla)      
    vocali=sorted(set(vocali))

    x22=[]
    suma = 0
    sumass=[]
    sumastt = [] 
    for x in vocali:
        suma=0
        sumastt=[]
        for q in range(len(vocales)):
            if vocales[q][0]==x:
                suma=(vocales[q][1]) 
                sumastt.append(suma)
        r=(x,int(min(sumastt)),int(max(sumastt)))
        x22.append(r)
        #print(x22)
    return(x22)



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    colu2=[]
    co=[]
    valores = []
    valor= []
    go=[]
    pp=[]
    for valor in colums:
            valores.append(valor[1])
            valor.append(valor)
    for x in valores:
        r= x
        colu2.append(r)
        t=sorted(set(colu2))
    for l in t:
        co=[] 
          
        for q in range(len(valores)):
            if valores[q]==l:
                g=(colums[q][0])
                co.append(g)    
        cp=(int(l),(co))
        pp.append(cp)           
    return (pp)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    colu2=[]
    co=[]
    valores = []
    valor= []
    go=[]
    pp=[]
    for valor in colums:
            valores.append(valor[1])
            valor.append(valor)
    for x in valores:
        r= x
        colu2.append(r)
        t=sorted(set(colu2))
    for l in t:
        co=[] 
          
        for q in range(len(valores)):
            if valores[q]==l:
                g=(colums[q][0])
                co.append(g)
        coo=sorted(set(co))     
        cp=(int(l),(coo))
        pp.append(cp)  
    return(pp)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    valos=[]
    valos1=[]
    valos2=[]
    valos3=[]
    suma=0
    y={}
    for valor in colums:
        rt=(valor[4])
        rt=rt.split(sep=',')
        for h in rt:
            valos.append(h)
    for jj in valos:
        v=jj.split(sep=':')
        n=(v[0])
        valos1.append(n)

    lista=sorted(set(valos1))
    for k in lista:
        suma=0
        for u in valos1:
            if u==k:
                suma = suma+1
        valos3.append(suma)
    for i in range(len(valos3)):
        y[lista[i]]=valos3[i]

                
   

    return(y)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r")as file:
        datos=file.readlines()
    datos=[line.replace("\n", "")for line in datos]
    datos=[line.split("\t")for line in datos]
    col4=[len(line[3].split(","))for line in datos]
    col5=[len(line[4].split(","))for line in datos]
    col1=[(line[0])for line in datos]
    data_base=list(zip(col1,col4,col5))
    
    return (data_base) 
   


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """
    with open("data.csv") as f:
        df = f.readlines()
        df = [row.replace("\n", "") for row in df]
        df = [row.split('\t') for row in df]

    counter = {}
    for row in df:
        value = int(row[1])
        pairs = row[3].split(',')
        for pair in pairs:
            if pair in counter.keys():
                counter[pair] += value
            else:
                counter[pair] = value

    return counter

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r")as file:
        datos_12=file.readlines()
    datos_12=[line.replace("\n","")for line in datos_12]
    datos_12=[line.split("\t")for line in datos_12]
    columna5=[line[4].split(",")for line in datos_12]
    columna1=[line[0]for line in datos_12]
    columna5_columna1=list(zip(columna1,columna5))
    di3_keys=sorted(set(columna1))
    di3={}
    for llave in di3_keys:
        di3[llave]=0
    for x, y in columna5_columna1:
        for z in y:
            di3[x]+=int(z[4:])
    

    return di3

    
