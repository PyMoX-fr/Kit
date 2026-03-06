import locale, os, shutil, sys

from flask import cli

locale.setlocale(locale.LC_ALL, "fr_FR")

# CLIW = SIMU_CLIW if SIMU_CLIW else CLIWR
# LG = "\n" + "-" * CLIWR
from ._cli_utils import *

# print ((str(CLIW)+' ')*55)

##########################################################################
# SIMU_CliW = 40  # @i Si on veut Pour simuler une cliW sinon: Commenter #
SLEEP_DURATION = 0.7  # @i Tempo des affichages en secondes des parties  #
IDEAL_CLIWS = range(50, 61)  # Utiliser 55 col. est conseillé            #
##########################################################################


def ansi(n):
    return f"\x1b[0;9{n}m"


BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = [ansi(i) for i in range(8)]

# x = 0 : noir - 31 : rouge - 32 : vert - 33 : jaune - 34 : bleu - 35 : magenta - 36 : cyan - 37 : blanc
# 3x pour encre, 4x pour fond, 7 reverse, 10x fonds vifs

ST = "\x1b[30;43m"  # Stabilo effect


def ansi_style(n):
    return f"\x1b[{n}m"


# Reset, Style Dim(Pâle), Bold, Italic, Underline, Reverse, Strikethrough
R, SB, SD, SI, SU, SR, SS = [ansi_style(i) for i in [*range(5), 7, 9]]
# \033[3mItalique\033[23m)
# \033[4mSouligné\033[24m)
# \033[3;4mSouligné & Italique\033[23;24m)

# print("-" * 55)
# print(f"{ST}Oki{R}")
# print("-" * 55)
# print("Yes")

# CLIW = get_cli_width() # ❌ Calcul réel


def cls():
    print("\033[2J\033[H", end="")  # Clear screen and move cursor to top-left


def get_cli_width_Pri_et_fonctionnel(default=80):
    """Récupère la largeur réelle de la console avec plusieurs stratégies."""

    for env_name in ("PY_CLI_WIDTH", "CLI_WIDTH", "COLUMNS"):
        env_val = os.environ.get(env_name)
        if env_val and env_val.isdigit() and int(env_val) > 0:
            return int(env_val)

    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes

            class COORD(ctypes.Structure):
                _fields_ = [("X", wintypes.SHORT), ("Y", wintypes.SHORT)]

            class SMALL_RECT(ctypes.Structure):
                _fields_ = [
                    ("Left", wintypes.SHORT),
                    ("Top", wintypes.SHORT),
                    ("Right", wintypes.SHORT),
                    ("Bottom", wintypes.SHORT),
                ]

            class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
                _fields_ = [
                    ("dwSize", COORD),
                    ("dwCursorPosition", COORD),
                    ("wAttributes", wintypes.WORD),
                    ("srWindow", SMALL_RECT),
                    ("dwMaximumWindowSize", COORD),
                ]

            get_std_handle = ctypes.windll.kernel32.GetStdHandle
            get_csbi = ctypes.windll.kernel32.GetConsoleScreenBufferInfo
            get_std_handle.argtypes = [wintypes.DWORD]
            get_std_handle.restype = wintypes.HANDLE
            get_csbi.argtypes = [
                wintypes.HANDLE,
                ctypes.POINTER(CONSOLE_SCREEN_BUFFER_INFO),
            ]
            get_csbi.restype = wintypes.BOOL

            for std_handle in (-11, -12, -10):  # stdout, stderr, stdin
                handle = get_std_handle(std_handle)
                if not handle or handle == wintypes.HANDLE(-1).value:
                    continue
                csbi = CONSOLE_SCREEN_BUFFER_INFO()
                if get_csbi(handle, ctypes.byref(csbi)):
                    cols = int(csbi.srWindow.Right - csbi.srWindow.Left + 1)
                    if cols > 0:
                        return cols
        except Exception:
            pass

    for stream in (
        getattr(sys, "__stdout__", None),
        sys.stdout,
        getattr(sys, "__stderr__", None),
        sys.stderr,
        getattr(sys, "__stdin__", None),
        sys.stdin,
    ):
        try:
            if stream is None:
                continue
            cols = os.get_terminal_size(stream.fileno()).columns
            if cols > 0:
                return cols
        except Exception:
            continue

    try:
        cols = shutil.get_terminal_size(fallback=(default, 24)).columns
        if cols > 0:
            return cols
    except Exception:
        pass

    return default


__all__ = [
    "BLACK",
    "RED",
    "GREEN",
    "YELLOW",
    "BLUE",
    "MAGENTA",
    "CYAN",
    "WHITE",
    "SB",
    "SD",
    "SI",
    "SU",
    "SR",
    "SS",
    "R",
    "cls"
]
