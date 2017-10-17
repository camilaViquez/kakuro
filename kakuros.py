
import random
import itertools



def crearTablero (fila,columna):
    listCasillas = []
    subLis = [0,0,0,0]
    tamano = fila * columna
    for i in range(tamano):
        listCasillas.append(subLis)
    llenarTablero(listCasillas,fila,columna)
    return(listCasillas)
    
def llenarTablero(listCasillas,fila,columna):
    c_negra = ["negra",0,0,0]
    c_blanca = ["blanca",0,0,0]

    listCasillas [0] = c_negra
    listCasillas [1] = ["negra",-1,3, -1]
    listCasillas [2] = ["negra",-1,20, -1] 
    listCasillas [3] = ["negra",-1,-1, -1]   
    listCasillas [4] = ["negra",-1,10, -1]
    listCasillas [5] = ["negra",-1,12, -1]
    listCasillas [6] = ["negra",-1,3, -1]
    listCasillas [7] = c_negra
    listCasillas [8] = ["negra", 9, -1, -1]
    listCasillas [9] = c_blanca
    listCasillas [10] = c_blanca
    listCasillas [11] = ["negra",13,-1, -1]
    listCasillas [12] = c_blanca
    listCasillas [13] = c_blanca
    listCasillas [14] = c_blanca
    listCasillas [15] = c_negra
    listCasillas [16] = ["negra",11,-1, -1]
    listCasillas [17] = c_blanca
    listCasillas [18] = c_blanca
    listCasillas [19] = ["negra",6,15, -1]
    listCasillas [20] = c_blanca
    listCasillas [21] = c_blanca
    listCasillas [22] = c_blanca
    listCasillas [23] = c_negra
    listCasillas [24] = c_negra
    listCasillas [25] = ["negra",6,-1, -1]
    listCasillas [26] = c_blanca
    listCasillas [27] = c_blanca
    listCasillas [28] = c_blanca
    listCasillas [29] = ["negra",-1,13, -1]
    listCasillas [30] = c_negra
    listCasillas [31] = c_negra
    listCasillas [32] = c_negra
    listCasillas [33] = ["negra",-1,12, -1]
    listCasillas [34] = ["negra",31,4, -1]
    listCasillas [35] = c_blanca
    listCasillas [36] = c_blanca
    listCasillas [37] = c_blanca
    listCasillas [38] = ["negra",-1,3, -1]
    listCasillas [39] = c_negra
    listCasillas [40] = ["negra",6,-1, -1]
    listCasillas [41] = c_blanca
    listCasillas [42] = c_blanca
    listCasillas [43] = c_blanca
    listCasillas [44] = ["negra",4,-1, -1]
    listCasillas [45] = c_blanca
    listCasillas [46] = c_blanca
    listCasillas [47] = c_negra
    listCasillas [48] = ["negra",16,-1, -1]
    listCasillas [49] = c_blanca
    listCasillas [50] = c_blanca
    listCasillas [51] = c_blanca
    listCasillas [52] = ["negra",3,-1, -1]
    listCasillas [53] = c_blanca
    listCasillas [54] = c_blanca
    listCasillas [55] = c_negra
    listCasillas [56] = c_negra
    listCasillas [57] = c_negra
    listCasillas [58] = c_negra
    listCasillas [59] = c_negra
    listCasillas [60] = c_negra
    listCasillas [61] = c_negra
    listCasillas [62] = c_negra
    listCasillas [63] = c_negra
    tablero = []
    cont = 0
    for i in range(0,fila):
        temp = []
        for j in range(0,columna):
            temp.append(listCasillas[cont])
            cont +=1
        tablero.append(temp)
    funcPrincipal(tablero,listCasillas)
    
    #accesarTablero(tablero)
def funcPrincipal(tablero,listCasillas):
    aux_tablero = []
    for i in range(0,len(tablero)):
        contB = 0 #cuantos son por fila blancos
        indice = 0 #guardas la posicion negro
        valorFila = 0
        listaPoda = []
        for j in range(0,len(tablero[0])):
            if(tablero[i][j][0] == "negra"):
                if(j < len(tablero[0])-1):
                    valorFila = tablero[i][j][1]
            else:
                valorColumna = getSuma(tablero,i,j)
                listaPoda = poda(tablero[i][j],valorFila,valorColumna)
                aux_tablero.append([listaPoda,i,j])#posicion del tablero y los posibles
    backTracking(aux_tablero,tablero)
                    

