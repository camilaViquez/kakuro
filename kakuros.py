import random



def crearTablero (fila,columna):
    print("hola")
    tablero = []
    subLis = [0,0,0,0]
    tamano = fila * columna
    for i in range(tamano):
        tablero.append(subLis)
    print(tablero)
    llenarTablero(tablero)


def llenarTablero(tablero):
    c_negra = ["negra",0,0,0]
    c_blanca = ["blanca",0,0,0]

    tablero [0] = c_negra
    tablero [1] = ["negra","none",3, "none"]
    tablero [2] = ["negra","none",20, "none"] 
    tablero [3] = ["negra","none","none", "none"]   
    tablero [4] = ["negra","none",10, "none"]
    tablero [5] = ["negra","none",12, "none"]
    tablero [6] = ["negra","none",3, "none"]
    tablero [7] = c_negra
    tablero [8] = ["negra", 9, "none", "none"]
    tablero [9] = c_blanca
    tablero [10] = c_blanca
    tablero [11] = ["negra",13,"none", "none"]
    tablero [12] = c_blanca
    tablero [13] = c_blanca
    tablero [14] = c_blanca
    tablero [15] = c_negra
    tablero [16] = ["negra",11,"none", "none"]
    tablero [17] = c_blanca
    tablero [18] = c_blanca
    tablero [19] = ["negra",6,15, "none"]
    tablero [20] = c_blanca
    tablero [21] = c_blanca
    tablero [22] = c_blanca
    tablero [23] = c_negra
    tablero [24] = c_negra
    tablero [25] = ["negra",6,"none", "none"]
    tablero [26] = c_blanca
    tablero [27] = c_blanca
    tablero [28] = c_blanca
    tablero [29] = ["negra","none",13, "none"]
    tablero [30] = c_negra
    tablero [31] = c_negra
    tablero [32] = c_negra
    tablero [33] = ["negra","none",12, "none"]
    tablero [34] = ["negra",31,4, "none"]
    tablero [35] = c_blanca
    tablero [36] = c_blanca
    tablero [37] = c_blanca
    tablero [38] = ["negra","none",3, "none"]
    tablero [39] = c_negra
    tablero [40] = ["negra",6,"none", "none"]
    tablero [41] = c_blanca
    tablero [42] = c_blanca
    tablero [43] = c_blanca
    tablero [44] = ["negra",4,"none", "none"]
    tablero [45] = c_blanca
    tablero [46] = c_blanca
    tablero [47] = c_negra
    tablero [48] = ["negra",16,"none", "none"]
    tablero [49] = c_blanca
    tablero [50] = c_blanca
    tablero [51] = c_blanca
    tablero [52] = ["negra",3,"none", "none"]
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
    #print(tablero)
    
    accesarTablero(tablero)


#func recursiva para acceder a los datos de subLista
def accesarTablero(tablero):
    for posicion in tablero:
        if isinstance(posicion, list):
            accesarTablero(posicion)
        else:
            print("\n\t","|",posicion,"|")

        
        
    


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



def backTraking(prueba, pp):
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
    return backTraking(prueba, pp)

            
   


    
        

                
                
            
    
    
        
        
'''     

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
    c_negra = Celda("negra","none","none","none")
    c_blanca = Celda("blanca","none","none",0)
    
    tablero [0] = c_negra
    tablero [1] = Celda("negra","none",3, "none")
    tablero [2] = Celda("negra","none",20, "none") 
    tablero [3] = Celda("negra","none","none", "none")   
    tablero [4] = Celda("negra","none",10, "none")
    tablero [5] = Celda("negra","none",12, "none")
    tablero [6] = Celda("negra","none",3, "none")
    tablero [7] = c_negra
    tablero [8] = Celda("negra", 9, "none", "none")
    tablero [9] = c_blanca
    tablero [10] = c_blanca
    tablero [11] = Celda("negra",13,"none", "none")
    tablero [12] = c_blanca
    tablero [13] = c_blanca
    tablero [14] = c_blanca
    tablero [15] = c_negra
    tablero [16] = Celda("negra",11,"none", "none")
    tablero [17] = c_blanca
    tablero [18] = c_blanca
    tablero [19] = Celda("negra",6,15, "none")
    tablero [20] = c_blanca
    tablero [21] = c_blanca
    tablero [22] = c_blanca
    tablero [23] = c_negra
    tablero [24] = c_negra
    tablero [25] = Celda("negra",6,"none", "none")
    tablero [26] = c_blanca
    tablero [27] = c_blanca
    tablero [28] = c_blanca
    tablero [29] = Celda("negra","none",13, "none")
    tablero [30] = c_negra
    tablero [31] = c_negra
    tablero [32] = c_negra
    tablero [33] = Celda("negra","none",12, "none")
    tablero [34] = Celda("negra",31,4, "none")
    tablero [35] = c_blanca
    tablero [36] = c_blanca
    tablero [37] = c_blanca
    tablero [38] = Celda("negra","none",3, "none")
    tablero [39] = c_negra
    tablero [40] = Celda("negra",6,"none", "none")
    tablero [41] = c_blanca
    tablero [42] = c_blanca
    tablero [43] = c_blanca
    tablero [44] = Celda("negra",4,"none", "none")
    tablero [45] = c_blanca
    tablero [46] = c_blanca
    tablero [47] = c_negra
    tablero [48] = Celda("negra",16,"none", "none")
    tablero [49] = c_blanca
    tablero [50] = c_blanca
    tablero [51] = c_blanca
    tablero [52] = Celda("negra",3,"none", "none")
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
    print (tablero)
    
    
    
    print ("Color tablero en posicion 1: " + str(tablero[1].color))
    

      
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



def backTraking(prueba, pp):
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
    return backTraking(prueba, pp)


    


    
    
    

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



    
