from typing_extensions import Annotated
from pydantic import BaseModel, model_validator, field_validator, Field
import re
from typing import Optional


# implementation de la config suivant config.txt
class MyBaseConfig(BaseModel):
    WIDTH: int
    HEIGHT: int
    ENTRY: Annotated[list[int], Field(min_length=2, max_length=2)]
    EXIT: Annotated[list[int], Field(min_length=2, max_length=2)]
    OUTPUT_FILE: Annotated[str, Field(min_length=7, max_length=25)]
    PERFECT: Annotated[bool, Field(True)]
    SEED: Annotated[Optional[int], Field(None)]

    @field_validator('OUTPUT_FILE', mode='before')
    @classmethod
    def output_file_is_available(cls, value: str) -> str:
        if value is None or (isinstance(value, str) and not value.strip()):
            return "output.txt"
        if isinstance(value, str):
            value = value.strip()
            if value and not value.endswith(".txt"):
                value += ".txt"
        return value

    @model_validator(mode='after')
    def limits_are_allowed(self):
        error = ""
        if self.WIDTH > 52:
            self.WIDTH = 52
            error += f"\nWIDTH max = 52, {self.WIDTH} must be transform in 52"
        if self.HEIGHT > 27:
            self.HEIGHT = 27
            error += (f"\nHEIGHT max = 27, {self.HEIGHT} must be transform"
                      f"in 27")

        ex, ey = self.ENTRY
        ex = max(0, min(int(ex), self.WIDTH - 1))
        ey = max(0, min(int(ey), self.HEIGHT - 1))
        self.ENTRY = [ex, ey]

        sx, sy = self.EXIT
        sx = max(0, min(int(sx), self.WIDTH - 1))
        sy = max(0, min(int(sy), self.HEIGHT - 1))
        self.EXIT = [sx, sy]

        if self.ENTRY == self.EXIT:
            self.ENTRY = [0, 0]
            self.EXIT = [(self.WIDTH - 1), (self.HEIGHT - 1)]
        return self


def config_method() -> MyBaseConfig:
    with open("config.txt", "r") as c:
        base_config = {"WIDTH": "", "HEIGHT": "", "ENTRY": "", "EXIT": "",
                       "MAX": "", "PERFECT": ""}
        config = {}
        file = c.read()
        for line in file.split("\n"):
            if not line.startswith("#") and "=" in line:
                key, value = line.split("=")
                key = key.strip()
                value = value.strip()
                if key in ["ENTRY", "EXIT"]:
                    value_lst = []
                    values = re.split(r"[,;.]+", value)
                    for v in values:
                        value_lst.append(v)
                    config[key] = value_lst
                else:
                    config[key] = value
        try:
            all(k in base_config for k in config.keys())
        except KeyError as e:
            print(f"ERROR: {e}")
    my_scope = MyBaseConfig(**config)
    return my_scope
