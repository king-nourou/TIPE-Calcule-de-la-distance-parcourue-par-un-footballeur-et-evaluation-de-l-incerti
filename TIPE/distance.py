import matplotlib.pyplot as plt
import seaborn as sns
import random as rd
import numpy as np


liste_distance_reelle1 = [51, 98, 123, 137, 151, 171, 217, 259, 283, 308, 330, 361]

lu = [38, 94, 125, 143, 160, 180, 227, 273, 299, 324, 345, 382]
lu1 = [112, 144, 179, 262, 307,356]

lg = [40, 98, 133, 156, 178, 202, 252, 300, 329, 358,383, 423]

lincer = [3.5, 4.1, 4, 3.1, 2.9, 2.8]
lzsc = [7, 2.9, 1.4, 1.29, 0.2, 1.65]

distance_reelle = 361
nombre_points =60
nombre_simulations = 1000

sigma_x = 1
sigma_y = 1


liste_abcisses1 = [52, 43.8, 36.8, 42.8, 49.6, 55.6, 75.2, 63.2, 46.8, 36.6, 28.4, 29.2, 29.8, 26.4, 27.4, 31.0, 33.2, 33.8, 33.4, 32.4, 33.2, 35.2, 38.4, 40.8, 41.8, 41.0, 41.0, 44.4, 48.2, 51.0, 50.0, 45.8, 37.4, 25.2, 16.8, 21.0, 26.4, 38.0, 47.2, 41.4, 39.2, 43.8, 36.8, 33.0, 29.4, 23.4, 17.6, 16.8, 19.8, 23.8, 24.8, 24.8, 23.6, 19.6, 15.6, 10.6, 5.0, 4.6, 9.0, 16.4]
liste_ordonnees1 = [42.6, 38.4, 38.4, 48.6, 56.8, 66.4, 58.2, 55.8, 57.2, 50.6, 49.8, 50.8, 53.4, 52.4, 50.4, 52.2, 54.4, 56.4, 56.8, 55.0, 56.8, 58.0, 57.6, 56.6, 53.6, 51.2, 48.8, 48.0, 48.4, 51.6, 58.0, 65.0, 68.4, 67.6, 61.4, 58.0, 55.0, 51.8, 58.2, 60.0, 60.2, 58.6, 58.8, 60.4, 60.8, 62.0, 62.2, 59.6, 59.4, 60.2, 57.8, 56.8, 55.8, 58.6, 58.2, 51.6, 59.8, 62.2, 61.4, 58.2]

liste_abcisses2 = [52.8, 52.0, 49.6, 43.8, 40.4, 38.4, 37.2, 36.6, 38.8, 42.8, 46.6, 49.8, 51.8, 56.0, 61.0, 63.4, 63.8, 63.2, 51.4, 47.0, 41.6, 36.6, 31.6, 28.4, 28.2, 29.0, 29.0, 29.8, 28.6, 26.4, 26.0, 27.4, 29.6, 31.0, 32.0, 33.0, 34.0, 33.6, 33.8, 33.4, 32.8, 32.4, 32.8, 33.4, 34.2, 35.2, 38.6, 39.6, 40.8, 41.8, 42.2, 42.2, 41.6, 41.2, 42.6, 44.4, 46.4, 48.4, 50.4, 50.8, 50.6, 50.0, 48.2, 45.8, 42.4, 31.4, 25.2, 19.0, 18.2, 16.8, 19.2, 21.0, 23.2, 26.6, 30.6, 37.8, 43.2, 47.0, 48.6, 41.2, 39.6, 39.2, 41.6, 43.8, 44.2, 42.2, 40.4, 38.4, 36.4, 32.6, 31.6, 28.4, 24.2, 22.2, 20.4, 21.0, 21.4, 22.6, 24.6, 28.4, 30.0, 29.6, 29.6, 30.0, 30.0, 28.4, 26.0, 24.2, 22.0, 20.0, 17.4, 15.0, 11.4, 9.0, 7.2, 8.6, 10.8, 13.4, 15.2, 16.4]
liste_ordonnees2 = [44.4, 42.6, 39.2, 38.2, 34.2, 35.2, 34.4, 38.4, 43.6, 48.8, 52.0, 56.8, 61.8, 66.6, 60.4, 58.2, 56.0, 55.8, 60.4, 57.2, 53.0, 50.6, 50.2, 49.6, 50.0, 50.6, 51.4, 53.4, 53.8, 52.2, 51.2, 50.4, 51.6, 52.2, 53.2, 54.2, 55.4, 56.4, 57.8, 56.6, 56.0, 55.8, 56.8, 57.8, 58.0, 57.4, 56.6, 55.0, 53.6, 53.6, 52.0, 51.2, 49.8, 48.8, 48.4, 48.2, 48.0, 48.4, 48.8, 51.6, 54.2, 58.0, 61.4, 65.0, 67.4, 68.4, 67.8, 64.6, 63.6, 61.6, 59.0, 58.2, 57.6, 55.0, 53.0, 51.8, 53.6, 58.0, 59.8, 60.0, 62.6, 60.4, 58.4, 58.8, 60.4, 61.6, 62.6, 63.0, 63.2, 63.6, 63.8, 65.2, 65.6, 65.2, 64.0, 63.2, 62.4, 61.8, 62.2, 63.0, 62.6, 60.8, 59.6, 59.4, 58.6, 58.4, 59.6, 62.0, 63.2, 60.8, 55.4, 53.8, 57.8, 62.6, 65.6, 65.0, 64.8, 64.0, 61.8, 58.4]

