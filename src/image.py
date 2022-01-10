from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        # preparaton du resultat : creation d'une image vide 
        im_modif = image()
        # affectation de l'image resultat par un tableau de 0, de meme taille
        # que le tableau de pixels de l'image self
        # les valeurs sont de type uint8 (8bits non signes)
        im_modif.set_pixels(np.zeros((self.H,self.W), dtype=np.uint8))
                                                
        # boucle imbriquees pour parcourir tous les pixels de l'image
        for l in range(self.H):
            for c in range(self.W):
                # modif des pixels d'intensite >= a S
                if self.pixels[l][c] >= S:
                    im_modif.pixels[l][c] = 255
                else :
                    im_modif.pixels[l][c] = 0
        return im_modif


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
       # preparaton du resultat : creation d'une image vide 
        im_modif = image()
        
        # initialisation des coordonnÃ©es maximum Ã  0 et minimm Ã  la valeur
        # de la dimension correspondante
        lmax = 0
        lmin = self.H
        cmax = 0
        cmin = self.W
                                                
        # boucle imbriquees pour parcourir tous les pixels de l'image
        for l in range(self.H):
            for c in range(self.W):
                # recherche des coordonnÃ©es maximum
                if self.pixels[l][c] == 0:
                    if l > lmax:
                        lmax = l
                    if c > cmax:
                        cmax = c
                # recherche des coordonÃ©es minimum
                    if l < lmin:
                        lmin = l
                    if c < cmin:
                        cmin = c
        
        # remplissage de l'image avec l'image self qui est elle meme recadrÃ©e
        # avec les coordonnÃ©es trouvÃ©es
        im_modif.set_pixels(self.pixels[lmin:lmax+1,cmin:cmax+1])
        return im_modif

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
       # preparaton du resultat : creation d'une image vide 
        im_modif = image()
        
        # crÃ©ation d'un tableau x reprenant les valeurs du tableau de l'image 
        # initiale et de la taille voulue
        x = resize(self.pixels, (new_H,new_W), 0)
        x = np.uint8(x*255)
        
        # remplissage de l'image avec le tableau x
        im_modif.set_pixels(x)
        return im_modif


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        pass

