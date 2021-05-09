# FMSI

![epita](https://img.shields.io/badge/EPITA-project-brightgreen)

## A Propos

Ce travail a été réalisé pour un projet d'EPITA. Vous y trouverez ici nos codes afin de tester les performances de différents algorithmes de crackage RSA.

Il a été réalisé par:

- Quentin Briolant
- Maxime Brouillard
- Damien Champeyroux
- Inès Chanou
- Elsa Laussucq

## Prérequis

1. Tout d'abord, vous devez cloner le projet.

```shell
git clone https://github.com/gastbob40/fmsi
```

2. **Créer un `environnement virtuel`, afin d'installer les dépendances localement.** Pour plus d'informations sur les environnements virtuels, [cliquez ici] (https://docs.python.org/3/library/venv.html).

```shell
python -m venv .venv
```

3. **Activer l'environnement virtuel**

Linux/macOS:

```shell
# Using bash/zsh
source .venv/bin/activate
# Using fish
. .venv/bin/activate.fish
# Using csh/tcsh
source .venv/bin/activate.csh
``` 

Windows:

```
# cmd.exe
.venv\Scripts\activate.bat
# PowerShell
.venv\Scripts\Activate.ps1
```

4. **Installer les dépendances**

```
pip install -r requirements.txt
```


## Lancer le code

Le point d'entrée de notre code est le fichier "hacker.py". Ainsi:

```
python hacker.py
```
