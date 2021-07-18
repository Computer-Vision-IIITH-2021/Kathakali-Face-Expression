# Imports
import cv2
import glob

# Global variables
IMAGES_PATH = '../images/'

# Iterate the images
for img_path in sorted(glob.glob(IMAGES_PATH + "*.jpg")):
    print(img_path)
    # cv2.imshow(cv2.imread(img_path))