def getSuma(tablero,i,j):
    while(i >= 0 ):
        if(tablero[i][j][0] == "negra"):
            return tablero[i][j][2]#valor de columna
        i-=1


def poda(posicion, debeSumarF, debeSumarC):
        l_posiblesF = crearListaPosibles(debeSumarF)
        conj_posiblesF = set(l_posiblesF)
        
        l_posiblesC = crearListaPosibles(debeSumarC)
        conj_posiblesC = set(l_posiblesC)
        
        interConj = conj_posiblesF.intersection(conj_posiblesC)
        listInterConj = list(interConj)
        return listInterConj
                
    #llamar backTrking

#func recursiva para acceder a los datos de subLista
def accesarTablero(tablero):
    for posicion in tablero:
        if isinstance(posicion, list):
            accesarTablero(posicion)
        else:
            print("\n\t","|",posicion,"|")
    
def crearListaPosibles(rango):
    if(rango > 0):
        lista = []
        num = 1
        while(num <= rango-1 and num <= 9):
            lista.append(num)
            num += 1
        return lista

#esta en mi funcion para recorrer el tablero, tengo que moverme por las casillas blancas
def evaluar(tablero):
    print("entra al metodo")
    blancas = []
    copia = tablero[:]
    while(copia != []):
        print("ddd",copia[0][0])
        if(copia[0][0] == 'negra'):
            debeSumarF = copia[0][1]
            debeSumarC = copia[0][2]
            print("nnnn",debeSumarF)
            print("rrrrr",debeSumarC)
        if(copia[0][0] == "blanco"):
            blancas = blancas.apped(copia[0])
        del copia[0]
    print("bakncas",blancas)
    return(blancas)
    
def backTracking(aux_tablero,tablero):
    fila = len(tablero)
    #print(aux_tablero)
    combinacionesF = []
    i = 0
    while(i < len(aux_tablero)):
        listaBlancas = []
        a = aux_tablero[i]
        listaBlancas.append(aux_tablero[i][0]) #lista posibles para la suma de esa fila
        indice = aux_tablero[i][2] # posicion
        p = i+1
        while (p < len(aux_tablero)):
            a = aux_tablero[p]
            if(aux_tablero[p][2] == indice+1 and aux_tablero[p][1] == aux_tablero[i][1] ): #se agrrega si esta en misma fila y misma columna
                a = aux_tablero[i][0]
                listaBlancas.append(aux_tablero[i][0])#sigue agregando blancas que esten juntas
                indice+=1
            else:
                break
            p += 1

        #print(listaBlancas)
        combinacionesF.append(productoCartesiano(listaBlancas))#resultado de combinaciones posibles para fila 
        i = p #avanzar a siguiente lista de blancas
    return combinacionesF

#resolver cuando se borran
# matriz blanca queden valores que no se repitan en una tupla
def productoCartesiano(matrizBlancas):
    #print("entra a producCartesiano")
    listaR = []
    for element in itertools.product(*matrizBlancas):
        listaR.append(element)
    print(listaR)
    for i in range(len(listaR)):
        flag
        for j in range(len(listaR[0])):
            p = len(listaR[0])
            k = j+1
            
            while(k < p ):
                if(listaR[i][j] == listaR[i][k]):
                    listaR.remove(listaR[i])
                    break
        
    return listaR


#bkt inseta valores de matriz blanca 



'''           
def backTracking(prueba, pp,suma,casillaActual):
    if(casillaActual == -0):
        return
    resulta = []
    copia = pp[:]
    while copia != []:
        print("prueba[0]: ",prueba[0],"copia[0]: ",copia[0])
        print("suma",prueba[0] + copia[0])
        if(prueba[0] + copia[0] == suma):
            resulta.append(prueba[0])
            resulta.append(copia[0])
            return resulta
        else:
            del copia[0]
    del prueba[0]
    return backTracking(prueba, pp,suma,casillaActual-1)
'''
#partiendo del hecho de que tengo la union de mis tres casiilas(le paso pisibles y can casillas y la suma de la fila)
def conjuntoPotencia():
    posibles = [1,2,3,4,5,6,7,8,9]#union
    cantCasillas = 3
    sumaF = 13
    comb = list(combinations(posibles, cantCasillas))
    evaluarConjunto(comb, sumaF)


