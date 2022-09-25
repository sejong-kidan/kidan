import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")

soup = BeautifulSoup(response.text, 'html.parser')

phone_numbers_tags = soup.select('span.phoneNum')

phone_numbers = []

for tag in phone_numbers_tags:
    phone_numbers.append(tag.get_text())

# 출력 코드
print(phone_numbers)