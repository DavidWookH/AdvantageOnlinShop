import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='../chromedriver.exe') # no deprecation
driver = webdriver.Chrome(service=s)

# # create a Chrome driver Instance, specify path to chromedriver file
# # this gives a DeprecationWarning
# driver = webdriver.Chrome('../chromedriver.exe')
# # driver = webdriver.Chrome('C:\Automation\Python\pytho_cctb\chromedriver.exe')

# ----- Moodle App and Data Parameter -------------------
app = 'Moodle'
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_title = 'Dashboard'

# Moodle Test Automation Plan
# launch Moodle App Website  - validate we are on the home page
# navigate to Login page - validate we are on the login page
# login with admin account - validate we are on the Dashboard page
# navigate to Add New User page - Site Administration > Users > Add New USer



def setUp():
    print(f'Launch {app} App')
    print(f'*--------------------------------------------------------*')
    # Make browser full screen
    driver.maximize_window()
    # Give the browser up to 15 seconds to respond
    driver.implicitly_wait(15)
    #Navigate to Moodle app website
    driver.get(moodle_url)
    ## Check that  Moodle URL and the home page titles are displayed
    if driver.current_url == moodle_url and driver.title == moodle_home_page_title:
        print(f'Yey!{app} launched successfully!')
        print(f'{app} homepage URL: {driver.current_url}, Homepage title: {driver.title} ' )
        print(f'*--------------------------------------------------------*')
        sleep(0.25)
    else:
        print(f'{app} did not launch. Check your code or the application')
        print(f'Current URL : {driver.current_url}, Homepage title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print(f'*--------------------------------------------------------*')
        print(f'The test is completed at : {datetime.datetime.now()}')
        print(f'*--------------------------------------------------------*')
        sleep(0.5)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == moodle_login_page_url and driver.title == moodle_login_page_title: # check login
           print(f'{app} App Login page is displayed! please Continue to log in.')
           print(f'*--------------------------------------------------------*')
           sleep(1)
           driver.find_element(By.ID, 'username').send_keys('wookhuang')
           sleep(1)
           driver.find_element(By.ID, 'password').send_keys('Moodle##5838108')
           sleep(1)
           driver.find_element(By.ID, 'loginbtn').click()
           if driver.current_url == moodle_dashboard_url and driver.title == moodle_dashboard_title:
               assert driver.current_url == moodle_dashboard_url
               assert driver.title == moodle_dashboard_title
               print(f'---- Login is successful. {app} Dashboard is displayed - Page title: {driver.title}')
           else:
               print(f'Dashboard is not displayed. Check your code or website and try again.')


def log_out():
    driver.find_element(By.CLASS_NAME,'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == moodle_url:
        print(f'----Logout Successful {datetime.datetime.now()}')
def create_new_user():
    #Navigate to 'Add a new user' form
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
# #
# Launch app
setUp()

# Login# Launch app
log_in()
sleep(3)

def create_new_user():
# Logout
# log_out()
#
# # Close app
# tearDown()

