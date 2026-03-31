from src.display import display, clear_screen
from collections import deque
from src.maze_class import MyLaby
import time


def resolve_lab(my_lab: MyLaby, colour: list) -> list:
    queue = deque()
    queue.append((my_lab.entry_x, my_lab.entry_y))
    visited = {(my_lab.entry_x, my_lab.entry_y)}
    parent = {}
    while queue:
        x, y = queue.popleft()
        if (x, y) == [my_lab.exit_x, my_lab.exit_y]:
            break
        for dir, nx, ny in my_lab.neighbor(x, y, "resolve_lab"):
            if (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    path = []
    current = (my_lab.exit_x, my_lab.exit_y)
    while current != (my_lab.entry_x, my_lab.entry_y):
        x, y = current
        path.append(current)
        current = parent[current]

    path.append((my_lab.entry_x, my_lab.entry_y))
    path.reverse()
    my_lab.output_maze(path)
    for x, y in path:
        my_lab.grid[y][x].resolved = True
        clear_screen()
        display(my_lab, colour)
        time.sleep(0.05)
    return path
