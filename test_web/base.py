# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base():
    def setup(self):
        # browser = os.getenv("browser")
        # if browser == 'chrome':
        #     self.driver = webdriver.Chrome()
        # elif browser == 'firfox':
        #     self.driver = webdriver.Firefox
        # else:
        #     self.driver = webdriver.safari
        # 复用浏览器
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        pass
        # self.driver.quit()
