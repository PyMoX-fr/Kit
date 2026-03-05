"""Runner commun pour comparer exécution locale vs package installé."""

from __future__ import annotations

import os
from pathlib import Path
from types import ModuleType

import dotenv


def run_package_comparer(package: ModuleType, *, label: str) -> int:
    """Exécute une démo standard pour un package `pymox_kit` importé."""

    dotenv.load_dotenv()

    color_reset = getattr(package, "R", "")
    color_red = getattr(package, "RED", "")
    color_cyan = getattr(package, "CYAN", "")
    hello = getattr(package, "hello", None)
    # print(f"{color_red}→ {label}{color_reset}")
  
    if os.getenv("PYMOX_DEBUG_IMPORT") == "1":
        print(f"[DEBUG] pymox_kit from: {getattr(package, '__file__', 'unknown')}")

    print("-" * 55)
    
    if callable(hello):
        print(f"{color_cyan}YEAHHH{color_reset}")
        print("\n260304 :\n")
        print(hello())
        print("-" * 55)

    print("CWD =", Path.cwd())
    print("ENV FILE EXISTS =", (Path(__file__).resolve().parent.parent / ".env").exists())
    print("DEBUG =", os.getenv("PYMOX_DEBUG_IMPORT"))
    print()
    return 0
