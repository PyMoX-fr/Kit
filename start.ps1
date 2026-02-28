param(
  [ValidateSet("run", "0", "1", "help", "--help")]
  [string]$mode = "run",

  [Alias("h", "help")]
  [switch]$HelpSwitch
)

# Encodage UTF‑8 complet
[System.Console]::InputEncoding = [System.Text.Encoding]::UTF8
[System.Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8


function Show-Help {
  Write-Host "Utilisation : ./start [mode]"
  Write-Host "  Sans argument  -> (.venv) flet run main.py"
  Write-Host "  0              -> Reset total (VEnv + dépendances)"
  Write-Host "  1              -> Ré-installe uniquement PyMoX_Kit"
}

function Deactivate-ExistingVenv {
  if (Get-Command deactivate -ErrorAction SilentlyContinue) {
    Write-Host "Je sors du venv actuel et le vide..."
    deactivate
    Write-Host "1 - Sorti → Root."
  }
}

function Remove-Venv {
  if (Test-Path ".venv") {
    Write-Host "2 - Suppression du VE (Virtual Environment)..."
    Remove-Item ".venv" -Recurse -Force
    Write-Host "Suppression du VE terminée."
  }
}

function Ensure-Venv {
  Write-Host "Création de l'environnement virtuel ← racine..."
  python -m venv .venv
  if (-not (Test-Path ".venv/Scripts/python.exe")) {
    Write-Host "[ERREUR] Échec de création de l'environnement virtuel."
    exit 1
  }
}

function Activate-Venv {
  if (-not (Test-Path ".venv/Scripts/Activate.ps1")) {
    Write-Host "[ERREUR] Le venv n'existe pas. Lancez le mode 0 pour le créer."
    exit 1
  }
  . ".\.venv\Scripts\Activate.ps1"
  Write-Host "VEnv activé."
}

function Upgrade-Pip {
  Write-Host "Mise à jour de pip..."
  python -m pip install --upgrade pip
}

function Install-Requirements {
  Write-Host "Installation des dépendances..."
  pip install -r requirements.txt
  if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERREUR] ❌ Installation échouée"
    exit 1
  }
  Write-Host "[OK] ✅ Dépendances installées"
}

function Run-PymoxKitFresh {
  Write-Host "Réinstallation de pymox_kit..."
  pip uninstall pymox_kit -y | Out-Null
  pip install pymox_kit
  if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERREUR] ❌ Réinstallation de pymox_kit échouée"
    exit 1
  }
}

function Start-App {
  Write-Host "========================================"
  Write-Host "  Lancement de ./main.py"
  Write-Host "========================================"
  Write-Host ""
  Write-Host "Démarrage automatique du script ./main.py... 🚀"
  Write-Host ""
  flet run -d -r --ignore-dirs __pycache__ main.py
}

if ($HelpSwitch -or $mode -in @("help", "--help")) {
  Show-Help
  exit 0
}

switch ($mode) {
  "0" {
    Write-Host "----------------------------------------"
    Write-Host "Reset..."
    Write-Host "----------------------------------------"
    Write-Host ""
    Write-Host "Suppression des fichiers et dossiers..."
    Write-Host ""

    Deactivate-ExistingVenv

    if (Test-Path ".pytest_cache") {
      Remove-Item ".pytest_cache" -Recurse -Force
      Write-Host "Suppression de .pytest_cache terminée."
    }

    Remove-Venv

    Write-Host "Réinitialisation terminée (Configuration réinitialisée et environnement supprimé)."
    Write-Host ""

    Write-Host "----------------------------------------"
    Write-Host "(Re)-Installation des dependances..."
    Write-Host "----------------------------------------"

    Ensure-Venv
    Activate-Venv
    Upgrade-Pip
    Install-Requirements

    Write-Host ""
    Write-Host "========================================"
    Write-Host "  (Re)-Installation terminée !"
    Write-Host "========================================"
    Write-Host ""
    Write-Host "Prochaines étapes:"
    Write-Host "  1. Copier/coller .env_example en .env le cas échéant"
    Write-Host "  2. Lire README.md pour les instructions détaillées"
    Write-Host ""

    Start-App
  }
  "1" {
    Write-Host "Mode 1 : réinstallation rapide de pymox_kit"
    Activate-Venv
    Run-PymoxKitFresh
    Start-App
  }
  default {
    if (-not (Test-Path ".venv/Scripts/python.exe")) {
      Write-Host "[ERREUR] Aucun .venv détecté. Lancer ./start 0 pour initialiser l'environnement."
      exit 1
    }
    $minVersion = [Version]"7.5.4"

    if ($PSVersionTable.PSVersion -lt $minVersion) {
      Write-Host ""
      Write-Host "*** ATTENTION: INSTALLER PowerShell >= 7.5.4 pour profiter pleinement des messages (Voir README.md, Tips/2) ***"
      Write-Host ""
      Write-Host "Appuyer sur une touche pour continuer..."
      Write-Host ""
      [void][System.Console]::ReadKey($true)
    }
    Activate-Venv
    Start-App
  }
}
