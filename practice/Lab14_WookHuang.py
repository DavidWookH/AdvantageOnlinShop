import datetime
from time import sleep
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='../chromedriver.exe')   # Chrome driver
driver = webdriver.Chrome(service=s)

# ----------------- CCTB Web App DATA PARAMETERS ----------------------
app = 'CCTB'
cctb_url = 'https://www.canadianctb.ca/'
cctb_page_title = 'CCTB | Canadian College of Technology and Business'
cctb_vsl_url = 'https://www.canadianctb.ca/virtual-student-lounge'
cctb_vsl_title = 'Virtual Student Lounge | CCTB'

# -----------------------------------------------------------------------
# 1. Using Selenium WebDriver, open the web browser.
# 2. Maximize the browser window.
# 3. Navigate to the 'https://www.canadianctb.ca/' website and
#    check that this page has 'CCTB | Canadian College of Technology and Business' in the title
#    and https://www.canadianctb.ca/ as the current URL.
# 4. Next, click by Virtual Student Lounge link text and navigate there.
# 5. Display current URL and title. Compare with your expected values. Use user-friendly messages.

def setUp():
    print("*-------------------------------------------------------*")
    print(" Lab14 Assignment :   Selenium-CCTB  by Wook Huang ")
    print("*-------------------------------------------------------*")
    print(f'Launch {app}- website App')


    # make browswer full screen
    driver.maximize_window()
    # give browser up to 10 seconds to respond
    driver.implicitly_wait(10)
    # navigate to CCTB website
    driver.get(cctb_url)
    # check that CCTB URL and the home page title are as expected
    if driver.current_url == cctb_url and driver.title == cctb_page_title:
        print(f'###----------------------------------------------------------------###')
        print(f'Good Job! {app} App website launched successfully! ')
        print(f'{app} Homepage URL: {driver.current_url} ')
        print(f'{app} Homepage title: " {driver.title} "')
        sleep(2)
    else:
        print(f'{app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: " {driver.title}"')
        tearDown()

def tearDown():
    if driver is not None:
        print(f'----------------------------------------------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        print(f'###----------------------------------------------------------------###')
        sleep(0.5)
        driver.close()
        driver.quit()

def vslounge():
    if driver.current_url == cctb_url:  # check we are on the CCTB homp page
        driver.find_element(By.LINK_TEXT, 'Virtual Student Lounge').click()
        if driver.current_url == cctb_vsl_url and driver.title == cctb_vsl_title: # check we are on the login page
            print(f'###----------------------------------------------------------------###')
            print(f'{app} App {cctb_vsl_title} is displayed!, check current URL & title ')
            print(f'###----------------------------------------------------------------###')
            sleep(0.25)
            print(f'current {app} page URL: {driver.current_url}')
            print(f'current {app} page title: " {driver.title} "')
            print(f'###----------------------------------------------------------------###')

            sleep(0.25)


# Launch app
setUp()

# Virtual Student Lounge
vslounge()

# Close app
tearDown()