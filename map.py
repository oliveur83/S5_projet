"""----------------------------------
#---- PROJET _CLEMENT_TOM_2021-----
#-----------------------------------
"""
"""
Ici nous avons toutes les fonctionnalités/relations pour créer la map

"""


import tkinter
from PIL import Image, ImageTk
from tkinter import PhotoImage, Tk, Canvas, Label
from functools import partial
""" nos bibliotheques"""
from cube import *
import texte
import sauver_plan
import global_

"""
répertoire des fonctions
cree_map

"""

def cree_map():
    """appeler une fois pour créer la map"""

    e=global_.hw_canvas/20
    """  e =épaisseur du cube """
    cpt=0
    "cpt pour compter les 25 premiers"
    cphaut=0
    " pour placer quand fichier chargé "
    for k in range(5):
        for j in range(5):
            for i in range(5):
                x, y = (i-j)*2*e, (i+j)*e
                x, y = x+global_.hw_canvas//2, y+(global_.hw_canvas//4)
                y=y-cphaut
                point1=(x,y)
                point2=(x+2*e,y+e)
                point3=(x,y+2*e)
                point4=(x-2*e,y+e)
                pts=[point1,point2,point3,point4]
                """----------save---"""
                """  on regarde si fichier chargé
                    on regarder si il y a un cube au niveu ijk
                    si c'est le cas on appele save_ajout()
                """
                if global_.charger==1:
                    nom=global_.plan_save[i,j,k]
                    if nom!=[]:
                        pt_save=(x,y,x+2*e,y+e,x,y+2*e,x-2*e,y+e)
                        save_ajout(pt_save,str(nom[0]),k)

                """----------------"""

                if cpt<25:
                    id=global_.liste_vue[global_.indice_vue].create_polygon(pts,tags=("poly_haut"),outline="yellow",activefill="red",fill='')
                    global_.liste_vue[global_.indice_vue].tag_lower(id)

                cpt=cpt+1
        cphaut=cphaut+100

    creation_couleur()

def save_ajout(idc,nom,k):
    """ save ajout permet d'ajouter un cube avec ses faces pour une sauvegarde
    chargée"""
    face_h=[[idc[0],idc[1]],[idc[2],idc[3]],[idc[4],idc[5]],[idc[6],idc[7]]]
    face_h[0][1]=face_h[0][1]-100
    face_h[1][1]=face_h[1][1]-100
    face_h[2][1]=face_h[2][1]-100
    face_h[3][1]=face_h[3][1]-100
    """pour poly droit"""
    face_d=[[0,0],[idc[2],idc[3]],[idc[4],idc[5]],[0,0]]
    """pour poly gauche"""
    face_g=[[0,0],[0,0],[idc[6],idc[7]],[0,0]]
    pts=(face_h,face_d,face_g)
    """ pour mettre le cube dans le plan """
    y=(2*idc[1]-idc[0])/(4*50)
    x=(idc[0]+2*idc[1])/(4*50)-5
    p=(int(x),int(y),k)
    """ pour aller chercher image  """
    nomi="image/"+nom+".png"
    image = Image.open(nomi)
    image=image.resize((200,190))
    global_.photo= ImageTk.PhotoImage(image)
    """ création cube et ajouter  """
    poly=Cube(pts,0,0)
    poly.draw(idc[0],idc[1],poly,global_.liste_vue[global_.indice_vue])
    """ mettre dans le plan """
    global_.plan1[p] = [poly,poly.polygon]
    """ correctement afficher """
    placer(poly,p[0],p[1],p[2])



