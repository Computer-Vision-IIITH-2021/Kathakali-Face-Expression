# Imports
from selenium import webdriver
import pickle
from utilities import ImageUrls

# Global variables
DRIVER_PATH = '/home/bullu/chromedriver_linux64/chromedriver'
RELATED_URLS_PATH = './urls_bing_related.pkl'
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
        key_pressed = input('Press the enter key after reaching the destination image. Enter "q" to proceed to the next related URL: ')
        if key_pressed.startswith("q"): break
        img_link = driver.find_element_by_xpath('//div[@class="mainImage  current"]//img[@class=" nofocus"]').get_attribute('src') # Fetch the src attribute of the image
        if not img_url.contains(img_link):
            print(img_link)
            img_url.add(img_link)
    if key_pressed == "quit all": break

# Quit the driver
del img_url
driver.quit()
print("---- Finished ----")