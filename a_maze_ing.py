from numpy.random import randint
import matplotlib.pyplot as plt
import random
from config import MyBaseConfig
from typing import Optional
import os
import time
from collections import deque

# definition de chaque cellule du labyrinthe
class Cellule():
    def __init__(self):
        self.north = True
        self.south = True
        self.east = True
        self.west = True
        self.visited = False
        self.ft = False
        self.current = False


class MyLaby():
    #  initialisation des donnees selon le fichier config.txt
    def __init__(self, config: MyBaseConfig):
        self.width = config.WIDTH
        self.height = config.HEIGHT
        self.entry_x, self.entry_y = config.ENTRY
        self.exit_x, self.exit_y = config.EXIT
        self.grid = [[Cellule() for x in range(self.width)]
                     for y in range(self.height)]

# *****************************************************************************
# *****************************************************************************
    # recherche des voisins disponibles (.visited=False)
    def neighbor(self, current_x: int, current_y: int, func: Optional[str]
                 ) -> list:
        neighb = [
            ("north", current_x, current_y-1),
            ("south", current_x, current_y+1),
            ("east", current_x+1, current_y),
            ("west", current_x-1, current_y)
        ]
        neighbors = []
        if func == "dfs":
            for dir, nx, ny in neighb:
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    self.grid[ny][nx].current = False
                    if not self.grid[ny][nx].visited:
                        neighbors.append([dir, nx, ny])
        elif func == "resolve_lab":
            for dir, nx, ny in neighb:
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if dir == "north" and\
                        not self.grid[current_x][current_y].north:
                        neighbors.append([dir, nx, ny])
                    if dir == "south" and\
                        not self.grid[current_x][current_y].south:
                        neighbors.append([dir, nx, ny])
                    if dir == "east" and\
                        not self.grid[current_x][current_y].east:
                        neighbors.append([dir, nx, ny])
                    if dir == "west" and\
                        not self.grid[current_x][current_y].west:
                        neighbors.append([dir, nx, ny])
        return neighbors
        # return [(dir, nx, ny) for dir, nx, ny in neighb\
                # if 0 <= nx < self.width and 0 <= ny < self.height\
                # and not self.grid[ny][nx].visited]

# *****************************************************************************
# *****************************************************************************
    # ouverture des murs concordants current_case = voisin
    def open_wall(self, x: int, y: int, direction: str, nx: int,
                  ny: int) -> None:
        opposed = {"north": "south", "south": "north", "east": "west",
                   "west": "east"}
        if not self.grid[y][x].ft and not self.grid[ny][nx].ft:
            setattr(self.grid[y][x], direction, False)
            setattr(self.grid[ny][nx], opposed[direction], False)

# *****************************************************************************
# *****************************************************************************
    # nettoyage de l'ecran du terminal
    def clear_screen(self):
        os.system('clear')

# *****************************************************************************
# *****************************************************************************
    # marquage des cases pour ecrire 42
    def case_ft(self):
        if self.width >= 9 and self.height >= 9:
            start_x = (self.width - 7) // 2
            start_y = ((self.height - 6) // 2) + 1
        
        for y in range(7):
            for x in range(7):
                target_y = start_y + y
                target_x = start_x + x
                if 0 <= target_x < self.width and 0 <= target_y < self.height:
                    if target_y == start_y and target_x in\
                        (start_x + nb for nb in [0, 4, 5, 6]):
                        self.grid[target_y][target_x].ft = True
                    elif target_y == start_y + 1 and target_x in\
                        (start_x + nb for nb in [0, 2, 6]):
                        self.grid[target_y][target_x].ft = True
                    elif target_y == start_y + 2 and target_x in\
                        (start_x + nb for nb in [0, 1, 2, 4, 5, 6]):
                        self.grid[target_y][target_x].ft = True
                    elif target_y == start_y + 3 and target_x in\
                        (start_x + nb for nb in [2, 4]):
                        self.grid[target_y][target_x].ft = True
                    elif target_y == start_y + 4 and target_x in\
                        (start_x + nb for nb in [2, 4, 5, 6]):
                        self.grid[target_y][target_x].ft = True

# *****************************************************************************
# *****************************************************************************
    # fichier de sortie du labyrinthe en hexadecimale
    def output_maze(self):
        with open("output.txt", "w") as f:
            for y in range(self.height):
                for x in range(self.width):
                    cellule = self.grid[y][x]
                    value = 0
                    if not cellule.north: value += 0b0001
                    if not cellule.south: value += 0b0010
                    if not cellule.west: value += 0b0100
                    if not cellule.east: value += 0b1000
                    f.write(hex(value)[2::])
                f.write("\n")
            f.write(f"\n{self.entry_x},{self.entry_y}")
            f.write(f"\n{self.exit_x},{self.exit_y}")

# *****************************************************************************
# *****************************************************************************
    # algorithme de creation du labyrinthe
    def dfs(self, current_x: Optional[int] = None,
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
        self.clear_screen()
        self.display()
        # time.sleep(0.1)
        # deplacement vers un voisin dispo
        for direction, nx, ny in free_neighbors:
            if not self.grid[ny][nx].visited:
                if not self.grid[current_y][current_x].ft:
                    self.open_wall(current_x, current_y, direction, nx, ny)
                    self.dfs(nx, ny)

# *****************************************************************************
# *****************************************************************************
    def resolve_lab(self) -> None:
        queue = deque()
        queue.append((self.entry_x, self.entry_y))
        visited = set()
        visited.add((self.entry_x, self.entry_y))
        parent = {}
        while queue:
            x, y = queue.popleft()
            if (x, y) == [self.exit_x, self.exit_y]:
                break
            for nx, ny in self.neighbor(x, y, "resolve_lab"):
                if (nx, ny) not in visited:
                    queue.append([nx, ny])
                    visited.add([nx, ny])
                    parent[(nx, ny)] = (x, y)

        path = []
        current = (self.exit_x, self.exit_y)

        while current != (self.entry_x, self.entry_y):
            path.append(current)
            current = parent[current]
        path.append((self.entry_x, self.entry_y))
        for x, y in path.reverse():
            self.grid[y][x].current = True
            self.clear_screen()
            self.display()
            time.sleep(0.1)

# *****************************************************************************
# *****************************************************************************
    # affichage
    def display(self, new_grid: Optional[list] = None) -> None:
        grid_to_display = new_grid if new_grid is not None else self.grid
        for y in range(self.height):
            north_line = ""
            for x in range(self.width):
                north_line += "+"
                north_line += "===" if grid_to_display[y][x].north else "   "
            north_line += "+"
            print(north_line)

            middle_line = ""
            for x in range(self.width):
                middle_line += "|" if grid_to_display[y][x].west else " "
                # case 42
                if grid_to_display[y][x].ft: 
                    middle_line += "\033[1;5;36m O \033[0m"
                # point de depart
                elif x == self.entry_x and y == self.entry_y:
                    middle_line += "\033[1;32m E \033[0m"
                # point d'arrive
                elif x == self.exit_x and y == self.exit_y:
                    middle_line += "\033[1;31m S \033[0m"
                # point de presence
                elif grid_to_display[y][x].current:
                    middle_line += "\033[1;35m A \033[0m"
                    grid_to_display[y][x].current = False
                # le reste
                else:
                    middle_line += "   "
            middle_line += "|" if grid_to_display[y][self.width-1].east\
                               else " "
            print(middle_line)
        south_line = ""
        for x in range(self.width):
            south_line += "+"
            south_line += "===" if grid_to_display[self.height-1][x].south\
                                else "   "
        south_line += "+"
        print(south_line)
