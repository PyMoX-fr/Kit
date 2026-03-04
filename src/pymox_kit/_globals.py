import locale, os, shutil, sys
locale.setlocale(locale.LC_ALL, "fr_FR")

# CLIW = SIMU_CLIW if SIMU_CLIW else CLIWR
# LG = "\n" + "-" * CLIWR
SB = "\033[1m"  # Début gras (Start Bold)
RED = "\033[0;31m"  # Début rouge (Start Red)
R = ES = "\x1b[0m"  # Fin (Reset) (End bold, end style)

FRENCH = "french"
(BLACK, RED_IDX, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE) = range(8)

# 0 : noir - 1 : rouge - 2 : vert - 3 : jaune - 4 : bleu - 5 : magenta - 6 : cyan - 7 : blanc
# 3x pour encre, 4x pour fond
# \033[3mItalique\033[23m)
# \033[4mSouligné\033[24m)
# \033[3;4mSouligné & Italique\033[23;24m)
