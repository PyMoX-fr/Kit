import json, os, sys, shutil, time
from ._globals import *
from ._cli_utils import *
from ._tools import *

# from diskcache import Cache ❌ À tester // cache 'maison'

CACHE_FILE = os.path.join(os.path.expanduser("~"), ".cli_width_cache.json")

def clear():
    # Try ANSI first (works in most modern terminals), then shell fallbacks.
    try:
        print("\033[2J\033[3J\033[H", end="", flush=True)
    except Exception:
        pass

    def _run_cmd(cmd):
        try:
            return subprocess.run(
                cmd,
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode == 0
        except Exception:
            return False

    term = os.environ.get("TERM", "")
    if term and shutil.which("tput") and _run_cmd(["tput", "clear"]):
        return

    if os.name == "nt":
        # Git Bash/mintty usually provides clear; cmd builtin is a Windows fallback.
        if shutil.which("clear") and _run_cmd(["clear"]):
            return
        _run_cmd(["cmd", "/c", "cls"])
        return

    if shutil.which("clear"):
        _run_cmd(["clear"])



def cls(title=None, filename="", page=None):
    """Réinitialise la console (CLI) ou la page (Flet).
    Affiche title sauf si title=0.
    """

    # cliWAnalysis() # //2ar
    
    # if title != 0: ❌ A remettre
    #     setTitle(title, filename)
    
    if page is None and hasattr(title, "clean") and callable(getattr(title, "clean")):
        page = title
        title = None

    if page is not None and hasattr(page, "clean") and callable(page.clean):
        page.clean()

        if title not in (None, 0) and hasattr(page, "title"):
            page.title = str(title)

        if hasattr(page, "update") and callable(page.update):
            page.update()
        return

    clear()

    print(f"{RED}{SR}Oki{R} ! {GREEN}{SI}Let's go...{R} !")

TTL = 7  # 7

def read_cache():
    if not os.path.exists(CACHE_FILE):
        return None
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if time.time() - data["ts"] < TTL:
            return data["width"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        # Cache invalide ou corrompu: on repart proprement au prochain calcul.
        try:
            os.remove(CACHE_FILE)
        except OSError:
            pass

    return None


def write_cache(width):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump({"width": width, "ts": time.time()}, f)

def get_cli_width():
    w = read_cache()
    if w is not None:
        # print(f" {GREEN}Cached{R} -" * 4)
        return w
    w = get_cli_width_process()
    # print(f"{RED}Process...{R}", f"→ {RED}{SB}{w}{R} cols\n")
    write_cache(w)
    return w

def get_cli_width_process(default=80):
    """
    Récupère la largeur réelle de la console avec plusieurs stratégies.

    Ordre volontairement choisi (et testé en conditions réelles) :
    1. Variables d'environnement explicites (prioritaires)
    2. Windows : interrogation directe de la console via WinAPI
    3. os.get_terminal_size() sur plusieurs flux (stdout, stderr, stdin)
    4. shutil.get_terminal_size() avec fallback
    5. Valeur par défaut

    Cet ordre est important : dans certains environnements (stdout non TTY,
    stderr/stdin TTY, consoles intégrées, Flet, IDE...), shutil renvoie
    systématiquement la valeur de fallback (80), alors que la WinAPI ou
    certains flux donnent la vraie largeur.
    """

    # for suffix in ("out", "err", "in"):
    #     stream = getattr(sys, f"std{suffix}")
    #     name = f"sys.std{suffix}.isatty()"
    #     print(f"{name:<19} = {stream.isatty()}")

    # 1) Variables d'environnement
    for env_name in ("PY_CLI_WIDTH", "CLI_WIDTH", "COLUMNS"):
        env_val = os.environ.get(env_name)
        if env_val and env_val.isdigit() and int(env_val) > 0:
            return int(env_val)

    # 2) Windows : WinAPI sur stdout / stderr / stdin
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

    # 3) os.get_terminal_size() sur plusieurs flux
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

    # 4) shutil.get_terminal_size() avec fallback
    try:
        cols = shutil.get_terminal_size(fallback=(default, 24)).columns
        if cols > 0:
            return cols
    except Exception:
        pass

    # 5) Fallback final
    return default


# print("ID get_cli_width =", id(get_cli_width))
# print("ID get_cli_width_process =", id(get_cli_width_process))

CLIW = get_cli_width()


def end(mode="Dev"):
    """
    Args:
        mode (str, optional): _description_. Defaults to "Dev".
    """
    label = mode
    biptime = bip_time()
    sp_w = CLIW - len(label) - len(biptime) - 2  # -2 pour les 2 , => 2 espaces
    w =CLIW
    # print(f"{w = }")
    
    # ❌ donne pypi version & cliw
    print()
    print(f"{chr(0x2500)}" * CLIW)
    print(f"{CYAN}{SB}{label}{R}", " " * sp_w, biptime)

__all__ = ["cls", "CLIW", "end"]
