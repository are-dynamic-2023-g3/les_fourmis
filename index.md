# Recherche du chemin le plus court entre deux points à travers les fourmis

Notre objectif était de réaliser une méthode de recherche du chemin le plus court entre deux points en utilisant le comportement de fourmis face à cette problématique. Pour ce faire, nous avons d'abord du analyser et comprendre comment les fourmis réuissent un tel exploit. C'est grâce à leur phéromone ; en déposant des phéromones sur le chemin de retour entre la nourriture et leur nid, le chemin le plus court finit par être le plus emprunté.


+résultats marquants obtenus

## Finding the shortest path between two points thanks to ants

Our objective was to create a method for finding the shortest path between two points by using the behaviours of ants when doing such a task. To do so, we first had to understand how ants are capable of such a feat. It's thanks to their pheromones ; by deposing a trail of pheromones on their way back to their nest from food, the shortest path is eventually the one used the most.


+results

## Présentation de l'équipe

|(⌐■_■)|(⌐■_■)|(⌐■_■)|(⌐■_■)|
|-----|--|--|--|
| L. Huang | L. Mao | E. Liani  | E. Bouaziz  |

## Description synthétique du projet

**Problématique :** 

Comment les fourmis, après une certaine période de temps, trouvent systématiquement le chemin le plus court entre la nourriture et leur nid ?

**Hypothèse principale :**

Les fourmis relâchent des hormonnes sur le chemin du retour entre la nourriture et leur nid, aidant ainsi les fourmis suivantes dans leur quête

**Hypothèses secondaires :** 

**Objectifs :**

Coder une méthode de recherche de chemin le plus court à l'aide de phéromone, et d'aléatoire

**Critère(s) d'évaluation :**

Est-ce que le chemin final est-il bien le plus court?

Temps nécessaire pour y parvenir

## Présentation structurée des résultats

Notre modèle est donc le suivant:
1. Plusieurs fourmis éclaireuses parcourt plus ou moins au hasard l’environnement autour de leur nid
2. Lorsqu'une fourmi trouve une source de nourriture, elle rentre plus ou moins directement au nid, en laissant sur son chemin une piste de phéromones
3. Ces phéromones étant attractives, les fourmis passant à proximité vont avoir tendance à suivre, de façon plus ou moins directe, cette piste
4. Ces mêmes fourmis vont renforcer la piste sur le chemin du retour
5. Si plusieurs pistes sont possibles pour atteindre la nourriture, la piste la plus courte sera plus souvent fréquenté
6. La piste la courte sera alors plus renforcé, et donc de plus en plus fréquenté
7. Les pistes plus longues finiront par être abandonnés
8. Finalement, les fourmis ont choisi le chemin le plus court

Pour la réalisation du projet, nous avons utilisé python, et tkinter pour la modélisation en graphe 2D

Présentation du code et des résultats (tableaux, courbes, animations...) (**avec une analyse critique**).

## Lien vers page de blog : <a href="blog.html"> C'est ici ! </a>

## Bibliographie :


![mindmap](https://user-images.githubusercontent.com/125261735/232340293-6c45479c-329b-4403-a7f1-8a783b0fb669.png)

1. Shelokar, P. S., et al. « An Ant Colony Approach for Clustering ». Analytica Chimica Acta, vol.
509, n
o 2, mai 2004, p. 187‑95. ScienceDirect, https://doi.org/10.1016/j.aca.2003.12.032.
2. Subing, Zhang, et Liu Zemin. « A QoS routing algorithm based on ant algorithm ». ICC 2001.
IEEE International Conference on Communications. Conference Record (Cat. No.01CH37240),
vol. 5, 2001, p. 1581‑85 vol.5. IEEE Xplore, https://doi.org/10.1109/ICC.2001.937186.
3. Jayadeva, et al. « Ants Find the Shortest Path: A Mathematical Proof ». Swarm Intelligence,
vol. 7, n
o 1, mars 2013, p. 43‑62. Springer Link, https://doi.org/10.1007/s11721-013-0076-9.
4. Ghoseiri, Keivan, et Behnam Nadjari. « An Ant Colony Optimization Algorithm for the
Bi-Objective Shortest Path Problem ». Applied Soft Computing, vol. 10, n
o 4, septembre 2010,
p. 1237‑46. ScienceDirect, https://doi.org/10.1016/j.asoc.2009.09.014.
5. Fan, Hui, et al. « Solving a shortest path problem by ant algorithm ». Proceedings of 2004
International Conference on Machine Learning and Cybernetics (IEEE Cat. No.04EX826), vol. 5,
2004, p. 3174‑77 vol.5. IEEE Xplore, https://doi.org/10.1109/ICMLC.2004.1378581.
6. Vittori, Karla, et al. « Path Efficiency of Ant Foraging Trails in an Artificial Network ». Journal
of Theoretical Biology, vol. 239, n
o 4, avril 2006, p. 507‑15. PubMed,
https://doi.org/10.1016/j.jtbi.2005.08.017.
7. Dorigo, Marco, et Thomas Stützle. Ant Colony Optimization. 2004. direct.mit.edu,
https://doi.org/10.7551/mitpress/1290.001.0001.
8. Lee, Kwang Y., et Mohamed A. El-Sharkawi. « Fundamentals of Ant Colony Search Algorithms
». Modern Heuristic Optimization Techniques: Theory and Applications to Power Systems,
IEEE, 2008, p. 89‑100. IEEE Xplore, https://doi.org/10.1002/9780470225868.ch5.
9. Blum, Christian. « Ant Colony Optimization: Introduction and Recent Trends ». Physics of Life
Reviews, vol. 2, no 4, décembre 2005, p. 353‑73. ScienceDirect,
https://doi.org/10.1016/j.plrev.2005.10.001 .
10. Garg, Shivam, et al. « Distributed Algorithms from Arboreal Ants for the Shortest Path
Problem ». Proceedings of the National Academy of Sciences, vol. 120, nᵒ 6, février 2023, p.
e2207959120. DOI.org (Crossref), https://doi.org/10.1073/pnas.2207959120 .
11. Ghoseiri, Keivan, et Behnam Nadjari. « An Ant Colony Optimization Algorithm for the
Bi-Objective Shortest Path Problem ». Applied Soft Computing, vol. 10, nᵒ 4, septembre 2010,
p. 1237‑46. DOI.org (Crossref), https://doi.org/10.1016/j.asoc.2009.09.014 


