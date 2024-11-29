class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def set_cell(self, x, y, state):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = state

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return 0

    def is_alive(self, x, y):
        return self.get_cell(x, y) > 0

    def set_seed(self, seed, x_offset, y_offset):
        for y, row in enumerate(seed):
            for x, cell in enumerate(row):
                self.set_cell(x + x_offset, y + y_offset, cell)

    def count_neighbors(self, x, y):
        neighbors = [
            (-1, -1), (0, -1), (1, -1),
            (-1,  0),         (1,  0),
            (-1,  1), (0,  1), (1,  1),
        ]
        count = 0
        for dx, dy in neighbors:
            count += self.is_alive(x + dx, y + dy)
        return count

    def next_generation(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                new_grid[y][x] = self.next_cell_state(x, y)
        self.grid = new_grid

    def next_cell_state(self, x, y):
        neighbors = self.count_neighbors(x, y)
        actual_state = self.get_cell(x, y)
        if actual_state > 0:
            if neighbors in (2, 3):
                return 1
            else:
                return -1
        else:
            if neighbors == 3:
                return 2
            else:
                return 0

    def __str__(self):
        return "\n".join("".join("O" if cell else "." for cell in row) for row in self.grid)
