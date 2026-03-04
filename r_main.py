"""Entrypoint réel qui invoque `pymox_kit` comme un utilisateur."""

from __future__ import annotations

import os, dotenv, sys
from pathlib import Path
dotenv.load_dotenv()
# dotenv.load_dotenv(dotenv_path=Path(__file__).parent / ".env")


def _prefer_installed_package() -> None:
    repo_root = Path(__file__).resolve().parent
    local_src = str((repo_root / "src").resolve())
    sys.path[:] = [path for path in sys.path if Path(path).resolve().as_posix() != Path(local_src).resolve().as_posix()]

from pymox_kit import hello, RED,CYAN, R

if __name__ == "__main__":
    _prefer_installed_package()
    import pymox_kit as _pkg

    if os.getenv("PYMOX_DEBUG_IMPORT") == "123":
        print(f"[DEBUG] pymox_kit from: {_pkg.__file__}")

    print(f"{RED}→ 7REAL USER{R}")
    print("-" * 55)
    print(f"{CYAN}YEAHHH{R}")
    print("\n260304 :\n")
    print(hello())
    print("-" * 55)
    print("DEBUG =", os.getenv("PYMOX_DEBUG_IMPORT"))
    raise SystemExit(0)
