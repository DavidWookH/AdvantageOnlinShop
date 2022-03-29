from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

# create a Chrome driver Instance, specify path to chromedriver file
# # this gives a DeprecationWarning
# driver = webdriver.Chrome('../chromedriver.exe')
# # driver = webdriver.Chrome('C:\Automation\Python\pytho_cctb\chromedriver.exe')

print("*-------------------------------------------------------*")
print(" Lab14 Assignment :   Selenium  by Wook Huang ")
print("*-------------------------------------------------------*")
print(" 1. Using Selenium WebDriver, open the web browser. ")
print(" 2. Maximize the browser window.")
print(" 3. Navigate to the Google Canada website ")
print("    and check that this page has Google in the title")
print("    and https://www.google.ca/ as the current URL.")
print(" 4. If yes, display a user-friendly message about successful landing")
print("    and correct title. Use condition to check URL and the Title.")

s = Service(executable_path='../chromedriver.exe') # no deprecation
driver = webdriver.Chrome(service=s)
# Make browser full screen
driver.maximize_window()
# Give the browser up to 30 seconds to respond
driver.implicitly_wait(30)

# Navigate to the Google Canada website
driver.get('https://www.google.ca/')

## Check that  Google URL and the home page titles are displayed

if driver.current_url == 'https://www.google.ca/' and driver.title == 'Google':
    print(f'*----------------------------------------------------*')
    print(f'Yey! Google canada site launched successfully!')
    print(f'Google homepage URL: {driver.current_url}')
    print(f'Homepage title:  {driver.title} ' )
    print(f'*----------------------------------------------------*')
    sleep(5)
    driver.close()
else:
    print(f'*--------------------------------------------------------*')
    print(f'Google did not launch. Check your code or the application')
    print(f'Current URL : {driver.current_url}')
    print(f'Home page title: {driver.title}')
    print(f'*--------------------------------------------------------*')
    driver.close()
    driver.quit()
