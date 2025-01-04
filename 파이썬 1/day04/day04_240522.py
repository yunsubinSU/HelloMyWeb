# # # 섹션 3 : 기본 입출력
# # # 표준 출력
# # # 이스케이프 문자
# #
# #     프로그래밍 할 때 사용할 수 있도록 미리 정의해둔 문자 조합
# #     출력물을 보기 좋게 보는 용도로 사용
# #     대표적인 것 --> \n (엔터)
#
# # 53page)
# print('Hello \'World\'')
# print("Hello 'World'")
#
# print("Hello \"World\"")
# print('Hello "World"')
#
# print('*\n**\n***')
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day04_240522.py
# # Hello 'World'
# # Hello 'World'
# # Hello "World"
# # Hello "World"
# # *
# # **
# # ***


# # 55page)
# print('재미있는', '파이썬')
# print('Python', 'Java', 'C', sep=',')
#
# print()  # 빈 줄
#
# print('영화 타이타닉')
# print('평점', end=':')
# print('5점')
#
# fos = open('sample.py', mode='wt')  # 파일 열기
# print('print("Hello World")', file=fos)  # 파일에 출력(내용 저장)
# fos.close()  # 파일 닫기
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day04_240522.py
# # 재미있는 파이썬
# # Python,Java,C
# #
# # 영화 타이타닉
# # 평점:5점


# # 형식을 갖춘 문자열 (문자열 포매팅)
# # 1) % 연산자 (기본 포매팅)
# # 58page)
# name = 'Kai'  # 문자열
# print('내 이름은 %s입니다.' % name)
#
# height = 120.5  # 실수
# print('내 키는 %fcm입니다.' % height) # 소수여섯째자리까지 출력
#
# weight = 23.55  # 실수
# print('내 몸무게는 %.1fkg입니다.' % weight) # 소수첫째자리까지 반올림
#
# year, month, day = 2014, 8, 25  # 정수
# print('내 생일은 %d년 %d월 %d일입니다.' % (year, month, day))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day04_240522.py
# # 내 이름은 Kai입니다.
# # 내 키는 120.500000cm입니다.
# # 내 몸무게는 23.6kg입니다.
# # 내 생일은 2014년 8월 25일입니다.


# # # .format()
# #
# #     <형식>
# #     '문자열 {}'.format(변수명)
# # 60page)
# zipcode = '06236'
# print('우편번호 : {}'.format(zipcode))
#
# address = '''서울특별시 강남구
# 테헤란로 146'''
# print('주소 : {addr}'.format(addr=address))
#
# tel1, tel2, tel3 = '02', '538', '0021'
# print('연락처 : {0}-{1}-{2}'.format(tel1, tel2, tel3))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day04_240522.py
# # 우편번호 : 06236
# # 주소 : 서울특별시 강남구
# # 테헤란로 146
# # 연락처 : 02-538-0021


# # ex)
# print('{0:<10}'.format('Hi'))  # 전체 10칸, 왼쪽 정렬
# print('{0:>10}'.format('Hi'))  # 전체 10칸, 오른쪽 정렬
# print('{0:^10}'.format('Hi'))  # 전체 10칸, 가운데 정렬
#
# print('{:=^30}'.format('python')) # 전체 30칸, 공백을 =로 표현, 가운데정렬
# print('{:!<30}'.format('python')) # 전체 30칸, 공백을 !로 표현, 왼쪽정렬
#
# n = 3.141592
# print('{:.3f}'.format(n)) # 소수셋째자리까지 반올림
#
# a = '파이썬 열공하여 첫 연봉 {}만원 만들기'.format(5000)
# b = '{} {}     {}'.format(100, 200, 300)
# c = '{} {} {}'.format(1, '파이썬', True)
# print(a)
# print(b)
# print(c)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day04_240522.py
# # Hi
# #         Hi
# #     Hi
# # ============python============
# # python!!!!!!!!!!!!!!!!!!!!!!!!
# # 3.142
# # 파이썬 열공하여 첫 연봉 5000만원 만들기
# # 100 200     300
# # 1 파이썬 True


# # # f-strings (f 문자열 포매팅)
# #
# #     <형식>
# #     f'문자열 {변수명} 문자열'
# # ex)
# name = '푸바오'
# age = 3
# print(f'나의 이름은 {name}입니다. 나의 나이는 {age}살입니다.')
# print(f'나는 내년이면 {age+1}살이 됩니다.')
#
# print(f'{"python":=^30}')  # 전체 30칸, 공백을 =로 표현, 가운데 정렬
# print(f'{"python":!<30}')  # 전체 30칸, 공백을 !로 표현, 왼쪽 정렬
#
# n = 3.141592
# print(f'{n:.3f}')  # 소수 셋째자리까지 반올림
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day04_240522.py
# # 나의 이름은 푸바오입니다. 나의 나이는 3살입니다.
# # 나는 내년이면 4살이 됩니다.
# # ============python============
# # python!!!!!!!!!!!!!!!!!!!!!!!!
# # 3.142


# # 포매팅 비교하기
# n = 3   # 정수
# print('I eat', n, 'apples.')
# print('I eat %d apples.' % n)  # % 연산자 포매팅(기본 포매팅)
# print('I eat {} apples.'.format(n))  # format메서드 포매팅
# print(f'I eat {n} apples.')  # f-strings (f 문자열 포매팅)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day04_240522.py
# # I eat 3 apples.
# # I eat 3 apples.
# # I eat 3 apples.
# # I eat 3 apples.


# # 표준 입력 (input)
# n = input('정수를 입력하세요 : ')
# print(n)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day04_240522.py
# # 정수를 입력하세요 : 3
# # 3


# # 63page)
# name = input('이름을 입력하세요 : ')
# age = input('나이를 입력하세요 : ')
# print('입력된 이름은 {}입니다.'.format(name))
# print('입력된 나이는 {}살입니다.'.format(age))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day04_240522.py
# # 이름을 입력하세요 : 춘식이
# # 나이를 입력하세요 : 20
# # 입력된 이름은 춘식이입니다.
# # 입력된 나이는 20살입니다.


# ##################################################
# # 포매팅 문제)
# # 변수 number에 정수 5를 담고, 오늘 배운 3가지 포매팅 형식으로 출력해보자.
# # [화면실행결과]
# # I eat 5 apples.
# # I eat 5 apples.
# # I eat 5 apples.
# number = 5
# print('I eat %d apples.' % number)
# print('I eat {} apples.'.format(number))
# print(f'I eat {number} apples.')





