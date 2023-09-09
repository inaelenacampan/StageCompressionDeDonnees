""" Tests sur des images"""

import images
import haar

test_array, size = images.read_image('cat.jpg')
reconstructed_image = images.generate_image(haar.HaarImageCompression(size, test_array, 200))

test_array, size = images.read_image('Google.png')
reconstructed_image = images.generate_image(haar.HaarImageCompression(size, test_array, 300))
