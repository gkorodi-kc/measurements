from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"name": "measurement unit converter",
            "description": "API to convert between various measurement units, and back."}


@app.get("/c2f/{C}")
def read_item(C: int, q: Union[str, None] = None):
    return {"C": C, "F": c2f(C)}


@app.get("/f2c/{F}")
def read_item(F: int, q: Union[str, None] = None):
    return {"F": F, "C": f2c(F)}


def c2f(C: int):
    return (C * 9 / 5) + 32


def f2c(F: int):
    return (F - 32) * 5 / 9
