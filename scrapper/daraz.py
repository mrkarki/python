###################
# Author:        Nabin Karki
# Plugin:        Get all the daraz data with given url
# Description:   Get all the data using  #BeautifulSoup and #selenium and #pandas
###################

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
# from selenium.webdriver import Firefox

driverpath="C:\\python\\chromedriver.exe"
#driverpath="C:\\python\\geckodriver-v0.27.0-win64\\geckodriver.exe"
#driver = webdriver.Firefox(executable_path="C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\selenium\\webdriver\\firefox\\webdriver.py")
driver = webdriver.Chrome(driverpath)
# for x in range(1,100):
list_data=[]
for x in range(1,2):
    #URL = "https://www.daraz.com.np/smartphones/?page="
    URL = "https://www.daraz.com.np/pet-supplies-shop/?page="
    #url= URL+str(x)+"&spm=a2a0e.11779170.cate_1.1.287d2d2bAWBB2q"
    url= URL+str(x)
    print(url)
    driver.get(url)

    time.sleep(5)

    content=driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
   
    contents=soup.find_all('div',class_='c2prKC')
    for single_content in contents:

        p_image_wrap=single_content.find_all('div',class_='cRjKsc')
        p_image_url=p_image_wrap[0].a.img
        print(p_image_wrap)
        exit
        if p_image_url:
            p_image_url=p_image_url['src']
        else:
            p_image_url=''

        p_name=single_content.find_all('div',class_='c16H9d')
        p_name=p_name[0].a.get_text()

        p_salep=single_content.find_all('div',class_='c3gUW0')
        salep=p_salep[0].span.get_text()

        p_regularp=single_content.find_all('div',class_='c3lr34')
        p_regularp=p_regularp[0].find('del')
        if p_regularp:
            regularp=p_regularp.get_text()
        else:
            regularp=salep

        if p_regularp:
            salep=salep
        else:
            salep=''

        new_dist={
            'Type'  : 'simple',
            'Name'  :  p_name,
            'Published'  :  1,
            'Images'  :  p_image_url,
            'Sale price'    :  salep,
            'Regular price' :  regularp,
            
        }
        list_data.append(new_dist)

df=pd.DataFrame(list_data)
print(df.head())
df.to_csv('Daraz_pet_new.csv')