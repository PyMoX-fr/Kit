<div style="text-align: center;">
    <img src="assets/imgs/PyMoX-Kit_Logo.png" alt="PyMoX-Kit">
</div>

# PyMoX-Kit

<div align="center"> <div style="background-color: #ccc; padding: 10px 20px; border-radius: 7px; display: inline-block; font-size: 18px; color: black;"> <span style="vertical-align: middle;"> Trousse à <b>Outils utiles pour devs en</b> </span> <a href="https://pymox.fr" target="_blank" rel="noopener noreferrer"> <img src="https://pymox.fr/assets/images/pymox_logo_tr_001.png" width="70" style="vertical-align: middle;" alt="Logo PyMoX FR"> </a> </div> </div>

----

<div align="center" style="margin-top: 0">

  <!-- Ligne OS -->
  <div style="margin: 0;">
    <img src="https://img.shields.io/badge/OS-Windows_&_Linux-0078D6" alt="Win & Linux compatibles">
    <img src="https://img.shields.io/badge/Windows-Ready-0078D6?logo=windows&logoColor=white" alt="Windows ready">
    <img src="https://img.shields.io/badge/Linux-Compatible-FCC624?logo=linux" alt="Linux compatible">
  </div>

  <!-- Ligne autres badges -->
  <div style="margin: 0;">
    <a href="https://www.python.org">
      <img src="https://img.shields.io/badge/Python-3.11→3.14-3776AB?logo=python">
    </a>
    <a href="https://pymox.fr/outils/logs/CHANGELOG">
      <img src="https://img.shields.io/github/v/tag/PyMoX-fr/PyMoX-fr.github.io?logo=python&logoColor=cyan&label=PyMoX.fr" alt="PyMoX">
    </a>
    <a href="https://pypi.org/project/pymox-kit">
      <img src="https://img.shields.io/pypi/v/pymox-kit?logo=python&logoColor=orange&label=PyMoX-Kit/Pypi.org" alt="PyMoX Kit">
    </a>
    </div>
    <div style="margin: 0;">
    <a href="https://github.com/PyMoX-fr/Kit">
      <img src="https://img.shields.io/badge/GitHub-Passing-2ea44f?logo=github&logoColor=white" alt="GitHub Ready">
    </a>
  </div>

</div>

## Installation

```bash
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip
pip install pymox_kit
```

## Utilisation

```python
from pytmox_kit import *

print(Hello())
```

----

## Dev & exécution locale du package

Vous pouvez lancer la librairie de plusieurs façons.

- Exécuter le package (recommandé) :

```powershell
$env:PYTHONPATH='src'; python -m pymox_kit
```

- Afficher la version du package :

```powershell
$env:PYTHONPATH='src'; python -m pymox_kit --version
```

- Exécuter un module directement (utile pour tests rapides) :

```powershell
& .venv\Scripts\python.exe src\pymox_kit\tokens.py
```

Notes :

- Le package expose désormais un `__main__.py` pour supporter `python -m pymox_kit`.
- `main.py` définit `main()` (importable: `from pymox_kit.main import main`) et peut être exécuté directement. Les importations sont résilientes : que vous lanciez depuis la racine du dépôt ou après installation, l'exécution devrait fonctionner.

## Contribution

Pour tester la lib **PyMox_Kit** : [![GitHub](https://img.shields.io/badge/GitHub-Dépôt_Test_Kit-2ea44f?logo=github&logoColor=white)](https://github.com/PyMoX-fr/Kit)

Si volonté d' ↑ la lib : → Merge Request [![GitHub Passing](https://img.shields.io/badge/GitHub-PyMox_Kit-2ea44f?logo=github&logoColor=white)](https://github.com/PyMoX-fr/Kit)

## Help

[![GitHub Issue](https://img.shields.io/badge/GitHub-PyMox_Kit_Issues-2ea44f?logo=github&logoColor=white)](https://github.com/PyMoX-fr/Kit/issues)
