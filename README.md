# Les Fourmis
## Introduction
La recherche d'un plus court chemin d'un point à un autre est un problème de la vie quotidienne. Lorsqu’on cherche à aller quelque part, on cherche souvent le moyen d’y aller avec le chemin le plus court possible, c'est-à-dire avec la distance la plus petite. Pour étudier ce problème nous nous intéresserons alors aux fourmis. Sur Terre, le nombre de fourmis serait d'au moins 20 millions de milliards. Malgré leur petite taille, les fourmis dans la nature ont une capacité de trouver des “chemins” les plus courts entre leur fourmilière et la source de nourriture. Pour ce faire nous utiliserons une modélisation graphique en 2D pour comprendre l’influence des phéromones par les fourmis les permettant de reconnaître les “chemins” les plus courts. 

## Règles de modélisation
Notre modélisation se base sur 4 paramètres :
- La taille de l'environnement
- Le champ de vision d'une fourmis
- Le nombre de fourmis
- Le taux d'influence des phéromones sur les fourmis

Pour notre modélisation, on a créé un programme en Python permettant de modéliser à l’aide d’une fenêtre Tkinter la recherche du chemin le plus court par les fourmis lorsqu'il cherche une source de nourriture.
Pour le modéliser, nous avons utiliser plusieurs tableaux. Un premier tableau contient le "monde", avec les obstacles et le nombre de fourmis différentes qui sont passées sur une case donnée à l'itération en cours. Un deuxième tableau contient la liste des déplacements effectuées à l'itération en cours pour chacune des fourmis, afin d'éviter de compter deux fois le passage d'une même fourmi sur une case durant la même itération.

Notre modèle expliquant ce comportement est le suivant : 
1. Plusieurs fourmis explorent l’environnement autour de leur nid laissant des traces de phéromones sur leur chemin. 
2. Lorsqu’une fourmis découvre une source de nourriture, celle-ci revient au nid et repart. 
3. Les autres fourmis peuvent également trouver la même source de nourriture et laisser des phéromones. Cependant si plusieurs chemins sont possibles pour atteindre la même source de nourriture, celle étant la plus courte sera, dans le même temps, parcourue par plus de fourmis que le chemin le plus long. 
4. Le niveau de phéromones sur le chemin le plus court sera élevé, comme ces phéromones sont attractives. 
5. A terme, l'ensemble des fourmis choisissent le chemin le plus court.

## Membres du groupe 
Loïc Huang | Lucke Mao | Ethan Liani  | Elia Bouaziz  

## Compte rendu 
https://github.com/are-dynamic-2023-g3/les_fourmis/blob/main/blog.md
