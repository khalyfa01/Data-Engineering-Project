# src/pipeline/data_loader.py

import pandas as pd

"""Chargement des données de films """

def load_movies_data(file_path):
    return load_data(file_path)

"""Chargement des données d'articles de presse"""   

def load_news_articles_data(file_path):
    return load_data(file_path)

"""Chargement des données de critiques"""    

def load_reviews_data(file_path):
    return load_data(file_path)


""" 
Fonction générique pour charger des données & gestion des erreurs, 
j'ai l'ajouter principalement pour gérer les erreurs de chargement des donnees
sinon on peut faire simplement un : return pd.read_csv(file_path) dans les fonctions 
précédentes sans faire appel à cette fonction :) 

"""

def load_data(file_path):

    try:

        return pd.read_csv(file_path)
        
    except FileNotFoundError as e:
        print(f"Erreur : Fichier non trouvé à l'emplacement : {file_path}")
        raise e
    except pd.errors.EmptyDataError as e:
        print(f"Erreur : Le fichier à l'emplacement {file_path} est vide ou a un format invalide.")
        raise e













