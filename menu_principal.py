"""----------------------------------
#---- PROJET _CLEMENT_TOM_2021-----
#-----------------------------------
"""
"""
ici nous avons le menu principal
"""
import tkinter
from functools import partial
import os
from pickle import load
""" nos bibliothèques"""
import ajouter_cube
import changer_cube
import suprimmer_cube
import global_
import map

def cree_menu_principal():

        tkinter.Button(global_.principal, text="créer map",command=page_map).pack()
        tkinter.Button(global_.principal, text="paramètre (ne fais rien )").pack()
        tkinter.Button(global_.principal, text="charger une scène ",command=charger_scene).pack()

def page_map():
    """ on charge la fenetre map
    et mettre les tag bind """
    global_.principal.destroy()
    global_.init()
    """test sur les polygones pour ajout"""

    global_.liste_vue[0].tag_bind("poly_haut", "<Button-1>", ajouter_cube.ajout_cube_haut)
    global_.liste_vue[0].tag_bind("poly_cd", "<Button-1>", ajouter_cube.ajout_cube_cd)
    global_.liste_vue[0].tag_bind("poly_cg", "<Button-1>", ajouter_cube.ajout_cube_cg)

    """test sur  les polygones pour changer"""

    global_.liste_vue[0].tag_bind("poly_haut", "<Button-3>", changer_cube.changer_cube_haut)
    global_.liste_vue[0].tag_bind("poly_cd", "<Button-3>",changer_cube.changer_cube_cd)
    global_.liste_vue[0].tag_bind("poly_cg", "<Button-3>", changer_cube.changer_cube_cg)

    """test sur  les polygones pour suprimmer"""

    global_.liste_vue[0].tag_bind("poly_haut", "<Button-2>", suprimmer_cube.suprime_cube_haut)
    global_.liste_vue[0].tag_bind("poly_cd", "<Button-2>", suprimmer_cube.suprime_cube_cd)
    global_.liste_vue[0].tag_bind("poly_cg", "<Button-2>", suprimmer_cube.suprime_cube_cg)


    """disposition dans la fenêtre"""

    global_.liste_vue[global_.indice_vue].pack(side="left")
    global_.frame_coul.pack(side="left")
    global_.frame_coul.pack()

    map.cree_map()

def charger_scene():
    """ affiche toutes les sauvegardes """
    root =tkinter.Toplevel(global_.principal)
    root.title("scene charger")
    list = os.listdir("./sauvegarde")
    i=0
    while i<len(list):

        tkinter.Button(root, text=str(list[i]),command=partial(charge,root,str(list[i]))).pack()
        i=i+1


def charge(fe,nom):
    fe.destroy()

    page_map_charge(nom)

def page_map_charge(nom):
    """même que pour page_map mais avec un fichier chargé """
    global_.principal.destroy()
    global_.init()
    global_.charger=1
    global_.recup_charge=nom
    p2 = load(open("sauvegarde/"+nom,"rb"))
    global_.plan_save=p2
    """test sur les polygones pour ajout"""

    global_.liste_vue[0].tag_bind("poly_haut", "<Button-1>", map.ajout_cube_haut)
    global_.liste_vue[0].tag_bind("poly_cd", "<Button-1>", map.ajout_cube_cd)
    global_.liste_vue[0].tag_bind("poly_cg", "<Button-1>", map.ajout_cube_cg)

    """test sur  les polygones pour changer"""

    global_.liste_vue[0].tag_bind("poly_haut", "<Button-3>", changer_cube.changer_cube_haut)
    global_.liste_vue[0].tag_bind("poly_cd", "<Button-3>", changer_cube.changer_cube_cd)
    global_.liste_vue[0].tag_bind("poly_cg", "<Button-3>", changer_cube.changer_cube_cg)

    """test sur  les polygones pour suprimmer"""

    global_.liste_vue[0].tag_bind("poly_haut", "<Button-2>", suprimmer_cube.suprime_cube_haut)
    global_.liste_vue[0].tag_bind("poly_cd", "<Button-2>", suprimmer_cube.suprime_cube_cd)
    global_.liste_vue[0].tag_bind("poly_cg", "<Button-2>", suprimmer_cube.suprime_cube_cg)


    """disposition dans la fenêtre"""

    global_.liste_vue[global_.indice_vue].pack(side="left")
    global_.frame_coul.pack(side="left")
    global_.frame_coul.pack()

    map.cree_map()
