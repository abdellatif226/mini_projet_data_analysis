import pandas as pd

# Définir l'URL du fichier zip (optionnel si vous le téléchargez manuellement)
url = 'http://download.geonames.org/export/dump/BF.zip'
import requests, zipfile, io
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

# Lire le fichier BF.txt en tant que DataFrame
# Le fichier est délimité par des tabulations et n'a pas d'en-tête
# Les colonnes sont identifiées par leur position (0, 1, 4, 5)
df = pd.read_csv('BF.txt', sep='\t', header=None, encoding='utf-8')

# Sélectionner les colonnes nécessaires
# geonameid est la colonne 0
# name est la colonne 1
# latitude est la colonne 4
# longitude est la colonne 5
df_filtered = df[[0, 1, 4, 5]]

# Renommer les colonnes pour une meilleure lisibilité
df_filtered.columns = ['ID', 'location_name', 'lat', 'long']

# Afficher les 5 premières lignes pour vérifier
print(df_filtered.head())

# Sauvegarder le DataFrame dans un nouveau fichier CSV
df_filtered.to_csv('burkina_location.csv', index=False, encoding='utf-8')

print("\nLe fichier 'burkina_location.csv' a été créé avec succès.")