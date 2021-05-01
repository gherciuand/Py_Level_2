from selenium.webdriver.common.keys import Keys
from time import sleep
import random

dict_names = {}


def Search_in_Google(search_browser, names, quantity=20, address="https://images.google.com/"):
    search_browser.get(address)

####### find name in google
    for name in names:
        img_list = []
        inputElement = search_browser.find_element_by_name('q')
        inputElement.clear()
        inputElement.send_keys(name)
        sleep(random.uniform(0.2, 0.7))
        inputElement.send_keys(Keys.ENTER)
        sleep(random.uniform(0.2, 0.7))

####### go to advanced search and apply portrait filter
        search_browser.find_element_by_class_name('PNyWAd').click()
        sleep(random.uniform(0.2, 0.7))
        search_browser.find_elements_by_class_name('SiT4cd-ibnC6b-bN97Pc')[2].click()
        sleep(random.uniform(0.2, 0.7))
        search_browser.find_element_by_id(':7z').click()
        sleep(random.uniform(0.2, 0.7))
        search_browser.find_element_by_id(':7u').click()
        sleep(random.uniform(0.2, 0.7))
        search_browser.find_element_by_class_name('jfk-button').click()

####### save image's URL in list
        n=0
        data_images = search_browser.find_elements_by_css_selector("img.rg_i")
        for image in data_images:
            img=image.get_attribute("src")
            img_list.append(img)
            n+=1
            if n>=quantity:
                break
####### save data in dictionary
        dict_names[name] = img_list
    search_browser.quit()
    return dict_names

