"""Entrypoint de développement qui parle au code local."""

from __future__ import annotations

import os

from scripts.dev_main_launcher import _add_src_to_path


if __name__ == "__main__":
    _add_src_to_path()
    import pymox_kit as _pkg
    from pymox_kit import R, RED, hello

    if os.getenv("PYMOX_DEBUG_IMPORT") == "1":
        print(f"[DEBUG] pymox_kit from: {_pkg.__file__}")

    print(f"{RED}LOCAL DEV{R}")
    print("-" * 55)
    print("YEAHHH")
    print("\n260304 :\n")
    print(hello())
    raise SystemExit(0)
