## Partie I : 
1. -> docker compose up -d
2. -> Base de donnée sql dans data
3. 
4. Nginx n'est pas nécessaire pour le moment, en effet même si on a deux service, et que ça pourrait servir à la communication, pour l'instant c'est juste 2 simple requête par api, dans le cas ou l'on voudrait une interface html avec css ou javascript, compléxifier que soit des redirection, utiliser plus de ressource ce qui nécessiterais de la répartition de charge ou alors de la sécurisation par https par exemple.
5. Complexifier le système avec une migration de docker compose vers Kubernetes n'est pas non plus idéal, car dans notre cas nous n'avont pas besoin des fonctionnalités de Kubernetes, comme la scalabilité ou même le monitoring de ressources, actuellement on a des APIs en local ou il n'y a qu'un seul utilisateur sur de petites requêtes.
Pour en avoir l'intérêt il faudrait soit un très grand nombre d'utilisateur ou alors des requêtes bien plus importantes.