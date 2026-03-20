#!/usr/bin/env python3.10


from venv_verif import venv_verif
from check_dependencies import check_dependencies

if venv_verif():
        if check_dependencies():
            from a_maze_ing import MyLaby
            from config import config_method
            # from labyrinthe import creation
            print("It's ready for A-Maze-ing project")
            config = config_method()
            lab = MyLaby(config)
            lab.case_ft()
            lab.display()
            lab.dfs()
            lab.output_maze()
            # laby = creation(6, 5)
            # laby.solution()
