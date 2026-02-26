from ._cached_kit import get_local_version, get_latest_version


def hello():
    local_v = get_local_version()
    latest_v, from_cache = get_latest_version()

    print("Local version :", local_v)

    if latest_v:
        print(
            "Latest PyPI version :", latest_v, "(cache)" if from_cache else "(network)"
        )
        if local_v != latest_v:
            print("⚠️ Une mise à jour est disponible !")
        else:
            print("✅ Vous êtes à jour !")
    else:
        print("⚠️ Impossible de vérifier la dernière version (offline ?)")

    return f"Salut les gens from Pymox-Kit version {local_v} !"


def bye():
    return "Bye-bye les gens !"
