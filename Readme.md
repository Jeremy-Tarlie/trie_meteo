# Application de Tri et Recherche avec Données Météo

Ce projet est une application Python qui récupère les données météorologiques de plusieurs villes, les stocke dans une base de données MongoDB, et permet d'effectuer des opérations de tri et de recherche sur les températures.

## Fonctionnalités

1. **Récupération des données météo** :
   - Les données météo sont récupérées via l'API [wttr.in](https://wttr.in).
   - Les informations incluent la température actuelle en degrés Celsius pour chaque ville.

2. **Stockage des données** :
   - Les données sont stockées dans une base de données MongoDB locale.

3. **Tri des températures** :
   - Plusieurs algorithmes de tri sont disponibles :
     - Tri à bulles (Bubble Sort)
     - Tri par insertion (Insertion Sort)
     - Tri rapide (Quick Sort)
     - Tri par sélection (Selection Sort)

4. **Recherche dans les températures** :
   - Deux algorithmes de recherche sont disponibles :
     - Recherche linéaire (Linear Search)
     - Recherche binaire (Binary Search)


## Prérequis

- Python 3.10 ou supérieur
- MongoDB installé et en cours d'exécution
- Bibliothèques Python nécessaires :
  - `pymongo`
  - `requests`

Pour installer les dépendances, exécutez :

```bash
pip install pymongo requests
```

## Utilisation
Lancez le script principal
```bash
python main.py
```