def evaluarConjunto(comb, sumaF):
    cont = 0
    lista = []   
    for i in comb:
        if isinstance(i,tuple):
            evaluarConjunto(i,sumaF)
        else:
                lista.append(i)
    validarSuma(lista, sumaF)

#validar los conjuntos que suman la suma que indica la llave, y asi permitar lo minimo posible
def validarSuma(lista, sumaF):
    resulta = []
    if lista != []:
        if(lista[0] + lista[1] + lista[2] == sumaF):
            resulta.append(lista)
            print("resulta: ", resulta)
            permutarConjunto(resulta)
            return resulta
    #print("resulta: ", resulta)
            
listaPosibles = []
def permutarConjunto(lista):
    global listaPosibles
    if(lista !=[]):
        per = list(permutations(lista[0]))
        listaPosibles.append(per)
    imprimir(listaPosibles)
    
def imprimir(listaPosibles):
    for i in listaPosibles:
        print(i)   


crearTablero(8,8)


                
                
            
    
    
        
        
'''
Kakuros implementado con clases

#celda = {'celdaNegra' : {'color' : 'negro', 'sumaF' : 'none', 'sumaC':'none'},'celdaBlanca':{'color' : 'blanco', 'valor' : '0' } }

tablero =[0,1,2,3,4,5,6,7,
          8,9,10,11,12,13,
          14,15,16,17,18,
          19,20,21,22,23,
          24,25,26,27,28,
          29,30,31,32,33,
          34,35,36,37,38,
          39,40,41,42,43,
          44,45,46,47,48,
          49,50,51,52,53,
          54,55,56,57,58,
          59,60,61,62,63]


class Celda:
    def __init__(self, color, sumaF , sumaC, valor):
        self.color = color
        self.sumaF = sumaF
        self.sumaC = sumaC
        self.valor = valor

    def getColor(self):
        return self.__color
    
    def getSumaF(self):
        return self.__sumaF
    
    def getSumaC(self):
        return self.__sumaC

    def getValor(self):
        return self.__valor

    def setColor(self,color):
        self.__color = color

    def setSumaF(sef, sumaF):
        self.__sumaF = sumaF

    def setValor(self, valor):
        self.__valor = valor
        
 
def rand():
    cont =0
    while cont<100:
        r = random.randint(1,9)
        print(r)
        cont = cont + 1
  
def kakuro(tablero):
<<<<<<< HEAD
    c_negra = Celda("negra","none","none","none")
    c_blanca = Celda("blanca","none","none",0)
=======
    c_negra = Celda("negra",None,None,None)
    c_blanca = Celda("blanca",None,None,0)
    
>>>>>>> develop
    tablero [0] = c_negra
    tablero [1] = Celda("negra",None,3, None)
    tablero [2] = Celda("negra",None,20, None) 
    tablero [3] = Celda("negra",None,None, None)   
    tablero [4] = Celda("negra",None,10, None)
    tablero [5] = Celda("negra",None,12, None)
    tablero [6] = Celda("negra",None,3, None)
    tablero [7] = c_negra
    tablero [8] = Celda("negra", 9, None, None)
    tablero [9] = c_blanca
    tablero [10] = c_blanca
    tablero [11] = Celda("negra",13,None, None)
    tablero [12] = c_blanca
    tablero [13] = c_blanca
    tablero [14] = c_blanca
    tablero [15] = c_negra
    tablero [16] = Celda("negra",11,None, None)
    tablero [17] = c_blanca
    tablero [18] = c_blanca
    tablero [19] = Celda("negra",6,15, None)
    tablero [20] = c_blanca
    tablero [21] = c_blanca
    tablero [22] = c_blanca
    tablero [23] = c_negra
    tablero [24] = c_negra
    tablero [25] = Celda("negra",6,None, None)
    tablero [26] = c_blanca
    tablero [27] = c_blanca
    tablero [28] = c_blanca
    tablero [29] = Celda("negra",None,13, None)
    tablero [30] = c_negra
    tablero [31] = c_negra
    tablero [32] = c_negra
    tablero [33] = Celda("negra",None,12, None)
    tablero [34] = Celda("negra",31,4, None)
    tablero [35] = c_blanca
    tablero [36] = c_blanca
    tablero [37] = c_blanca
    tablero [38] = Celda("negra",None,3, None)
    tablero [39] = c_negra
    tablero [40] = Celda("negra",6,None, None)
    tablero [41] = c_blanca
    tablero [42] = c_blanca
    tablero [43] = c_blanca
    tablero [44] = Celda("negra",4,None, None)
    tablero [45] = c_blanca
    tablero [46] = c_blanca
    tablero [47] = c_negra
    tablero [48] = Celda("negra",16,None, None)
    tablero [49] = c_blanca
    tablero [50] = c_blanca
    tablero [51] = c_blanca
    tablero [52] = Celda("negra",3,None, None)
    tablero [53] = c_blanca
    tablero [54] = c_blanca
    tablero [55] = c_negra
    tablero [56] = c_negra
    tablero [57] = c_negra
    tablero [58] = c_negra
    tablero [59] = c_negra
    tablero [60] = c_negra
    tablero [61] = c_negra
    tablero [62] = c_negra
    tablero [63] = c_negra
<<<<<<< HEAD
    print tablero
=======
    print (tablero)
    
    
>>>>>>> develop
    
    print ("Color tablero en posicion 1: " + str(tablero[1].color))
    

<<<<<<< HEAD
    
def imprimirKakuro(tablero):
    cont = 0
    for i in tablero:
        for j in i:
            ptint (tablero)
            
    
   
=======
      
>>>>>>> develop
def recorrerTablero(tablero):
    print("recorrer tablero entra")
    casillaJuego = 9
    posi_actual = tablero[casillaJuego]
    print("posiiocn actuar: " + str(posi_actual))
    posi_llaveF = tablero[casillaJuego - 1]
    print("posi:llaveF: " + str(posi_llaveF))
    posi_llaveC = tablero[casillaJuego - 6]
    print("posi:llaveC: " + str(posi_llaveC))
    debeSumarF = posi_llaveF.sumaF
    debeSumarC = posi_llaveC.sumaC
    #llega a una casilla blanca entonces llama a poda
    #mandarle celdas negras con claves
    poda(posi_actual, debeSumarF, debeSumarC)

    #llamar a poda


def poda(posicion, debeSumarF, debeSumarC):
    valores = set('123456789')
    print("debeSumarf: " +str(debeSumarF))
    print("debeSumarC: " +str(debeSumarC))
    
    if(str(debeSumarF)!= 'none'):
        print("validacion: " + str(debeSumarF))
        lis_posiblesF = crearListaPosibles(debeSumarF)
        print("lista: " + str(lis_posiblesF))
        conj_posiblesF = set(l_posiblesF)
        print("conjuntos: " + str(conj_posiblesF))
        
    if(str(debeSumarC)!= 'none'):
        print("validacionbu: " + str(debeSumarC))
        lis_posiblesC = crearListaPosibles(debeSumarC)
        conj_posiblesC = set(l_posiblesC)
    else:
        print("hol2")
    
    #llamar backTrking

    
def crearListaPosibles(rango):
    print("rango" + str(rango))
    if(rango != 'none'):
        lista = []
        num = 1
        while(num <= rango):
            lista = lista.append(num)
            num += 1
            print (lista)
        return lista
    else:
        print("hola")



def backTracking(prueba, pp):
    resulta = []
    copia = pp
    suma = 9
    while copia != []:
        if(prueba[0] + pp[0] == suma):
            resulta.append(prueba[0])
            resulta.append(pp[0])
            #resulta = resulta[copia[0], pp[0]]
            print("resulta suma: " + str(resulta))
            return resulta
        else:
            del copia[0]
            print("lista recortada: " + str(copia))
    del prueba[0]
    return backTracking(prueba, pp)


    


    
    
    

def draw():
    s = "4"
    s2 = "5"
    x,y = 0,0 
    for fila in grid:
        for columna in fila:
            rect(x, y, w, w)
            fill(0, 102, 153)
            textSize(10);
            textAlign(RIGHT, TOP);
            text(s,x,y);
            textAlign(LEFT, BOTTOM);
            text(s2,x,y);
            fill(50)#celeste
            x = x + w
        y = y + w
        x = 0
           
'''