liste_abcisses = liste_abcisses1[:60]
liste_ordonnees = liste_ordonnees1[:60]
'''
def coordonnees(nombre_points):
    # Taille du terrain de foot
    longueur = 105
    largeur = 68
    dmax = 10

    # Initialiser une liste pour stocker les coordonnées des points
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
    return liste_abcisses, liste_ordonnees

# Décommenter cette ligne pour générer des coordonnées aléatoires
liste_abcisses, liste_ordonnees = coordonnees(nombre_points)

# Affichage des coordonnées
plt.plot(liste_abcisses, liste_ordonnees, 'bo')
plt.plot(liste_abcisses, liste_ordonnees, 'r-')
plt.xlim(0, 110)
plt.ylim(0, 70)
plt.show()
'''


def generateur_coordonnees_modele_1(liste_abcisses, liste_ordonnees, nombre_points, nombre_simulations):
    matrice_abcisses = []  # Initialisation de l'ensemble des listes des abcisses
    matrice_ordonnees = []  # Initialisation de l'ensemble des listes des ordonnees
    
    for _ in range(nombre_simulations):
        matrice_abcisses.append([])
        matrice_ordonnees.append([])
    
    for i in range(nombre_points):  # Iteration pour chaque coordonnee
        x0 = liste_abcisses[i]  # Recuperation de la ieme abcisse
        y0 = liste_ordonnees[i]  # Recuperation de la ieme ordonnee
        
        for j in range(nombre_simulations):  # On releve n points coordonnes autour de chaque point
            x1 = rd.uniform(x0 - sigma_x, x0 + sigma_x)  # Aleatoirement
            y1 = rd.uniform(y0 - sigma_y, y0 + sigma_y)
            
            matrice_abcisses[j].append(x1)  # Ajout à la jeme liste des abcisses
            matrice_ordonnees[j].append(y1)  # Ajout à la jeme liste des ordonnees
        
    return matrice_abcisses, matrice_ordonnees 


matrice_abcisses, matrice_ordonnees = generateur_coordonnees_modele_1(liste_abcisses, liste_ordonnees, nombre_points, nombre_simulations)
'''
plt.figure(figsize=(10, 8))
sns.heatmap(matrice_abcisses, annot=True, fmt='.2f', annot_kws={"size": 20}, linewidths=0.5)
plt.title('Matrice des abcisses générées avec la distribution gaussienne', fontsize=20)
plt.xlabel('abcisses', fontsize=20)
plt.ylabel('simulations', fontsize=20)
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(matrice_ordonnees, annot=True, fmt='.2f', annot_kws={"size": 20}, linewidths=0.5)
plt.title('Matrice des ordonnées générées avec la distribution gaussienne', fontsize=20)
plt.xlabel('ordonnées', fontsize=20)
plt.ylabel('simulations', fontsize=20)
plt.show()
'''
def distance_euclidienne(liste_abcisses, liste_ordonnees):
    n = len(liste_abcisses)
    distance = 0 
    for i in range(n-1):
        x1 = liste_abcisses[i]
        x2 = liste_abcisses[i+1]
        y1 = liste_ordonnees[i]
        y2 = liste_ordonnees[i+1]
        
        distance += np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance

# Simulation de la distance euclidienne pour chaque simulation
liste_distance = []
for i in range(nombre_simulations):
    liste_distance.append(distance_euclidienne(matrice_abcisses[i], matrice_ordonnees[i]))

# Affichage de l'histogramme des distances
plt.hist(liste_distance, bins='auto', alpha=0.4, edgecolor='blue')
plt.show()

distance_moyenne = np.mean(liste_distance)
distance_relevee = distance_euclidienne(liste_abcisses, liste_ordonnees)

print("distance reelle: ", distance_reelle)
print("Distance_relevee :", distance_relevee)
print('Distance moyenne = :', distance_moyenne)

