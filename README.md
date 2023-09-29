# Plan Isométrique

![Licence](https://img.shields.io/badge/Licence-Open--Source-brightgreen)

## Auteurs
- OLIVIER Tom
- BAZAN Clément

## Présentation
Bienvenue dans le projet "Plan Isométrique". L'objectif de ce projet est de créer une carte avec une vue isométrique en 3D.

## Table des matières
I. Cahier des charges
II. Fichiers programmes
III. Nos choix
IV. Comment faire ?
V. Problèmes connus

## I. Cahier des charges
Le projet remplit les critères suivants :
- Définir une scène en 3D isométrique de manière interactive ou via des commandes (fait)
- Permettre le choix des couleurs et de la "hauteur" des cubes (fait)
- Offrir une aide en ligne contextuelle si possible (fait)
- Permettre la modification ou la suppression de parties de la scène (fait)
- Sauvegarder et charger des scènes (fait)
- Paramétrer les composants de l'application
- Associer des images aux cubes

## II. Fichiers programmes
Les fichiers de classe :
- cube.py
- plan.py

Fichier à exécuter :
- projet.py

Fichier de variables globales :
- global_.py

Fichiers pour le déroulement de l'application :
- menu_principal.py
- map.py

Fichiers contenant des fonctions :
- texte.py
- supprimer_cube.py
- sauver_plan.py
- changer_cube.py

## III. Nos choix
La base de construction est une carte de 5x5x5. Lorsqu'un cube est ajouté, une image par défaut lui est attribuée. Il n'y a pas de fonctionnalité d'ajout en x, y ou z.

Par manque de temps, le bouton "paramètres" n'est pas fonctionnel.

## IV. Comment faire ?
Pour tester l'application, exécutez projet.py. Vous aurez besoin de Python 3.X et de la bibliothèque tkinter.

## V. Problèmes connus
Il peut y avoir des problèmes d'affichage, mais ils sont normalement résolus.
