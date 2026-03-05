"""Entrypoint réel qui invoque `pymox_kit` comme un utilisateur."""

from __future__ import annotations

import sys
from pathlib import Path

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
    import pymox_kit as package

    label = "REAL USER"

    print("-" * 55)
    print(f"\x1b[96m{label}\x1b[0m", time_marker())

    # Pour comparer local (./main) et réel (./r_main)
    # return run_package_comparer(package, label=label)


if __name__ == "__main__":
    raise SystemExit(main())