def creation_couleur():
    """ affichage des fonctionnalités """
    Label(global_.frame_coul,text="image_cube").grid(row=0)
    tkinter.Button(global_.frame_coul, text="sable",command=partial(afficher_couleur,"sable")).grid(row=1,column=0)
    tkinter.Button(global_.frame_coul, text="eau", command=partial(afficher_couleur,"eau")).grid(row=1,column=1)
    tkinter.Button(global_.frame_coul, text="herbe",command=partial(afficher_couleur,"herbe")).grid(row=2,column=0)
    tkinter.Button(global_.frame_coul, text="goudron",command=partial(afficher_couleur,"goudron")).grid(row=2,column=1)
    tkinter.Button(global_.frame_coul, text="glace",command=partial(afficher_couleur,"glace")).grid(row=3,column=0)
    tkinter.Button(global_.frame_coul, text="bois",command=partial(afficher_couleur,"bois")).grid(row=3,column=1)
    tkinter.Button(global_.frame_coul, text="eau",command=partial(afficher_couleur,"eau2")).grid(row=4,column=0)
    tkinter.Button(global_.frame_coul, text="herbe",command=partial(afficher_couleur,"herbe2")).grid(row=4,column=1)
    tkinter.Button(global_.frame_coul, text="help",command=help).grid(row=7,column=1)
    tkinter.Button(global_.frame_coul, text="sauver",command=sauver).grid(row=7,column=0)

def sauver():
    sauver_plan.sauver()
def help():
    texte.fenetre_help()

def afficher_couleur(nom):
    """ changement image """
    if nom=="sable":
        global_.image = Image.open("image/cube.png")
        """save_im est pour le plan de sauvegarde"""
        global_.save_image="cube"
    elif nom=="eau":
        global_.image = Image.open("image/cube1.png")
        global_.save_image="cube1"
    elif nom=="herbe":
        global_.image = Image.open("image/cube2.png")
        global_.save_image="cube2"
    elif nom=="goudron":
        global_.image = Image.open("image/cube3.png")
        global_.save_image="cube3"
    elif nom=="glace":
        global_.image = Image.open("image/cube4.png")
        global_.save_image="cube4"
    elif nom=="bois":
        global_.image = Image.open("image/cube5.png")
        global_.save_image="cube5"
    elif nom=="eau2":
        global_.image = Image.open("image/cube6.png")
        global_.save_image="cube6"
    elif nom=="herbe2":
        global_.image = Image.open("image/cube7.png")
        global_.save_image="cube7"

    global_.image=global_.image.resize((200,190))

    global_.photo= ImageTk.PhotoImage(global_.image)

