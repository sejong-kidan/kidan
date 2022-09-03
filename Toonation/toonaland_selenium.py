from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = 'https://dev2.toon.at:8443/donator/land'
driver.get(url)
time.sleep(1)

driver.get('https://dev2.toon.at:8443/tools/bypass/donator/1/284033')
time.sleep(1)

driver.get(url)
time.sleep(1)

driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div[2]/div/div[3]/div[2]/button').click()
time.sleep(2)

count = 0
while count < 10:

    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[1]/div[3]/div[1]/div[3]/button[2]').click()
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[1]/div[5]/div[2]/div[2]/div[14]/div[2]').click()
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[1]/div[3]/div[3]/div[3]/button').click()
    time.sleep(2)
    
    go = None
    try:
        go = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[4]/div[3]/div/div[3]/div[2]/button')
    except Exception:
        pass

    if go:
        go.click()
        time.sleep(5)
    else:
        time.sleep(5)

    count = count + 1
    time.sleep(2)
    driver.refresh()
    time.sleep(3)
driver.close()