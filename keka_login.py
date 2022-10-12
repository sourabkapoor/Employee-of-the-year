import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


EMAIL = ''
PASSWORD = ''

print(EMAIL)

# Using this to check if its the first time of the day or not
# Default initiated with True.
f = open("status_storage.txt", "r")
status = f.read()

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Locations:
# Gandhi nagar 32.695225@74.860401
# Muthi 32.761866@74.820853
# Chandigarh 30.720009@76.784099

def keka_login():
    global f

    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    
    Map_coordinates = dict({
        "latitude": 32.761866,
        "longitude": 74.820853,
        "accuracy": 100
        })
    browser.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)

    print('Attendance Process Started: ')
    browser.get("")
    print('Website Opened')

    time.sleep(15)

    email = browser.find_element("xpath", '//*[@id="email"]')
    email.send_keys(EMAIL)
    print('Email Entered')


    password = browser.find_element("xpath", '//*[@id="password"]')
    password.send_keys(PASSWORD)
    print('Password Entered')


    time.sleep(5)

    login_button = browser.find_element("xpath", '//*[@id="login-container-center"]/div/div/form/div/div[4]/div/button[1]')
    login_button.click()
    print('Login Button Clicked')


    time.sleep(15)

    web_clockin_button = browser.find_element("xpath", '//*[@class="card text-white bg-accent-violet"]/div[1]/div[1]/div[2]/div/div[2]/div[1]/button ')
    web_clockin_button.click()
    print('Clicked WebClock In')


    time.sleep(5)

#  Geo location: 32.761866, 74.820853
    # location_request_button = browser.find_element("xpath", '//*[@id="ng-app"]/body/div[1]/div/div/div[3]/button')
    # location_request_button.click()
    # print('Location Request Declined')

    # driver.switchTo().alert().dismiss();

    # if status == True:
    note_text_area = browser.find_element("xpath", '//*[@class="modal-body"]/form/div/textarea')
    note_text_area.send_keys("Clocking In")
    print('Entered Description')


    time.sleep(5)

    request_button = browser.find_element("xpath", '//*[@class="modal-footer"]/button[2]')
    request_button.click()
    print('Clicked Request Button')


    time.sleep(15)
    print('Successfully logged in')
    # f.close()
    # f = open("status_storage.txt", "w")
    # f.write("False")
    # f.close()
    # print time.strftime("Cron Successfully ran last at: " + "%Y-%m-%d %H:%M")
    browser.quit()

keka_login()
