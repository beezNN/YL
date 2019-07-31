# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
# 引入unittest框架包
import unittest, time, re
import os
import HTMLTestRunner


class BaiduTest(unittest.TestCase):
    #dakai
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium ide")
        driver.find_element_by_id("su").click()
        time.sleep(5)
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


def is_alert_present(self):
    try:
        self.driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True


def close_alert_and_get_its_text(self):
    try:
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        self.accept_next_alert = True


def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(BaiduTest("setUp"))
    suiteTest.addTest(BaiduTest("test_baidu"))
    return suiteTest


if __name__ == "__main__":
    unittest.main()

    print("main-start")
    s = unittest.TestSuite()  # 实例化
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(BaiduTest))  # 加载用例
    now = time.strftime('%Y-%m-%d %H%M%S')
    print("main-getcwd")
    filename = open(os.getcwd() + "/testResult_report" + now + ".html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=filename,
        title='单元测试报告',
        description='单元测试报告',
        tester='youreyebows')
    runner.run(s)
    print("main-stop")
