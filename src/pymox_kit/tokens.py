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

    try:
        from . import kit as gt
    except Exception:
        import sys
        import os
        import importlib

        # When executed directly (python tokens.py) the package-relative import
        # fails because there's no parent package. Add the parent of the
        # package (the `src` folder) to sys.path and import by package name.
        pkg_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if pkg_root not in sys.path:
            sys.path.insert(0, pkg_root)

        gt = importlib.import_module("pymox_kit.kit")

    # from pymox_tools import greetings as gt

    print(gt.hello(), "\n" + gt.bye())
