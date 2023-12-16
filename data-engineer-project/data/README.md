# Data Engineer - Coding Challenge

## A) Python et Data Engineering

**Objectif** : Réaliser un code clair et proprement structuré. Mettre en avant les éléments considérés comme essentiels pour du code utilisable dans un environnement de production. Mettre l’accent sur vos connaissances en conception de jobs de manipulation de données ainsi que les bonnes pratiques python.

### 1. Les données

Vous avez à votre disposition les 4 fichiers de données suivants :
- ***movies.csv*** : contient les noms des films avec un id (id) et un nom (title)
- ***news_articles.csv*** : contient des titres d’articles de presse non spécialisée avec un titre (title) associés à un journal (journal) à une date donnée (date) ainsi qu’un id (id)
- ***news_articles.json*** : même structure que news_articles.csv mais en format JSON
- ***reviews.csv*** : contient des articles de presse spécialisée avec un titre (title), un id (id), un journal ou un site (media) et une date (date).

### 2. Le travail à réaliser

Votre travail est de construire une data pipeline permettant de traiter les données définies dans la partie précédente afin de générer le résultat décrit en partie 3.

Pour ce faire, vous devez mettre en place un projet en python organisé de la manière qui vous paraît la plus pertinente pour résoudre ce problème. Il est attendu que vous identifiez une structure de projet et une séparation des étapes nécessaires qui permettent de mettre en évidence vos connaissances autour du développement de jobs data en python.

Il faudra essayer de considérer les hypothèses de travail suivantes :
- Certaines étapes de votre data pipeline pourraient être réutilisées par d’autres data pipelines
- Votre code doit respecter les pratiques que vous mettriez en place dans un cadre professionnel au sein d’une équipe de plusieurs personnes

Il est volontairement laissé un cadre assez libre pour voir votre manière de structurer un projet, de rédiger votre code et de mettre en place les éléments qui vous semblent essentiels dans un projet d’équipe. Si vous n’avez pas le temps ou la possibilité de mettre en place certains aspects que vous considérez comme importants, il sera important de préciser ces aspects et comment vous les auriez mis en place. N’hésitez pas à argumenter votre proposition et les choix que vous faites si nécessaire.

### 3. Data pipeline

Votre data pipeline doit produire en sortie un unique fichier JSON qui représente les différents films et leurs mentions respectives dans les différents médias (non spécialisés et spécialisés), avec la date associée à chacune de ces mentions. Il peut y avoir plusieurs manières de modéliser cet output et vous pouvez justifier votre vision.

**Règles de gestion** :

- Un film est considéré comme mentionné dans un article s’il est mentionné dans le titre de la publication.
- Un film est considéré comme mentionné par un journal s’il est mentionné dans une publication émise par ce journal.

### 4. Traitement ad-hoc

Vous devez aussi mettre en place (hors de la data pipeline, vous pouvez considérer que c’est une partie annexe) une feature permettant de répondre à la problématique suivante :

- Extraire depuis le json produit par la data pipeline le nom du journal qui mentionne le plus de films différents ?

### 5. Le rendu

Vous devez partager votre proposition sur un repo git hébergé sur github.

### 6. Pour aller plus loin

Par retour de mail (ou directement sur le repo git si vous le souhaitez), vous pouvez répondre aux questions suivantes (ne nécessite pas d’implémentation dans votre projet) :

- Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
- Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?

<br />

## B) SQL

**Objectif** : Réaliser des requêtes SQL claires et facilement compréhensbles.

On possède les 2 tables suivantes :

Table ***application***, contenant des informations sur les applications du playstore Google.

Nom de la colonne | Type | Description
--- | --- | ---
id | int | Id de l’app
name | str | Nom de l’app
category | str | Catégorie de l’app
downloads | int | Nombre de téléchargements de l’app

Table ***review***, contenant des informations sur les avis sur les applications de la tableprécédente.

Nom de la colonne | Type | Description
--- | --- | ---
id | int | Id de l’avis
app_id | int | Id de l’app qui a reçu cet avis
rating | int | Note attribuée à l’app, entre 1 et 5
user_id | int | Id de l’utilisateur qui a laissé cet avis
review | str | Avis laissé pour l’app (ex: « appli trop bien »)

Vous écrirez les requêtes SQL permettant d’obtenir les informations suivantes :

- Le nombre d’applications téléchargées plus de 100 000 fois
- La note moyenne de l’application « DUNK »
- Les 10 applications les mieux notées en moyenne
- La catégorie la mieux notée en moyenne

