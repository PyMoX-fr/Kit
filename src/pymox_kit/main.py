"""Point d'entrée simple du package `pymox_kit`."""

from __future__ import annotations


def main() -> int:
    """Affiche un message de démonstration du package."""

    from .kit import hello, bye

    print("->" * 55)
    print("\n260304 :\n")
    print(hello() + bye())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
