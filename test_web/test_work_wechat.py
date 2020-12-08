# -*- coding: utf-8 -*-
import shelve
from selenium import webdriver
from test_web.base import Base


class TestWork():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 获取当前页面的cookie
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 带有登录信息的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853548133453'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325129202699'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'KOf_uwoaz7_ba2SJERKJFRi1ZbjvB5mVbBWxDVFbN0Qgu_xdkZ1P1sK3HkddQ--u'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a2584055'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'vnKh5vl6P-Xle35eBtJpZJJ02cfyyc6WIOr9clf9CWMy_cxoV8O1Whli9X3wen69j5dkSOwPEpGPqnojLrIMaIvozZ82MsoRyBbsx_moa0wQi25zLu1InsS0o2LaqJEWB1MMfLUfJyS07Wnvvor7zpZmK0_cW1NjvbitcO6HFWJTIYZHXv2hnwRJtN07k_MniGfq04G3Efb3YLs8O1cfiq32xTLFJ0EvGubv7RAy0ugB1M41lUmLQJBAykhCxMmmw8MQO0snbTlmrJxLcLk88g'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1638956236, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1607414074,1607415013,1607418794,1607420236'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '1371414780'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1607426344, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '51t2cn3'},
            {'domain': '.qq.com', 'expiry': 1607506663, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.253241673.1607335801'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853548133453'},
            {'domain': '.qq.com', 'expiry': 1921056029, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False,
             'value': '0'},
            {'domain': '.qq.com', 'expiry': 1921056029, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_8f15d50a5bc45'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1607420236'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '20593217032234921'},
            {'domain': '.qq.com', 'expiry': 1920804923, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': 'd4162a44194afc6b'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1610012465, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1670492263, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1828180546.1606808071'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636256714, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'}]

        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 重新打开 已有cookie的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #
    #     # def test_importcontacts():
    #     #     self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]')

    def test_shelvecookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # shelvePython内置模块 小型数据库
        db = shelve.open('./dbdata/cookies')
        # db['cookie'] = cookies
        # db.close()
        cookies = db['cookie']
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
