from src.display import display, clear_screen
from src.resolved_lab import resolve_lab
from src.config import MyBaseConfig
from src.maze_class import MyLaby


class UserMenu():
    def __init__(self, config: MyBaseConfig) -> None:
        self.config = config

    def generate_maze(self, colour: list, algo: int) -> MyLaby:
        from src.dfs import DfsLab
        from src.blobby_rsa import BlobbyLab
        from src.imperfect import imperfect_maze

        # algo dfs utilise
        if algo == 0:
            lab = DfsLab(self.config)
            lab.case_ft()

        # algo blobby utilise
        elif algo == 1:
            lab = BlobbyLab(self.config)
            lab.case_ft()
            lab.ext_walls()

        lab.maze_creator(colour)
        display(lab, colour)
        if not self.config.PERFECT:
            imperfect_maze(lab)
        clear_screen()
        display(lab, colour)

        lab.output_maze()
        return lab

    def display_menu(self):
        print("\n=== A-Maze-ing Menu ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Change maze wall colours")
        print("4. Change algorithm")
        print("5. Quit")

    def re_generate(self, colour: list, algo: int) -> MyLaby:
        clear_screen()
        lab = self.generate_maze(colour, algo)
        return lab

    def show_hide(self, lab: MyLaby, i: int, colour: list) -> int:
        import time
        # if i % 2 != 0:
        path = resolve_lab(lab, colour)
        for x, y in path:
            lab.grid[y][x].resolved = False
            clear_screen()
            display(lab, colour)
            time.sleep(0.05)
        # else:
        #     resolve_lab(lab, colour, i)
        # i += 1
        # return i

    def colour_change(self, lab: MyLaby, colour_list: dict, c: int) -> int:
        colour_choice = ["normal", "darker", "purple", "blue", "red"]
        colour = colour_list.get(colour_choice[c])
        clear_screen()
        display(lab, colour)
        return colour

    def algo_change(self, algo: int, colour: list) -> int:
        algo += 1
        if algo == 2:
            algo = 0
        if algo == 0:
            clear_screen()
            self.generate_maze(colour, algo)
            print("\nChanged algorithm to dfs")
        elif algo == 1:
            clear_screen()
            self.generate_maze(colour, algo)
            print("\nChanged algorithm to blobby")
        return algo
