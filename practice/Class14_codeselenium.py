from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

# create a Chrome driver Instance, specify path to chromedriver file
# # this gives a DeprecationWarning
# driver = webdriver.Chrome('../chromedriver.exe')
# # driver = webdriver.Chrome('C:\Automation\Python\pytho_cctb\chromedriver.exe')

s = Service(executable_path='../chromedriver.exe') # no deprecation
driver = webdriver.Chrome(service=s)    # open the web browser.

# Make browser full screen
driver.maximize_window()

# Give the browser up to 30 seconds to respond
driver.implicitly_wait(30)

# Navigate to CCTB  website
driver.get('http://52.39.5.126/')

## Check that  Moodle URL and the home page titles are displayed

if driver.current_url == 'http://52.39.5.126/' and driver.title == 'Software Quality Assurance Testing':
    print(f'Yey! Moodle launched successfully!')
    print(f'Moodle homepage URL: {driver.current_url}')
    print(f'Homepage title:  {driver.title} ' )
    sleep(5)
    driver.close()
else:
    print(f'Moodle did not launch. Check your code or the application')
    print(f'Current URL : {driver.current_url}')
    print(f'Home page title: {driver.title}')
    driver.close()
    driver.quit()
