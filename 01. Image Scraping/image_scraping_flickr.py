# Imports
from utilities import ImageUrls
from selenium import webdriver

# Global variables
DRIVER_PATH = '/home/bullu/chromedriver_linux64/chromedriver'

# webdriver initialization
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("./extension_1_36_2_0.crx") # adblock extension
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
driver.implicitly_wait(10) # seconds
driver.maximize_window()

# initialize the web page
driver.get('https://www.flickr.com/groups/kathakali/')

# Iterate all the images
img_url = ImageUrls()
try:
    driver.find_element_by_xpath('//a[@class="overlay"]').click() # Click the first image
    while True:
        key_pressed = input('Choice (y or n): ')
        img_link = driver.find_element_by_xpath('//img[@class="main-photo"]').get_attribute('src') # Fetch the src attribute of the image
        if not img_url.contains(img_link): # If the url is not scanned earlier
            if key_pressed == 'y': # If y is pressed
                print(img_link)
                img_url.add(img_link) # Add the image source to the ImageUrl class
        driver.find_element_by_xpath('//a[@class="navigate-target navigate-next"]/span[@class="hide-text"]').click()
except Exception as e:
    print(e)
finally:
    # Quit the driver and delete img_url
    del img_url
    driver.quit()
    print("---- Finished ----")