def tokens():
    from setuptools_scm import get_version

    print("\nDernière version pymox_tools1: " + get_version() + "\n" + ("-" * 71))
    from dotenv import load_dotenv
    import os

    load_dotenv()  # Charge les variables depuis .env
    # load_dotenv(override=True)

    GH_TOKEN = os.getenv("GH_TOKEN")
    pypi_token = os.getenv("PYPI_TOKEN")

    print(f"GH_TOKEN: {GH_TOKEN}\n\nPYPI_TOKEN: {pypi_token}\n")

    return f"Salut les gens !"


if __name__ == "__main__":

    try:
        tokens()
    except Exception as e:
        print(f"Erreur lors de l'exécution de tokens(): {e}")

    import kit as gt

    # from pymox_tools import greetings as gt

    print(gt.hello(), "\n" + gt.bye())
