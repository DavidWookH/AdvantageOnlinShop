import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#[delete] import moodle_locators as locators
# to use drop down scroll
from selenium.webdriver.support.ui import Select # <-- add this import for drop down list

# # create a Chrome driver Instance, specify path to chromedriver file
# # this gives a DeprecationWarning
# driver = webdriver.Chrome('C:\Automation\Python\pytho_cctb\chromedriver.exe')

s = Service(executable_path='../chromedriver.exe') # no deprecation
driver = webdriver.Chrome(service=s)

# --------- DATA PARAMETERS -------------------------
app = 'Wikipedia'
wiki_url1 = 'https://en.wikipedia.org/' # initial url for wiki
wiki_home_page_title = 'Wikipedia, the free encyclopedia'
wiki_word = 'Python (programming language)'
wiki_word1 = 'Python'

#moodle_login_page_url = 'http://52.39.5.126/login/index.php'
#intro heading of code writer
def headintro():
    print("*-------------------------------------------------------*")
    print(" Lab15 Assignment :   Wikipedia Selenium  by Wook Huang ")
    print("*-------------------------------------------------------*")
    print("1. Using Selenium WebDriver, open the web browser.")
    print("2. Maximize the browser window.")
    print("3. Navigate to https://en.wikipedia.org/ web URL")
    print("4. Check URL and title are as expected. ")
    print("5.In a search field, find Python (programming language) and click on it.")
    print("6.Check that the title Python (programming language) is displayed. ")
    print("7. Click by the Wikipedia main image (logo) to navigate back to the home page and close the browser. ")
    print(f'*--------------------------------------------------------*')

def lab15_fn():
    print(f'Launch {app} App')
    print(f'*--------------------------------------------------------*')

    # Make browser full screen
    driver.maximize_window()     # 2. Maximize the browser window.

    # Give the browser up to 15 seconds to respond
    driver.implicitly_wait(15)

    # Navigate to Wikipedia app website
    driver.get(wiki_url1)  #Initialization       # 3. Navigate to https://en.wikipedia.org/ web URL
#    print(f'url1= {wiki_url1}')
    wiki_url = driver.current_url  # 1. Using Selenium WebDriver, open the web browser.
#    print(f'url2= {wiki_url}')

    ## Check that  Wikipedia URL and the home page titles are displayed
    if driver.current_url == wiki_url and driver.title == wiki_home_page_title:
        print(f'Yey!{app} launched successfully!')
        print(driver.current_url)
        # 4. Check URL and title are as expected.
        print(f'{app} homepage URL: {driver.current_url}, ')
        print(f'Homepage title: {driver.title} ' )
        print(f'*--------------------------------------------------------*')
        sleep(0.25)
    else:
        print(f'{app} did not launch. Check your code or the application')
        print(f'Current URL : {driver.current_url}, Homepage title: {driver.title}')
        tearDown()

    # Perform under same function 5. In a search field, find Python (programming language) and click on it.")
    # 6.Check that the title Python (programming language) is displayed. ")
    # if driver.current_url == wiki_url

    if driver.current_url == wiki_url :
       driver.find_element(By.ID,'searchInput').send_keys(wiki_word1)
       sleep(0.25)
       #driver.find_element(By.ID,'searchButton').click() # option solution, press search icon
       driver.find_element(By.LINK_TEXT,'Python (programming language)').click() # option solution, press search icon
       sleep(0.25)
       # driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
       print(f'Current page title: {driver.title}')
       sleep(0.25)
       #Select(driver.find_element(By.CLASS_NAME, 'mw-searchSuggest-link')).select_by_visible_text(wiki_word).click()
       #Select(driver.find_element(By.ID, 'searchInput').send_keys(wiki_word)).select_by_visible_text(wiki_word)

       # 7. Click by the Wikipedia main image (logo) to navigate back to the home page and close the browser.
       driver.find_element(By.ID, 'p-logo').click()
       print(f'Current URL : {driver.current_url}')

       sleep(0.25)
       # breakpoint()

def tearDown():
    if driver is not None:
        print(f'*--------------------------------------------------------*')
        print(f'The test is completed at : {datetime.datetime.now()}')
        print(f'*--------------------------------------------------------*')
        sleep(0.5)
        driver.close()
        driver.quit()

# Launch app
headintro()
lab15_fn()
#tearDown()