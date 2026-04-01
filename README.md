*This project has been created as part of the 42 curriculum by frrenaux and npillet.*

## Description
The goal of this project is to generate a maze. *(petite description de ce qu'on a fait)*

For the bonuses, an animation for the apparition of the maze, a second algorithm to generate the maze were made. You can switch between the two of them in the menu below the maze.

---

## Instructions
Here are the Makefile commands:
```bash
# install the necessary dependencies in a .venv folder
make install

# executes the program
make run

# runs the main script in debug mode using pdb
make debug

# removes any unecessary files from the folders
make clean

# verifies the norm is correctly applied in the files
make lint

# verifies the norm more stricly
make lint-strict
```
For make lint and make lint-strict, if it comes accross an issue, the commands will send back said issue. Otherwise, nothing will be sent back in the terminal.

It is also possible to execute this program using this command at the root of the folder:
```bash
python3 a_maze_ing.py config.txt
```

---

## Explanation and justification
### Complete structure and format of config.txt
| KEY | Description | Example |
| :---: | --- | --- |
| WIDTH | Define the maze width | WIDTH=20 |
| HEIGHT | Define the maze height | HEIGHT=15 |
| ENTRY | Define the entry's coordinates (x,y) | ENTRY=0,0 |
| EXIT | Define the exit's coordinates (x,y) | EXIT=19,14 |
| OUTPUT_FILE | Define the output file's name | OUTPUT_FILE=maze.txt |
| PERFECT | Define if the maze has only one way out or more (True for yes, False for no) | PERFECT=True |

---

### Maze generation algorithm
  1. **Explanation:**
      - *DFS Algorithm:*

      - *Blobby Algorithm:* 

  2. **The reason(s) why we chose it:**

---

### Code reusability
  (le package qu'il faut pouvoir créer + instruction pour le créer)
  (PS: les instructions sont aussi dans le package (copier/coller de l'un dans l'autre))

---

### Team and project management
  1. **Roles of each team member:**
  
     - **frrenaux:**
       - Parsing
       - DFS algorithm
       - Blobby algorithm
       - Maze output

     - **npillet:**
       - Makefile
       - User menu
       - Play mode (a venir)
       - README.md

  2. **Original planning and how it evolved:**

  3. **What worked well and what could be improved:**

---

### Specific tools usage
The dependencies we used, other than the mandatory ones, are:
- **Pydantic:** to check the config.txt file
- **Arcade:** for the play mode (a venir)

(autre outils specifique utilise si il y a)

---

### Advanced features
(multiple algo, display options) en faire une description

---

## Resources
### Maze generation:
#### Algorithms:
- site explication algo

#### User interactions:
- https://jobbinge.in/menu-driven-programs-in-python/
- https://medium.com/@ajineer/introducing-the-special-menu-class-in-python-simplifying-user-choices-87f3bf58b495

#### Play mode:
- https://api.arcade.academy/en/stable/index.html
- https://arcade-pk.readthedocs.io/en/latest/

### Other:
#### Makefile:
- https://earthly.dev/blog/python-makefile/

#### Code reusability:
- generation du package
