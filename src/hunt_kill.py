import random
from typing import Optional
from src.maze_class import MyLaby


class HuntKill(MyLaby):
    def maze_creator(self) -> None:
        stack = [(self.entry_x, self.entry_y)]
        self.grid[self.entry_y][self.entry_x].visited = True
        while stack:
            current_x, current_y = stack[-1]
            free_neighbors = self.neighbor(current_x, current_y, "create")
            if free_neighbors:
                random.shuffle(free_neighbors)
                direction, nx, ny = free_neighbors[0]
                self.grid[ny][nx].visited = True
                if not self.grid[current_y][current_x].ft:
                    self.open_wall(current_x, current_y, direction, nx, ny)
                    stack.append((nx, ny))
            else:
                for y in range(self.height):
                    for x in range(self.width):
                        if self.grid[y][x].visited == False:
                            stack.append((x, y))
