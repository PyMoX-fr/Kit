"""Entrypoint réel qui invoque `pymox_kit` comme un utilisateur."""

from __future__ import annotations
from pymox_kit import RED, R
from pymox_kit.main import main

if __name__ == "__main__":
    # print( f'{RED} REAL USER {R}')
    print( f'REAL USER')
    raise SystemExit(main())
