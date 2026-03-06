"""Entrypoint de développement qui parle au code local."""

from __future__ import annotations

from scripts.dev_main_launcher import _add_src_to_path

_add_src_to_path()
from pymox_kit import *

# from scripts.compare_runner import run_package_comparer


def main() -> int | None:
    label = "LOCAL DEV"

    print("-" * 55)
    print(f"\x1b[96m{label}\x1b[0m", '-',bip_time())
    
    print (f'{SS}Lionel{R} CÔTE')

    # Pour comparer local (./main) et réel (./r_main)
    # return run_package_comparer(package, label=label)


if __name__ == "__main__":
    raise SystemExit(main())
