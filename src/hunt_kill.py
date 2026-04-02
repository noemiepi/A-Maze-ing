import random
from typing import Optional
from src.maze_class import MyLaby


class HuntKill(MyLaby):
    def maze_creator(self) -> None:
        current_x, current_y = self.entry_x, self.entry_y
        self.grid[current_y][current_x].visited = True
        while True:
            free_neigbhors = self.neighbor(current_x, current_y, "create")
            if free_neigbhors:
                random.shuffle(free_neigbhors)
                for direction, nx, ny in free_neigbhors:
                    if not self.grid[ny][nx].ft:
                        self.grid[ny][nx].visited = True
                        self.open_wall(current_x, current_y, direction, nx, ny)
                        current_x, current_y = nx, ny
                        break
            else:
                found = False
                print("5")
                for y in range(self.height):
                    print("6")
                    for x in range(self.width):
                        print("7")
                        if not self.grid[y][x].visited:
                            vn = self.neighbor(current_x, current_y, "hunt")
                            print(f"8 {vn}")
                            direction, vx, vy = vn[0]
                            self.open_wall(x, y, direction, vx, vy)
                            current_x, current_y = x, y
                            found = True
                            break
                    if found:
                        break
                if not found:
                    return
