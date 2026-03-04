"""Module principal exposant une fonction `main()`.

Ce module est importable (`from pymox_kit.main import main`) et exécutable
directement (`python src/pymox_kit/main.py`). Il utilise des importations
robustes pour fonctionner depuis la racine du repo ou comme paquet installé.
"""

from __future__ import annotations

from typing import Callable, Optional, Sequence, Tuple


def _get_helpers() -> Tuple[Callable[[], str], Callable[[], str], Callable[..., str]]:
    try:
        # prefer package-relative import when used as package
        from . import _globals
        from .kit import hello, bye, nf

        return hello, bye, nf
    except Exception:
        # fallback when executed as a script: ensure package root is on sys.path
        import sys
        import os
        import importlib

        pkg_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if pkg_root not in sys.path:
            sys.path.insert(0, pkg_root)

        mod = importlib.import_module("pymox_kit.kit")
        return mod.hello, mod.bye, mod.nf


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Point d'entrée principal.

    Arguments:
        argv: liste d'arguments (optionnel, pour tests). Retourne code de sortie.
    """

    print('-'*55)
    print('YEAHHH')

    # hello, bye, nf = _get_helpers()

    # # print('\n260304 :\n\n' + hello())
    # # print(bye(), end='\n\n')
    # print(nf(123456.789))
    # print('\x1b[1;31mFin.\033[0m')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# python -m pymox_kit
