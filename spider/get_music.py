#encoding:utf-8
from selenium import webdriver
import time,urllib
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
def get_url():
    driver = webdriver.Firefox()
    url = 'http://www.kugou.com/'
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()
    a = driver.find_element_by_xpath('html/body/div/div[1]/div[1]/div[1]/input').click()
    b = driver.find_element_by_xpath('html/body/div/div[1]/div[1]/div[1]/div/i').click()
    result_url = driver.current_url
    driver.quit()
    return result_url
def music_title():
    driver = webdriver.Firefox()
    driver.get(get_url())
    for i in range(1,11):
        try:
            print driver.find_element_by_xpath('//*[@id="search_song"]/div[2]/ul[2]/li[%d]/div[1]/a'%i).get_attribute('title')
            name = driver.find_element_by_xpath('//*[@id="search_song"]/div[2]/ul[2]/li[%d]/div[1]/a' % i)

        except NoSuchElementException:
            break
    choice = input('>>>which one do you want to download')
    name = driver.find_element_by_xpath('//*[@id="search_song"]/div[2]/ul[2]/li[%d]/div[1]/a' % choice)
    choice_name = name.get_attribute('title')
    actions = ActionChains(driver)
    actions.move_to_element(name)
    actions.click(name)
    actions.perform()
    driver.switch_to_window(driver.window_handles[1])
    address = driver.find_element_by_xpath('//*[@id="myAudio"]').get_attribute('src')
    urllib.urlretrieve(address,'/Users/xiaoxiao/Desktop/test/%s.mp3'%choice_name)
    #driver.switch_to_window(driver.window_handles[0])
def main():
    print 'start'
    music_title()
if __name__ == '__main__':
    main()