import _cached_kit as ck


if __name__ == "__main__":
    local_v = ck.get_local_version()
    latest_v, from_cache = ck.get_latest_version()

    print("Local version :", local_v)
    print("Latest PyPI version :", latest_v, "(cache)" if from_cache else "(network)")

    if local_v != latest_v:
        print("⚠️ Une mise à jour est disponible !")
    else:
        print("✅ Vous êtes à jour !")
