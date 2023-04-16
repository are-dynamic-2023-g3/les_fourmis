from random import *
from tkinter import *

#les paramètres:
taille = 200
nb_fourmis = 50
vision = 10
influence_phero = 0.999

fen = Tk()
canvas = Canvas(fen, width=2*taille, height=2*taille, background="black")

#Les coordonnées du nid et de la nourriture
depart = (1,1)
arrive = (taille-2, taille-2)

#générer le tableau, avec les bords vides
def generer_tab(taille):
    tab = []
    for y in range(taille):
        tab.append([])
        for j in range(taille):
            tab[y].append(0)
    
    for i in range(0,taille):
        tab[i][0] = -1
        tab[i][taille-1] = -1

    for i in range(0,taille):
        tab[0][i] = -1
        tab[taille-1][i] = -1
    return tab

#vider les valeurs du tableau
def nettoyer_tab():
    global tab, taille
    for x in range(taille):
        for y in range(taille):
            if tab[x][y] != -1:
                tab[x][y] = 0

#generer des obstacles
def generer_obstacles(x0, y0, dist, prob_new, i):
    global tab, taille

    for x in range(taille):
        for y in range(taille):
                if max(abs(x-x0), abs(y-y0)) <= dist:
                    tab[x][y] = -1

    if i > 0:
        for x in range(max(x0-dist, 1), min(taille-2, x0+dist)):
            if random() <= prob_new:
                dist2 = randint(dist//4, 8*dist//10)
                generer_obstacles(x, max(1, y0-dist), dist2, prob_new, i-1)
            if random() <= prob_new:
                dist2 = randint(dist//4, 8*dist//10)
                generer_obstacles(x, min(taille-2, y0+dist), dist2, prob_new, i-1)

        for y in range(max(y0-dist, 1), min(taille-2, y0+dist)):
            if random() <= prob_new:
                dist2 = randint(dist//4, 8*dist//10)
                generer_obstacles(max(1, x0-dist), y, dist2, prob_new, i-1)
            if random() <= prob_new:
                dist2 = randint(dist//4, 8*dist//10)
                generer_obstacles(min(taille-2, x0+dist), y, dist2, prob_new, i-1)


#générer le tableau des cases
def generer_plan(tab):
    taille = len(tab)
    tab_cases = []

    for y in range(taille):
        tab_cases.append([])
        for x in range(taille):
            if tab[y][x] >= 0:
                case = canvas.create_rectangle(2*x+1+2,2*y+1+2,2*x+2+2,2*y+2+2, outline = "white")
                tab_cases[y].append(case)
            else:
                case = canvas.create_rectangle(2*x+1+2,2*y+1+2,2*x+2+2,2*y+2+2, outline = "black")
                tab_cases[y].append(case)
    return tab_cases

#initialiser les listes
def init_fourmis(nb_fourmis):
    global depart
    l = []
    for i in range(nb_fourmis):
        l.append([])
        l[i].append(depart)
    return l

def init_retours(nb_fourmis):
    l = []
    for i in range(nb_fourmis):
        l.append([])
        l[i].append(depart)
    return l

def init_etats(nb_fourmis):
    l = []
    for i in range(nb_fourmis):
        #[Retour? , Pheromones?]
        #Retour: -2 = stop temporaire, -1 = stop après aller, 0 = stop après retour, 1 = aller, 2 = retour
        #Pheromones: 0 = ignore, 1 = influence / 0 = ne dépose pas, 1 = dépose
        l.append([0,0])
    return l

def init_liste_vide(nb_fourmis):
    l = []
    for i in range(nb_fourmis):
        l.append([])
    return l

#liste contenant le chemin des fourmis à une itération
liste_fourmis = init_fourmis(nb_fourmis).copy()
#liste contenant la dernière case des itérations précédentes, à utiliser pour le retour
liste_retours = init_retours(nb_fourmis).copy()
#liste contenant les états des fourmis: si est sur le chemin de l'aller ou du retour ou si elle ne bouge pas, et si elle va ignorer ou non les pheromones
liste_etats = init_etats(nb_fourmis).copy()
#dictionnaire associant une coordonnée possédant des phéromones à la force de celle-ci
pheromones = {}
#liste contenant les cases de phéromones déjà traversées
liste_pheromones_passees = init_liste_vide(nb_fourmis).copy()
#liste contenant les futurs déplacements
a_venir = init_liste_vide(nb_fourmis).copy()



#Effectuer un déplacement aléatoire
def deplacement_une_fourmi(coord, fourmi):
    global tab

    x = coord[0]
    y = coord[1]
    dir = randint(0,1)
    sens = randint(0,1)

    if sens == 0:
        sens = -1

    if dir == 0:
        if tab[x][y+sens] != -1:
            y += sens
        elif tab[x][y-sens] != -1:
            y -= sens
    else:
        if tab[x+sens][y] != -1:
            x += sens
        elif tab[x-sens][y] != -1:
            x -= sens
    
    return (x,y)

#Effectuer un retour, en se dirigeant sur certaines cases des itérations précédentes
def retour_une_fourmi(coord, fourmi):
    global tab, liste_fourmis, liste_retours
    x,y = coord[0], coord[1]
    if len(liste_retours[fourmi]) == 0:
        liste_retours[fourmi].append(depart)
    path = shortest_path((x,y), (liste_retours[fourmi][-1]), tab)

    longueur = len(liste_fourmis[fourmi])
    i = 0

    while (longueur < 4999 and i < len(path)):
        if not path[i] in liste_fourmis[fourmi]:
            tab[path[i][0]][path[i][1]] += 1
        liste_fourmis[fourmi].append(path[i])

        if random() < 1/taille:
            ajout = False
            for phero in pheromones:
                if (phero[0]-path[i][0])**2 + (phero[1]-path[i][1])**2 <= vision**2:
                    pheromones[phero] += 1
                    ajout = True
            
            if ajout == False:
                if path[i] in pheromones:
                    pheromones[path[i]] += 1
                else:
                    pheromones[path[i]] = 1

        i += 1
        longueur += 1
    
    if liste_fourmis[fourmi][-1] == depart:
        liste_etats[fourmi][0] = 0

#Se diriger directement vers la nourriture, dans le cas où celle-ci est dans la vision de la fourmi
def diriger_nourriture(coord, fourmi):
    global tab, liste_fourmis, liste_retours
    x,y = coord[0], coord[1]
    path = shortest_path((x,y), arrive, tab)

    longueur = len(liste_fourmis[fourmi])
    i = 0

    while (longueur < 4999 and i < len(path)):
        if not path[i] in liste_fourmis[fourmi]:
            tab[path[i][0]][path[i][1]] += 1
        liste_fourmis[fourmi].append(path[i])
        i += 1
        longueur += 1
    
    if liste_fourmis[fourmi][-1] == arrive:
        liste_etats[fourmi][0] = -1
    else:
        liste_etats[fourmi][0] = -2

#Diriger la fourmi selon les phéromones autour d'elle
def influencer_pheromones(coord, fourmi):
    global tab, pheromones, liste_etats, liste_fourmis, a_venir, liste_pheromones_passees, liste_etats
    x = coord[0]
    y = coord[1]
    pheromones_proches = {}
    phero_possibles = []

    for phero in pheromones:
        if (not phero in liste_pheromones_passees[fourmi]) and (phero[0]-x)**2+(phero[1]-y)**2 <= vision**2:
            pheromones_proches[phero] = pheromones[phero]
    
    if pheromones_proches == {}:
        npos = deplacement_une_fourmi((x,y),fourmi)

        if not npos in liste_fourmis[fourmi]:
            tab[npos[0]][npos[1]] += 1
            liste_fourmis[fourmi].append(npos)
    
    else:
        for phero in pheromones_proches:
            for _i in range(pheromones_proches[phero]):
                phero_possibles.append(phero)
        
        choix = randint(0, len(phero_possibles)-1)
        phero_choix = phero_possibles[choix]
        liste_pheromones_passees[fourmi].append(phero_choix)

        path = shortest_path((x,y), phero_choix, tab)

        for case in path:
            a_venir[fourmi].append(case)


#effectuer les deplacements à toutes les fourmis, en regardant si la nourriture dans le champs de vision, ainsi que les phéromones
def deplacement_toutes_fourmis():
    global tab
    global liste_fourmis, liste_retours, liste_etats

    x0 = arrive[0]
    y0 = arrive[1]

    for fourmi in range(len(liste_fourmis)):
        x = liste_fourmis[fourmi][-1][0]
        y = liste_fourmis[fourmi][-1][1]
        
        if len(a_venir[fourmi]) != 0:
            print(a_venir[fourmi])
            if not a_venir[fourmi][0] in liste_fourmis[fourmi]:
                tab[a_venir[fourmi][0][0]][a_venir[fourmi][0][1]] += 1
            liste_fourmis[fourmi].append(a_venir[fourmi][0])
            del[a_venir[fourmi][0]]

        else:

            if liste_etats[fourmi][0] == 1:
                if ((x-x0)**2+(y-y0)**2 <= vision**2):
                    diriger_nourriture((x,y), fourmi)
                    
                    if (liste_fourmis[fourmi][-1] == arrive):
                        print("ARRIVE")
                    
                elif liste_etats[fourmi][1] == 1:
                    influencer_pheromones((x,y), fourmi)
                    if random() < influence_phero:
                        liste_etats[fourmi][1] = 1
                    else:
                        liste_etats[fourmi][1] = 0

                else:
                    npos = deplacement_une_fourmi((x,y),fourmi)

                    if not npos in liste_fourmis[fourmi]:
                        tab[npos[0]][npos[1]] += 1
                    liste_fourmis[fourmi].append(npos)

                    if npos == arrive:
                        liste_etats[fourmi][0] = -1
            
            if liste_etats[fourmi][0] == 2:
                retour_une_fourmi((x,y), fourmi)
                liste_retours[fourmi].pop()
                if (liste_fourmis[fourmi][-1] == depart):
                    print("DEPART")

#actualiser les couleurs des cases
def update_couleurs():
    global tab, tab_cases
    for x in range(taille):
        for y in range(taille):
            if tab[x][y] != -1:
                if tab[x][y] == 0:
                    canvas.itemconfig(tab_cases[x][y], outline = "white")
                elif tab[x][y] == 1:
                    canvas.itemconfig(tab_cases[x][y], outline = "light gray")
                elif tab[x][y] <= 5:
                    canvas.itemconfig(tab_cases[x][y], outline = "green")
                elif tab[x][y] <= 10:
                    canvas.itemconfig(tab_cases[x][y], outline = "yellow")
                elif tab[x][y] <= 15:
                    canvas.itemconfig(tab_cases[x][y], outline = "orange")
                else:
                    canvas.itemconfig(tab_cases[x][y], outline = "red")

#changement lorsque le bouton est appuyé
def changement():
    global tab
    nettoyer_tab()

    global liste_fourmis, liste_retours, liste_etats, liste_pheromones_passees, pheromones
    nliste = []
    print(pheromones)

    for i in range(len(liste_etats)):
        if liste_etats[i][0] == -1:
            liste_etats[i][0] = 2
            liste_pheromones_passees[i] = []
        if liste_etats[i][0] == 0 or liste_etats[i][0] == -2:
            liste_etats[i][0] = 1
            liste_retours[i] = []
            liste_retours[i].append(depart)

        if random() < influence_phero:
            liste_etats[i][1] = 1
        else:
            liste_etats[i][1] = 0

    for i in range(len(liste_fourmis)):
        nliste.append([])
        nliste[i].append(liste_fourmis[i][-1])
    liste_fourmis = nliste.copy()
    
    for i in range(5000):
        deplacement_toutes_fourmis()
    
    for i in range(nb_fourmis):
        if liste_etats[i][0] == 1:
            liste_retours[i].append(liste_fourmis[i][-1])

    canvas.after(0, update_couleurs)

#Effectuer 10 changements
def changement_plus():
    for i in range(10):
        changement()
        print(i)

import heapq

#Basé sur l'algorithme A*, pour trouver le chemin le plis rapide lorsque la nourriture est dans le champs de vision des fourmis
def shortest_path(start, end, matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    heap = [(0, start, [])]
    while heap:
        (cost, curr, path) = heapq.heappop(heap)
        if curr == end:
            return path + [end]
        if curr in visited:
            continue
        visited.add(curr)
        x, y = curr
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1),
                     (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != -1:
                if (nx, ny) not in visited:
                    if (nx-x, ny-y) in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        if (x, ny) not in visited and (nx, y) not in visited:
                            # Si les deux déplacements adjacents sont libres, on privilégie le déplacement en bas à droite
                            if matrix[x][ny] != -1 and matrix[nx][y] != -1:
                                new_path = path+[(x, ny), (nx, ny)]
                                for cx, cy in new_path[len(path):-1]:
                                    visited.discard((cx, cy))
                                heapq.heappush(heap, (cost+1, (nx, ny), new_path))
                            # Sinon, on utilise l'autre option de déplacement en diagonale
                            else:
                                heapq.heappush(heap, (cost+1, (nx, ny), path+[(nx, y), (nx, ny)]))
                        elif (x, ny) not in visited:
                            heapq.heappush(heap, (cost+1, (x, ny), path+[(x, ny)]))
                        elif (nx, y) not in visited:
                            heapq.heappush(heap, (cost+1, (nx, y), path+[(nx, y)]))
                    else:
                        heapq.heappush(heap, (cost+1, (nx, ny), path+[curr]))
    return []

####################################

#creer le tableau
tab = generer_tab(taille)


#creer les obstacles (ici 7)
for i in range(7):
    x = randint(0,taille-1)
    y = randint(0,taille-1)
    dist = randint(10,20)
    generer_obstacles(x, y, dist, 0.03, 3)

    
#creer les cases
tab_cases = generer_plan(tab)


#creer les boutons "suivant"
bouton = Button(fen, text ="Étape suivante", command = changement)
bouton2 = Button(fen, text ="Étape suivante x10", command = changement_plus)


bouton.pack()
bouton2.pack()
canvas.pack()

fen.mainloop() 