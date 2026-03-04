"""Entrypoint de développement qui parle au code local."""

from __future__ import annotations

from scripts.dev_main_launcher import _add_src_to_path, main


if __name__ == "__main__":
    _add_src_to_path()
    from pymox_kit import R, RED

    print(f"{RED}LOCAL DEV{R}")
    raise SystemExit(main())
