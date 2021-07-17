# Imports
from skimage import io
import cv2
from utilities import ImageUrls
import glob
import tqdm
import logging

# Global Variables
DOWNLOAD_PATH = '../images/'
logging.basicConfig(filename=DOWNLOAD_PATH+"errors.log", level=logging.INFO, filemode='a')

# Initializations
img_url = ImageUrls(category='url')
img_down_url = ImageUrls(category='download')

# Download each image
i = len(glob.glob("*.jpg")) + 1
for url in tqdm.tqdm(img_url.fetch_all_urls()):
    if not img_down_url.contains(url):
        try:
            img_down_url.add(url)
            cv2.imwrite(DOWNLOAD_PATH + "%05d.jpg" % (i, ), cv2.cvtColor(io.imread(url), cv2.COLOR_RGB2BGR))
            i += 1
        except Exception as e:
            logging.error("Cannot download the image: %s" % (url, ))
            logging.info(str(e) + '\n')

# Release the ImageUrls
del img_url, img_down_url