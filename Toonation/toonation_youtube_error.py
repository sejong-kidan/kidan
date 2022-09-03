from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import clipboard
import pytest

def test_youtube_donation_error():
    try:
        def submit(v='', error_msg=''):
            driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[3]/div/div[4]').click()
            time.sleep(2)

            media_url = driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[10]/div/div/div/div/div/input')
            media_url.clear()
            media_url.send_keys("https://www.youtube.com/watch?v=" + v)
            time.sleep(1)

            driver.find_element_by_xpath('//*[@id="baselayout"]/div/div/div/div[13]/button').click()
            time.sleep(5)
            error_reason = driver.find_element_by_class_name('AlertContent').text
            error_pass = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button')

            if error_reason == error_msg:
                error_pass.click()
                time.sleep(1)
            else:
                driver.save_screenshot('youtube_error.png')
                time.sleep(2)
                error_pass.click()
                time.sleep(1)

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

        # 퍼가기 금지
        submit('DqHfozzG1uI', '해당 영상은 게시자에 의해 공유가 금지된 영상입니다.')

        # 성인영상
        submit('DtSP7JsV5Yk', '해당 영상은 성인 인증이 필요하여 후원이 불가합니다.')
        
        # 지역제한
        submit('wAsBta25OGQ', '해당 영상은 일부 지역에서만 재생이 가능하여 후원이 불가합니다.')

        # 비공개
        submit('b7udAluJwlI', '해당 영상은 비공개 영상이므로 후원이 불가합니다.')

        # 삭제
        submit('OA82cIPWVj0', '후원이 불가한 영상입니다.')

        # 유튜브 뮤직 프리미엄 전용 영상
        submit('oplDWPrtOOI', '해당 영상은 유튜브 뮤직 프리미엄 전용 영상이므로 후원이 불가합니다.')

        # 채널 멤버쉽 전용 영상
        submit('OUQxjoameTU', '해당 영상은 채널 멤버쉽 전용 영상이므로 후원이 불가합니다.')

        # 유튜브 유료 영상
        submit('Gj3ETxehJc8', '해당 영상은 유튜브 유료 영상이므로 후원이 불가합니다.')

        # 라이브 영상
        submit('dG0pB6xmXtQ', '실시간 라이브 영상은 후원이 불가합니다.')

        driver.close()

    except Exception as ex:
        print(ex)
        assert False
    assert True
