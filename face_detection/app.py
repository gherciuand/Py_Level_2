from selenium import webdriver
from images import saveImage
from se import Search_in_Google

names = ["мальвина", "буратино", "папа карло"]
select_browser = int(input('Please select browser:\n'
                           '----------------\n'
                           '1 - Crome\n'
                           '2 - Edge\n'
                           '----------------\n'))

if select_browser == 1:
    browser = webdriver.Chrome("drivers/chromedriver.exe")
elif select_browser == 2:
    browser = webdriver.Edge("drivers/msedgedriver.exe")
else:
    print('Please select available browser')



img_dict=Search_in_Google(browser, names)

for name in names:
    for img in range(len(img_dict[name])):
        saveImage(img, name)