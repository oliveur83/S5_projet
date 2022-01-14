
"""----------------------------------
#---- PROJET _CLEMENT_TOM_2021-----
#-----------------------------------
"""
"""
Ce programme nous sert à sauvegardé notre plan
isométrique.
"""

from pickle import dump
from pickle import load
import os

import global_

import tkinter as tk
def sauver():

    root =tk.Toplevel(global_.principal)

    root.title("sauvegarde")


    list = os.listdir("./sauvegarde")
    list.sort()
    text_frame = tk.Frame(root)
    txt = tk.Text(text_frame)
    changen="sauvegarde/new"+str(len(list))+".sc"
    mess="sauvegarde reussi sous le nom de new"+ str(len(list))+".sc"
    txt.insert(tk.END,mess)
    txt.pack(fill="both",expand=True)
    text_frame.pack(fill="both",expand=True)
    dump(global_.plan_save,open(changen,"wb"))
