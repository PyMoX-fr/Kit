"""Entrypoint de développement qui parle au code local."""

from scripts.dev_main_launcher import _add_src_to_path
_add_src_to_path()

import pymox_kit._globals as g

g.main()

from pymox_kit import *
import sys
import scripts.various as kit_dev

# from pymox_kit._globals import main as globals_main
# globals_main()

# from scripts.compare_runner import run_package_comparer


def main() -> int | None:

    cls()

    print(f"\n\n\t\t\t\t{SB}MON LOCAL MAIN MODE{R}\n")

    print(f"Bon {GREEN}{SI}{SB}code{R} !\n")

    # Pour comparer local (./main) et réel (./r_main)
    # return run_package_comparer(package, label=label)
    g.main()

    end()

    # end('Local Kit Dev')


if __name__ == "__main__":
    raise SystemExit(main())
