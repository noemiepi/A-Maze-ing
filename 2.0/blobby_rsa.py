import random
from typing import Optional
from config import MyBaseConfig
from maze_class import MyLaby, Cellule

class Cel():
    def __init__(self):
        self.north = False
        self.south = False
        self.east = False
        self.west = False
        self.visited = False
        self.ft = False
        self.current = False
        self.resolved = False
        self.full = False
        super().__init__()


class BlobbyLab(MyLaby):
    def __init__(self, config: MyBaseConfig):
        super().__init__(config)
        self.grid = [[Cel() for x in range(self.width)] 
                     for y in range(self.height)]

    def ext_walls(self):
        for y in range(self.height):
            for x in range(self.width):
                # if self.grid[y][x].ft:
                #     self.grid[y][x].north = True
                #     self.grid[y][x].south = True
                #     self.grid[y][x].west = True
                #     self.grid[y][x].east = True
                self.grid[0][x].north = True
                self.grid[self.height - 1][x].south = True
                self.grid[y][0].west = True
                self.grid[y][self.width - 1].east = True

    def maze_creator(self, current_x: Optional[int] = None,
            current_y: Optional[int] = None) -> None:
        width = self.width - 1
        height = self.height - 1
        x = random.randint(0, width)
        y = random.randint(0, height)
        c = random.choice(("x", "y"))
        if c == "y" and y not in (0, height):
            for xx in range(self.width):
                if self.grid[y][xx].full == False:
                    self.grid[y][xx].south = True
                    self.grid[y][xx].full = True
                for yy in range(y, self.height):
                    self.grid[yy][x].full = False
        elif c == "x" and x not in (0, width):
            for yy in range(self.height):
                if self.grid[yy][x].full == False:
                    self.grid[yy][x].south = True
                    self.grid[yy][x].full = True
                for xx in range(x, self.width):
                    self.grid[y][xx].full = False













        # # marquage de la case visitee et current 
        # self.grid[current_y][current_x].visited = True
        # self.grid[current_y][current_x].current = True
        # # recherche des voisins dispo
        # free_neighbors = self.neighbor(current_x, current_y, "dfs")
        # random.shuffle(free_neighbors)
        # # self.clear_screen()
        # # self.display()
        # # time.sleep(0.1)
        # # deplacement vers un voisin dispo
        # for direction, nx, ny in free_neighbors:
        #     if not self.grid[ny][nx].visited:
        #         if not self.grid[current_y][current_x].ft:
        #             self.open_wall(current_x, current_y, direction, nx, ny)
        #             self.maze_creator(nx, ny)
