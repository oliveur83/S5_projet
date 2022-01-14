"""----------------------------------
        --- PROJET _CLEMENT_TOM_2021-----
-----------------------------------
"""
"""
Ce programme nous sert à ajouter l'image du cube.
Dans ce programme trois fonctions chacune correspondant
aux polygones (est donc aux faces du cube visible).

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

def ajout_cube_haut(event=None):
    """récupération de id et des  coordonnées du polygones    """
    id = global_.liste_vue[global_.indice_vue].find_withtag("current")
    idc=global_.liste_vue[global_.indice_vue].coords(id)
    """calcul des positions pour les polygones
    polygone du haut"""
    face_h=[[idc[0],idc[1]],[idc[2],idc[3]],[idc[4],idc[5]],[idc[6],idc[7]]]
    face_h[0][1]=face_h[0][1]-100
    face_h[1][1]=face_h[1][1]-100
    face_h[2][1]=face_h[2][1]-100
    face_h[3][1]=face_h[3][1]-100
    """pour polygone droit"""
    face_d=[[0,0],[idc[2],idc[3]],[idc[4],idc[5]],[0,0]]
    """pour polygone gauche"""
    face_g=[[0,0],[0,0],[idc[6],idc[7]],[0,0]]
    pts=(face_h,face_d,face_g)
    """ pour mettre le cube dans le plan """
    y=(2*idc[1]-idc[0])/(4*50)
    x=(idc[0]+2*idc[1])/(4*50)-5
    """pour mettre le cube au bon z"""
    p= level(id[0],x,y)

    global_.photo= ImageTk.PhotoImage(global_.image)
    poly=Cube(pts,0,id)

    """dessiner image et les polygones"""
    poly.draw(idc[0],idc[1],poly,global_.liste_vue[global_.indice_vue])
    """ mettre dans le plan """
    print(p)
    global_.plan1[p] = [poly,poly.polygon]

    global_.plan_save[p]=[poly.saveim]
    """ correctement afficher """
    map.placer(poly,p[0],p[1],p[2])

def level(id,x,y):
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

                            return (xl,yl,z+1)
                        if global_.plan1[p][0].cd==id:
                            return (xl+1,yl,z)
                        if global_.plan1[p][0].cg==id:
                            return (xl,yl+1,z)

def ajout_cube_cd(event=None):

    """récupération de id et des  coordonnées du polygone   """
    id = global_.liste_vue[global_.indice_vue].find_withtag("current")
    idc=global_.liste_vue[global_.indice_vue].coords(id)
    """calcul des positions pour les polymones
    polygone du haut,droit,gauche"""
    face_h=[[idc[0],idc[1]],[idc[0]+100,idc[1]+50],[idc[6]+100,idc[7]+50],[idc[6],idc[7]]]
    face_d=[[0,0],[idc[0]+100,idc[1]+150],[idc[6]+100,idc[7]+150],[0,0]]
    face_g=[[0,0],[0,0],[idc[4],idc[5]],[0,0]]

    """ pour mettre le cube dans le plan """
    y=(2*idc[1]-idc[0])/(4*50)
    x=(idc[0]+2*idc[1])/(4*50)-5
    p= level(id[0],x,y)
    """ voir si on est hors limite du plan """
    try:
        print(global_.plan1[p])
    except IndexError:
        print("\n\n\n error")
        return 0
    print(p)
    """création cube"""
    pts=(face_h,face_d,face_g)
    poly=Cube(pts,0,id)

    poly.draw(idc[0],idc[1]+100,poly,global_.liste_vue[global_.indice_vue])
    global_.plan1[p] = (poly,poly.polygon)

    global_.plan_save[p]=[poly.saveim]
    """ correctement afficher """
    map.placer(poly,p[0],p[1],p[2])

def ajout_cube_cg(event=None):


    """récupération de id et des  coordonnées du polygone    """
    id = global_.liste_vue[global_.indice_vue].find_withtag("current")
    idc=global_.liste_vue[global_.indice_vue].coords(id)
    """calcul des positions pour les polymones
    polygone du haut,droit,gauche"""
    face_h=[[idc[6],idc[7]],[idc[0],idc[1]],[idc[0]-100,idc[1]+50],[idc[6]-100,idc[7]+50]]
    face_d=[[0,0],[idc[2],idc[3]],[idc[2]-100,idc[3]+50],[0,0]]
    face_g=[[0,0],[0,0],[idc[4]-100,idc[5]+50],[0,0]]
    """création cube"""
    pts=(face_h,face_d,face_g)
    poly=Cube(pts,0,id)

    """ pour mettre le cube dans le plan """
    y=(2*idc[1]-idc[0])/(4*50)
    x=(idc[0]+2*idc[1])/(4*50)-5
    p= level(id[0],x,y)
    """ voir si on est hors limite du plan """
    try:
        print(global_.plan1[p])
    except IndexError:
        print("\n\n\n error")
        return 0

    poly.draw(idc[0]-100,idc[1]+50,poly,global_.liste_vue[global_.indice_vue])
    print(p)
    global_.plan1[p] = (poly,poly.polygon)
    global_.plan_save[p]=[poly.saveim]
    """ correctement afficher """
    map.placer(poly,p[0],p[1],p[2])
