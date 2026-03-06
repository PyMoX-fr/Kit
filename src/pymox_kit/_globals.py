import locale, os, shutil, sys

from flask import cli

locale.setlocale(locale.LC_ALL, "fr_FR")

# CLIW = SIMU_CLIW if SIMU_CLIW else CLIWR
# LG = "\n" + "-" * CLIWR
# from ._cli_utils import *

# print ((str(CLIW)+' ')*55)

##########################################################################
# SIMU_CliW = 40  # @i Si on veut Pour simuler une cliW sinon: Commenter #
SLEEP_DURATION = 0.7  # @i Tempo des affichages en secondes des parties  #
IDEAL_CLIWS = range(50, 61)  # Utiliser 55 col. est conseillé            #
##########################################################################


def ansi(n):
    return f"\x1b[0;9{n}m"


def ansi_style(n):
    return f"\x1b[{n}m"


# x = 0 : noir - 31 : rouge - 32 : vert - 33 : jaune - 34 : bleu - 35 : magenta - 36 : cyan - 37 : blanc
# 3x pour encre, 4x pour fond, 7 reverse, 10x fonds vifs
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = [ansi(i) for i in range(8)]
ST = "\x1b[30;43m"  # Stabilo effect
# Reset, Style Dim(Pâle), Bold, Italic, Underline, Reverse, Strikethrough
R, SB, SD, SI, SU, SR, SS = [ansi_style(i) for i in [*range(5), 7, 9]]

if __name__ == "__main__":
    print(
        f"{GREEN}{SB}Green{R} {RED}{SD}Red{R} {YELLOW}{SI}Yellow{R} {BLUE}{SU}Blue{R} {MAGENTA}{SR}Magenta{R} {CYAN}{SS}Cyan{R} {WHITE}White{R}"
    )

__all__ = [
    "BLACK",  # Noir"
    "RED",  # Rouge
    "GREEN",  # Vert
    "YELLOW",  # Jaune
    "BLUE",  # Bleu
    "MAGENTA",
    "CYAN",
    "WHITE",  # Blanc
    "SB",  # Style Bold (gras)
    "SD",  # Style Dim (pâle)
    "SI",  # Style Italic (italique)
    "SU",  # Style Underline (souligné)
    "SR",  # Style Reverse (inverse)
    "SS",  # Style Strikethrough (barré)
    "R",  # Reset (réinitialiser)
]
