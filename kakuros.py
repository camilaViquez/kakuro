from itertools import combinations, permutations
import random
import itertools

termine=False

def crearTablero (fila,columna):
    listCasillas = []
    subLis = [0,0,0,0]
    tamano = fila * columna
    for i in range(tamano):
        listCasillas.append(subLis)
    llenarTablero(listCasillas,fila,columna)
    return(listCasillas)
    
def llenarTablero(listCasillas,fila,columna):
    c_negra = ["negra",-1,-1,0]
    c_blanca = ["blanca",-1,-1,0]

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
    listCasillas [34] = ["negra",21,4, -1]
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
                aux_tablero.append([listaPoda,i,j,valorFila,valorColumna])#posicion del tablero y posibles numero pasa suma posicion i,j y debe sumarFC
    combinaciones = listaPermutaciones(aux_tablero,tablero) #combinaciones ya esta filtrada se valida en funcSuma
    bkt = backTracking(combinaciones, aux_tablero, tablero)
    printMatriz(bkt)
    return bkt
                    

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
    
def listaPermutaciones(aux_tablero,tablero):
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
                a = aux_tablero[p][0]
                listaBlancas.append(aux_tablero[p][0])#sigue agregando blancas que esten juntas
                indice+=1
            else:
                break
            p += 1
        
        pCartesiano = productoCartesiano(listaBlancas,aux_tablero[i][3]) #enviamos lo que debe sumar en fila[3]
        combinacionesF.append(pCartesiano)#resultado de combinaciones posibles para fila 
        i = p #avanzar a siguiente lista de blancas
    return combinacionesF


#resolver cuando se borran
# matriz blanca queden valores que no se repitan en una tupla
def productoCartesiano(matrizBlancas,suma):
    listaR =auxProdCartesiano(matrizBlancas)
    i = 0
    largo = len(listaR)
    while(i < largo):
        flag = True
        for j in range(len(listaR[i])):
            p = len(listaR[i])
            k = j+1
            posibleSumar = verificarSuma(listaR[i],suma)
            if(posibleSumar):
                while(k < p ):
                    if(listaR[i][j] == listaR[i][k]):
                        listaR.remove(listaR[i])
                        largo -= 1
                        flag = False #si borro una tupla igual
                        break 
                    k+=1
            else:
                #si no sumalo que debe tambien se quita
                listaR.remove(listaR[i])
                largo -= 1
                flag = False #si borro una tupla igual
                break
            if(not flag): # para que el for no intente comparar tupla eliminada
                break
        if(flag):
            i += 1
    return listaR
def auxProdCartesiano(matriz):
    listaR = []
    for element in itertools.product(*matriz):
        listaR.append(element)
    return listaR

def verificarSuma(listaFila,suma):
    resulta = []
    sumaPrueba = 0
    for i in range(len(listaFila)):
        sumaPrueba += listaFila[i]
    if(sumaPrueba == suma):
        return True
    return False

#llega número valido por fila 
def backTracking(combinaciones,aux_tablero,tablero):
    nuevoTablero = getNewTablero(tablero)
    listaCombinaciones=auxProdCartesiano(combinaciones)
    print(listaCombinaciones[86490])
    #Evalua las combinaciones
    for i in range(0,len(listaCombinaciones)):
        nuevoTablero = getNewTablero(tablero)
        resultado = poblarTablero(nuevoTablero, listaCombinaciones[i])
        if resultado[0]:
            nuevoTablero = resultado[1]
            break
    return nuevoTablero

        
def poblarTablero(nuevoTablero,combinaciones): #combinaciones es solo los numeros que se van a usar
    cont =0  
    sumaValida=True
    #Este pobla el tablero
    for i in range(len(nuevoTablero)):
        j = 0
        while j < len(nuevoTablero[i]):
            if(nuevoTablero[i][j][1] == True and nuevoTablero[i][j][0] > -1):
                nuevoTablero = ingresarValor(nuevoTablero,combinaciones[cont],i,j)
                j += len(combinaciones[cont])
                cont+=1
            else:
                j +=1

    #Este evalua el tablero
    cont=0
    for i in range(len(nuevoTablero)):
        j = 0
        while j < len(nuevoTablero[i]):
            if(nuevoTablero[i][j][1] == True and nuevoTablero[i][j][0] > -1):
                cont+=1
                if(nuevoTablero[i-1][j][1]==False):#Evalua si el que esta arriba es una casilla negra de columna
                    esValid=sumaColumna(i,j,nuevoTablero[i-1][j][0],nuevoTablero)#Esto lo saca siempre
                if not esValid:
                    sumaValida=False
                    break
            j +=1
        if not sumaValida:
            nuevoTablero=0
            break

    result=[sumaValida,nuevoTablero]
    return result

#pone las convinaciones en en tablero, donde estan los espacios en blanco
def ingresarValor(nuevoTablero,lista,i,j):
    for n in range(len(lista)):
        nuevoTablero[i][j][0] = lista[n]
        j +=1
    return nuevoTablero

def sumaColumna(i,j,valor,nuevotablero):#i fila, j columna
    suma = 0
    for n in range(i,len(nuevotablero)):
        # si en la columna se acaban las blancas no sigue evaluando
        if(nuevotablero[n][j][1] == False):
            break
        else:
            if(nuevotablero[n][j][0] == -1):
                break
            else:
                suma += nuevotablero[n][j][0] #0 contiene el numero -1 o 0 
    if(suma == valor):
        return True
    else:
        return False

   
def getNewTablero(tablero):
    matrizEvaluada = []
    for i in range(len(tablero)):
        listaFila = []
        for j in range(len(tablero[i])):
            listaElemFila = []
            lista = tablero[i][j]
            if(lista[0] == "negra"):
                if(lista[2] > -1):
                    listaElemFila =[lista[2],False] #negra con cuma en columna
                else:
                    listaElemFila =[-1,True]# blancas, o una negra con valor en fila, o negras sin nada. Entonces es true, -1 representa todas las negras con esas caracteristicas
            else:
                listaElemFila =[0,True] #cero valor de casilla blanca
            listaFila.append(listaElemFila)
        matrizEvaluada.append(listaFila)
    return matrizEvaluada


def printMatriz(tablero):
    for i in range(0,len(tablero)):
        msj="| "
        for j in range(0,len(tablero[i])):
            if(len(str(tablero[i][j][0]))>1):
                tmp= tablero[i][j]
                msj+=str(tmp[0])+" "
            else:
                tmp= tablero[i][j]
                msj+=str(tmp[0])+"  "
        msj+=" |"
        print(msj)



def probarListas(prueba, listaFila,suma):
    resulta = []
    copia = listaFila[:]
    sumaPrueba = 0
    while copia != []:
        for i in range(len(listaFila)):
            sumaPrueba += listaFila[i]
        if(prueba[0] + copia[0] == suma):
            resulta.append(prueba[0])
            resulta.append(copia[0])
            return resulta
        else:
            del copia[0]
    del prueba[0]
    return backTracking(prueba, listaFila,suma)

crearTablero(8,8)

