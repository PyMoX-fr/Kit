import json
import os
import time
import urllib.request
import urllib.error
from pathlib import Path
from importlib.metadata import PackageNotFoundError, version

# ✅ timeout court (ne pas bloquer le CLI)
# ✅ fallback offline (si PyPI indisponible)
# ✅ cache local (éviter un appel réseau à chaque exécution)
# ✅ zéro dépendance externe
# ✅ code simple et maintenable

PACKAGE_NAME = "pymox-kit"
CACHE_FILE = os.path.join(os.path.expanduser("~"), ".pymox_kit_version_cache.json")
CACHE_TTL = 60  # 3600 (1 heure) //2ar


def _is_site_packages_mode() -> bool:
    return "site-packages" in Path(__file__).resolve().parts


def get_local_version():
    if not _is_site_packages_mode():
        return "Dev-local"

    try:
        return version("pymox_kit") # Danger: Version de la dépendance, pas forcément la même que celle du package lui-même (ex: si on a installé une ancienne version de pymox-kit mais qu’on a une nouvelle version de kit dans le code, ça peut être trompeur). C’est pour ça que j’ai ajouté le mode dev-local qui affiche "Dev-local" pour éviter les confusions pendant le développement.
    except PackageNotFoundError:
        return "unknown"


def read_cache():
    if not os.path.exists(CACHE_FILE):
        return None

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Vérifie expiration
        if time.time() - data["timestamp"] < CACHE_TTL:
            return data["version"]
    except Exception:
        pass

    return None


def write_cache(latest_version):
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "version": latest_version,
                    "timestamp": time.time(),
                },
                f,
            )
    except Exception:
        pass


def fetch_latest_version(timeout=3):
    url = f"https://pypi.org/pypi/{PACKAGE_NAME}/json"
    with urllib.request.urlopen(url, timeout=timeout) as response:
        data = json.load(response)
        return data["info"]["version"]


def get_latest_version():
    # 1️⃣ Essaye cache
    cached = read_cache()
    if cached:
        return cached, True

    # 2️⃣ Essaye réseau
    try:
        latest = fetch_latest_version()
        write_cache(latest)
        return latest, False
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
        # 3️⃣ Fallback offline
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data["version"], True
            except Exception:
                pass

        return None, False


def hello():
    local_v = get_local_version()
    latest_v, from_cache = get_latest_version()

    # Affiche la version PyPI si disponible
    if latest_v:
        print(
            "Latest PyPI version :",
            latest_v,
            "(cache)" if from_cache else "(network)",
        )
    else:
        print("⚠️ Impossible de vérifier la dernière version (offline ?)")

    # Vérification des updates
    if latest_v:
        if local_v < latest_v:
            print("⚠️ Une mise à jour est disponible !")
        else:
            print("✅ Vous êtes à jour !")

    return f"Salut les gens 😊 !\n\t 👉 From Pymox-Kit, version {local_v} !"


def bye():
    return "Bye-bye les gens, & @ ++ ⏳..."

__all__ = ["hello", "bye"]

if __name__ == "__main__":
    print(hello())
