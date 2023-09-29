licence :open-source
#################################################

Projet réalisé par OLIVIER tom et BAZAN clément

#################################################

              Présentation :
Ici se développe le projet "plan isométrique".
Le but du projet est donc de créer une map avec une vue
isométrique.
                Sommaire:
I Cahier des charges
II Fichiers programmes
III Nos choix
IV Comment faire ?
V Certain bug
                I Cahier des charges :

-définir interactivement ou par commandes une scène
en 3D isométrique(fait)
-choisir couleurs et "hauteur" des cubes(fait)
-offrir une aide en ligne si possible contextuelle(fait)
-modifier ou de supprimer des parties de la scène(fait)
-sauvegarder et de charger des scènes(fait)
-paramètrer les constituants de APP
-associer des pixmaps aux cubes

                  II Fichiers programmes :

Il y a deux fichiers classe:
-cube.py
-plan.py

Le fichier à exécuter:
-projet.py

Un fichier répertoire de variables:
global_.py

Les deux fichiers pour le déroulement:
-menu_principal.py
-map.py

Quatre fichier constituants de fonction :
-texte.py
-supprimer_cube.py
-sauver_plan.py
-changer_cube.py

Et pour finir ce fichier :
readme.txt

                    III Nos choix

La base de construction est une map de 5*5*5.
Quand on ajoute un cube au début une image est par défaut.
Il n'y a pas de fonctionnalité d'ajout en x ou y ou z.

Par manque de temps le bouton paramètre ne fais rien


                    IV Comment faire ?

 Il faut exécuter le projet.py pour pouvoir tester l'application.
 pour cela il vous faudra python 3.X ainsi que tkinter.

                    V Certain bug

il y a peut être des bugs affichage qui sont normalement résolus.
