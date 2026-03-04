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
CACHE_TTL = 3600  # 3600 (1 heure)


def _is_site_packages_mode() -> bool:
    return "site-packages" in Path(__file__).resolve().parts


def get_local_version():
    if not _is_site_packages_mode():
        return "dev-local"

    try:
        return version("pymox_kit")
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


def hello(check_updates: bool | None = None):
    if check_updates is None:
        check_updates = _is_site_packages_mode()

    local_v = get_local_version()
    latest_v, from_cache = get_latest_version()

    print("Local version :", local_v)

    if not check_updates:
        if latest_v:
            print(
                "Latest PyPI version :",
                latest_v,
                "(cache)" if from_cache else "(network)",
            )
        return f"Salut les gens 😊 !\n\t 👉 From Pymox-Kit, version {local_v} !"

    if latest_v:
        print(
            "Latest PyPI version :",
            latest_v,
            "(cache)" if from_cache else "(network)",
        )

        if local_v < latest_v:
            print("⚠️ Une mise à jour est disponible !")
        else:
            print("✅ Vous êtes à jour !")
    else:
        print("⚠️ Impossible de vérifier la dernière version (offline ?)")

    return f"Salut les gens 😊 !\n\t 👉 From Pymox-Kit, version {local_v} !"


def bye():
    return "Bye-bye les gens, & @ ++ ⏳..."

__all__ = ["hello", "bye"]

if __name__ == "__main__":
    print(hello())
