from pymox_kit import *


def footer(mode="LOCAL DEV"):
    # ❌  2 remove

    label = mode
    biptime = bip_time()
    sp_w = CLIW - len(label) - len(biptime) - 2  # -2 pour les 2 , => 2 espaces

    # Voir tous les caractère box - 0x2500 → ALT + 2500 => ─
    # for i in range(0x2400, 0x2580):
    #     print(f"{i} (0x{i:04X}) → {chr(i) * (CLIW-20)}")
    
    print(f"{chr(0x2500)}" * CLIW)
    print(f"{CYAN}{SB}{label}{R}", " " * sp_w, biptime)
