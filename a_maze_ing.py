from numpy.random import randint
import matplotlib.pyplot as plt
import random


class Cellule():
    def __init__(self):
        self.north = True
        self.south = True
        self.east = True
        self.west = True
        self.visited = False


class MyLaby():

    def __init__(self, width: int, height: int, entry: list):
        self.width = width
        self.height = height
        self.x, self.y = entry
        self.grid = [[Cellule() for x in range(self.width)]
                     for y in range(self.height)]

    def neighbor(self) -> list:
        neighb = [
            ("north", self.x, self.y-1),
            ("south", self.x, self.y+1),
            ("east", self.x+1, self.y),
            ("west", self.x-1, self.y)
        ]
        return [(dir, nx, ny) for dir, nx, ny in neighb\
                if 0 <= nx < self.width and 0 <= ny < self.height\
                and not self.grid[ny][nx].visited]



    def open_wall(self, direction, nx: int, ny: int) -> None:
        opposed = {"north": "south", "south": "north", "east": "west", "west": "east"}
        setattr(self.grid[self.y][self.x], direction, False)
        setattr(self.grid[ny][nx], opposed[direction], False)


    def dfs(self, nx, ny) -> None:
        self.grid[self.y][self.x].visited = True

        free_neighbor = self.neighbor()
        random.shuffle(free_neighbor)

        for direction, nx, ny in free_neighbor:
            if not self.grid[ny][nx].visited:
                self.open_wall(direction, nx, ny)
                self.dfs(nx, ny)


    def display(self) -> None:
        for y in range(self.height):
            north_line = ""
            for x in range(self.width):
                north_line += "+"
                north_line += "=" if self.grid[y][x].north else " "
            north_line += "+"
            print(north_line)

            middle_line = ""
            for x in range(self.width):
                middle_line += "|" if self.grid[y][x].west else " "
                middle_line += " "
            middle_line += "|"
            print(middle_line)
        print("+" + "=+" * self.width)
