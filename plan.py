"""----------------------------------
#---- PROJET _CLEMENT_TOM_2021-----
#-----------------------------------
"""
"""
Classe plan
"""


from cube import Cube


class Plan:

    @property
    def plan(self):
        return self.__plan
    @property
    def size(self):
        return self.__size

    def __init__(self,size_x,size_y,size_z):
        """
        Création d'un plan en 3D représenté par une matrice de dimension X*X*Z
        pour accéder à la valeur cube en (0,2,3) on fait plan[0][2][3]
        """
        self.__plan = [[[[] for z in range(size_z)] for y in range(size_y)] for x in range(size_x)]
        self.__size = (size_x,size_y,size_z)

    def __getitem__(self,index):
        x,y,z = index
        return self.__plan[x][y][z]

    def __setitem__(self,index,value):
        """
        On verifie que la donnée à insérer est valide
        """
        x,y,z = index

        if (len(value)>2):
            raise(TypeError)

        self.__plan[x][y][z] = value
