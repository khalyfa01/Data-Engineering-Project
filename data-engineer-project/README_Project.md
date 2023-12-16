# Projet Data Engineer
Ce projet vise à mettre en place une data pipeline pour traiter des données de films, d'articles de presse et de critiques, ainsi qu'à réaliser des requêtes SQL pour l'analyse d'applications, en utilisant un code clair et proprement structuré. Il se compose de deux parties principales : Python et Data Engineering, et SQL.

## Python et Data Engineering 
### Description
Cette section traite de la mise en place d'une pipeline en Python pour traiter les données de films, d'articles de presse et de critiques, afin de générer un fichier JSON récapitulant les mentions de films dans les différents médias. En utilisant un code clair, modifiable et réutilisable par d’autres data pipelines !

### Structure du Projet

- Dossier Principal
   - data/ : Contient les fichiers de données
   - src/
      - pipeline/
          - data_loader.py : Chargement des données depuis les fichiers CSV   
          - data_processor.py : Traitement des données pour trouver les mentions de films
          - json_writer.py : Génération du fichier JSON consolidé
      - journal_mentions_analysis.py : Extraction du média mentionnant le plus de films différents depuis le fichier JSON généré
      - main.py : Module principal pour exécuter la pipeline
      - test.py : Tests unitaires pour valider le chargement des données,.. (Optionnel)

### Exécution du Projet

Pour exécuter la pipeline :

```
python src/main.py

```
Le fichier de sortie est nommé output.json.

### Pour aller plus loin

- Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
- Quelles sont les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?
  
### Réponse:

**Pour traiter des volumes massifs de données, on peut considérer les aspects suivants :**

- On peut utiliser des techniques de lecture/écriture pour éviter de charger en mémoire tout le fichier simultanément. Par exemple, utiliser des librairies telles que Dask ou des options de lecture par morceaux de pandas (chunksize) peut être efficace. Par exemple dans la fonction load_data(file_path) employée pour importer les données, il suffit d'intégrer un deuxième paramètre, 'chunksize', afin de spécifier la quantité de lignes à lire à chaque itération. Cela pourrait se matérialiser ainsi (en prenant par exemple 10000 lignes):   ``` def load_data(file_path, chunksize=10000) ```.
  
- Traitement par morceaux de données : Travailler avec des sections de données en intégrant par exemple un paramètre 'article_chunk' dans la fonction  ``` def find_movie_mentions(movie_titles) ``` afin d'itérer sur des sections de données, et en ajoutant row['title'] dans la ligne :  ``` if re.search(r'\b{}\b'.format(re.escape(movie)), article_title, re.IGNORECASE) ``` Cela suppose que " article_chunk " est un morceau de données et la fonction iterrows() itère sur les lignes de ce morceau et effectue le traitement de recherche de mentions pour chaque titre d'article.
  
- Optimisation de l'écriture de fichiers JSON : Optimiser le processus d'écriture en écrivant les données morceau par morceau. Au lieu de json.dump(data, outfile), utiliser une boucle pour écrire chaque morceau :
- 
   ```
  for chunk in data:
    json.dump(chunk, outfile)
    ```
- Utilisation de traitement parallèle :  L'utilisation de plusieurs processus ou threads peut accélérer le traitement, on peut utiliser des bibliothèques de traitement parallèle pour traiter de gros volumes de données. Par exemple des outils comme Apache Spark ou Dask peuvent aider pour répartir les données sur plusieurs nœuds.
  
- On doit également considérer le stockage distribué avec des technologies comme Hadoop ou Spark, ainsi que l'utilisation de bases de données NoSQL pour gérer des volumes massifs de données.
 



## SQL
### Description
Cette partie concerne l'utilisation de requêtes SQL pour analyser des tables d'applications et de critiques. L'objectif est de réaliser des requêtes SQL claires et facilement compréhensibles !

On possède les 2 tables suivantes :

Table ***application***, contenant des informations sur les applications du playstore Google.

Nom de la colonne | Type | Description
--- | --- | ---
id | int | Id de l’app
name | str | Nom de l’app
category | str | Catégorie de l’app
downloads | int | Nombre de téléchargements de l’app

Table ***review***, contenant des informations sur les avis sur les applications de la table précédente.

Nom de la colonne | Type | Description
--- | --- | ---
id | int | Id de l’avis
app_id | int | Id de l’app qui a reçu cet avis
rating | int | Note attribuée à l’app, entre 1 et 5
user_id | int | Id de l’utilisateur qui a laissé cet avis
review | str | Avis laissé pour l’app (ex: « appli trop bien »)

### Requêtes SQL:

**- Le nombre d’applications téléchargées plus de 100 000 fois:**
   ```
   SELECT COUNT(*) AS nombre_applications
   FROM application
   WHERE downloads > 100000;
   ```
**- La note moyenne de l’application « DUNK »:**

  ```
  SELECT AVG(rating) AS note_moyenne
  FROM review
  WHERE app_id = (SELECT id FROM application WHERE name = 'DUNK');
  ```
**- Les 10 applications les mieux notées en moyenne:**

 ```
  SELECT app_id, AVG(rating) AS note_moyenne
  FROM review
  GROUP BY app_id
  ORDER BY note_moyenne DESC
  LIMIT 10;
 ```
**- La catégorie la mieux notée en moyenne:**
 ```
  SELECT a.category, AVG(r.rating) AS note_moyenne
  FROM application a
  JOIN review r ON a.id = r.app_id
  GROUP BY a.category
  ORDER BY note_moyenne DESC
  LIMIT 1;
 ```
