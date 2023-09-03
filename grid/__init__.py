from grid import Grid

grid = Grid(5, 5)  # Crea una instancia de la clase Grid con un tablero de 5x5
start = (0, 0)     # Define la posición de inicio
end = (4, 4)       # Define la posición de destino

# Llama a la función depth_first_search para encontrar el camino desde 'start' hasta 'end'
path = grid.depth_first_search(start, end)

# Imprime el camino encontrado
print(path)

print('UCS')
grid = Grid(5, 5)  # Crea una instancia de la clase Grid con un tablero de 5x5
grid = Grid(5, 5)
start = (0, 0)
end = (4, 4)
path = grid.uniform_cost_search(start, end)
print(path)


