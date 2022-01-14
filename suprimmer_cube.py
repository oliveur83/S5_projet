"""----------------------------------
#---- PROJET _CLEMENT_TOM_2021-----
#-----------------------------------
"""
"""
Ce programme nous sert à supprimer l'image du cube et le cube.
Dans ce programme trois fonctions chacune correspondant
aux polygones (est donc aux faces du cube visible).

"""
import tkinter

from PIL import Image, ImageTk
from tkinter import PhotoImage, Tk, Canvas, Label
from functools import partial

from cube import *
import texte
import sauver_plan
import map
import global_


def suprime_cube_haut(event=None):
    """récupération de id et les coordonnées du polygone    """

    id = global_.liste_vue[global_.indice_vue].find_withtag("current")
    if id[0]<25:
        return 0
    idc=global_.liste_vue[global_.indice_vue].coords(id)

    """ pour mettre le cube dans le plan """
    y=(2*idc[1]-idc[0])/(4*50)
    x=(idc[0]+2*idc[1])/(4*50)-5
    x,y=x+1,y+1
    p= sup_level(id[0],int(x),int(y))

    """ tout suprimmer"""
    global_.liste_vue[global_.indice_vue].delete(id[0])
    global_.liste_vue[global_.indice_vue].delete(id[0]+1)
    global_.liste_vue[global_.indice_vue].delete(id[0]+2)
    global_.liste_vue[global_.indice_vue].delete(global_.plan1[p][1])
    global_.liste_vue[global_.indice_vue].delete(global_.plan1[p][0])
    global_.plan1[p]=[]



def suprime_cube_cd(event=None):
    """récupération de id et les coordonnées du polygone    """

    id = global_.liste_vue[global_.indice_vue].find_withtag("current")
    idc=global_.liste_vue[global_.indice_vue].coords(id)
    """ pour mettre le cube dans le plan """
    y=(2*idc[1]-idc[0])/(4*50)
    y=y+1
    x=(idc[0]+2*idc[1])/(4*50)-5

    p= sup_level(id[0],int(x),int(y))
    """ tout suprimmer"""
    global_.liste_vue[global_.indice_vue].delete(id[0])
    global_.liste_vue[global_.indice_vue].delete(id[0]-1)
    global_.liste_vue[global_.indice_vue].delete(id[0]+1)
    global_.liste_vue[global_.indice_vue].delete(global_.plan1[p][1])
    global_.liste_vue[global_.indice_vue].delete(global_.plan1[p][0])
    global_.plan1[p]=[]


def suprime_cube_cg(event=None):
    """récupération de id et les coordonnées du polygone    """

    id = global_.liste_vue[global_.indice_vue].find_withtag("current")
    idc=global_.liste_vue[global_.indice_vue].coords(id)
    """ pour mettre le cube dans le plan """
    y=(2*idc[1]-idc[0])/(4*50)
    x=(idc[0]+2*idc[1])/(4*50)-5
    p= sup_level(id[0],int(x),int(y))
    """ tout suprimmer"""
    global_.liste_vue[global_.indice_vue].delete(id[0])
    global_.liste_vue[global_.indice_vue].delete(id[0]-1)
    global_.liste_vue[global_.indice_vue].delete(id[0]-2)
    global_.liste_vue[global_.indice_vue].delete(global_.plan1[p][1])
    global_.liste_vue[global_.indice_vue].delete(global_.plan1[p][0])
    global_.plan1[p]=[]

def sup_level(id,x,y):

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
