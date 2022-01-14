"""----------------------------------
#---- PROJET _CLEMENT_TOM_2021-----
#-----------------------------------
"""
"""
Ce programme nous sert à repertorié toutes les
variables indispensables qui transitent dans
nos fichiers


"""

import tkinter

from tkinter import Canvas,Frame,Listbox
from plan import Plan

from PIL import Image, ImageTk
from tkinter import PhotoImage, Tk, Canvas

def init():
    global plan1,x,y,z ,frame_coul,lb
    global principal,hw_canvas,nord,sud,est,ouest
    global frame_coul,liste_cube
    global image,photo,new_photo
    global lb,liste_hexa,liste_vue,indice_vue,liste_hexa_plus
    global cpt_id_im # pour les identifiant de polygon
    global save_image,plan_save
    global charger,recup_charge
    """ permet de savoir si c'est une nouvelle map ou map chargée """
    charger=0
    recup_charge=""
    """variable xyz pour notre plan"""
    x=5
    y=5
    z=5
    """image par défaut  """
    image = Image.open("image/cube.png")
    save_image="cube"
    image=image.resize((200,190))
    """création du plan """
    plan1=Plan(x,y,z)
    plan_save=Plan(x,y,z)
    """ dimension du canvas"""
    hw_canvas=1000
    """ pour les vues"""
    liste_vue=[]
    indice_vue=0
    """ fenêtre principale """
    principal=tkinter.Tk()

    sud=Canvas(principal,height=hw_canvas,width=hw_canvas,bg="black")
    est=Canvas(principal,height=hw_canvas,width=hw_canvas,bg="black")
    ouest=Canvas(principal,height=hw_canvas,width=hw_canvas,bg="black")
    nord=Canvas(principal,height=hw_canvas,width=hw_canvas,bg="black")

    liste_vue=[nord,est,sud,ouest]
    """ frame qui contiendra toutes les fonctionnalités """
    frame_coul=Frame(width=300,bg="green")
    lb=Listbox(frame_coul)
