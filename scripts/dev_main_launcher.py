"""Point d'entrée qui expose un `main()` plaçant le code local dans `sys.path`."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


def _add_src_to_path() -> None:
    root = Path(__file__).resolve().parent.parent
    src = root / "src"
    if not src.exists():
        return
    entry = str(src)
    if entry not in sys.path:
        sys.path.insert(0, entry)


def main(argv: Sequence[str] | None = None) -> int:
    """Appelle `pymox_kit.main` avec `src` dans `sys.path`."""
    _add_src_to_path()
    from pymox_kit.main import main as kit_main

    return kit_main(argv)
