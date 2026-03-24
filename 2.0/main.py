#!/usr/bin/env python3.10


from venv_verif import venv_verif
from check_dependencies import check_dependencies

if venv_verif():
        if check_dependencies():
            from dfs import DfsLab
            from maze_class import MyLaby
            from config import config_method
            from imperfect import imperfect_maze
            from blobby_rsa import BlobbyLab
            from display import display
            print("It's ready for A-Maze-ing project")
            config = config_method()
            lab2 = BlobbyLab(config)
            lab2.case_ft()
            lab2.ext_walls()
            # lab2.maze_creator()
            display(lab2)
            # lab = DfsLab(config)
            # lab.case_ft()
            # lab.maze_creator()
            # lab.display()
            # if not config.PERFECT:
            #       imperfect_maze(lab)
            # lab.display()
            # lab.output_maze()
            # lab.resolve_lab()
