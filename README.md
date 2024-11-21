# TIPE 2024 : Mesure de la Distance Parcourue par un Footballeur et Évaluation de l'Incertitude

## Description
Ce projet vise à déterminer la distance parcourue par un footballeur à l'aide de coordonnées relevées (via des capteurs ou la stéréovision) et à évaluer précisément l'incertitude associée. Le travail comprend :
- La modélisation théorique des déplacements.
- L'utilisation de distributions statistiques pour analyser les données.
- La génération de matrices de covariance et de corrélation pour estimer l'incertitude.

## Objectifs
1. Développer un algorithme en Python pour calculer la distance parcourue à partir de coordonnées.
2. Évaluer l'incertitude sur la distance calculée.
3. Explorer des approches statistiques, telles que les distributions gaussiennes et uniformes, pour modéliser les incertitudes.

## Contenu
### Théorie
- **Principe de la triangulation** : Utilisation de capteurs pour déterminer les positions des joueurs.
- **Calculs théoriques** : Distance euclidienne, incertitude segmentaire, et distance totale.

### Étude Statistique
- Analyse des coordonnées via des distributions (gaussienne et uniforme).
- Construction de matrices (segments, covariance, corrélation).
- Génération de heatmaps et d'autres visualisations.

### Résultats
- Distance réelle vs distance relevée vs distance moyenne.
- Exemple pour 1 minute de jeu avec 60 coordonnées :
  - Distance réelle : 361 m
  - Distance relevée : 349 m
  - Distance moyenne : 356 m
  - Incertitude : ±10 m
  - Z-Score : 1.65


## Utilisation
### Pré-requis
- Python 3.7 ou plus récent.
- Bibliothèques Python nécessaires : NumPy, Matplotlib, Pandas, etc.

### Installation
Clonez le projet :
```bash
git clone https://github.com/king-nourou/TIPE-2024.git
cd TIPE-2024
Améliorations Potentielles

Prendre en compte les interférences des signaux.
Intégrer des algorithmes plus adaptés aux déplacements des joueurs.
Confronter les résultats théoriques aux données réelles.
Auteur

Mouhamed Nourou Dine Cisse
TIPE 2023-2024
