from maze.maze_class import MyLaby
import random
from typing import Optional


def imperfect_maze(my_lab: MyLaby, cx: Optional[int] = None,
                   cy: Optional[int] = None) -> None:
    if not my_lab.perfect:
        nb = int(((my_lab.width * my_lab.height) * 20) / 100)
        cx, cy = my_lab.entry_x, my_lab.entry_y
        for i in range(nb):
            x = random.randint(1, (my_lab.width - 1))
            y = random.randint(1, (my_lab.height - 1))
            if x != cx and y != cy:
                cx, cy = x, y
                free_neighbors = my_lab.neighbor(x, y, "imperfect")
                random.shuffle(free_neighbors)
                for direction, nx, ny in free_neighbors:
                    if not my_lab.grid[cy][cx].ft:
                        my_lab.grid[cy][cx].visited = False
                        my_lab.open_wall(cx, cy, direction, nx, ny)
