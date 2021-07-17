# Imports
from utilities import ImageUrls
from selenium import webdriver
import sys
import pickle

# Check proper execution command
if len(sys.argv) != 2: raise Exception("Error: Execution command is: python %s <int_limit_images>" % (sys.argv[0], ))

# Global variables
DRIVER_PATH = '/home/bullu/chromedriver_linux64/chromedriver'
ANCHORS_LOADING_SECS = 10
DELAY_SECS = 3
SEARCH_KEYWORDS = 'kathakali'
LIMIT_IMAGES = int(sys.argv[1])
OUTPUT_PATH = './urls_bing_related.pkl'

# webdriver initialization
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("./extension_1_36_2_0.crx") # adblock extension
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
driver.implicitly_wait(10) # seconds
driver.maximize_window()

# initialize the web page
driver.get('https://www.bing.com/images/trending?FORM=ILPTRD')
driver.find_element_by_id('sb_form_q').send_keys(SEARCH_KEYWORDS)
driver.find_element_by_id('sb_form_go').click()

# Iterate all the images
img_url = ImageUrls()
list_visited_urls = []
try:
    driver.find_element_by_class_name('mimg').click() # Click the first image
    driver.switch_to.frame(driver.find_element_by_id('OverlayIFrame'))
    while True:
        key_pressed = input('Choice (y or n): ')
        img_link = driver.find_element_by_xpath('//div[@class="mainImage  current"]//img[@class=" nofocus"]').get_attribute('src') # Fetch the src attribute of the image
        if not img_url.contains(img_link): # If the url is not scanned earlier
            if key_pressed == 'y': # If y is pressed
                print(img_link)
                list_visited_urls.append(driver.current_url) # Add the current URL to the visited URLs list
                img_url.add(img_link) # Add the image source to the ImageUrl class
        else:
            list_visited_urls.append(driver.current_url) # Add the current URL to the visited URLs list
        driver.find_element_by_xpath('//span[@class="icon" and @title="Next image result"]').click() # Go to the next image
except Exception as e:
    print(e)

# Quit the driver, delete img_url and save the visited urls
del img_url
driver.quit()
with open(OUTPUT_PATH, "wb") as file_output:
    pickle.dump(list_visited_urls, file_output)
print("---- Finished ----")