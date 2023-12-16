# src/pipeline/json_writer.py
import json 

"""
    Cette fonction génère un fichier JSON à partir des données fournies.

    Args:
        data (dict): Données à sauvegarder dans le fichier JSON.
        output_file (str): Chemin du fichier de sortie.
"""

def generate_json_output(data, output_file):

    with open(output_file, 'w', encoding='utf-8') as outfile:  # Pour assurer l'encodage en utf-8
        json.dump(data, outfile, ensure_ascii=False)  # ensure_ascii=False: pour conserver les caractères spéciaux, sinon il va les remplacer par "\u00e0"
