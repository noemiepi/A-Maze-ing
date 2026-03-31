*This project has been created as part of the 42 curriculum by frrenaux and npillet.*

## Description
The goal of this project is to generate a maze. *(petite description de ce qu'on a fait)*

The bonuses are *(bonus fait)* consists of *(a quoi ils servent)*.

## Instructions
To run this project, the first command to do is:
```bash
make
or
make all
or
make install then make run
```
It will create a virtual environment in which the needed dependencies will be installed, it isn't necessary to enter it, but if wanted, this is the command:
```bash
source .venv/bin/activate
```

To verify the norm is correctly applied in the files, use:
```bash
make lint
```
If it comes accross an issue, the command will send back said issue. Otherwise, nothing will be sent back in the terminal.
For a stricter check, use:
```bash
make lint-strict
```

To run the main script in debug mode, using pdb:
```bash
make debug
```

To remove any unecessary files from the project, use this command:
```bash
make clean
```
To execute this program, this command must be used at the root of the folder:
```bash
python3 a_maze_ing.py config.txt
or
make run
```

## Explanation and justification

### Complete structure and format of config.txt

### Maze generation algorithm chosen and why

### Reusable part of the code and how

### Team project management
- Roles of each member
- anticipated planning and how it evolved until the end
- what worked well and what could be improved
- did we used any specific tools and, if yes, which ones?

### Advanced features (si on en a fait)
(multiple algo, display options) en faire une description

### Additional features (c'est pas demande)
(les bonus fait si il y en a)

## Resources

- [Makefile](https://earthly.dev/blog/python-makefile/)

- [User Menu](https://medium.com/@ajineer/introducing-the-special-menu-class-in-python-simplifying-user-choices-87f3bf58b495)

- [User menu](https://jobbinge.in/menu-driven-programs-in-python/)

- [Doc Arcade](https://api.arcade.academy/en/stable/index.html)

- [Doc Arcade (outdated)](https://arcade-pk.readthedocs.io/en/latest/)
