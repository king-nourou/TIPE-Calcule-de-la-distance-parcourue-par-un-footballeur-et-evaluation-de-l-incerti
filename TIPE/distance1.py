import matplotlib.pyplot as plt
import seaborn as sns
import random as rd
import numpy as np


distance_reelle = 361
nombre_points = 10
nombre_simulations = 1000
sigma_x = 1
sigma_y = 1


liste_abcisses1 = [52, 43.8, 36.8, 42.8, 49.6, 55.6, 75.2, 63.2, 46.8, 36.6, 28.4, 29.2, 29.8, 26.4, 27.4, 31.0, 33.2, 33.8, 33.4, 32.4, 33.2, 35.2, 38.4, 40.8, 41.8, 41.0, 41.0, 44.4, 48.2, 51.0, 50.0, 45.8, 37.4, 25.2, 16.8, 21.0, 26.4, 38.0, 47.2, 41.4, 39.2, 43.8, 36.8, 33.0, 29.4, 23.4, 17.6, 16.8, 19.8, 23.8, 24.8, 24.8, 23.6, 19.6, 15.6, 10.6, 5.0, 4.6, 9.0, 16.4]
liste_ordonnees1 = [42.6, 38.4, 38.4, 48.6, 56.8, 66.4, 58.2, 55.8, 57.2, 50.6, 49.8, 50.8, 53.4, 52.4, 50.4, 52.2, 54.4, 56.4, 56.8, 55.0, 56.8, 58.0, 57.6, 56.6, 53.6, 51.2, 48.8, 48.0, 48.4, 51.6, 58.0, 65.0, 68.4, 67.6, 61.4, 58.0, 55.0, 51.8, 58.2, 60.0, 60.2, 58.6, 58.8, 60.4, 60.8, 62.0, 62.2, 59.6, 59.4, 60.2, 57.8, 56.8, 55.8, 58.6, 58.2, 51.6, 59.8, 62.2, 61.4, 58.2]

liste_abcisses = liste_abcisses1[:10]
liste_ordonnees = liste_ordonnees1[:10]


def coordonnees(nombre_points):
# Taille du terrain de foot
    longueur = 105
    largeur = 68
    dmax = 30

    # Initialiser une liste pour stocker les coordonnées des points
    #liste_coordonnee = []
    liste_abcisses = []
    liste_ordonnees = []
    x0, y0 = 50, 25
    x = rd.uniform(max(0, x0 - dmax), min(longueur, x0 + dmax))
    y = rd.uniform(max(0, y0 - dmax), min(largeur, y0 + dmax))
# Placer des points aléatoires sur le terrain
    for _ in range(nombre_points):
        x0, y0 = x, y
        x = rd.uniform(max(0, x0 - dmax), min(longueur, x0 + dmax))
        y = rd.uniform(max(0, y0 - dmax), min(largeur, y0 + dmax))
        liste_abcisses.append(x)
        liste_ordonnees.append(y)
        #liste_coordonnee.append((x, y))
    return liste_abcisses, liste_ordonnees

liste_abcisses, liste_ordonnees = coordonnees(nombre_points)


def generateur_coordonnees_modele_2(liste_abcisses, liste_ordonnees, nombre_points, nombre_simulations):
    
        matrice_abcisses = [] # initialisation de l'ensemble des listes des abcisses
        matrice_ordonnees = [] # initialisation de l'ensemble des listes des ordonnees
        
        for _ in range(nombre_simulations):
            matrice_abcisses.append([])
            matrice_ordonnees.append([])
        
        for i in range(nombre_points-1): # iteration pour chaque coordonnees
            
            x0= liste_abcisses[i] # recuperation de la ieme abcisse
            y0 = liste_ordonnees[i] # recuperation de la ieme ordonnees
            
            x1= liste_abcisses[i+1]
            y1 = liste_ordonnees[i+1]
            
            
            for j in range(nombre_simulations): # On releve un point coordonnees au tour de deux chaque points
                
                 # aleatoirement
                x01 = rd.uniform(x0-1, x0+1)
                y01 = rd.uniform(y0-1, y0+1)
                 
                x02 = rd.uniform(x1-1, x1+1)
                y02 = rd.uniform(y1-1, y1+1)
                
                matrice_abcisses[j].append((x01,x02)) # ajout a la jeme liste des abcisses
                matrice_ordonnees[j].append((y01,y02)) # ajout a la jeme liste des ordonnees
            
            
        return matrice_abcisses, matrice_ordonnees
    


matrice_abcisses, matrice_ordonnees = generateur_coordonnees_modele_2(liste_abcisses, liste_ordonnees, nombre_points, nombre_simulations)

def distance_euclidienne_2(liste_abcisse, liste_ordonnee):
    distance = 0 
    n = len(liste_abcisse)
    for i in range(n):
        x1 = liste_abcisse[i][0]
        x2 = liste_abcisse[i][1] 
        y1 = liste_ordonnee[i][0]
        y2 = liste_ordonnee[i][1]
        distance += np.sqrt((x1-x2)**2+(y1-y2)**2)
    
    return distance

distance_2 = []

for i in range(nombre_simulations):

    distance_2.append(distance_euclidienne_2(matrice_abcisses[i], matrice_ordonnees[i]))
    
plt.hist(distance_2,'auto',alpha=0.4,edgecolor='blue')
plt.show()
print('distance moyenne 2:',np.mean(distance_2))



    
    



