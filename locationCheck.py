from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Locations:
# Gandi nagar 32.695225@74.860401
# Muthi 32.761866@74.820853
# Chandigarh 30.720009@76.784099

def locationCheck():
  service = Service(executable_path=ChromeDriverManager().install())
  browser = webdriver.Chrome(service=service)
  Map_coordinates = dict({
        "latitude": 32.695225,
        "longitude": 74.860401,
        "accuracy": 100
        })
  browser.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)

  print("start location search")
  browser.get("https://www.gps-coordinates.net/my-location")

  time.sleep(20)

  browser.quit()

locationCheck()