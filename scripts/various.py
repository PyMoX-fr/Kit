from pymox_kit import *


def all_box_cars():
    """Voir tous les caractère box - 0x2500 → ALT + 2500 => ─"""
    for i in range(0x2400, 0x2580):
        print(f"{i} (0x{i:04X}) → {chr(i) * (CLIW-20)}")
