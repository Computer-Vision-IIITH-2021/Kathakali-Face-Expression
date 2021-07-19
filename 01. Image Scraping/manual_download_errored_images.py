# Imports
from selenium import webdriver
import glob

# Global initializations
DOWNLOAD_PATH = '../images/'
DRIVER_PATH = '/home/bullu/chromedriver_linux64/chromedriver'
IMAGES_ERROR_PATH = DOWNLOAD_PATH + 'errors.log'
OUTPUT_FILE_PATH = DOWNLOAD_PATH + "images_ordered_urls.txt"

# webdriver initialization
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("./extension_1_36_2_0.crx") # adblock extension
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
driver.implicitly_wait(10) # seconds
driver.maximize_window()

# This file holds the URLs in the order in which these images are downloaded
file_downloaded_urls = open(OUTPUT_FILE_PATH, "a")

try:
    # Iterate the errored images
    i = len(glob.glob(DOWNLOAD_PATH + "*.jpg")) + 1
    with open(IMAGES_ERROR_PATH, "r") as file_errored_urls:
        while True:
            line1 = file_errored_urls.readline()
            line2 = file_errored_urls.readline()
            line3 = file_errored_urls.readline()
            if line1 == "" and line2 == "" and line3 == "": break
            img_link = line1.split()[-1]
            assert img_link.startswith("http")
            driver.get(img_link)
            input("Please save the image manually as '%05d.jpg' and hit enter" % (i, ))
            file_downloaded_urls.write(img_link + '\n')
            i += 1
except Exception as e:
    print(e)
finally:
    # Quit the driver and close the file(s)
    driver.quit()
    file_downloaded_urls.write('\n')
    file_downloaded_urls.close()
    print('---- Finished ----')