'''
#partiendo del hecho de que tengo la union de mis tres casiilas(le paso pisibles y can casillas y la suma de la fila)
def conjuntoPotencia(sumaF_1, sumaF_2):
    posibles = [1,2,3,4,5,6,7,8,9]#union
    cantCasillas = 3
    comb = list(combinations(posibles, cantCasillas))
    evaluarConjunto(comb, sumaF_1, sumaF_2)


def evaluarConjunto(comb, sumaF_1, sumaF_2):
    cont = 0
    lista_1 = []
    lista_2 = [] 
    for i in comb:
        if isinstance(i,tuple):
            evaluarConjunto(i,sumaF_1, sumaF_2)
        else:
                lista_1.append(i)
                lista_2.append(i)
    #print("lista_1: ",lista_1)
    #print("lista_2: ",lista_2)
                
    validarSuma(lista_1, lista_2, sumaF_1, sumaF_2)

#validar los conjuntos que suman la suma que indica la llave, y asi permitar lo minimo posible
resulta_1 = []
resulta_2 = []
def validarSuma(lista_1, lista_2, sumaF_1, sumaF_2):
    global resulta_1, resulta_2
    if lista_1 != []:
        if(lista_1[0] + lista_1[1] + lista_1[2] == sumaF_1):
            resulta_1.append(lista_1)
    if lista_2 != []:
        if(lista_2[0] + lista_2[1] + lista_2[2] == sumaF_2):
            resulta_2.append(lista_2)
    permutarConjunto(resulta_1, resulta_2)
    
listaPosibles_1 = []
listaPosibles_2 = []   
def permutarConjunto(lista_1, lista_2):
    global listaPosibles_1, listaPosibles_2
    if(lista_1 !=[]):
        per_1 = list(permutations(lista_1[0]))
        listaPosibles_1.append(per_1)
    if(lista_2 !=[]):
        per_2 = list(permutations(lista_2[0]))
        listaPosibles_2.append(per_2)
        
    productoCartesiano(listaPosibles_1, listaPosibles_2)
    

def productoCartesiano(listaPosibles_1, listaPosibles_2):
    print(listaPosibles_1)
    print(listaPosibles_2)
    #http://elclubdelautodidacta.es/wp/2013/05/python-el-producto-cartesiano/
    return([(k,n)for i in listaPosibles_1 for j in listaPosibles_2 for k in i for n in j])
'''
'''
from math import factorial
from itertools import combinations, permutations

def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c):
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)

def combinaciones(c, n):
    """Calcula y devuelve una lista con todas las
       combinaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return [s for s in potencia(c) if len(s) == n]

def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]


def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])

def permutaciones(c, n):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return sum([permuta(s)
                for s in combinaciones(c, n)],
               [])
listaR_1 = []
listaR_2 = []
def prueba(sumaF_1, sumaF_2):
    lista = permutaciones([1,2,3,4,5,6,7,8,9],3)
    for i in lista:
        validarSuma(i, sumaF_1, sumaF_2)
        
def validarSuma(valor, sumaF_1, sumaF_2):
    print("valor", valor)
    global listaR_1,listaR_2
    if(valor [0]+ valor[1] + valor[2] == sumaF_1):
        listaR_1.append(valor)
    if(valor [0]+ valor[1] + valor[2] == sumaF_2):
        listaR_2.append(valor)

def camila(listaR_1, listaR_2):
    print("lista del 13: ",listaR_1,"\n")
    print("lista del 6: ",listaR_2,"\n")

'''
'''
ESTA
from math import factorial
from itertools import combinations, permutations

def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c):
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)

def combinaciones(c, n):
    """Calcula y devuelve una lista con todas las
       combinaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return [s for s in potencia(c) if len(s) == n]

def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]


def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])

def permutaciones(c, n):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return sum([permuta(s)
                for s in combinaciones(c, n)],
              [])



'''

