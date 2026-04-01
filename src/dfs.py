import random
from typing import Optional
from src.maze_class import MyLaby
# from src.display import display, clear_screen
# import time


class DfsLab(MyLaby):

    # def maze_creator(self) -> None:
    #     stack = [(self.entry_x, self.entry_y)]
    #     self.grid[self.entry_y][self.entry_x].visited = True
    #     while stack:
    #         current_x, current_y = stack[-1]
    #         free_neighbors = self.neighbor(current_x, current_y, "create")
    #         if free_neighbors:
    #             random.shuffle(free_neighbors)
    #             direction, nx, ny = free_neighbors[0]
    #             self.grid[ny][nx].visited = True
    #             if not self.grid[current_y][current_x].ft:
    #                 self.open_wall(current_x, current_y, direction, nx, ny)
    #                 stack.append((nx, ny))
    #         else:
    #             stack.pop()
    def maze_creator(self, current_x: Optional[int] = None,
                     current_y: Optional[int] = None) -> None:

        # initialisation lors du 1er appel
        if current_x is None or current_y is None:
            current_x, current_y = self.entry_x, self.entry_y
        # marquage de la case visitee et current
        self.grid[current_y][current_x].visited = True
        self.grid[current_y][current_x].current = True
        # recherche des voisins dispo
        free_neighbors = self.neighbor(current_x, current_y, "create")
        random.shuffle(free_neighbors)
        # animation du labyrinthe
        # clear_screen()
        # display(self, colour)
        # time.sleep(0.1)
        # deplacement vers un voisin dispo
        for direction, nx, ny in free_neighbors:
            if not self.grid[ny][nx].visited:
                if not self.grid[current_y][current_x].ft:
                    self.open_wall(current_x, current_y, direction, nx, ny)
                    self.maze_creator(nx, ny)
