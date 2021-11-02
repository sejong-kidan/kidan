from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = 'https://toon.at/donate/kidan'
driver.get(url)
time.sleep(1)

driver.get('https://toon.at/tools/bypass/donator/1/613853')
time.sleep(1)

driver.get(url)
time.sleep(1)

# 프로필 숨기기
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[7]/div/div/div').click()
time.sleep(1)

# 후원 닉네임 변경
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[8]/div/div/div/div/div[1]/input').clear()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[8]/div/div/div/div/div[1]/input').send_keys('test')
time.sleep(1)

# 텍스트 내용 입력
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[10]/div/div/textarea').send_keys("test")
time.sleep(1)

# 보이스 선택
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[1]/div/div/div/div/div/input').send_keys("찬구",(Keys.ENTER))
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[3]/div[2]/button').click()
time.sleep(1)

# 후원하기 버튼
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[14]/button').click()

