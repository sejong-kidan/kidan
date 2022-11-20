from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://naver.com"

driver.get(url)

time.sleep(1)

"""
<input id="query" name="query" type="text" title="검색어 입력" maxlength="255" class="input_text" tabindex="1" a
ccesskey="s" style="ime-mode:active;" autocomplete="off" placeholder="검색어를 입력해 주세요." onclick="document.getElementById('fbm').value=1;" 
value="" data-atcmp-element="">
"""

# driver.find_element(By.CLASS_NAME, "input_text").send_keys("블랙핑크")
# time.sleep(1)

# driver.find_element(By.ID, "query").send_keys("뉴진스")
# time.sleep(1)

# driver.find_element(By.NAME, "query").send_keys("트와이스")
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, "[title='검색어 입력']").send_keys("에스파")
# time.sleep(1)

# driver.find_element(By.LINK_TEXT, "쇼핑LIVE").click()
# time.sleep(1)

# driver.find_element(By.PARTIAL_LINK_TEXT, "핑LI").click()
# time.sleep(1)

driver.find_element(By.TAG_NAME, "")


