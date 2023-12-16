import unittest

from pipeline.data_loader import load_movies_data, load_news_articles_data, load_reviews_data


"""
Utilisation de la classe unittest.TestCase pour créer des méthodes de test, et les methodes 'assert' 
pour vérifier que les résultats attendus sont obtenus:)

"""

class TestDataLoader(unittest.TestCase):

    def test_load_movies_data(self):

        # Teste le chargement des données de films
        
        movies_data = load_movies_data('C:\\Users\\FatihaKHALIFA\\OneDrive\\Desktop\\data-engineer-reflect_FK\\data\\movies.csv')

        self.assertIsNotNone(movies_data)  # Vérifiez si les données sont chargées

    def test_load_news_articles_data(self):

        # Teste le chargement des données d'articles de presse.

        news_articles_data = load_news_articles_data('C:\\Users\\FatihaKHALIFA\\OneDrive\\Desktop\\data-engineer-reflect_FK\\data\\news_articles.csv')
        self.assertIsNotNone(news_articles_data)  # Vérifiez si les données sont chargées

    def test_load_reviews_data(self):

        # Teste le chargement des données de critiques.

        reviews_data = load_movies_data('C:\\Users\\FatihaKHALIFA\\OneDrive\\Desktop\\data-engineer-reflect_FK\\data\\reviews.csv')

        self.assertIsNotNone(reviews_data)  # Vérifiez si les données sont chargées

""" 

On peut ajouter d'autres tests par exemple: 

# Tests de validation de la structure du fichier JSON généré : en vérifiant par exemple 
# la présence des clés importantes ou le format des données.
# Tests de fonctionnalités spécifiques,... .

"""

if __name__ == '__main__':
    unittest.main()

