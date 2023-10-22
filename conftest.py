import pytest
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    driver.get('https://try.vikunja.io')
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('demo')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('demo')
    driver.find_element(By.XPATH, '//*[@id="loginform"]/button').click()
    yield driver
    driver.close()