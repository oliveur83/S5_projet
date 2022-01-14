import tkinter as tk
import global_


"""Init Texte"""

def init_texte():
    global_.scope = False
    global_.txt.delete(1.0,tk.END)
    global_.txt.insert(tk.END,message)
    global_.txt.tag_add("RMB",1.22,1.25)
    global_.txt.tag_add("LMB",2.25,2.28)
    global_.txt.tag_add("SMB",3.25,3.28)
    global_.txt.tag_config("RMB",underline=1,font="italic")
    global_.txt.tag_config("LMB",underline=1,font="italic")
    global_.txt.tag_config("SMB",underline=1,font="italic")
"""Texte"""
mrmb = """Il suffit de survoler l'une des surfaces d'un cube ou survoler une case du quadrillage\nPuis de clicker sur le bouton gauche de la souris"""
msmb="""Il suffit de survoler l'une des surfaces d'un cube ou survoler une case du quadrillage\nPuis de clicker sur le bouton centre  de la souris"""
mlmb = """Il suffit de survoler l'une des surfaces d'un cube précedemment place \nPuis de cliquer sur le bouton droit de la souris"""

message = """Pour placer un cube : RMB\nPour modifier un cube : LMB\n Pour suprimmer un cube : SMB\n"""

"""Texte principal"""


"""Definition des Hyperliens"""
def RMB(Event=None):

    global_.scope = True
    global_.txt.delete(1.0,tk.END)
    global_.txt.insert(tk.END,mrmb)
def SMB(Event=None):

    global_.scope = True
    global_.txt.delete(1.0,tk.END)
    global_.txt.insert(tk.END,msmb)

def LMB(Event =None):

    global_.scope = True
    global_.txt.delete(1.0,tk.END)
    global_.txt.insert(tk.END,mlmb)

"""Fonction pour revenir au texte principal"""
def retour(Event = None):
    if(global_.scope):
        init_texte()

def fenetre_help():

    root =tk.Toplevel(global_.principal)

    root.title("Hyperlien")
    text_frame = tk.Frame(root)
    frame_button = tk.Frame(root)
    global_.scope = False

    global_.txt = tk.Text(text_frame)
    init_texte()
    retourb = tk.Button(frame_button,text="retour",command=retour)

    global_.txt.pack(fill="both",expand=True)
    text_frame.pack(fill="both",expand=True)
    frame_button.pack(side="bottom",fill =tk.Y)

    retourb.pack()

    global_.txt.tag_bind("RMB","<Button-1>",RMB)
    global_.txt.tag_bind("LMB","<Button-1>",LMB)
    global_.txt.tag_bind("SMB","<Button-1>",SMB)
    tk.mainloop()
