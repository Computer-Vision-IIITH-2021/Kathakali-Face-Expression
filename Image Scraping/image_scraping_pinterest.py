# imports
from utilities import ImageUrls
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium.webdriver.common.action_chains import ActionChains

if len(sys.argv) != 2: raise Exception("Error: Execution command is: python %s <int_limit_images>" % (sys.argv[0], ))

# Global variables
DRIVER_PATH = '/home/bullu/chromedriver_linux64/chromedriver'
ANCHORS_LOADING_SECS = 4
DELAY_SECS = 2
SEARCH_KEYWORDS = 'kathakali'
LIMIT_IMAGES = int(sys.argv[1])

# initialization
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("./extension_1_36_2_0.crx")
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
driver.implicitly_wait(10) # seconds
driver.maximize_window()

# load the web page
driver.get('https://in.pinterest.com/')
driver.find_element_by_xpath('//div[@class="tBJ dyH iFc yTZ erh tg7 mWe"]').click()
driver.find_element_by_id('email').send_keys('<email_id>')
for c in '<password>':
    driver.find_element_by_id('password').send_keys(c)
    time.sleep(0.2)
driver.find_element_by_xpath('//button[@type="submit"]').click()
driver.find_element_by_xpath('//input[@type="text"]').send_keys(SEARCH_KEYWORDS) # write the query words
driver.find_element_by_xpath('//input[@type="text"]').send_keys(Keys.RETURN)
time.sleep(ANCHORS_LOADING_SECS)

# Scroll to the bottom until LIMIT_IMAGES is reached
prev_scroll_height = driver.execute_script("return document.body.scrollHeight")
while len(driver.find_elements_by_xpath('//img[@class="hCL kVc L4E MIw"]')) < LIMIT_IMAGES:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(ANCHORS_LOADING_SECS)
    if prev_scroll_height == driver.execute_script("return document.body.scrollHeight"): break
    else: prev_scroll_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script("window.scrollTo(0, 0)")

# Iterate through all the images
main_window = driver.current_window_handle # Getting the current tab identifier
i = 1
img_url = ImageUrls()
for img_element in driver.find_elements_by_xpath('//img[@class="hCL kVc L4E MIw"]'):
    while True:
        try:
            ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(img_element).key_up(Keys.LEFT_CONTROL).perform() # Opening the image in the new tab
            driver.switch_to.window(driver.window_handles[1]) # Switching to the new tab
            break
        except IndexError:
            driver.execute_script("window.scrollTo(0, %d)" % (650 * i, ))
            i += 1
    key_pressed = input('Choice (y or n): ')
    if key_pressed == 'y':
        img_link = driver.find_element_by_xpath('//div[@data-test-id="closeup-image"]//div[@class="XiG zI7 iyn Hsu"]//div[@class="XiG zI7 iyn Hsu"]/img').get_attribute('src') # getting the image link
        if not img_url.contains(img_link):
            print(img_link)
            img_url.add(img_link)
    driver.close() # close the current tab
    driver.switch_to.window(main_window) # switch back to the original tab

# Quit the driver, delete img_url
del img_url
driver.quit()
print("---- Finished ----")