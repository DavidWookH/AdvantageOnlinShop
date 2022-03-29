# import datetime
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# s = Service(executable_path='../chromedriver.exe') # no deprecation
# driver = webdriver.Chrome(service=s)

item = ['Nexus 6','Sony xperia z5','Samsung galaxy s6']
i= len(item);

for i in item:
    if i <= len(item):
        print(item[i])
        i+=1
    else :
        print('Bang')
