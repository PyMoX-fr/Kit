# PyMoX-Tools

Trousse à outils utiles pour devs en PyMoX

---

## Rapide mémo (Cf. GH)

### Bases VE (Virtual Env)

```bash
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip
pip install -r requirements.txt

# Installer en editable mode
# pip install -e .
```

### Définir les TOKENs (TK) nécessaires :

GH_TOKEN dans compte GH User/Settings/Dev settings/PAT/TK (Classic) → new
→ IMPORTANT: Droits Repo & Wkf
PYPI_TOKEN dans compte Pypi.org User/Params/Jetons API

Les insérer dans dépôt GH: Settings / Secrets... / Actions / New Repo secret

Mettre GH TK dans .env
(GH PP que si on veut build + upload PP depuis local)

### Adapter les params Pypi project name

PROJECT\pyproject.toml
(name & repository)

### Faire un push de la main avec fix: msg, feat: msg ou idem avec ! (fix!: msg)

→ patch, minor ou major

### Build local

```bash
py -m build
twine check dist/*
twine upload dist/* --verbose

twine upload dist/* -u __token__ -p pypi-pypi-AgEIcHlwaS5vcmcCJDc0ZmY4NWVmLTk0ZjgtNGI5NS05ZmM3LWIyN2M2OTMwMGY0OQACKlszLCJlOGU2N2YxNy1hMWYyLTQ3YjMtOTUzMC00ZDE1YTM2M2YwOWYiXQAABiBWCOyR8YbuSSuyW_untgjDXeG10j7VBBqDAFxiSe_etw

git log --oneline

semantic-release version
semantic-release version --print

semantic-release publish

semantic-release --noop version
Cela te dira si une version serait générée.

semantic-release version --commit --tag --no-push

Cela va :
Lire les commits
Calculer la prochaine version (ex: 0.2.0)
Modifier __version__ dans gc7/__init__.py
Créer un commit et un tag localement

Remove-Item -Recurse -Force dist, src/gc7/gc7.egg-info

git commit --allow-empty -m "feat: add dummy feature for version bump"
git commit --allow-empty -m "fix: déclenchement de la release 1.0.1" 
git push origin main

voir conventional commits: https://www.conventionalcommits.org/en/v1.0.0/

En cas de volonté de revenir sur une version précédente (Problème avec PyPI: Interdit de reculer):
git revert <hash du commit> (pour ramener la main du dépôt GH)
dans le __ini__.py, mettre : __version__='x.y.z' (> au dernier de PyPI)
refaire le build + renvoi:
py -m build
twine upload dist/*

Désinstaller tous les packages de l'env global :
pip freeze | ForEach-Object { pip uninstall -y $_ }

# 1. Crée une branche temporaire pour garder les fichiers
git checkout --orphan temp_branch

# 2. Ajoute tous les fichiers à cette nouvelle branche
git add .

# 3. Fais un commit initial
git commit -m "Initial commit"

# 4. Supprime l'ancienne branche main
git branch -D main

# 5. Renomme la branche temporaire en main
git branch -m main

# 6. Force le push vers GitHub (⚠️ cela écrase l’historique distant)
git push -f origin main

git log main --decorate --oneline

---

from pymox_tools1 import greetings as gt
from pymox_tools1 import tokens as tk

if __name__ == "__main__":
    tk.tokens()
    print(gt.hello(), "\n" + gt.bye())

```
## 📦 Règles de versionnement (semantic‑release)

Semantic‑release détermine automatiquement le numéro de version en fonction du type de commit :

| Type de commit                         | Effet sur la version | Exemple de résultat |
|----------------------------------------|----------------------|---------------------|
| `fix:`                                 | patch                | `0.0.7 → 0.0.8`     |
| `feat:`                                | minor                | `0.0.7 → 0.1.0`     |
| `BREAKING CHANGE:` ou `feat!` / `fix!` | major                | `0.0.7 → 1.0.0`     |

---

Vérifier les secrets dans .env
