import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# # create a Chrome driver Instance, specify path to chromedriver file
# # this gives a DeprecationWarning

s = Service(executable_path='../chromedriver.exe') # no deprecation
driver = webdriver.Chrome(service=s)

# --------- DATA PARAMETERS -------------------------
dbz_url = 'https://www.demoblaze.com/' # initial url for demoblaze
dbz_home_page_title = 'STORE'


def headintro():
    print("*-------------------------------------------------------*")
    print(" Lab16 Assignment :   Selenium: Demoblaze  by Wook Huang ")
    print("*-------------------------------------------------------*")
    print("1. Using Selenium WebDriver, open the web browser.")
    print("2. Maximize the browser window.")
    print("3. Navigate to https://www.demoblaze.com/  web URL")
    print("4. Check URL and title are as expected. ")
    print("5. On the home page, find the Nexus 6 model and click on it")
    print("6. On the product page, check Nexus 6 h2 title is displayed. Use assert. ")
    print("7.  Click by Add to Cart button. If you'll see an alert at the top, ")
    print("    use this command - driver.switch_to.alert.accept()")
    print("8. Go to Cart at the top menu and click on it.")
    print("9. Check the order is displayed and click by Delete link.")
    print("10. Close the browser and display a user-friendly message. ")
    print(f'*--------------------------------------------------------*')

def setup():
    print(f'Launch Demoblaze website')
    print(f'*--------------------------------------------------------*')
    # Make browser full screen
    driver.maximize_window()     # 2. Maximize the browser window.
    # Give the browser up to 15 seconds to respond
    driver.implicitly_wait(15)
    # Navigate to Demoblaze app website
    driver.get(dbz_url)  #Initialization

    if driver.current_url == dbz_url and driver.title == dbz_home_page_title:
        print(f'---------------------------------------------------------------')
        print(f'Good Job! Demoblaze App website launched successfully! ')
        print(f'---------------------------------------------------------------')
        print(f'Demoblaze Homepage URL: {driver.current_url} ')
        print(f'Demoblaze Homepage title: " {driver.title} "')
        sleep(0.5)
    else:
        print(f'demoblaze web site  did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: " {driver.title}"')
        print(f'*--------------------------------------------------------*')
        sleep(0.5)

def dbz_nexus_demo():
    if  driver.current_url == dbz_url:  # check we are on the Demoblaze homp page
        driver.find_element(By.LINK_TEXT, 'Nexus 6').click()
        sleep(1.5)
    # driver.find_element(By.LINK_TEXT, 'Nexus 6').click()
        assert driver.find_element(By.XPATH, '//h2[contains(., "Nexus 6")]').is_displayed()
        sleep(1.5)   # 6. h2 title checked with assert
        driver.find_element(By.LINK_TEXT, 'Add to cart').click()
        sleep(1.5)
        driver.switch_to.alert.accept()
        sleep(1)
        # breakpoint()
        driver.find_element(By.LINK_TEXT,'Cart').click()
        # driver.find_element(By.ID, 'cartur').click() #7, add to cart
        sleep(1)
        #breakpoint()

        assert driver.find_element(By.XPATH, '//td[contains(., "Nexus 6")]').is_displayed()
        sleep(1.5)
        driver.find_element(By.LINK_TEXT,'Delete').click()
        sleep(1.5)
        print(f'----- Demoblaze exercise is done ------------------ ')
    else:
         print(f'    for Demoblaze web, Something went wrong!')
         print(f'*--------------------------------------------------------*')
         sleep(0.5)

def tearDown():
    if driver is not None:
        print(f'*--------------------------------------------------------*')
        print(f'The test is completed at : {datetime.datetime.now()}')
        print(f'*--------------------------------------------------------*')
        sleep(0.5)
        driver.close()
        driver.quit()


#--------------------------------------------
# Run Code:
#--------------------------------------------
headintro()
setup()
dbz_nexus_demo()
#tearDown()
