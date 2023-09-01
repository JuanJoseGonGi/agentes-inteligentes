from collections import deque
from queue import PriorityQueue

graph = {
    '[0, 0]': ['[1, 0]'], 
    '[0, 1]': [], 
    '[0, 2]': ['[0, 3]'], 
    '[0, 3]': ['[1, 3]', 
    '[0, 4]', '[0, 2]'], 
    '[0, 4]': ['[0, 5]', '[0, 3]'], 
    '[0, 5]': ['[1, 5]', '[0, 4]'], 
    '[1, 0]': ['[2, 0]', '[0, 0]'], 
    '[1, 1]': [], 
    '[1, 2]': [], 
    '[1, 3]': ['[2, 3]', '[0, 3]'], 
    '[1, 4]': [], 
    '[1, 5]': ['[2, 5]', '[0, 5]'], 
    '[2, 0]': ['[3, 0]', '[1, 0]', '[2, 1]'], 
    '[2, 1]': ['[2, 2]', '[2, 0]'], 
    '[2, 2]': ['[2, 3]', '[2, 1]'], 
    '[2, 3]': ['[1, 3]', '[2, 2]'], 
    '[2, 4]': [], 
    '[2, 5]': ['[3, 5]', '[1, 5]'], 
    '[3, 0]': ['[4, 0]', '[2, 0]'], 
    '[3, 1]': [], 
    '[3, 2]': [], 
    '[3, 3]': [], 
    '[3, 4]': [], 
    '[3, 5]': ['[4, 5]', '[2, 5]'], 
    '[4, 0]': ['[3, 0]', '[4, 1]'], 
    '[4, 1]': ['[4, 2]', '[4, 0]'], 
    '[4, 2]': ['[4, 3]', '[4, 1]'], 
    '[4, 3]': ['[4, 4]', '[4, 2]'], 
    '[4, 4]': ['[4, 5]', '[4, 3]'], 
    '[4, 5]': ['[3, 5]', '[4, 4]']
}




def showRoute(table,input_data):
    ruta = [input_data]
    while input_data != "0":
        ruta.append(table[input_data])
        input_data = table[input_data]
    print("ruta",ruta)

def ucs(start_node, end_node, graph):
    # cola de prioridad con el nodo inicial y un costo acumulado de 0.
    priority_queue = PriorityQueue()
    priority_queue.put((0, start_node))
    
    # diccionario para rastrear los costos acumulados hasta cada nodo.
    table = {start_node: 0}
    
    # diccionario para rastrear los padres de cada nodo en la ruta.
    parent = {start_node: "0"}
    
    exists = False
    while not priority_queue.empty():
        # Obtiene el nodo con el costo acumulado más bajo.
        _, current_node = priority_queue.get()
        
        # Si el nodo actual es la meta, termina.
        if current_node == end_node:
            print(parent)
            exists = True
            showRoute(parent, current_node)
            break
        
        # Expande a los hijos.
        for next_node in graph[current_node]:
            new_cost = table[current_node] + 1  # Costo igual para todos los arcos.
            if next_node not in table or new_cost < table[next_node]:
                table[next_node] = new_cost
                priority_queue.put((new_cost, next_node))
                parent[next_node] = current_node
    
    if not exists:
        print("No existe ruta")

ucs("[0, 0]", "[3, 5]", graph )