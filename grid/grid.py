from typing import List, Tuple, Set


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
        if not self.is_valid(start) or not self.is_valid(end):
            raise ValueError("Start and end must be valid coordinates")

        visited = set()
        path = []
        self._depth_first_search(start, end, visited, path)

        return path

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) != abs(j) and self.is_valid((position[0] + i, position[1] + j)):
                    neighbors.append((position[0] + i, position[1] + j))

        return neighbors

    def _depth_first_search(self, start: Tuple[int, int], end: Tuple[int, int], visited: Set, path: List[Tuple[int, int]]) -> bool:
        if start == end:
            return True

        visited.add(start)
        path.append(start)

        for neighbor in self.get_neighbors(start):
            if neighbor not in visited and self._depth_first_search(neighbor, end, visited, path):
                return True

        path.pop()
        return False
