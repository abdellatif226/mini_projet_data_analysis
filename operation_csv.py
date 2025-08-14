import pandas as pd

# Charger le fichier CSV
df_burkina = pd.read_csv('burkina_location.csv')

# Afficher les 5 premières lignes pour s'assurer que tout est correct
print("Données originales (5 premières lignes) :")
print(df_burkina.head())
print("-" * 30)

# 4.1 Extraire les données contenant le nom 'gounghin'
# La méthode .str.contains() permet de chercher une sous-chaîne dans la colonne
df_gounghin = df_burkina[df_burkina['location_name'].str.contains('gounghin', case=False, na=False)]
df_gounghin.to_csv('gounghin.csv', index=False)
print("Fichier 'gounghin.csv' créé avec les données contenant le nom 'gounghin'.")
print(df_gounghin)
print("-" * 30)


# 4.2 Extraire les lieux dont les premières lettres sont comprises entre 'A' et 'P'
# Utiliser la méthode .str.startswith() pour filtrer les noms de lieux
df_a_to_p = df_burkina[df_burkina['location_name'].str.upper().str[0].between('A', 'P')]
print("Données filtrées de 'A' à 'P' (5 premières lignes) :")
print(df_a_to_p.head())
print("-" * 30)

# 4.3 Identifier les coordonnées minimales et les noms de lieux correspondants
min_lat = df_a_to_p['lat'].min()
min_long = df_a_to_p['long'].min()

print(f"Latitude minimale (entre 'A' et 'P') : {min_lat}")
print(f"Longitude minimale (entre 'A' et 'P') : {min_long}")

# Trouver les noms de lieux qui correspondent à la latitude minimale
lieu_min_lat = df_a_to_p[df_a_to_p['lat'] == min_lat]['location_name'].values
print(f"Lieu(x) correspondant(s) à la latitude minimale : {lieu_min_lat}")

# Trouver les noms de lieux qui correspondent à la longitude minimale
lieu_min_long = df_a_to_p[df_a_to_p['long'] == min_long]['location_name'].values
print(f"Lieu(x) correspondant(s) à la longitude minimale : {lieu_min_long}")
print("-" * 30)


# 4.4 Quels sont les lieux dont les coordonnées sont comprises entre (lat >= 11 et long <= 0.5)
df_specific_coords = df_burkina[(df_burkina['lat'] >= 11) & (df_burkina['long'] <= 0.5)]
print("Lieux dont les coordonnées sont (lat >= 11 et long <= 0.5) :")
print(df_specific_coords)
print("-" * 30)