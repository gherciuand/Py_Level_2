from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from time import sleep
from images import saveImage

name = input('Find :')

browser = webdriver.Chrome("drivers/chromedriver.exe")
browser.get('https://images.google.com/')
inputElement = browser.find_element_by_class_name('gLFyf')
inputElement.send_keys(name)
inputElement.send_keys(Keys.ENTER)
data_image = browser.find_element_by_class_name("rg_i")
src = data_image.get_attribute("src")
# print(src)
# img = urllib.request.urlretrieve(src, f'./orig_img_dir/{name}.jpg')
# print(img)
browser.quit()

saveImage(src, name)
