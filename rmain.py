"""Entrypoint réel qui invoque `pymox_kit` comme un utilisateur."""

from __future__ import annotations

from pymox_kit.main import main


if __name__ == "__main__":
    raise SystemExit(main())
