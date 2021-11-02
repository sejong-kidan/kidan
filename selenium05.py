from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://www.google.com/'
driver.get(url)
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='gb']/div/div[2]/a").click()

# driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[3]/div[2]/button[3]').click()

