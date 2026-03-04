import json
import urllib.request
from importlib.metadata import version


def get_local_version():
    return version("pymox_kit")


def get_latest_version():
    with urllib.request.urlopen("https://pypi.org/pypi/pymox-kit/json") as response:
        data = json.load(response)
        return data["info"]["version"]


def hello():
    local_v = get_local_version()
    latest_v = get_latest_version()

    print("Local version :", local_v)
    print("Latest PyPI version :", latest_v)

    if local_v != latest_v:
        print("⚠️ Une mise à jour est disponible !")
    else:
        print("✅ Vous êtes à jour !")

    return f"Salut les gens from Pymox-Kit version {local_v} !"


def bye():
    return f"Bye-bye les gens !"


__all__ = ["hello", "bye"]

if __name__ == "__main__":
    print(hello())
