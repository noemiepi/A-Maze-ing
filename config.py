from typing_extensions import Annotated
from pydantic import BaseModel, model_validator, Field, ValidationError
import re


class MyBaseConfig(BaseModel):
    WIDTH: int
    HEIGHT: int
    ENTRY: Annotated[list, Field(min_length=2, max_length=2)]
    EXIT: Annotated[list, Field(min_length=2, max_length=2)]
    OUTPUT_FILE: Annotated[str, Field(min_length=7, max_length=25)]
    PERFECT: Annotated[bool, Field(True)]

    @model_validator(mode='after')
    def width_is_allowed(self):
        if self.WIDTH > 100:
            print("Your width's choice is too big, 100 is max")
            self.WIDTH = 100
        return self

    def height_is_allowed(self):
        if self.HEIGHT > 100:
            print("Your height's choice is too big, 100 is max")
            self.HEIGHT = 100
        return self

    def entry_is_allowed(self):
        entries = re.split(r"[,;.]+", self.ENTRY)
        if len(entries) > 2:
            raise ValueError("ENTRY must be for example: '1,1' or '1.1'")
        x, y = entries
        try:
            x = int(x)
            y = int(y)
            if 0 > x:
                x = 0
            elif self.WIDTH < x:
                x = self.WIDTH
            if 0 > y:
                y = 0
            elif self.HEIGHT < y:
                y = self.HEIGHT
            self.ENTRY = [x, y]
        except Exception:
            print("ERROR")
        return self

    def exit_is_allowed(self):
        exits = re.split(r"[,;.]+", self.EXIT)
        if len(exits) > 2:
            raise ValueError("ENTRY must be for example: '1,1' or '1.1'")
        x, y = exits
        try:
            x = int(x)
            y = int(y)
            if 0 > x:
                x = 0
            elif self.WIDTH < x:
                x = self.WIDTH
            if 0 > y:
                y = 0
            elif self.HEIGHT < y:
                y = self.HEIGHT
            self.EXIT = [x, y]
        except Exception:
            print("ERROR")
        return self

    def exit_entry(self):
        if self.ENTRY == self.EXIT:
            raise ValueError("ENTRY and EXIT must be differents")
        return self

    def output_is_allowed(self):
        if not self.OUTPUT_FILE.endswith('.txt'):
            raise ValueError("OUTPUT_FILE must be finish with '.txt'")

def config_method():
    with open("config.txt", "r") as c:
        base_config = {"WIDTH": "", "HEIGHT": "","ENTRY": "", "EXIT": "",
                       "MAX": "", "PERFECT": ""}
        config = {}
        file = c.read()
        for line in file.split("\n"):
            if "=" in line:
                key, value = line.split("=")
                key = key.strip()
                value = value.strip()
                config[key] = value
        try:
            all(k in base_config for k in config.keys())
        except KeyError as e:
            print(f"ERROR: {e}")
    my_scope = MyBaseConfig(**config)
    return my_scope


if __name__ == "__main__":
    config_method()