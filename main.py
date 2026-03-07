"""Entrypoint de développement qui parle au code local."""

from __future__ import annotations

from scripts.dev_main_launcher import _add_src_to_path

_add_src_to_path()

from pymox_kit import *
import sys
import scripts.various as kit_dev

# from scripts.compare_runner import run_package_comparer


def main() -> int | None:

    cls()

    print(f"\n\n\t\t\t\t{SB}MON LOCAL MAIN MODE{R}\n")

    print(f"Bon {GREEN}{SI}{SB}code{R} !\n")

    # kit_dev.all_box_cars()

    # Pour comparer local (./main) et réel (./r_main)
    # return run_package_comparer(package, label=label)
    end('Local Kit Dev')


if __name__ == "__main__":
    raise SystemExit(main())
