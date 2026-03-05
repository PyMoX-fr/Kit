import locale, inspect, os, sys, time, winsound

CLIW = CLIWR = 55


def time_marker() -> str:
    """Affiche un marqueur temporel dans la console."""
    # ❌ marker

    # print("\a")
    # winsound.PlaySound("bip.wav", winsound.SND_FILENAME)
    # winsound.MessageBeep()

    winsound.Beep(5000, 100)
    return time.strftime("%H:%M:%S")


def cls(title=None, filename="", page=None):
    """Réinitialise la console (CLI) ou la page (Flet).
    Affiche title sauf si title=0.
    """

    if page is None and hasattr(title, "clean") and callable(getattr(title, "clean")):
        page = title
        title = None

    if page is not None and hasattr(page, "clean") and callable(getattr(page, "clean")):
        page.clean()

        if title not in (None, 0) and hasattr(page, "title"):
            page.title = str(title)

        if hasattr(page, "update") and callable(getattr(page, "update")):
            page.update()
        return

    def _force_home_windows():
        if os.name != "nt":
            return
        try:
            import ctypes

            class COORD(ctypes.Structure):
                _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            if handle not in (0, -1):
                ctypes.windll.kernel32.SetConsoleCursorPosition(handle, COORD(0, 0))
        except Exception:
            pass

    out = getattr(sys, "__stdout__", None)

    try:
        if out and hasattr(out, "write"):
            out.write("\033[3J\033[2J\033[H")
            out.flush()
    except Exception:
        pass

    if os.name == "nt":
        try:
            with open("CON", "w", encoding="utf-8", errors="ignore") as con:
                con.write("\033[3J\033[2J\033[H")
                con.flush()
        except Exception:
            pass

    _force_home_windows()
    os.system("cls" if os.name == "nt" else "clear")
    _force_home_windows()

    # cliWAnalysis() # //2ar

    if title != 0:
        setTitle(title, filename)


def sl(
    color: str | None = None,
    w: int = CLIW,
    trait="─",
    finTrait="",
    toPrint: bool = True,
) -> str | None:
    """Simple Line\nparm: BLUE, RED, ... or FRENCH"""
    global lineColor

    if color == "french":
        lineCode = frenchLine(trait=trait)
    else:
        lineColor = color if color else GREEN if CLIWR in IDEAL_CLIWS else RED
        lineCode = (
            f"\033[0;3{lineColor};40m" + f"{trait}{finTrait}" * w + "\033[0;37;40m"
        )

    if toPrint:
        print(lineCode)
        return None
    else:
        return lineCode


def frenchLine(
    w: int | None = CLIWR,
    trait="─",
) -> str:
    """w is None | w != CLIWR Print a BLUE-WHITE-RED line"""

    def partsLength(totalLength: int) -> tuple:
        """Calculate pure length of each part (tuple) first and third (egal), central part"""
        a = totalLength // 3
        if totalLength % 3 == 0:  # Cas où n = 1, 4, 7,...
            b = a
        elif totalLength % 3 == 1:  # Cas où n = 2, 5, 8,...
            b = a + 1
        else:  # Cas où n = 3, 6, 9,...
            a += 1
            b = a - 1
        return (a, b)

    # w = 21
    pL = partsLength(w)  # (a, b) patriotPartLength
    # print("w =", w, "→", *pL, pL[0])
    # print("-" * 65 + "8888")

    colorsCodes = [4, 7, 1, 7]

    endsLine = f"{trait}" * pL[0]
    centerLine = f"{trait}" * pL[1]

    endColors = ""
    (partBlue, partWhite, partRed, endColors) = (
        "\033[1;34m" + endsLine,
        "\033[1;37m" + centerLine,
        "\033[1;31m" + endsLine,
        "\033[0;37m" + endColors,
    )
    sFinale = partBlue + partWhite + partRed + endColors

    # print(partBlue, len(partBLUE), "(partBLUE)")
    # print(partWHITE, len(partpartWhiteWHITE), "(partWHITE)")
    # print(partRed, len(partRed), "(partRed)")
    # print(endColors, len(endColors), "(endColors)")
    # print(
    #     sFinale,
    #     len(partBlue + partWhite + partRed + endColors),
    #     "(partBlue + partWhite + partRed + endColors)",
    # )

    # print(len(sFinale), "(len(sFinale))")
    # print(rawStrLength(sFinale), "(rawStrLength(sFinale))")

    # print("\n" + "-" * 21, "21", "(Réfce.)")
    # name = " Lionel "

    # complete = sFinale + name

    # print(
    #     sFinale + name,
    #     rawStrLength(sFinale + name),
    #     "(sFinale + name)",
    # )
    return sFinale
    exit()  # 2ar


def nf(f, dec=2):
    "Number Format 123456.789 → 123 456,79"
    try:
        f = float(f)
        return locale.format_string(f"%.{dec}f", f, grouping=True)
    except ValueError:
        src = caller_info()
        # print(src)
        print(
            f"⚠️ Errorfor nf() in main_tools:\n\033[1;31mBad data type ({type(f).__name__}) -> {f} (Line {src[2]} in {src[0]}){EB}"
        )
        return str(f)


def caller_info(justfilename: bool = False, level=2) -> tuple | str:
    """
    Return (tuple) Path of caller file, caller function name, index of line where is the instruction.\nIf argument is True (or 1): (str) Just theCcller file name
    """

    frame = inspect.currentframe()

    # Vérifier la profondeur de la pile avant d'accéder à f_back plusieurs fois
    for _ in range(level):
        if frame is not None and frame.f_back is not None:
            frame = frame.f_back
        else:
            return "Frame introuvable"

    # Vérifier si frame est toujours valide avant de l'utiliser
    if frame is None:
        return "Frame introuvable"

    try:
        callerFilePath = os.path.relpath(inspect.getfile(frame))  # Chemin relatif
    except TypeError:
        return "Impossible de récupérer le fichier appelant"
    # Obtenir le numéro de ligne
    # callerLineNumber = frame.f_lineno
    callerLineNumber = int(frame.f_lineno) if frame is not None else -1

    # Nom de la fonction appelante
    function_name = frame.f_code.co_name
    context = "main" if function_name == "<module>" else f"{function_name}()"

    if justfilename:
        # return callerFilePath # 2ar vérif si dessous ok
        return os.path.basename(callerFilePath)
    return callerFilePath, context, callerLineNumber


def get_caller_function() -> str | None:
    """Return caller function if exists"""
    stack = inspect.stack()
    if len(stack) > 2:  # Vérifie qu'il y a une fonction appelante
        caller_frame = stack[2]
        caller_function = caller_frame.function  # Récupère le nom de la fonction
        return caller_function
    return None


__all__ = ["time_marker", "cls", "sl", "nf"]
