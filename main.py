from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import time

options = ChromeOptions()

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
# accept cookies
consent = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
consent.click()
time.sleep(2)

language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language.click()
time.sleep(2)

cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
cookies.click()

# game ON
playing = True

# create timing mechanism
timeout = time.time() + 5
i = 0
timeout_multiplier = 1

# Click on cookie
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
while playing:
    cookie.click()
    # upgrade / products every 5 seconds
    if time.time() > timeout:
        # check for available upgrades
        upgrades = driver.find_elements(By.CLASS_NAME, "crate.upgrade.enabled")
        try:
            upgrades[0].click()
        except IndexError:
            pass
        # check for available products
        products = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
        try:
            products[-1].click()
        except IndexError:
            pass
        # Change time multiplier every 10 iterations to allow for increasing product values
        timeout = time.time() + 5 * timeout_multiplier
        i += 1
        if i % 10 == 0:
            timeout_multiplier += .5





