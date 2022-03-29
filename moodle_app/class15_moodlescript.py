import datetime
from time import sleep
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

# ----------------- Moodle Web App DATA PARAMETERS ----------------------
app = 'Moodle'
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_title = 'Dashboard'

admin_username = 'tkuser'
admin_password='Moodle!123'
# -----------------------------------------------------------------------

# Moodle Test Automation Plan
# launch Moodle App website - validate we are on the home page

# navigate to Login page - validate we are on the login page
# login with admin account - validate we are on the Dashboard page

# navigate to Add New User page - Site Administration > Users > Add New User - validate we are on the Add new User page
# populate the new user form fields using Faker library fake random data
# submit a new user form

# validate new user added:
# search for a new user using email - validate new is found
# logout of admin account
# login as a new user - validate a new user can login
# logout of new user account
# login with admin acount
# search for a new user using email address
# delete new user

def setUp():
    print(f'Launch {app} App')
    print(f'-------------------------~*~--------------------------')
    # make browswer full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to Moodle App website
    driver.get(moodle_url)
    # check that Moodle URL and the home page title are as expected
    if driver.current_url == moodle_url and driver.title == moodle_home_page_title:
        print(f'Yey! {app} App website launched successfully!')
        print(f'{app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'-------------------------~*~--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == moodle_url:  # check we are on the home page
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == moodle_login_page_url and driver.title == moodle_login_page_title: # check we are on the login page
            print(f'{app} App Login page is displayed! Continue to log in.')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(admin_username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(admin_password)
            driver.find_element(By.ID, 'loginbtn').click()
            # validate login successfull Dashboard page is displayed
            if driver.current_url == moodle_dashboard_url and driver.title == moodle_dashboard_title:
                assert driver.current_url == moodle_dashboard_url
                assert driver.title == moodle_dashboard_title
                print(f' ---- Login is successful. {app} Dashboard is displayed - Page title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code or website and try again.')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == moodle_url:
        print(f' ---- Logout successful! {datetime.datetime.now()}')


# Launch app
setUp()
# Login
log_in()
# Logout
log_out()
# Close app
tearDown()