def calcul_segments(liste_abcisses, liste_ordonnees):
    liste_segments = [] 
    n = len(liste_abcisses)
    
    for i in range(n-1):
        liste_segments.append(distance_euclidienne(liste_abcisses[i:i+2], liste_ordonnees[i:i+2]))
        
    return liste_segments

liste_segments = calcul_segments(liste_abcisses, liste_ordonnees)

def matrice_segment(matrice_abcisses, matrice_ordonnees):
    n = len(matrice_abcisses)
    matrice_segments = []
    for i in range(n):
        segments = calcul_segments(matrice_abcisses[i], matrice_ordonnees[i])
        matrice_segments.append(segments)
        
    return matrice_segments

matrice_segments = matrice_segment(matrice_abcisses, matrice_ordonnees)
'''
plt.figure(figsize=(10, 8))
sns.heatmap(matrice_segments, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"size": 20}, linewidths=0.5)
plt.title(' Matrice des Segments')
plt.xlabel('Segments')
plt.ylabel('Simulations')
plt.show()
'''

#print("Matrice des segments:", matrice_segment(matrice_abcisses, matrice_ordonnees))

def incertitude_segment(sigma_x, sigma_y, liste_abcisses, liste_ordonnees, liste_segments):
    n = len(liste_segments)
    liste_incertitudes = []
    
    for i in range(n):
        x1 = liste_abcisses[i]
        x2 = liste_abcisses[i+1]
        y1 = liste_ordonnees[i]
        y2 = liste_ordonnees[i+1]
        d = liste_segments[i]
        
        incertitude_segment = np.sqrt(2) * np.sqrt(((x1 - x2) / d * sigma_x)**2 + ((y1 - y2) / d * sigma_y)**2)
        
        liste_incertitudes.append(incertitude_segment)
    return liste_incertitudes

incertitudes_segments = incertitude_segment(sigma_x, sigma_y, liste_abcisses, liste_ordonnees, liste_segments)


#print("Incertitudes des segments:", incertitude_segment(sigma_x, sigma_y, liste_abcisses,liste_ordonnees, liste_segments))

def moyenne_colonnes(matrice):
    n = len(matrice)
    m = len(matrice[0])
    moyennes_colonne = []

    for j in range(m):
        colonne = [matrice[i][j] for i in range(n)]
        moyenne_colonne = np.mean(colonne)
        moyennes_colonne.append(moyenne_colonne)

    return moyennes_colonne

def matrice_covariance(liste_segments, matrice_segments):
    n = len(matrice_segments[0])
    mat_cov = np.zeros((n, n))
    seg_moy = moyenne_colonnes(matrice_segments)
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat_cov[i][j] += (matrice_segments[k][i] - seg_moy[i]) * (matrice_segments[k][j] - seg_moy[j]) / (n - 1)
    
    return mat_cov
    
matrice_covariance = matrice_covariance(liste_segments, matrice_segments)


'''
# Visualiser la matrice de covariance
plt.figure(figsize=(10, 8))
sns.heatmap(matrice_covariance, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"size": 20}, linewidths=0.5)
plt.title(' Matrice de Covariance des Segments')
plt.xlabel('Segments')
plt.ylabel('Segments')
plt.show()
'''
#print(matrice_covariance(liste_segments, matrice_segments))

def coefficient_correlation(matrice_covariance):
    n  = len(matrice_covariance)
    mat_corl = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            mat_corl[i][j] = matrice_covariance[i][j]/np.sqrt(matrice_covariance[i][i]*matrice_covariance[j][j])
            
    return mat_corl
        
matrice_correlation = coefficient_correlation(matrice_covariance)

#print(coefficient_correlation(matrice_covariance))
'''
# Visualiser la matrice de correlation
plt.figure(figsize=(10, 8))
sns.heatmap(matrice_correlation, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"size": 20}, linewidths=0.5)
plt.title(' Matrice_correlationdes Segments')
plt.xlabel('Segments')
plt.ylabel('Segments')
plt.show()
'''
def calcul_incertitude(matrice_correlation, matrice_covariance):
    n = len(matrice_correlation)
    somme= 0
    incertitude_segment = 0
    
    for i in range(n):
        incertitude_segment += (incertitudes_segments[i])**2
        
    for i in range(n):
        for j in range(i+1, n):
            rij = matrice_correlation[i][j]
            sigma_i = matrice_covariance[i][i]
            sigma_j = matrice_covariance[j][j]
            
            somme += 2* rij * sigma_i * sigma_j
    return np.sqrt(incertitude_segment + somme)

incertitude = calcul_incertitude(matrice_correlation, matrice_covariance)
print("Incertitude: ", incertitude)

def z_score(x_reel, x_moyenne, incertitude):
    return (abs(x_reel - x_moyenne))/np.sqrt(incertitude)

print("z_score: ", z_score(distance_reelle, distance_moyenne, incertitude))




