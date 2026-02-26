import asyncio
import aiohttp
from importlib.metadata import version

# Version asynchrone de kit.py, pour montrer l’intérêt de l’async dans certains cas (ex: API web) mais peu utile ici en réalité, car on n’a pas besoin de faire autre chose pendant qu’on attend la version. C’est juste pour la démo.

def get_local_version():
    return version("pymox_kit")


async def get_latest_version():
    url = "https://pypi.org/pypi/pymox-kit/json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            await asyncio.sleep(7)  # Simulation lente non bloquante
            return data["info"]["version"]


async def background_task():
    for i in range(7):
        print("Je tourne pendant que ça charge...", i)
        await asyncio.sleep(1)


async def hello():
    local_v = get_local_version()

    # On lance les deux tâches en parallèle
    task_version = asyncio.create_task(get_latest_version())
    task_background = asyncio.create_task(background_task())

    # On attend la version (mais le background continue pendant ce temps)
    latest_v = await task_version

    # On attend que le background finisse
    await task_background

    print("\nLocal version :", local_v)
    print("Latest PyPI version :", latest_v)

    if local_v != latest_v:
        print("⚠️ Une mise à jour est disponible !")
    else:
        print("✅ Vous êtes à jour !")


if __name__ == "__main__":
    asyncio.run(hello())
