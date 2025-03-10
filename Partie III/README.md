## Partie III :
Pour l'architecture d'une plateforme d'annotation automatique de données brutes

Nous mettons en place 3 conteneurs Docker :

Un pour l'API

Un pour la base de données

Un pour les scripts Python

Cela nous permet d'avoir des conteneurs plus légers, qui vont limiter les problèmes de dépendances, notamment pour Python s'il y a beaucoup de librairies et que certaines ne sont pas compatibles avec celles de la base de données ou de l'API. De plus, cela offre de la flexibilité : on peut simplement remplacer la base de données ou la restaurer en cas de problème.

Pour le reste, c'est assez simple :

Les utilisateurs peuvent ajouter des enregistrements bruts dans la base de données.

Les administrateurs peuvent également en ajouter, les récupérer, paramétrer des annotations automatiques, ajouter des modèles d'annotation ou gérer le monitoring.

Nous avons une seule base de données qui gère à la fois les données brutes et les données annotées, ainsi qu'une seule API qui gère à la fois les utilisateurs et les administrateurs.

Pour s'adapter à une question de scalabilité, nous pouvons répartir la base de données sur davantage de matériel, de même pour l'API. Il serait également envisageable d'isoler l'annotation automatique, qui est très coûteuse en ressources.