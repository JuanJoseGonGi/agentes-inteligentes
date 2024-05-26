from typing import List, Tuple, Set
import heapq

class Grid:
    grid: List[List[List[any]]] = []

    def __init__(self, height, width) -> None:
        if height <= 0 or width <= 0:
            raise ValueError("Height and width must be positive integers")

        self.grid = self.build_grid(height, width)

    def build_grid(self, height, width) -> List[List[List[any]]]:
        return [[[] for _ in range(width)] for _ in range(height)]

    def is_valid_position(self, position: Tuple[int, int]) -> bool:
        return self.is_valid(position) and self.is_empty(position)

    def is_valid(self, position: Tuple[int, int]) -> bool:
        return 0 <= position[0] < len(self.grid) and 0 <= position[1] < len(self.grid[0])

    def is_empty(self, position: Tuple[int, int]) -> bool:
        return len(self.grid[position[0]][position[1]]) == 0

    def depth_first_search(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        if not self.is_valid_position(start) or not self.is_valid_position(end):
            raise ValueError("Start and end must be valid coordinates")

        visited = set()
        path = []
        self._depth_first_search(start, end, visited, path)

        return path

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) != abs(j) and self.is_valid_position((position[0] + i, position[1] + j)):
                    neighbors.append((position[0] + i, position[1] + j))

        return neighbors

    def get_orthogonal_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = []

        for i in range(-1, 2):
            if i == 0:
                continue

            if self.is_valid_position((position[0] + i, position[1])):
                neighbors.append((position[0] + i, position[1]))

            if self.is_valid_position((position[0], position[1] + i)):
                neighbors.append((position[0], position[1] + i))

        return neighbors

    def _depth_first_search(self, start: Tuple[int, int], end: Tuple[int, int], visited: Set, path: List[Tuple[int, int]]) -> bool:
        if start == end:
            return True

        visited.add(start)
        path.append(start)

        for neighbor in self.get_orthogonal_neighbors(start):
            if neighbor not in visited and self._depth_first_search(neighbor, end, visited, path):
                return True

        path.pop()
        return False
    
    def uniform_cost_search(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        if not self.is_valid_position(start) or not self.is_valid_position(end):
            raise ValueError("Start and end must be valid coordinates")
        # cola de prioridad con el nodo inicial y un costo acumulado de 0.
        frontier = [(0, start)]
        came_from = {}  # diccionario para reconstruir el camno
        cost_so_far = {start: 0}  # diccionario para rastrear los costos acumulados hasta cada nodo

        while frontier:
            _, current = heapq.heappop(frontier)  # Obtiene el nodo con el costo acumulado más bajo.
            if current == end: # Si el nodo actual es la meta, termina.
                break 

            # Expande a los hijos.
            for neighbor in self.get_orthogonal_neighbors(current):
                new_cost = cost_so_far[current] + 1  #  Costo igual para todos los arcos.

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

        # Reconstruir el camino óptimo desde 'end' hasta 'start'
        path = []
        current = end
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()  # Revertir el camino para que sea desde 'start' hasta 'end'

        return path
