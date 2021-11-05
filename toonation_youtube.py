from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import clipboard
import pytest

def test_youtube_donation():
    try:
        driver = webdriver.Chrome()
        youtube = 'https://www.youtube.com/watch?v=j59HTVY1oCc'

        driver.get(youtube)
        time.sleep(1)
        driver.maximize_window()

        # 후원페이지로 이동
        driver.execute_script('window.open("https://dev2.toon.at:8443/donate/kidantest");')
        time.sleep(1)

        driver.execute_script('window.open("https://dev2.toon.at:8443/tools/bypass/donator/1/284033");')
        time.sleep(1)

        # 후원페이지 탭으로 이동
        creator_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=creator_tab)
        driver.refresh()
        time.sleep(1)

        # 바이패스 탭 닫기
        bypass_tab = driver.window_handles[1]
        driver.switch_to.window(window_name=bypass_tab)
        time.sleep(1)

        driver.close()
        time.sleep(1)

        # 후원페이지 탭으로 이동
        driver.switch_to.window(window_name=creator_tab)
        time.sleep(1)

        # Youtube 화면으로 이동
        youtube_tab = driver.window_handles[0]
        driver.switch_to.window(window_name=youtube_tab)
        time.sleep(1)

        count = 0
        while count < 5:

            # 유튜브 뮤트
            mute = driver.find_element(By.CSS_SELECTOR, ".ytp-mute-button")
            if count == 1:
                mute.click()
            else:
                time.sleep(1)

            element = driver.find_element(By.CSS_SELECTOR, ".style-scope:nth-child(3) > .yt-simple-endpoint > #button > #button > .style-scope")
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            element = driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(driver)
            driver.find_element(By.CSS_SELECTOR, ".style-scope:nth-child(3) > .yt-simple-endpoint > #text").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "#copy-button #text").click()
            time.sleep(1)

            # 후원페이지 탭으로 이동
            driver.switch_to.window(window_name=creator_tab)
            time.sleep(1)

            # 복사한 영상공유 후원
            driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[3]/div/div[4]').click()
            time.sleep(2)

            media_cash = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[9]/div/div/div/div/div/input')
            media_cash.clear()
            time.sleep(1)
            media_cash.send_keys("3000")
            time.sleep(1)

            media_url = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[10]/div/div/div/div/div/input')
            media_url.clear()
            media_url.send_keys(clipboard.paste())
            time.sleep(1)

            driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[13]/button').click()
            time.sleep(2)

            go = None
            try:
                go = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button')
            except Exception:
                pass

            if go:
                go.click()
                time.sleep(3)
            else:
                time.sleep(2)

            # Youtube 화면으로 이동
            youtube_tab = driver.window_handles[0]
            driver.switch_to.window(window_name=youtube_tab)
            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, "#button > .ytd-unified-share-panel-renderer").click()
            time.sleep(1)
            driver.find_element(By.ID, "video-title").click()
            time.sleep(2)

            count = count + 1
        driver.close()
    except Exception as ex:
        print(ex)
        assert False
    assert True
