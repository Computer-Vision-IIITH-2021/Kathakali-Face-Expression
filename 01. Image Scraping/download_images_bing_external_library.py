# Imports
import glob
import pickle
from utilities import ImageUrls
from skimage import io
import os
import cv2
import logging

# Global variables
DOWNLOAD_PATH = '../images/'
URLS_PATH = "./urls_bing_external.pkl"
OUTPUT_FILE = DOWNLOAD_PATH + "images_ordered_urls.txt"
if os.path.isfile(URLS_PATH):
    with open(URLS_PATH, "rb") as file_urls:
        LIST_URLS = pickle.load(file_urls)
else: raise Exception("Error: Please execute the bing_external_library.py file first")
logging.basicConfig(filename=DOWNLOAD_PATH+"errors.log", level=logging.INFO, filemode='a')

# This file holds the URLs in the order in which these images are downloaded
file_downloaded_urls = open(OUTPUT_FILE, "a")

# Initializations
img_url = ImageUrls(category='url')
img_down_url = ImageUrls(category='download')

i = len(glob.glob(DOWNLOAD_PATH + "*.jpg")) + 1
for url in LIST_URLS:
    if not img_url.contains(url):
        try:
            np_img = cv2.cvtColor(io.imread(url), cv2.COLOR_RGB2BGR)
            cv2.imshow("img_window", np_img)
            key_pressed = cv2.waitKey(0)
            if key_pressed == "y":
                img_url.add(url)
                img_down_url.add(url)
                cv2.imwrite(DOWNLOAD_PATH + "%05d.jpg" % (i, ), np_img)
                file_downloaded_urls.write(url + '\n')
                i += 1
        except Exception as e:
            logging.error("Cannot download the image: %s" % (url, ))
            logging.info(str(e) + '\n')

# Release the ImageUrls and close the output file
del img_url, img_down_url
file_downloaded_urls.write('\n')
file_downloaded_urls.close()
cv2.destroyAllWindows()
print("---- Finished ----")