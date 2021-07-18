# Imports
from selenium import webdriver
import pickle
from utilities import ImageUrls

# Global variables
DRIVER_PATH = '/home/bullu/chromedriver_linux64/chromedriver'
RELATED_URLS_PATH = './urls_yandex_related.pkl'
with open(RELATED_URLS_PATH, "rb") as file_input:
    LIST_URLS = pickle.load(file_input)

# webdriver initialization
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("./extension_1_36_2_0.crx") # adblock extension
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
driver.implicitly_wait(10) # seconds
driver.maximize_window()

img_url = ImageUrls()
for url in LIST_URLS:
    driver.get(url)
    while True:
        key_pressed = input('Press the enter key after reaching the destination image. Enter "quit" to proceed to the next related URL: ')
        if key_pressed == "quit": break
        img_link = driver.find_element_by_xpath('//img[@class="MMImage-Origin"]').get_attribute('src') # Fetch the src attribute of the image
        if not img_url.contains(img_link):
            print(img_link)
            img_url.add(img_link)

# Quit the driver
del img_url
driver.quit()
print("---- Finished ----")