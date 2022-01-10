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
        im_bin = Image()
        # affectation a l'image im_bin d'un tableau de pixels de meme taille
        # que self dont les intensites, de type uint8 (8bits non signes),
        # sont mises a 0
        im_bin.set_pixels(np.zeros((self.H,self.W), dtype=np.uint8))
        # TODO: boucle imbriquees pour parcourir tous les pixels de l'image im_bin
        # et calculer l'image binaire
        for l in range(self.H):
            for c in range(self.W):
                # modif des pixels d'intensite >= a S
                if self.pixels[l][c] >= S:
                    im_bin.pixels[l][c] = 255
                    # Le pixel est transformé en blanc s’il dépasse le seuil
                else :
                    im_bin.pixels[l][c] = 0
                    # Le pixel est transformé en noir s’il est en dessous du seuil
        return im_bin
        


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        c = []
        l = []
        l_min = 0
        c_min = 0
        l_max = 0
        c_max = 0
        im_reca =Image()
        # on cree toutes nos variables qui nous seront utiles pour les
        #coordonnees du rectangle et pour définir l'image recadree
        

        for a in range(self.H):
           for k in range(self.W):
               # On parcourt tous les pixels de l'image
               if self.pixels[a][k] == 0:
                   c.append(k)
                   l.append(a)
                   # On repere tous les pixels noirs (qui nous serviront donc 
                   #pour les coordonnees du rectangle) pour les stocker dans
                   #nos listes.
                 
        l_min = min(l)
        c_min = min(c)
        l_max = max(l)
        c_max = max(c)
        # on repere ensuite les lignes et colonnes min et max de nos pixels 
        #noirs qui seront donc les coordonnees de notre rectangle
        im_reca.pixels = self.pixels[l_min:l_max,c_min:c_max]
        return (im_reca)
    # On retourne donc ensuite notre image bornee au rectangle dont nous
    # avons obtenu les coordonnees.
    
    
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        # on prepare le résultat en creant une image vide
        im_resized = Image()
        im_resized.pixels = resize(self.pixels, (new_H, new_W), 0)
        # on utilise la fonction resize 
        im_resized.pixels = np.uint8(im_resized.pixels*255)
        # Les valeurs de la fonction resize doivent etre des reels compris entre 
        #entre 0 et 1, pour cela, on les multiplie par 255
        # et on les convertit en entier non signe sur 8 bits
        im_resized.H = new_H
        im_resized.W = new_W
        # On precise bien les nouvelles valeurs des dimensions de notre 
        #image recadree
        return (im_resized)


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        # On definit d'abord les variables qui nous serviront
        #pour trouver la correlation entre les 2 images
        res = 0
        correl = 0
        # on peut tout aussi bien utiliser self.H/W que im.H/W 
        #pour parcourir tous les pixels des images car 
        #les images possedent les mêmes dimensions grace à la methode
        #resize_im
        for l in range(self.H):
            for c in range(self.W):
                if self.pixels[l][c] == im.pixels[l][c]:
                    res = res + 1
                    # a chaque fois que les pixels sont egaux au meme endroit
                    # on ajoute 1 a une variable quelconque
        
        correl = res / (self.H * self.W)
        # Puis on divise le resultat obtenu apres avoir parcouru tous les 
        # pixels par le nombre total de pixels afin d'obtenir un résultat
        # compris entre 0 et 1
        return (correl)

