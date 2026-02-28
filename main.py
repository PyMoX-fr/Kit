"""Entrypoint de développement qui parle au code local."""

from __future__ import annotations

from scripts.dev_main_launcher import main


if __name__ == "__main__":
    raise SystemExit(main())
