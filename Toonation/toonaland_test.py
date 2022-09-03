from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import clipboard
import pytest


driver = webdriver.Chrome()
# live = 'https://toon.at/donate/kidan'
dev = 'https://dev3.toon.at/donator/land'
# live_bypass = 'https://toon.at/tools/bypass/donator/1/613853'
dev_bypass = 'https://dev3.toon.at/tools/bypass/donator/1/284033'

driver.get(dev_bypass)
time.sleep(1)

driver.get(dev)
time.sleep(1)
driver.maximize_window()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[2]/div[2]').click()
time.sleep(1)
# 당첨왕으로 이동

driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[2]/div[2]/div[1]/div[8]/div/div/div[3]').click()
time.sleep(1)
# 채널 입장

driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[2]/div[2]/table/tbody/tr[1]/td[6]/div/button').click()
time.sleep(1)
# 방 입장

driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[2]/div[3]/div/div/div[3]/div/div[1]/button').click()
time.sleep(1)
# 건너뛰기 선택

count = 0
while count < 4:

    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[2]/div[2]/div[2]/div').click()
    # 칸 선택
    time.sleep(1)
    
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/button[1]').click()
    # 칸 선택 후 팝업 예 선택
    time.sleep(1)
    
    count = count + 1

time.sleep(3)

driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[2]/div[2]/div[2]/div').click()
# 칸 선택

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/button[1]').click()
# 칸 선택 후 팝업 예 선택

driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[2]/div[2]/div[3]/div').click()
# 칸 선택
time.sleep(1)

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/button[1]').click()
# 칸 선택 후 팝업 예 선택

time.sleep(2)
driver.close()