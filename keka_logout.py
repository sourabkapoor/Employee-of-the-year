import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from os.path import join, dirname
# from dotenv import load_dotenv

#Loading .env file
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

EMAIL = ''
PASSWORD = ''

# Using this to check if its the first time of the day or not
# Default initiated with True.
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# prefs = {
#         'profile.default_content_setting_values':
#             {
#                 'notifications': 1,
#                 'geolocation': 1
#             },
#         'devtools.preferences': {
#             'emulation.geolocationOverride': "\"32.761866@74.820853:\"",
#         },
#         'profile.content_settings.exceptions.geolocation':{
#             'BaseUrls.Root.AbsoluteUri': {
#                 'setting': '1'
#             }
#         },
#         'profile.geolocation.default_content_setting': 1

#     }
# chrome_options.add_experimental_option("prefs", prefs)

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() + "/chromedriver"
print(chrome_driver)

def keka_logout():
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    Map_coordinates = dict({
        "latitude": 32.761866,
        "longitude": 74.820853,
        "accuracy": 100
        })
    browser.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)
    print('Logout Process Started: ')

    browser.get("")
    print('Website Opened')

    time.sleep(5)

    email = browser.find_element("xpath", '//*[@id="email"]')
    email.send_keys(EMAIL) # Enter your email here
    print('Email Entered')

    password = browser.find_element("xpath", '//*[@id="password"]')
    password.send_keys(PASSWORD) # Enter your password here
    print('Password Entered')


    time.sleep(5)

    login_button = browser.find_element("xpath", '//*[@id="login-container-center"]/div/div/form/div/div[4]/div/button[1]')
    login_button.click()
    print('Login Button Clicked')


    time.sleep(15)

    web_clockout_button = browser.find_element("xpath", '//*[@class="card text-white bg-accent-violet"]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/button')
    web_clockout_button.click()
    print('WebClock Out Button Clicked')

    time.sleep(5)

    web_clockout_confirm_button = browser.find_element("xpath", '//*[@class="card text-white bg-accent-violet"]/div[1]/div[1]/div[2]/div/div[2]/div/div/button')
    web_clockout_confirm_button.click()
    print('Confirmed WebClock Out')


    time.sleep(5)

    # location_request_button = browser.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div/div[3]/button')
    # location_request_button.click()
    # print('Rejected location request')

    # time.sleep(15)
    print('Successfully logged out')
    f = open("status_storage.txt", "w")
    f.write("True")
    f.close()

    time.sleep(10)
    # print time.strftime("Cron Successfully ran last at: " + "%Y-%m-%d %H:%M")
    browser.quit()


keka_logout()
