from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# You have to download the driver for your own web-browser
# - Chrome: https://chromedriver.chromium.org/downloads
# - Firefox: https://pythonbasics.org/selenium-firefox/
# - Safari: https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari/

# **Change the value to your driver path**
DRIVER_PATH = "BROWSER DRIVER PATH"

driver = webdriver.Chrome(DRIVER_PATH)


# Selects language at start
def sel_lang():
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    time.sleep(5)

    lang_sel = driver.find_element(By.ID, "langSelect-EN")
    lang_sel.click()


# Clicks cookie
def cookie_clicker():
    cookie_btn = driver.find_element(By.ID, "bigCookie")
    end_t = time.time() + 5
    while time.time() < end_t:
        cookie_btn.click()


# Upgrade products
def upgrade():
    products = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")

    for product in products:
        product.click()
        
    cookie_clicker()


# Upgrade upgrades
def click_up():
    ups = driver.find_element(By.ID, "upgrade0")
    ups.click()
    

# Main
sel_lang()
time.sleep(5)
cookie_clicker()
i = 0
while True:
    if i % 2 == 0:
        upgrade()
        i += 1
    else:
        click_up()
        i += 1
