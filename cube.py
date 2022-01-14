"""----------------------------------
#---- PROJET _CLEMENT_TOM_2021-----
#-----------------------------------
"""
"""
Ce fichier permet de créer la classe cube
cube permet de créer l'image et les trois polygones

"""
import global_
from PIL import Image, ImageTk
from tkinter import PhotoImage, Tk, Canvas, Label

class Cube():
    """  ch = polygone du polygone haut, cd pour le droit
    , cg pour le gauche
    image= image pour le cube
    saveim = nom de l'image pour la sauvegarde
    """
    def __init__(self,coords,polyid,rel):
        self.__coords=coords
        self.__rel = rel
        self.__polygon=polyid
        self.__image=global_.photo
        self.__saveim=global_.save_image
        self.__ch=0
        self.__cd=0
        self.__cg=0

    @property
    def coords(self):
        return self.__coords
    @property
    def rel(self):
        return self.__rel
    @property
    def polygon(self):
        return self.__polygon
    @property
    def saveim(self):
        return self.__saveim
    @property
    def cg(self):
        return self.__cg
    @property
    def ch(self):
        return self.__ch
    @property
    def cd(self):
        return self.__cd

    """
    coords : (face1, face2, face3)

                    o(x1,y1)

            o(x4,y4)           o(x2,y2)
            |                   |
            |       o(x3,y3)    |
            |       |           |
            |       |           |
            |       |           |
            o(x6,y6)|           o(x7,y7)
                    |
                    o(x5,y5)

    faceh : ((x1,y1),(x2,y2),(x3,y3),(x4,y4)))
    faced : ((x2,y2),(x7,y7),(x5,y5),(x3,y3))
    faceg:  ((x3,y3),(x5,y5),(x6,y6),(x4,y4)))

    Contraintes :
    x1y1 : coords[0][0]
    x2y2 : coords[0][1] == coords[1][0]
    x3y3 : coords[0][2] == coords[1][3]== coords[2][0]
    x4y4 : coords[0][3] == coords[2][3]
    x5y5 : coords[1][2] == coords[2][1]
    x6y6 : coords[2][2]
    x7y7 : coords[1][1]



    """

    def draw(self,xp,yp,cube,canva):

        """
        cette fonction permet de dessiner trois polygones
        car trois faces du cube sont visibles et une image
        représente le cube
        """
        xy = cube.coords
        p1 = xy[0][0]
        p2 = xy[0][1]
        p3 = xy[0][2]
        p4 = xy[0][3]
        p5 = xy[1][2]
        p6 = xy[2][2]
        p7 = xy[1][1]
        self.__ch=canva.create_polygon(p1,p2,p3,p4,tags=("poly_haut"),outline="orange",activefill="green",fill='')
        self.__cd=canva.create_polygon(p2,p7,p5,p3,tags=("poly_cd"),outline="pink",activefill="pink",fill='')
        self.__cg=canva.create_polygon(p3,p5,p6,p4,tags=("poly_cg"),outline="orange",activefill="yellow",fill='')
        self.__polygon=canva.create_image(xp-100 ,yp-100, anchor="nw",tags=("image"), image=self.__image)
        canva.tag_raise(self.__ch)
        canva.tag_raise(self.__cg)
        canva.tag_raise(self.__cd)

    def change(self,xp,yp,canva):
        """
        cette fonction permet de changer l'image du cube
        on suprimme donc l'image pour ensuite en remetre une
        """
        canva.delete(self.__polygon)
        self.__image=global_.photo
        self.__polygon=canva.create_image(xp ,yp-50, anchor="nw",tags=("image"), image=self.__image)
        self.__saveim=global_.save_image
