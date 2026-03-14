import re
from ._globals import *
from ._cli_utils import *

def title_fr(n=3):
    """_summary_

    Args:
        n (int, optional): _description_. Defaults to 3.

    Returns:
        _type_: _description_
    """
    cases = {
        1: "{1}Bleu {2}Blanc {3}Rouge{0}",
        2: "{1}Mais {2}même un text {3}terriblement + long....{0}",
        3: "Demo {1}Py{2}MoX_{3}Kit{0}",
    }
    title = cases.get(n, "Titre par défaut")

    tags = re.findall(r"\{\d\}", title)  # → ["{1}", "{2}", "{3}", "{0}"]
    tags_len = sum(len(t) for t in tags)  # → 4 * 3 = 12

    tiret = CLIW - len(title) + tags_len - 1 # -1 pour l'espace entre t de Kit et le premier ─

    title = (
        title.replace("{1}", BLUE)
        .replace("{2}", WHITE)
        .replace("{3}", RED)
        .replace("{0}", R)
    )

    return title + " " + "─" * tiret

__all__ = ["title_fr"]
