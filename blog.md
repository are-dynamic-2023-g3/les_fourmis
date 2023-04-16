## Travail effectué 

### Semaine 1

Pendant la 1ère semaine, nous avons discuter pour trouver un projet, et nous sommes tombés d'accord pour travailler sur les fourmis, et notamment leur recherche du chemin le plus court entre
la nourriture et leur nid ; elles sont en effet capable de systématique trouvé le chemin le plus court, malgré leur taille par rapport à leur environnement.

En recherchant un peu sur le sujet, on a découvert que notre interet était partagé, et qu'il existait un Ant Colony Optimzation algorithm

https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms

### Semaine 2

Au cours des cette semaine, nous avons pu réfléchir au modèle que nous allions pouvoir suivre, afin d'avoir un objectif clair lors du code. Notre modèle est donc le suivant:
1. Plusieurs fourmis éclaireuses parcourt plus ou moins au hasard l’environnement autour de leur nid
2. Lorsqu'une fourmi trouve une source de nourriture, elle rentre plus ou moins directement au nid, en laissant sur son chemin une piste de phéromones
3. Ces phéromones étant attractives, les fourmis passant à proximité vont avoir tendance à suivre, de façon plus ou moins directe, cette piste
4. Ces mêmes fourmis vont renforcer la piste sur le chemin du retour
5. Si plusieurs pistes sont possibles pour atteindre la nourriture, la piste la plus courte sera plus souvent fréquenté
6. La piste la courte sera alors plus renforcé, et donc de plus en plus fréquenté
7. Les pistes plus longues finiront par être abandonnés
8. Finalement, les fourmis ont choisi le chemin le plus court


### Semaine 3

Au début de la semaine, nous avons eu notre séance de recherche documentaire en bibliothèque pour nous aider à remplir notre carnet de bord. Nous avons donc commencé à remplir ce dernier,
et avons pu établir une mind map afin de nous aider dans nos recherches.

![mindmap](https://user-images.githubusercontent.com/125261735/232339997-e6679534-2a33-4ac4-8738-d50f2884e2c2.png)


### Semaine 4

Cette semaine, nous commencons à rentrer dans le dur, le code. Nous avons commencé par construire un tableau et d'y mettre des obstacles. Nous avons codé des déplacements
pseudo aléatoire de fourmi, en faisant attention à ne pas passer à travers des obstacles.

![imagefourmis](https://user-images.githubusercontent.com/125261735/232340122-e884f8f8-4079-4e0d-b567-b7aab7e37969.PNG)


### Semaine 5

Durant cette semaine, nous nous sommes rendus compte qu'avec la façon de représenté les fourmis qui avait été fait la semaine précédente, il serait impossible de représenter une colonie qui explore en même temps. Nous sommes donc presque repartis de zéro et avons décidé d'utiliser des tableaux qui contiennent les informations nécessaires pour chaque fourmi.

### Semaine 6

Cette semaine est encore centrée sur le code. Le code a avancé et désormais il est possible de faire plusieurs itérations de déplacement à la suite à l'aide d'un bouton sur la page d'affichage. Malheureusement chaque itération prend un certain temps avant de s'effectuer, plus ou moins long dépendant de la taille du monde et du nombre de fourmis.

### Semaine 7

L'avancée du code de cette semaine se résume aux déplacements qui sont influencés. Tout d'abord nous avons implémenté un code qui trouve le chemin le plus court entre deux points (algorithme A*) afin de pouvoir simuler un champ de vision pour nos fourmis. Ensuite nous avons implémentés les phéromones avec l'aide d'autres tableaux et de dictionnaires. Après avoir réglé de nombreuses erreurs et corrigé le code une multitude de fois, les phéromones ne nous permettent pas de simuler la façon dont les fourmis trouvent le chemin le plus court entre le nid et la source de nourriture. Nos fourmis semble toujours se déplacer de façon plus ou moins aléatoire. Dans le code final, nous avons donc laissé la version avec les phéromones générant le moins d'erreurs et avec laquelle nous avons effectué le plus de tests. Malheureusement chaque itération peut prendre entre cinq et plusieurs dizaines de secondes, ce qui ralenti considérablement les tests.

<a href="index.html"> Retour à la page principale </a>
