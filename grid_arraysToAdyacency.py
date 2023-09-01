"""
el mundo es un mundo "grid" 2d

dado un grafo usando arrays de arrays
crea un grafo usando listas de adyacencia
para facilitar el recorrido dfs, bfs, ucs

si las celdas contienen letras es porque son un agente
si no tienen nada no hay un agente

un agente puede ser dinamico, osea que se mueve
o estatico que no cambia de posicion

si dice A es un agente si dice P es una pared

entrada = [
    [["A"],[],[],[]],
    [[],["P"],[],["A"]],
    [["A","A"],[],["A"],[]]
]

"[i j]"

son las posiciones del mundo "grid"

si hay una pared P no hay conexión con ese nodo
si hay un agente A y un campo vacio si hay conexion
si hay un agente A y otro agente si hay conexion, pero esto se puede cambiar

salida = {
    "[0 0]":["[0 1]","[1 0]"],
    "[1 0]":["[0 0]"],
    ...
}

como hay agentes dinamicos el grafo se tiene actualizar 
cada páso que un agente cambia el entorno

"""

def esPared(grafoArraysDeArrays,i,j):
    try:
        if "P" in grafoArraysDeArrays[i][j]:
            return True
        return False
    except IndexError:
        return None


def crearGrafoConListaAdyacencia(grafoArraysDeArrays):
    grafo = {}
    for i in range(len(grafoArraysDeArrays)):
        for j in range(len(grafoArraysDeArrays[0])):
            grafo[str([i,j])] = []
            #verificar si el nodo es una pared
            if esPared(grafoArraysDeArrays,i,j) == True:
                #si es una pared vaya al siguiente nodo
                continue
            else:    
                if esPared(grafoArraysDeArrays,i+1,j) != True and i+1>=0 and i+1<len(grafoArraysDeArrays):
                    grafo[str([i,j])].append(str([i+1,j]))  

                if esPared(grafoArraysDeArrays,i-1,j) != True and i-1>=0 and i-1<len(grafoArraysDeArrays):
                    grafo[str([i,j])].append(str([i-1,j])) 

                if esPared(grafoArraysDeArrays,i,j+1) != True and j+1>=0 and j+1<len(grafoArraysDeArrays[0]):
                    grafo[str([i,j])].append(str([i,j+1]))  

                if esPared(grafoArraysDeArrays,i,j-1) != True and j-1>=0 and j-1<len(grafoArraysDeArrays[0]):
                    grafo[str([i,j])].append(str([i,j-1]))   
    print(grafo)
    for k in grafo:
       print(k,grafo[k])
    return grafo
                

entrada = [
    [["A"],[],[],[]],
    [[],["P"],[],["A"]],
    [["A","A"],[],["A"],[]]
]

crearGrafoConListaAdyacencia(entrada)