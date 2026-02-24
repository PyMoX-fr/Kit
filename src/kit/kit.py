from importlib.metadata import version


def hello():
    v = version("pymox-tools")
    return f"Salut les gens from Pymox-tools {v} !"


def bye():
    return f"Bye-bye les gens !"


if __name__ == "__main__":
    print(hello(), "\n" + bye())
