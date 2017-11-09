#encoding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
'''url = 'http://weibo.com/'
driver.get(url)
time.sleep(3)
driver.maximize_window()
account = driver.find_element_by_xpath('//*[@id="loginname"]')
account.send_keys('wangxiaoxiao2009@126.com')
password = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
password.send_keys('15153510854haha')
button = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
button.click()
time.sleep(3)'''
driver.get('http://weibo.com/u/1537790411')
a = driver.find_element_by_xpath('//*[@id="Pl_Core_T8CustomTriColumn__3"]/div/div/div/table/tbody/tr/td[2]/a/strong')
b = a.get_attribute('W_f12')
print b