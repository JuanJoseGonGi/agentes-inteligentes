from collections import deque

grafo = {
    "A":["B","C","D"],
    "B":["A"],
    "C":["A","D","E"],
    "D":["A","C","E"],
    "E":["D","F","C"],
    "F":["E"]
}

def mostrarRuta(tabla,entrada):
    ruta = [entrada]
    while entrada != "0":
        ruta.append(tabla[entrada])
        entrada = tabla[entrada]
    print("ruta",ruta)

#nodoI nodoInicial
#nodoF nodoFinal
def bfs(nodoI,nodoF,grafo):
    fila = deque([nodoI])
    visitados = []
    tabla = {nodoI:"0"}
    existe = False
    while fila:
        for nodo in grafo[nodoI]:
            if nodo not in visitados:
                fila.append(nodo)
                tabla[nodo] = nodoI
        if nodoI not in visitados:
            visitados.append(nodoI)
        nodoI = fila.popleft()

        if nodoI == nodoF:
            print(tabla)
            existe = True
            mostrarRuta(tabla,nodoI)
            break
    if not existe:
        print("No existe ruta")

bfs("C","E",grafo)