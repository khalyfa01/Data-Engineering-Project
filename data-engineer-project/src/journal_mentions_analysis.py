import json
from collections import defaultdict



""" Chargement d'un fichier JSON """


def load_json_file(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)


"""
    Cette fonction extrait les mentions pour une entité spécifique.

    Args:
        data (dict): Données JSON.
        entity_key (str): Clé de l'entité.
        mention_key (str): Clé des mentions.

    Returns:
        dict: Dictionnaire des mentions par entité.
"""

def extract_mentions(data, entity_key, mention_key):
    mentions = defaultdict(set)

    for entity_id, entity_value in data[entity_key].items():
        entity_mentions = data[mention_key][entity_id]
        if entity_mentions:
            mentions[entity_value].update(entity_mentions)

    return mentions


    """
    Cette fonction identifie l'entité ayant le plus de mentions.

    Args:
        file_path (str): Chemin du fichier JSON.

    Returns:
        tuple: Entité avec le plus de mentions et le nombre de mentions.

    """

def extract_journal_with_most_mentions(file_path):

    data = load_json_file(file_path)

    articles_mentions = extract_mentions(data['news_articles_data'], 'journal', 'mentions')
    reviews_mentions = extract_mentions(data['reviews_data'], 'media', 'mentions')

    combined_mentions = defaultdict(set)
    combined_mentions.update(articles_mentions)
    combined_mentions.update(reviews_mentions)

    max_entity = max(combined_mentions, key=lambda k: len(combined_mentions[k]))

    return max_entity, len(combined_mentions[max_entity])



if __name__ == "__main__":


    try:

        file_path = 'C:\\Users\\FatihaKHALIFA\\OneDrive\\Desktop\\data-engineer-reflect_FK\\output.json'
        journal, mentions_count = extract_journal_with_most_mentions(file_path)
        print(f"Le média mentionnant le plus de films différents est '{journal}' avec {mentions_count} mentions.")


    except FileNotFoundError as e:
        print(f"Erreur : Fichier JSON non trouvé à l'emplacement : {file_path}")
    except json.JSONDecodeError as e:
        print(f"Erreur : Format JSON invalide pour le fichier à l'emplacement : {file_path}")
  