import requests

### 코드를 작성하세요 ###
rating_pages = []
# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
for year in range(3):
    for month in range(1, 13):
        for weekIndex in range(5):
            url = "https://workey.codeit.kr/ratings/index?year=201{}&month={}&weekIndex={}".format(year, month, weekIndex)
            response = requests.get(url)
            rating_page = response.text
            rating_pages.append(rating_page)


# 출력 코드
print(len(rating_pages)) # 가져온 총 페이지 수
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드