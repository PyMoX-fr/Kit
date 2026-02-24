import time
from importlib.metadata import version


def hello():

    print("Reload marker:", int(time.time())%100)

    v = version("pymox_kit")
    return f"Salut les gens from Pymox-Kit version {v} !"


def bye():
    return f"Bye-bye les gens !"


if __name__ == "__main__":
    print(hello(), "\n" + bye())
