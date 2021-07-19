# Imports
import pickle
from utilities import ImageUrls
from skimage import io
import os
import cv2

# Global variables
URLS_PATH = "./urls_bing_external.pkl"
if os.path.isfile(URLS_PATH):
    with open(URLS_PATH, "rb") as file_urls:
        LIST_URLS = pickle.load(file_urls)
else: raise Exception("Error: Please execute the bing_external_library.py file first")

# Initializations
img_url = ImageUrls(category='url')

flag = False
for url in LIST_URLS:
    if not img_url.contains(url):
        try:
            np_img = cv2.cvtColor(io.imread(url), cv2.COLOR_RGB2BGR)
            cv2.imshow("img_window", np_img)
            while True:
                key_pressed = cv2.waitKey(0) & 0xFF
                if key_pressed == ord("y"):
                    img_url.add(url)
                    break
                elif key_pressed == ord("n"):
                    break
                elif key_pressed == ord('e'):
                    flag = True
                    break
        except Exception as e:
            print(e)
    if flag: break

# Release the ImageUrls and close the output file
del img_url
cv2.destroyAllWindows()
print("---- Finished ----")