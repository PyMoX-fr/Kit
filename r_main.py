"""Entrypoint réel qui invoque `pymox_kit` comme un utilisateur."""

from __future__ import annotations

import sys
from pathlib import Path
from pymox_kit import *
# import scripts.common_footer as kit_dev

# from scripts.compare_runner import run_package_comparer


def _prefer_installed_package() -> None:
    repo_root = Path(__file__).resolve().parent
    local_src = str((repo_root / "src").resolve())
    sys.path[:] = [
        path
        for path in sys.path
        if Path(path).resolve().as_posix() != Path(local_src).resolve().as_posix()
    ]


def main() -> int | None:
    _prefer_installed_package()
    cls()

    print(f"\n\n\t\t\t\t{SB}MON REAL USER MODE{R}\n")

    # Pour comparer local (./main) et réel (./r_main)
    # return run_package_comparer(pk, label=label)
    
    end("REAL USER")

if __name__ == "__main__":
    raise SystemExit(main())
