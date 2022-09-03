greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
i = 0

while i < len(greetings):
    print(greetings[i])
    i += 1
  

# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1
# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력


# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd * 125

# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
# prices를 원화(￦)에서 달러($)로 변환하기

i = 0
while i < len(prices):
    prices[i] = round(krw_to_usd(prices[i]), 1)
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)으로 변환하기
i = 0
while i < len(prices):
    prices[i] = round(usd_to_jpy(prices[i]), 1)
    i += 1
    
# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))

# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
i = 0
while i < len(numbers): 
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)

# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
for i in range(len(numbers)):
    print(i, numbers[i])
    
for i in range(11):
    print("{}^{} = {}".format(2, i, 2 ** i))
    
for i in range(1, 10):
    for ii in range(1, 10):
        print("{} * {} = {}".format(i, ii, i * ii))

# a**2 + b**2 == c**2
# a + b + c == 400
# a < b < c
# a * b * c = ?
# c = 400-a-b

for a in range(1, 400):
    for b in range(1, 400):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c and a + b + c == 400:
            print(a * b * c)
            
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1  
    
    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]  

print("뒤집어진 리스트: " + str(numbers))

my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}

print(my_dictionary[5])

from re import M


my_family = {
    '엄마': '박찬선',
    '아빠': '최명철',
    '형': '최세창',
    '동생': '최미연'
}

for key, value in my_family.items():
    print(key, value)

# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    for key, value in dict.items():
        new_dict[value] = key
    
    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {
}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
i = 0
for name in votes:
    if i != 3:
        vote_counter[name] = 1
        i += 1
    else:
        vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter)

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {
}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter)

alphabet_string = 'ABCDEFGHIJ'

print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4])

str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
print(str_3)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)


my_list = [2, 3, 5, 7, 11]
print(len(my_list))

my_string = 'Hello world!'
print(len(my_string))

numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

def sum_digit(num):
    total = 0
    str_num = str(num)
    
    for digit in str_num:
        total += int(digit)

    return total
    


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit_total = 0
for i in range(1, 1001):
    digit_total += sum_digit(i)
    
print(digit_total)


def mask_security_number(security_number):
    mask_security_number_list = list(security_number)
    mask_security_number_list[-4] = '*'
    mask_security_number_list[-3] = '*'
    mask_security_number_list[-2] = '*'
    mask_security_number_list[-1] = '*'
    mask_security_number = ''.join(str(s) for s in mask_security_number_list)
    return mask_security_number

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"
        
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]

    return total_str


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))


def mask_security_number(security_number):
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True
        

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))


from run import add, multiply, subtract

print(add(2, 5))
print(multiply(3, 4))
print(subtract(5, 7))


#import math

#print(math.log10(100))
#print(math.cos(0))
#print(math.pi)

#import random

#print(random.random())

#import os

#print(os.getlogin())
#print(os.getcwd())


name = input("이름을 입력하세요: ")
print(name)

x = int(input("숫자를 입력하세요: "))
print(x + 5)

import random

random_number = random.randint(1, 20)
i = 4
ii = 0

while ii <= 4: 
    input_number = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(i)))
    if random_number > input_number:
        print("UP")
        i -= 1
        ii += 1
    elif random_number == input_number:
        ii += 1
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(ii))
        ii -= 1
        break
    else:
        print("Down")
        i -= 1
        ii += 1
if ii == 4:
    print("아쉽습니다. 정답은 {}입니다.".format(random_number))