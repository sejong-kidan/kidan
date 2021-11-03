from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
live = 'https://toon.at/donate/kidan'
dev = 'https://dev2.toon.at:8443/donate/kidantest'
live_bypass = 'https://toon.at/tools/bypass/donator/1/613853'
dev_bypass = 'https://dev2.toon.at:8443/tools/bypass/donator/1/284033'

driver.get(dev)
time.sleep(1)
driver.maximize_window()

driver.get(dev_bypass)
time.sleep(1)

driver.get(dev)
time.sleep(1)

# 프로필 숨기기
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[7]/div/div/div').click()
time.sleep(1)

# 후원 닉네임 변경
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[8]/div/div/div/div/div[1]/input').clear()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[8]/div/div/div/div/div[1]/input').send_keys('test')
time.sleep(1)

voices = ["초롱"] # dev일 경우 "초롱", "찬구", "투나", "테스트" 사용 / live일 경우 "초롱", "찬구", "투나", "마왕루야" 사용

for voice in voices:
    # 텍스트 내용 입력
    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[10]/div/div/textarea').send_keys("test")
    time.sleep(1)

    # 보이스 선택
    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div/div[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]').click()
    time.sleep(1)
    search = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[1]/div/div/div/div/div/input')
    search.clear()
    time.sleep(1)
    search.send_keys(voice,(Keys.ENTER))
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]').click()
    # try:
    #     driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]').click()
    # except Exception:
    #     print('보이스를 찾을수 없음', voice)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[3]/div[2]/button').click()
    time.sleep(1)

    # 후원하기 버튼
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[14]/button').click()
    time.sleep(5)

# 차단된 보이스 후원을 위한 환경 준비
driver.execute_script('window.open("https://dev2.toon.at:8443/streamer/login");') # dev서버
# driver.execute_script('window.open("https://toon.at/streamer/login");') # live서버
time.sleep(3)

driver.execute_script('window.open("https://dev2.toon.at:8443/tools/bypass/streamer/1/24306");') # dev서버 크리에이터 바이패스
time.sleep(1)

# 크리에이터 탭으로 이동
creator_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=creator_tab)
time.sleep(2)

# 바이패스 탭 닫기
bypass_tab = driver.window_handles[1]
driver.switch_to.window(window_name=bypass_tab)
time.sleep(2)

driver.close()
time.sleep(1)

# 크리에이터 탭으로 이동
driver.switch_to.window(window_name=creator_tab)
time.sleep(2)

driver.refresh()
time.sleep(2)

# 보이스 차단 설정
driver.find_element_by_xpath('/html/body/div/div[1]/aside/ul/div/li[5]/div').click() # 위젯
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/aside/ul/div/li[5]/ul/li[1]/a').click() # 알림창
time.sleep(5)
for c in range(0,1):
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div[1]/div[1]').click() # 공통 설정
time.sleep(3)
for c in range(0,1):
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div[1]/div[2]/div[4]/div[5]/div[1]/div[1]/button[6]').click() # 밀라 OFF
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[3]/div[4]/button').click() # 설정저장
time.sleep(1)

# 후원페이지로 다시 이동
donator_tab = driver.window_handles[0]
driver.switch_to.window(window_name=donator_tab)
time.sleep(2)

# 차단된 보이스로 후원
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[10]/div/div/textarea').send_keys("test")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]').click()
time.sleep(1)
research = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[1]/div/div/div/div/div/input')
research.clear()
time.sleep(1)
research.send_keys("밀라",(Keys.ENTER))
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div[2]/div/div[3]/div[2]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[14]/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button').click()
time.sleep(1)

# 차단된 보이스 다시 원복
driver.switch_to.window(window_name=creator_tab)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div[1]/div[2]/div[4]/div[5]/div[1]/div[1]/button[6]').click() # 밀라 ON
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[3]/div[4]/button').click() # 설정저장
time.sleep(1)

# 후원페이지로 다시 이동
driver.switch_to.window(window_name=donator_tab)
time.sleep(2)

# 미니후원
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[3]/div/div[2]').click()
time.sleep(1)
mini = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[10]/div/div/div/div/div/input')
mini.send_keys("test")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[13]/button').click()
time.sleep(2)

# 미니후원 (엔터키)
mini.send_keys("test")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[11]/div/div/div').click()
time.sleep(1)
mini.click()
mini.send_keys(Keys.ENTER)
time.sleep(2)

# 미니후원 (텍스트 색상 변경)
mini_cash = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[9]/div/div/div/div/div/input')
mini_cash.clear()
time.sleep(1)
mini_cash.send_keys("1000")
time.sleep(1)
mini.send_keys("test")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[12]/div/div/div[1]/div').click()
time.sleep(2)
mini_color = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[12]/div/div/div[2]/div[1]/div/div/div/input')
for c in range(0,6):
    mini_color.send_keys(Keys.BACK_SPACE)
    time.sleep(2)
mini_color.send_keys("09C2FF")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[13]/button').click()
time.sleep(3)
# 음성 녹음 (직접 녹음)
driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[3]/div/div[3]').click()
time.sleep(2)

# 음성 녹음 (파일 등록)