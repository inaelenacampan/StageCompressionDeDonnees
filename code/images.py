"""
Manipulation des images
"""

""" Bibliotheques """

import numpy as np
from PIL import Image

def read_image(image_path):
    """ fonction de lecture de l'image \\
        format attendu : taille une puissance de 2
    """

    """ lecture et conversion en noir et blanc """

    image = Image.open(image_path).convert('L')
    image_array = np.array(image)

    """ verification que la taille de la matrice est de la bonne forme """

    print('Taille matrice : ' + str(image_array.shape))

    """ Affichage de l'image en NB """

    image.show()
    
    return image_array, int(image_array.shape[1])


def generate_image(array):
    
    """ fonction qui genere l'image, a partir d'une matrice """
    
    reconstructed_image = Image.fromarray(array.astype(np.uint8))
    reconstructed_image.show()
    
    return reconstructed_image