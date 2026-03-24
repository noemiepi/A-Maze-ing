from maze_class import MyLaby
import random
from typing import Optional


def imperfect_maze(self: MyLaby, cx: Optional[int] = None,
                   cy: Optional[int] = None):
    if not self.perfect:
        nb = int(((self.width * self.height) * 15) / 100)
        cx, cy = self.entry_x, self.entry_y
        for i in range(nb):
            x = random.randint(1, (self.width - 1))
            y = random.randint(1, (self.height - 1))
            if x != cx and y != cy:
                cx, cy = x, y
                free_neighbors = self.neighbor(x, y, "imp")
                random.shuffle(free_neighbors)
                for direction, nx, ny in free_neighbors:
                    if not self.grid[cy][cx].ft:
                        self.open_wall(cx, cy, direction, nx, ny)
