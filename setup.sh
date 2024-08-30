#!/bin/bash

# Crée un environnement virtuel avec Python 3
python3 -m venv venv

# Active l'environnement virtuel
source venv/bin/activate

# Installe les dépendances depuis le fichier requirements.txt
pip install -r requirements.txt

# Message de confirmation
echo "Environnement virtuel créé et dépendances installées avec succès."
