
# Mini Projet - Analyse de données du Burkina Faso

Ce projet Python a pour objectif de réaliser une analyse de données géographiques sur le Burkina Faso. Le script télécharge, nettoie et traite un ensemble de données provenant de Geonames.org, puis génère des fichiers CSV et un fichier Excel récapitulatif pour les résultats.

# Fonctionnalités

Le script effectue les tâches suivantes :

Vérification et Installation des Dépendances : Il s'assure que toutes les bibliothèques requises (pandas, requests, openpyxl) sont installées et les installe automatiquement si nécessaire.

Téléchargement des Données : Il télécharge le fichier de données compressé (BF.zip) directement depuis l'API de Geonames.org.

Prétraitement : Il décompresse le fichier, lit les données, filtre les colonnes pertinentes (ID, location_name, lat, long) et les enregistre dans un nouveau fichier CSV appelé burkina_location.csv.

Analyse de Données : Il réalise plusieurs extractions, notamment :

Les lieux dont le nom contient "gounghin".

Les lieux dont le nom commence par une lettre comprise entre 'A' et 'P'.

Les coordonnées minimales (latitude et longitude) pour les lieux de la catégorie précédente.

Les lieux ayant des coordonnées spécifiques (lat >= 11 et long <= 0.5).

Génération de Rapport : Il consolide les résultats dans un fichier Excel nommé mini_projet.xlsx avec deux feuilles : gounghin et A_to_P.

# Prérequis

Pour exécuter ce projet, vous devez disposer d'une installation de Python et de Jupyter Notebook (ou JupyterLab) sur votre système.

Utilisation
Ouvrez le fichier mini_projet.ipynb (le carnet Jupyter) dans votre environnement Jupyter.

Exécutez chaque cellule du carnet séquentiellement, de haut en bas.

Le script affichera les étapes d'exécution et les aperçus des données directement dans la sortie de chaque cellule.

Une fois l'exécution terminée, les fichiers suivants seront générés dans le même répertoire que le carnet :

burkina_location.csv : Le fichier de données filtré pour le Burkina Faso.

gounghin.csv : Une extraction des lieux nommés "gounghin".

mini_projet.xlsx : Le rapport final consolidant les résultats.

Un dossier BF contenant le fichier brut BF.txt sera également créé.

# Auteur

Ce projet a été réalisé dans le cadre d'un mini-projet d'ecole # Master FD_IA.
