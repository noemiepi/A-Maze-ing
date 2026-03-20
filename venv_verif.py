import sys
import venv
import subprocess
import os

# verification qu'on est bien dans un venv, sinon creation de celui-ci
ENV_NAME = "A-Maze-ing_env"


def venv_verif() -> bool:
    if sys.prefix == sys.base_prefix:
        print("\n**** Creation of the virtual environment ****")
        venv.create(ENV_NAME, with_pip=True)
        python_path = os.path.join(ENV_NAME, "bin", "python")
        print("\n**** Installation and upgrade of pip ****")
        subprocess.check_call([python_path, "-m", "pip", "install",
                               "--upgrade", "pip"])
        print("\n**** Installation of poetry ****")
        subprocess.check_call([python_path, "-m", "pip", "install",
                               "poetry"])
        print("\n**** Installation of pydantic ****")
        subprocess.check_call([python_path, "-m", "pip", "install",
                               "pydantic"])
        print("\n\033[1;32mYour venv is created")
        print("poetry is installed")
        print(f"Please restart with:\033[0m "
              f"\033[1;31msource {ENV_NAME}/bin/activate\033[0m")
        return False
    return True