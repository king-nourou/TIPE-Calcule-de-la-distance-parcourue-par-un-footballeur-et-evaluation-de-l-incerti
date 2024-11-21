import matplotlib.pyplot as plt

# Données
distance_reelle = [ 98,  137, 171, 259,  308, 361]

lg= [112, 144, 179, 262, 307,356]
lincer = [3.5, 4.1, 4, 3.1, 2.9, 2.8]
lzsc = [7, 2.9, 1.4, 1.29, 0.2, 1.65]

# Nombre d'expériences
experiences = range(1, len(distance_reelle) + 1)

# Création du graphique principal
fig, ax1 = plt.figure(figsize=(10, 12)), plt.gca()

ax1.plot(experiences, distance_reelle, marker='o', label='Distance Réelle', color='blue')
ax1.plot(experiences, lg, marker='o', label='Longueur Expérience', color='red')

# Ajouter des labels et un titre avec une taille de police augmentée
ax1.set_xlabel('Expériences', fontsize=14)
ax1.set_ylabel('Distance en m', fontsize=14)
ax1.set_title('Comparaison des distances réelles et celles de la distribution uniforme', fontsize=20)

# Ajouter la légende avec une taille de police augmentée
ax1.legend(loc='upper left', fontsize=12)

# Ajouter un axe secondaire pour les incertitudes et les z-scores

plt.show()
