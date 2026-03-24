def resolve_lab(self) -> None:
        queue = deque()
        queue.append((self.entry_x, self.entry_y))
        visited = {(self.entry_x, self.entry_y)}
        parent = {}
        while queue:
            x, y = queue.popleft()
            if (x, y) == [self.exit_x, self.exit_y]:
                break
            for dir, nx, ny in self.neighbor(x, y, "resolve_lab"):
                if (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)

        path = []
        current = (self.exit_x, self.exit_y)
        while current != (self.entry_x, self.entry_y):
            x, y = current
            path.append(current)
            current = parent[current]

        path.append((self.entry_x, self.entry_y))
        path.reverse()
        self.output_maze(path)
        for x, y in path:
            self.grid[y][x].resolved = True
            self.clear_screen()
            self.display()
            time.sleep(0.1)