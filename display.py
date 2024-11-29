import tkinter as tk

colors = {
    -1: "gray20",
    0: "black",
    1: "snow",
    2: "white"
}

class Display:
    def __init__(self, width, height, cell_size=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.window = tk.Tk()
        self.window.title("Game of Life Display")
        self.canvas = tk.Canvas(
            self.window,
            width=self.width * self.cell_size,
            height=self.height * self.cell_size,
            bg="black"
        )
        self.canvas.pack()

        self.cells = [
            [self.canvas.create_rectangle(
                x * self.cell_size, y * self.cell_size,
                (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                fill="black",
                outline=""
            ) for x in range(self.width)]
            for y in range(self.height)
        ]


    def update(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                color = colors[grid[y][x]]
                self.canvas.itemconfig(self.cells[y][x], fill=color)

    def start(self):
        self.window.mainloop()
