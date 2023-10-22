import pytest
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup')
class TestMain:

    def test_1(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/main/div/div[2]/div/div/div/div/div[1]/div/label/svg').click()

    def test_2(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[1]/menu/li[4]/div/button/svg').click()

    def test_3(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[1]/menu/li[4]/div/div/button/svg').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[1]/menu/li[4]/div/div/div/div/a[6]/span[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div[3]/button[2]').click()

    def test_4(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[1]/div/div/button/svg').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[1]/div/div/div/div/a[2]/span[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/div/ul/li[2]/button/img').click()

    def test_5(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[1]/div/a/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/main/div/div[1]/div[2]/div/button').click()
        self.driver.find_element(By.XPATH, '//html/body/section/div/div/div/div/div/div[3]/div/div[2]/label/svg').click()

    def test_6(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[1]/div/a/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/main/div/div[1]/div[1]/a[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/main/div/div[1]/div[2]/div/div/div/div[2]/label/svg').click()

    def test_7(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[3]/div/a/span[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/main/div/div[2]/div/div/div/ul/div[1]/div/label/svg').click()

    def test_8(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[3]/div/a/span[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/div[1]/div/button/svg').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/div[1]/div/div/div/a[2]/span[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/div/ul/li[1]/button/img').click()

    def test_9(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[1]/div/a/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/div[2]/div[2]/button/span[2]/svg').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/div[2]/div[2]/div/div/a[2]/span').click()
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div/footer/button').click()

    def test_10(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[1]/menu/li[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/main/div/p/div[2]/label/svg').click()

    def test_11(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/header/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/aside/nav[3]/menu/li[1]/div/button[1]/svg').click()
