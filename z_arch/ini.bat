@echo off
chcp 65001 >nul

@REM Get-ChildItem -Path . -Directory -Recurse | Where-Object { $_.Name -eq "__pycache__" } | ForEach-Object { $_.FullName; Remove-Item -Path $_.FullName -Recurse -Force }

echo ----------------------------------------
echo Reset...
echo ----------------------------------------
echo .
echo Suppression des fichiers et dossiers...

@REM Efface :
@REM - .venv

call deactivate
rmdir /s /q .pytest_cache
rmdir /s /q .venv

echo Réinitialisation terminée (Configuration réinitialisée et environnement supprimé).


@REM Re-installation des dependances
echo ----------------------------------------
echo (Re)-Installation des dependances...
echo ----------------------------------------
if exist .venv\Scripts\python.exe (
    echo Environnement virtuel detecte - racine
    call .venv\Scripts\activate
) else (
    if exist .venv (
        echo [INFO] Environnement virtuel incomplet - suppression...
        rmdir /s /q .venv
    )
    echo Création de l'environnement virtuel - racine...
    python -m venv .venv
    @REM py -0
    @REM py -3.12 venv .venv # pour installer une VEnv avec py 3.12
    if not exist .venv\Scripts\python.exe (
        echo [ERREUR] Echec de creation de l'environnement virtuel.
        pause
        exit /b 1
    )
    call .venv\Scripts\activate
)

echo Mise a jour de pip...
python -m pip install --upgrade pip

pip install -r requirements.txt
if errorlevel 1 (
    echo [ERREUR] ❌ Installation echouée
    pause
    exit /b 1
)
echo [OK] ✅ Dépendances installées
echo.

@REM Retour à la racine
@REM cd ..

REM Vérification des fichiers .env
@REM echo ----------------------------------------
@REM echo Vérification de la configuration...
@REM echo ----------------------------------------

@REM if not exist ".env" (
@REM     echo [INFO] Fichier .env non trouvé - Création depuis .env.example...
@REM     copy .env.example .env
@REM     echo [ATTENTION] Éditez le fichier .env avec vos valeurs avant de lancer l'application
@REM )

@REM echo [OK] Fichiers .env configurés
@REM echo.

echo ========================================
echo   (Re)-Installation terminée !
echo ========================================
echo.
echo Prochaines étapes:
echo   1. Editez .env avec vos paramètres si nécessaires
echo   2. Lire README.md pour les instructions de lancement et d'utilisation

echo ========================================
echo   Lancement de main.py
echo ========================================
echo.
echo Démarrage automatique du script...
call flet run src/pymox_kit/main.py