def placer(poly,x,y,z):
    """ bien afficher image du cube """
    """ der=derrier et dev=devant"""
    pdev=(int(x),int(y)+1,z)

    pder=(int(x),int(y)-1,z)
    pcg=(int(x)-1,int(y),z)
    pcd=(int(x)+1,int(y),z)
    derdia=(int(x)-1,int(y)-1,z)
    dessus=(int(x),int(y),z+1)
    dessous=(int(x),int(y),z-1)

    if global_.plan1[pcg]!=[] and global_.plan1[pcd]!=[] and global_.plan1[pder]!=[]:
        """ côté g et d et der """

        global_.liste_vue[global_.indice_vue].tag_raise(poly.polygon)
        global_.liste_vue[global_.indice_vue].tag_lower(poly.polygon,global_.plan1[pcd][1])

        global_.liste_vue[global_.indice_vue].tag_lower(poly.cd,global_.plan1[pcd][1])
        global_.liste_vue[global_.indice_vue].tag_lower(poly.cd,global_.plan1[pcd][1])
    elif global_.plan1[pcg]!=[] and global_.plan1[pdev]!=[] and global_.plan1[pder]!=[]:
        """ côté g der dev"""
        global_.liste_vue[global_.indice_vue].tag_raise(poly.polygon)
        global_.liste_vue[global_.indice_vue].tag_lower(poly.polygon,global_.plan1[pdev][1])

        global_.liste_vue[global_.indice_vue].tag_lower(poly.cg,global_.plan1[pcg][1])
        global_.liste_vue[global_.indice_vue].tag_lower(poly.cg,global_.plan1[pcg][1])
    elif global_.plan1[pcg]!=[] and global_.plan1[pcd]!=[]:
        """ côté g d"""
        global_.liste_vue[global_.indice_vue].tag_raise(poly.polygon)
        global_.liste_vue[global_.indice_vue].tag_lower(poly.polygon,global_.plan1[pcd][1])

        global_.liste_vue[global_.indice_vue].tag_lower(poly.cd,global_.plan1[pcd][1])
        global_.liste_vue[global_.indice_vue].tag_lower(global_.plan1[pcg][0].cd,poly.polygon)
    elif global_.plan1[pder]!=[] and global_.plan1[pcd]!=[]:
        "côté d et der"
        global_.liste_vue[global_.indice_vue].tag_lower(poly.polygon,global_.plan1[pcd][1])
        global_.liste_vue[global_.indice_vue].tag_lower(poly.cd,global_.plan1[pcd][1])
    elif global_.plan1[pdev]!=[] and global_.plan1[pder]!=[]:
        global_.liste_vue[global_.indice_vue].tag_raise(poly.polygon)
        global_.liste_vue[global_.indice_vue].tag_lower(poly.polygon,global_.plan1[pdev][1])

        global_.liste_vue[global_.indice_vue].tag_lower(poly.cg,global_.plan1[pdev][1])
        global_.liste_vue[global_.indice_vue].tag_lower(global_.plan1[pder][0].cg,poly.polygon)
    elif global_.plan1[pdev]!=[]:
        """dev"""

        if global_.plan1[derdia]!=[]:
            global_.liste_vue[global_.indice_vue].tag_raise(poly.polygon)

        global_.liste_vue[global_.indice_vue].tag_lower(poly.polygon,global_.plan1[pdev][1])
        global_.liste_vue[global_.indice_vue].tag_lower(poly.cg,global_.plan1[pdev][1])
    elif global_.plan1[pder]!=[]:
        """der"""

        global_.liste_vue[global_.indice_vue].tag_lower(global_.plan1[pder][0].cg,poly.polygon)
    elif global_.plan1[pcg]!=[]:
        """cg"""
        if z!=0:
            if global_.plan1[dessous]!=[]:

                global_.liste_vue[global_.indice_vue].tag_raise(poly.polygon,global_.plan1[dessous][1])



    elif global_.plan1[pcd]!=[]:
        """cd"""
        if z!=0:
            if global_.plan1[dessous]!=[]:

                global_.liste_vue[global_.indice_vue].tag_raise(poly.polygon,global_.plan1[dessous][1])

        if global_.plan1[derdia]!=[]:
            global_.liste_vue[global_.indice_vue].tag_raise(poly.polygon)

        global_.liste_vue[global_.indice_vue].tag_lower(poly.polygon,global_.plan1[pcd][1])

        global_.liste_vue[global_.indice_vue].tag_lower(poly.cd,global_.plan1[pcd][1])

    elif global_.plan1[pcd]==[] and global_.plan1[pcg]==[] and global_.plan1[pdev]==[] and global_.plan1[pder]==[]:
        "si c'est vide "
        global_.liste_vue[global_.indice_vue].tag_raise(poly.ch)
        global_.liste_vue[global_.indice_vue].tag_raise(poly.cg)
        global_.liste_vue[global_.indice_vue].tag_raise(poly.cd)
    if global_.plan1[pcd]!=[] and global_.plan1[pdev]!=[]:
        global_.liste_vue[global_.indice_vue].tag_lower(poly.polygon,global_.plan1[pcd][1])


    if global_.plan1[dessus]!=[]:

        if z!=0:
            if global_.plan1[dessous]!=[]:

                global_.liste_vue[global_.indice_vue].tag_raise(poly.polygon,global_.plan1[dessous][1])

        global_.liste_vue[global_.indice_vue].tag_raise(global_.plan1[dessus][1],poly.polygon)

        global_.liste_vue[global_.indice_vue].tag_raise(global_.plan1[dessus][0].ch)
        global_.liste_vue[global_.indice_vue].tag_raise(global_.plan1[dessus][0].cg)
        global_.liste_vue[global_.indice_vue].tag_raise(global_.plan1[dessus][0].cd)

        global_.liste_vue[global_.indice_vue].tag_lower(poly.ch,global_.plan1[dessus][1])
