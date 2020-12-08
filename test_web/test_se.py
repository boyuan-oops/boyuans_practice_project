# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web.base import Base


class TestSele(Base):

    def test_sele(self):
        self.driver.get("https://testerhome.com/")
        #显式等待1
        def wait(w):
            return len(self.driver.find_element_by_link_text("社团"))>0
            WebDriverWait(self.driver, 5).until(wait)
        self.driver.find_element_by_link_text("社团").click()

        # 显式等待2
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "testerhome管理委员会")))
        self.driver.find_element_by_link_text("testerhome管理委员会").click()
