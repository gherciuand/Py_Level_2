from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from time import sleep

name = input('Find :')

browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
browser.get('https://images.google.com/')
inputElement = browser.find_element_by_class_name('gLFyf')
inputElement.send_keys(name)
inputElement.send_keys(Keys.ENTER)
data_image = browser.find_element_by_class_name("rg_i")
scr = data_image.get_attribute("src")

img = urllib.request.urlretrieve(scr, f'./orig_img_dir/{name}.jpeg')

browser.quit()