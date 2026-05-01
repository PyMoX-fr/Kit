# Se placer dans la racine du projet
Set-Location -Path "$PSScriptRoot"

# Lancer explicitement l'app racine
uv run --active flet run -r
