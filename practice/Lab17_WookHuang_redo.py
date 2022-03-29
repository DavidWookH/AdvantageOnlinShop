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
item_lst=['Nexus 6', 'Sony xperia z5', 'Samsung galaxy s6']
leng_lst = len(item_lst)
def headintro():
    print("*-------------------------------------------------------*")
    print(" Lab17 Assignment :   Selenium: Demoblaze  by Wook Huang ")
    print("*-------------------------------------------------------*")
    print("1. _4 Refer to Lab 16 ")
    print("5. -6 find the Nexus 6 model and assert, 7. Add to Cart")
    print("8.-10 Repeat 6-7  for Sony and Samsung model ")
    print("10. Close the browser and display a user-friendly message. ")
    print(f'*--------------------------------------------------------*')
# Check all your added items are displayed and click the Delete link only for the second item in the list.
# Your goal is to figure out how to differentiate one Delete link from another.
# Close the browser and display a user-friendly message.

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

def dbz_nexus_demo(product):
    # if  driver.current_url == dbz_url:  # check we are on the Demoblaze homp page
        driver.find_element(By.LINK_TEXT, product).click()
        sleep(0.5)
    # driver.find_element(By.LINK_TEXT, 'Nexus 6').click()
        assert driver.find_element(By.XPATH, '//h2[contains(., product)]').is_displayed()
        sleep(0.5)   # 6. h2 title checked with assert
        driver.find_element(By.LINK_TEXT, 'Add to cart').click()
        print(f'The product - {product} is added to the List ')
        print("-------------------------------------------------")
        sleep(0.5)
        driver.switch_to.alert.accept()
        sleep(0.5)
        # breakpoint()
        driver.find_element(By.LINK_TEXT,'Cart').click()
        # driver.find_element(By.ID, 'cartur').click() #7, add to cart
        sleep(0.5)

        driver.find_element(By.ID, 'nava').click() #6. click site logo  to go home
        sleep(1.5)

def check_cart():
    # Check all your added items are displayed and click the Delete link only for the second item in the list.
    # Your goal is to figure out how to differentiate one Delete link from another.
    driver.find_element(By.LINK_TEXT, 'Cart').click()
    sleep(1.5)
    print('#--- Check the items in the Cart -----------------')
    for i in range(leng_lst):
        assert driver.find_element(By.XPATH,f'//td[contains(., "{item_lst[i]}")]').is_displayed()
        checkorder = driver.find_element(By.XPATH, f'//td[contains(.,"{item_lst[i]}")]').is_displayed()
        print(f'The order item of {item_lst[i]}  is staged: {checkorder} ')

def delete_item_in_2():
    print("---------------------------------------------------------------")
    driver.find_element(By.XPATH, f'//td[contains(.,"{item_lst[1]}")]/../td/a[contains(.,"Delete")]').click()
    sleep(0.5)
    print(f'the item {item_lst[1]} is is deleted')
    print(f'-----------------Thank very much ------------------------------------- ')


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
for i in range(len(item_lst)):
    prod=item_lst[i]
    dbz_nexus_demo(prod)
check_cart()
delete_item_in_2()
tearDown()

# breakpoint()
#tearDown()
