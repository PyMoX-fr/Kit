@echo off
chcp 65001 >nul

Supprime la lib PyMox-Kit et la re-installe pour s'assurer d'avoir la dernière version

@REM Get-ChildItem -Path . -Directory -Recurse | Where-Object { $_.Name -eq "__pycache__" } | ForEach-Object { $_.FullName; Remove-Item -Path $_.FullName -Recurse -Force }

echo ----------------------------------------
echo Reset...
echo ----------------------------------------
echo .
echo Suppression des fichiers et dossiers...

@REM Efface :
@REM - .venv

@REM call deactivate
@REM rmdir /s /q .pytest_cache
@REM rmdir /s /q .venv

call pip uninstall pymox_kit -y

echo Réinitialisation terminée (Configuration réinitialisée et environnement supprimé).


@REM @REM Re-installation des dependances
@REM echo ----------------------------------------
@REM echo (Re)-Installation des dependances...
@REM echo ----------------------------------------
@REM if exist .venv\Scripts\python.exe (
@REM     echo Environnement virtuel detecte - racine
@REM     call .venv\Scripts\activate
@REM ) else (
@REM     if exist .venv (
@REM         echo [INFO] Environnement virtuel incomplet - suppression...
@REM         rmdir /s /q .venv
@REM     )
@REM     echo Création de l'environnement virtuel - racine...
@REM     python -m venv .venv
@REM     @REM py -0
@REM     @REM py -3.12 venv .venv # pour installer une VEnv avec py 3.12
@REM     if not exist .venv\Scripts\python.exe (
@REM         echo [ERREUR] Echec de creation de l'environnement virtuel.
@REM         pause
@REM         exit /b 1
@REM     )
@REM     call .venv\Scripts\activate
@REM )

@REM echo Mise a jour de pip...
@REM python -m pip install --upgrade pip

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
