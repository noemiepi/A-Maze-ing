#!/usr/bin/env python3.10

from src.check_dependencies import check_dependencies
import time

if check_dependencies():
    from src.display import display, clear_screen
    from src.user_interaction import UserMenu
    print("It's ready for A-Maze-ing project")
    i = 0
    c = 1
    algo = 0
    colour_list = {"normal": [97, 96, 33, 31, 92],
                   "darker": [37, 36, 33, 31, 32],
                   "purple": [95, 96, 33, 91, 92],
                   "blue": [94, 95, 33, 91, 92],
                   "red": [91, 96, 93, 97, 92]}
    colour = colour_list.get("normal")
    while True:
        menu = UserMenu()
        if not menu.config:
            clear_screen()
            print("\033[1;31m[NOTE] The configuration has be automaticaly "
                "upgrade :\033[0m")
            for warn in menu.critical_error.errors():
                loc = warn['loc'] if warn['loc'] else "Global Error"
                print(f"\033[5;35m{loc}\033[0m")
                print(f" \033[1;31m{warn['msg']}\033[0m")
            while not menu.config:
                time.sleep(2)
                menu = UserMenu()

        else:
            lab = menu.generate_maze(colour, algo)
            menu.display_menu()
            try:
                choice = int(input("Choice? (1-5): "))
                if not 1 < choice < 6:
                    clear_screen()
                    display(lab, colour)
                    print("\nInvalid choice! Please select a number between "
                        "1 and 5")
                if choice == 1:
                    lab = menu.re_generate(colour, algo)
                    i *= 2
                elif choice == 2:
                    i = menu.show_hide(lab, i, colour)
                elif choice == 3:
                    colour = menu.colour_change(lab, colour_list, c)
                    c += 1
                    if c == 5:
                        c = 0
                elif choice == 4:
                    algo = menu.algo_change(algo, colour)
                elif choice == 5:
                    print("\nExiting the program...")
                    break
            except ValueError:
                clear_screen()
                display(lab, colour)
                print("\nYou didn't enter an int")
            except Exception as e:
                clear_screen()
                display(lab, colour)
                print(f"\n{e}")
