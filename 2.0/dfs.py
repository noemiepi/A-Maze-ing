import random
from typing import Optional
from maze_class import MyLaby, Cellule


class DfsLab(MyLaby):

    # algorithme de creation du labyrinthe
    def maze_creator(self, current_x: Optional[int] = None,
            current_y: Optional[int] = None) -> None:

        # initialisation lors du 1er appel
        if current_x is None or current_y is None:
            current_x, current_y = self.entry_x, self.entry_y
        # marquage de la case visitee et current 
        self.grid[current_y][current_x].visited = True
        self.grid[current_y][current_x].current = True
        # recherche des voisins dispo
        free_neighbors = self.neighbor(current_x, current_y, "dfs")
        random.shuffle(free_neighbors)
        # self.clear_screen()
        # self.display()
        # time.sleep(0.1)
        # deplacement vers un voisin dispo
        for direction, nx, ny in free_neighbors:
            if not self.grid[ny][nx].visited:
                if not self.grid[current_y][current_x].ft:
                    self.open_wall(current_x, current_y, direction, nx, ny)
                    self.maze_creator(nx, ny)