'''
#listas para producto cartesiano
listaR_1 = []
listaR_2 = []

def conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas):
    lista = permutaciones(unionConj,celdas)
    for i in lista:
        validarSuma(i, sumaF_1, sumaF_2,celdas)
        
def validarSuma(valor, sumaF_1, sumaF_2,celdas):
    global listaR_1,listaR_2
    if(celdas == 3):
        if(valor [0]+ valor[1] + valor[2] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 4):
        if(valor [0]+ valor[1] + valor[2] + valor[3] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 5):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4]== sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 6):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 7):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6]== sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 8):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] + valor[7] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] + valor[7] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 9):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] + valor[7] + valor[8] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] + valor[7] + valor[8] == sumaF_2):
            listaR_2.append(valor)
    
pCartesiano = []
def productoCartesiano(listaR_1, listaR_2):
    global pCartesiano
    pCartesiano = [(i,j)for i in listaR_1 for j in listaR_2]
    
  

    print (pCartesiano[0])
    print (pCartesiano[1])
    print (pCartesiano[2])
    print (pCartesiano[3])
 
def ver(pCartesiano):
        for i in pCartesiano:
            print(i)
            
                

def camila(listaR_1, listaR_2):
    print("lista del 13: ",listaR_1,"\n")
    print("lista del 6: ",listaR_2,"\n")
    del listaR_1[0]
    del listaR_2[0]
    print("lista del 13: ",listaR_1,"\n")
    print("lista del 6: ",listaR_2,"\n")
'''
'''
from math import factorial
from itertools import combinations, permutations

def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c):
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)

def combinaciones(c, n):
    """Calcula y devuelve una lista con todas las
       combinaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return [s for s in potencia(c) if len(s) == n]

def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]


def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])

def permutaciones(c, n):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return sum([permuta(s)
                for s in combinaciones(c, n)],
              [])



'''

