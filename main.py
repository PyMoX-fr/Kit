"""Entrypoint de développement qui parle au code local."""

from __future__ import annotations

from scripts.dev_main_launcher import _add_src_to_path

_add_src_to_path()

from pymox_kit import *
import sys

# from scripts.compare_runner import run_package_comparer


def main() -> int | None:

    cls()

    label = "LOCAL DEV"
    print(f"\n{CYAN}{SB}{label}{R}", "-", bip_time())
            
    # Voir tous les caractère box - 0x2500 → ALT + 2500 => ─
    # for i in range(0x2400, 0x2580):
    #     print(f"{i} (0x{i:04X}) → {chr(i) * (CLIW-20)}")



    # print(f"Bon {GREEN}{SI}{SB}code{R} !\n{hello()}")
    # print(CLIW)

    # Pour comparer local (./main) et réel (./r_main)
    # return run_package_comparer(package, label=label)

    # print("─" * CLIW)
    # Idem avec :
    print(f"{chr(0x2500)}" * CLIW)
    
    print(f"Bon {GREEN}{SI}{SB}code{R} !\n")


if __name__ == "__main__":
    raise SystemExit(main())
