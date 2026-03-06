import locale, os, shutil, sys

from flask import cli
locale.setlocale(locale.LC_ALL, "fr_FR")

# CLIW = SIMU_CLIW if SIMU_CLIW else CLIWR
# LG = "\n" + "-" * CLIWR

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

CLIW =55 # ❌ Calcul réel

__all__ = ["CLIW", "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE", "SB", "SD", "SI", "SU", "SR", "SS", "R"]