'''
#listas para producto cartesiano
listaR_1 = []
listaR_2 = []

def conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas):
    lista = permutaciones(unionConj,celdas)
    for i in lista:
        validarSuma(i, sumaF_1, sumaF_2,celdas)
        
def validarSuma(valor, sumaF_1, sumaF_2,celdas):
    global listaR_1,listaR_2
    if(celdas == 3):
        if(valor [0]+ valor[1] + valor[2] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 4):
        if(valor [0]+ valor[1] + valor[2] + valor[3] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 5):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4]== sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 6):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 7):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6]== sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 8):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] + valor[7] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] + valor[7] == sumaF_2):
            listaR_2.append(valor)
    if(celdas == 9):
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] + valor[7] + valor[8] == sumaF_1):
            listaR_1.append(valor)
        if(valor [0]+ valor[1] + valor[2] + valor[3] + valor[4] + valor[5] + valor[6] + valor[7] + valor[8] == sumaF_2):
            listaR_2.append(valor)
    
pCartesiano = []
def productoCartesiano(listaR_1, listaR_2):
    global pCartesiano
    pCartesiano = [(i,j)for i in listaR_1 for j in listaR_2]
    
'''        
  
'''
def ver(pCartesiano):
        for i in pCartesiano:
            print(i)
            
                
#me dice cuantas casillas blancas hay que llenar
#se lo pasa la funcion del recorrido
def cantCasilla(sumaF_1, sumaF_2, unionConj, celdas,col_1,col_2, col_3,col_4,col_5,col_6, col_7,col_8, col_9):
    if (celdas == 2):
        conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas)
        print(listaR_1)
        print(listaR_2)
        productoCartesiano(listaR_1, listaR_2)
        print(pCartesiano)
        BKT(pCartesiano,celdas,col_1,col_2, col_3,col_4,col_5,col_6, col_7,col_8, col_9)
    if (celdas == 3):
        conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas)
        print(listaR_1)
        print(listaR_2)
        productoCartesiano(listaR_1, listaR_2)
        BKT(pCartesiano,celdas,col_1,col_2, col_3,col_4,col_5,col_6, col_7,col_8, col_9)
    if (celdas == 4):
        conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas)
        print(listaR_1)
        print(listaR_2)
        productoCartesiano(listaR_1, listaR_2)
        BKT(pCartesiano)
    if (celdas == 5):
        conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas)
        print(listaR_1)
        print(listaR_2)
        productoCartesiano(listaR_1, listaR_2)
        BKT(pCartesiano)
    if (celdas == 6):
        conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas)
        print(listaR_1)
        print(listaR_2)
        productoCartesiano(listaR_1, listaR_2)
        BKT(pCartesiano)
    if (celdas == 7):
        conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas)
        print(listaR_1)
        print(listaR_2)
        productoCartesiano(listaR_1, listaR_2)
        BKT(pCartesiano)
    if (celdas == 8):
        conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas)
        print(listaR_1)
        print(listaR_2)
        productoCartesiano(listaR_1, listaR_2)
        BKT(pCartesiano)
    if (celdas == 9):
        conjuntoPosible(sumaF_1, sumaF_2, unionConj, celdas)
        print(listaR_1)
        print(listaR_2)
        productoCartesiano(listaR_1, listaR_2)
        BKT(pCartesiano)
        

def BKT(pCartesiano,celdas,col_1,col_2, col_3,col_4,col_5,col_6, col_7,col_8, col_9):
    resulta = []
    copia = pCartesiano
    while copia != []:
        s = suma(copia[0],celdas,col_1,col_2, col_3,col_4,col_5,col_6, col_7,col_8, col_9)
        if(s != []):
            resulta.append(s)
            print("suma valida")
            return(resulta)
        else:
            del copia[0]
    #del pCartesiano[0]
    #return (pCartesiano,celdas,col_1,col_2, col_3,col_4,col_5,col_6, col_7,col_8, col_9)
    
            
   
#la carnita de esto
def suma(producCartesiano,celdas,col_1,col_2, col_3,col_4,col_5,col_6, col_7,col_8, col_9):
    resulta = []
    if(celdas == 2):
        lis1 = producCartesiano[0]
        lis2 = producCartesiano[1]
        if(lis1[0] + lis2[0] == col_1 &
           lis1[1] + lis2[1] == col_2):
            resulta.append(lis1)
            resulta.append(lis2)
            print(resulta)
            return (resulta)
        else:
            print("esta no era la suma")
            return ([])
    if(celdas == 3):
        lis1 = producCartesiano[0]
        lis2 = producCartesiano[1]

        print("lista1",lis1)
        print ("lista2",lis2)
        print("col1:" ,lis1[0] + lis2[0],"=",col_1)
        print("col2:" ,lis1[1] + lis2[1],"=",col_2)
        print("col3:" ,lis1[2] + lis2[2],"=",col_3)
        if(lis1[0] + lis2[0] == col_1 & lis1[1] + lis2[1] == col_2 & lis1[2] + lis2[2] == col_3 ):
            resulta.append(lis1)
            resulta.append(lis2)
            print("resp correcta",resulta)
            return (resulta)
        else:
            print("esta no era la suma")
            return ([])

    if(celdas == 4):
        lis1 = producCartesiano[0]
        lis2 = producCartesiano[1]
        if(lis1[0] + lis2[0] == col_1 &
           lis1[1] + lis2[1] == col_2 &
           lis1[2] + lis2[2] == col_3 &
           lis1[3] + lis2[3] == col_4):
            resulta.append(lis1)
            resulta.append(lis2)
            print(resulta)

    if(celdas == 5):
    if(celdas == 6):
    if(celdas == 7):
    if(celdas == 8):
    if(celdas == 9):
    
    
    
    
    
    






    
def camila(listaR_1, listaR_2):
    print("lista del 13: ",listaR_1,"\n")
    print("lista del 6: ",listaR_2,"\n")
    del listaR_1[0]
    del listaR_2[0]
    print("lista del 13: ",listaR_1,"\n")
    print("lista del 6: ",listaR_2,"\n")

 


    

            
            


http://edupython.blogspot.com/2016/06/potenciando-conjuntos.html

producto_1=[]
producto_2=[]

 #partiendo del hecho de que tengo la union de mis tres casiilas(le paso pisibles y can casillas y la suma de la fila)
def conjuntoPotencia(sumaF):
    posibles = [1,2,3,4,5,6,7,8,9]#union
    cantCasillas = 3
    #sumaF = 13
    comb = list(combinations(posibles, cantCasillas))
    evaluarConjunto(comb, sumaF)


def evaluarConjunto(comb, sumaF):
    cont = 0
    lista = []   
    for i in comb:
        if isinstance(i,tuple):
            evaluarConjunto(i,sumaF)
        else:
                lista.append(i)
    validarSuma(lista, sumaF)

#validar los conjuntos que suman la suma que indica la llave, y asi permitar lo minimo posible
def validarSuma(lista, sumaF):
    resulta = []
    if lista != []:
        if(lista[0] + lista[1] + lista[2] == sumaF):
            resulta.append(lista)
            permutarConjunto(resulta)
            return resulta
            

def permutarConjunto(lista):
    listaPosibles = []
    if(lista !=[]):
        per = list(permutations(lista[0]))
        listaPosibles.append(per)
        print(listaPosibles)
    imprimir(listaPosibles)

       
    #imprimir(listaPosibles)
    #while(listaPosibles != []):
        

def imprimir(listaPosibles):
    listaR = []
    for i in listaPosibles:
        listaR.append(i)
    print("print",listaR)
    print("posi0",listaR[0])
    print("posi0",listaR[1])
    
    
 
#obtener combinaciones y permutar sobre esas combinaciones 


formula de combinaciones
mCn = m! / n!(m-n)!



def numero_combinaciones(m,n):
    return factorial(m)//(factorial(n)*factorial(m-n))

'''



