# src/pipeline/data_processor.py

# Traitement des données

"""
    Trouve les mentions de films dans les article en utilisant les expressions régulieres.

    Args:
        article_title (str): Titre de l'article.
        movie_titles (list): Liste des titres de films.

    Returns:
        list: Liste des films mentionnés dans le titre de l'article.
"""

import re

def find_movie_mentions(article_title, movie_titles):
    mentions = []
    for movie in movie_titles:
        if re.search(r'\b{}\b'.format(re.escape(movie)), article_title, re.IGNORECASE):
            mentions.append(movie)
    return mentions


