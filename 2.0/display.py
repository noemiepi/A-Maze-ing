from maze_class import MyLaby


# affichage
def display(my_lab: MyLaby) -> None:
    grid_to_display = my_lab.grid
    for y in range(my_lab.height):
        north_line = ""
        for x in range(my_lab.width):
            north_line += "+"
            if grid_to_display[y][x].north or\
                grid_to_display[y][x].ft or\
                grid_to_display[y - 1][x].ft:
                north_line += "==="
            else:
                north_line += "   "
        north_line += "+"
        print(north_line)

        middle_line = ""
        for x in range(my_lab.width):
            if grid_to_display[y][x].west or\
                grid_to_display[y][x].ft or\
                grid_to_display[y][x - 1].ft:
                middle_line += "|" 
            else:
                middle_line += " "
            # case 42
            if grid_to_display[y][x].ft: 
                middle_line += "\033[1;5;36m O \033[0m"
            # chemin de resolution
            elif grid_to_display[y][x].resolved:
                if x == my_lab.entry_x and y == my_lab.entry_y:
                    middle_line += "\033[5;33m W \033[0m"
                elif x == my_lab.exit_x and y == my_lab.exit_y:
                    middle_line += "\033[5;31m W \033[0m"
                else:
                    middle_line += "\033[1;32m W \033[0m"
            # point de depart
            elif x == my_lab.entry_x and y == my_lab.entry_y:
                middle_line += "\033[1;33m E \033[0m"
            # point d'arrive
            elif x == my_lab.exit_x and y == my_lab.exit_y:
                middle_line += "\033[1;31m S \033[0m"
            # point de presence
            elif grid_to_display[y][x].current:
                middle_line += "\033[1;35m A \033[0m"
                grid_to_display[y][x].current = False
            # le reste
            else:
                middle_line += "   "
        middle_line += "|" if grid_to_display[y][my_lab.width-1].east\
                            else " "
        print(middle_line)
    south_line = ""
    for x in range(my_lab.width):
        south_line += "+"
        south_line += "===" if grid_to_display[my_lab.height-1][x].south\
                            else "   "
    south_line += "+"
    print(south_line)
