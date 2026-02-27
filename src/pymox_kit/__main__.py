"""Entrypoint package : `python -m pymox_kit`.

Offre un petit CLI :
- `--version` / `-V` : affiche la version (installation locale ou PyPI)
- sans option : délègue à `pymox_kit.main.main()` si présent, sinon appelle
  `pymox_kit.kit.hello()` / `bye()`.
"""

from __future__ import annotations

from typing import Sequence, Optional


def _get_package_version() -> str:
    try:
        from importlib.metadata import version, PackageNotFoundError

        try:
            # distribution name may be either 'pymox_kit' or 'pymox-kit'
            return version("pymox_kit")
        except PackageNotFoundError:
            try:
                return version("pymox-kit")
            except PackageNotFoundError:
                pass
    except Exception:
        pass

    # fallback to package attribute
    try:
        import pymox_kit

        return getattr(pymox_kit, "__version__", "unknown")
    except Exception:
        return "unknown"


def main(argv: Optional[Sequence[str]] = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m pymox_kit", description="PyMoX Kit CLI"
    )
    parser.add_argument(
        "-V", "--version", action="store_true", help="Afficher la version"
    )
    args = parser.parse_args(argv)

    if args.version:
        print(_get_package_version())
        return 0

    # Délégation principale vers pymox_kit.main.main() si disponible
    try:
        from importlib import import_module

        mod = import_module("pymox_kit.main")
        if hasattr(mod, "main"):
            mod.main()
            return 0
    except Exception:
        pass

    # Sinon usage direct des helpers
    try:
        from .kit import hello, bye

        print(hello())
        print(bye())
        return 0
    except Exception as exc:
        print("Erreur lors de l'exécution du package:", exc)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
