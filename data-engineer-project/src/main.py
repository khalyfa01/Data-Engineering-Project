# src/main.py

import json
from pipeline.data_loader import load_movies_data, load_news_articles_data, load_reviews_data
from pipeline.data_processor import find_movie_mentions
from pipeline.json_writer import generate_json_output

# Chargement des données

movies_data = load_movies_data('C:\\Users\\FatihaKHALIFA\\OneDrive\\Desktop\\data-engineer-reflect_FK\\data\\movies.csv')
news_articles_data = load_news_articles_data('C:\\Users\\FatihaKHALIFA\\OneDrive\\Desktop\\data-engineer-reflect_FK\\data\\news_articles.csv')
reviews_data = load_reviews_data('C:\\Users\\FatihaKHALIFA\\OneDrive\\Desktop\\data-engineer-reflect_FK\\data\\reviews.csv')

# Traitement des données: trouver les mentions de films dans les titres d'articles

movie_titles = movies_data['title'].tolist()
news_articles_data['mentions'] = news_articles_data['title'].apply(lambda x: find_movie_mentions(x, movie_titles))
reviews_data['mentions'] = reviews_data['title'].apply(lambda x: find_movie_mentions(x, movie_titles))

# Génération du fichier JSON: Fusion des données traitées et génération du fichier JSON

combined_data = {
    'movies_data': movies_data.to_dict(),
    'news_articles_data': news_articles_data.to_dict(),
    'reviews_data': reviews_data.to_dict()
}



generate_json_output(combined_data, 'output.json') 