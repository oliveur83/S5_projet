"""----------------------------------
        --- PROJET _CLEMENT_TOM_2021-----
-----------------------------------
"""
"""
Ce programme nous sert à modifier l'image du cube.
Dans ce programme trois fonctions chacune correspondant
aux polygones (et donc aux faces du cube visible).

"""

import tkinter

from PIL import Image, ImageTk
from tkinter import PhotoImage, Tk, Canvas, Label
from functools import partial

""" nos bibliothèques"""
from cube import *
import texte
import sauver_plan
import global_
import map
def mod_level(id,x,y):

    """" fonction permettant de mettre le bon z"""

    if (id<26):
        return (int(x),int(y),0)
    else:
        for z in range(5):
            for yl in range(5):
                for xl in range(5):
                    p=(xl,yl,z)

                    if global_.plan1[p]!=[]:

                        if global_.plan1[p][0].ch==id:

                            return (xl,yl,z)
                        if global_.plan1[p][0].cd==id:
                            return (xl,yl,z)
                        if global_.plan1[p][0].cg==id:
                            return (xl,yl,z)

def changer_cube_haut(event=None):
    """les 25  premier polygone qui ne sont pas des cubes """
    if id[0]<25:
        return 0
    """récupération de id et les coordonnées du polygone    """
    id = global_.liste_vue[global_.indice_vue].find_withtag("current")
    idc=global_.liste_vue[global_.indice_vue].coords(id)
    """ pour trouver les cooordonnées correspondant au polygone dans le plan  """
    y=(2*idc[1]-idc[0])/(4*50)
    y=y+1
    x=(idc[0]+2*idc[1])/(4*50)-5
    x=x+1
    p= mod_level(id[0],int(x),int(y))
    print(p)
    """ensuite on change l'image du cube et aussi le nom de l'image dans plan save """
    global_.plan1[p][0].change(idc[0]-100,idc[1]+50,global_.liste_vue[global_.indice_vue])
    map.placer(global_.plan1[p][0],p[0],p[1],p[2])
    global_.plan_save[p]=[global_.save_image]


def changer_cube_cd(event=None):
    """récupération de id et les coordonnées du polygone  """
    id = global_.liste_vue[global_.indice_vue].find_withtag("current")
    idc=global_.liste_vue[global_.indice_vue].coords(id)
    """ pour trouver les coordonnéres correspondant au polygone dans le plan  """
    y=(2*idc[1]-idc[0])/(4*50)
    y=y+1
    x=(idc[0]+2*idc[1])/(4*50)-5
    p= mod_level(id[0],int(x),int(y))
    print(p)
    """ensuite on change l'image du cube et aussi le nom de l'image dans plan save """

    global_.plan1[p][0].change(idc[0]-200,idc[1],global_.liste_vue[global_.indice_vue])
    global_.plan_save[p]=[global_.save_image]
    map.placer(global_.plan1[p][0],p[0],p[1],p[2])

def changer_cube_cg(event=None):
    """récupération de id et les coordonnées du polygone   """
    id = global_.liste_vue[global_.indice_vue].find_withtag("current")
    idc=global_.liste_vue[global_.indice_vue].coords(id)
    """ pour trouver les coordonnées correspondant au polygone dans le plan """
    y=(2*idc[1]-idc[0])/(4*50)
    x=(idc[0]+2*idc[1])/(4*50)-5
    p= mod_level(id[0],int(x),int(y))
    print(p)
    """ensuite on change l'image du cube et aussi le nom de l'image dans plan save """

    global_.plan1[p][0].change(idc[0]-100,idc[1]-50,global_.liste_vue[global_.indice_vue])
    global_.plan_save[p]=[global_.save_image]
    map.placer(global_.plan1[p][0],p[0],p[1],p[2])
