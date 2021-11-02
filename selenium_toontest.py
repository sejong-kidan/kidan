from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = 'https://toon.at/donate/kidan'
driver.get(url)
driver.maximize_window()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[3]/div[2]/button[3]').click()
time.sleep(2)
username = driver.find_element_by_xpath('//*[@id="id_email_2"]') 
username.send_keys('cmc4047@naver.com') 
password = driver.find_element_by_xpath('//*[@id="id_password_3"]') 
password.send_keys('Tpwhd8589*')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[14]/button').click()

# text = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[8]/div/div/div')
# username.send_keys('셀레니움을 이용한 텍스트 후원 테스트') 
print("hello")