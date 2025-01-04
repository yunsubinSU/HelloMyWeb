# # ex) input의 형변환
# a = input('입력 : ')
# print('변수 a의 값 : {}'.format(a))
# print('변수 a의 자료형(타입) : {}'.format(type(a)))
# print()
#
# b = int(input('입력 : '))
# print('변수 b의 값 : {}'.format(b))
# print('변수 b의 자료형(타입) : {}'.format(type(b)))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 입력 : 1
# # 변수 a의 값 : 1
# # 변수 a의 자료형(타입) : <class 'str'>
# #
# # 입력 : 2
# # 변수 b의 값 : 2
# # 변수 b의 자료형(타입) : <class 'int'>


# # ex) 더하기 계산의 차이
# s1 = input('입력 s1 : ')  # 문자열로 입력됨
# s2 = input('입력 s2 : ')
# print('s1 + s2 = {}'.format(s1 + s2)) # 문자열이니까 이어붙임(연결)
# print()
#
# i1 = int(input('입력 i1 : '))  # 정수형으로 형변환
# i2 = int(input('입력 i2 : '))
# print('i1 + i2 = {}'.format(i1 + i2))  # 정수형이니까 더하기 계산
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 입력 s1 : 12
# # 입력 s2 : 34
# # s1 + s2 = 1234
# #
# # 입력 i1 : 12
# # 입력 i2 : 34
# # i1 + i2 = 46


# # ex) 실수형으로 입력받기
# num1 = float(input('실수로 된 첫번째 숫자 : '))
# num2 = float(input('실수로 된 두번째 숫자 : '))
# print('덧셈 결과 : {}'.format(num1 + num2))
# print('뺄셈 결과 : {}'.format(num1 - num2))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 실수로 된 첫번째 숫자 : 12.3
# # 실수로 된 두번째 숫자 : 11.1
# # 덧셈 결과 : 23.4
# # 뺄셈 결과 : 1.200000000000001


# # 65page)
# price = 50000   # 물건값
# n = int(input('할부 개월 입력 >>> ')) # 정수형으로 형변환
# print('매달 내는 돈은 {}원입니다.'.format(price / n)) # 실수형으로 출력
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 할부 개월 입력 >>> 5
# # 매달 내는 돈은 10000.0원입니다.


# # 섹션 4 : 연산자
# # 산술연산자
# # 73page)
# a = 7
# b = 2
# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} ** {} = {}'.format(a, b, a ** b))  # 거듭제곱
# print('{} / {} = {}'.format(a, b, a / b))    # 나누기->결과가 실수형
# print('{} // {} = {}'.format(a, b, a // b))  # 몫
# print('{} % {} = {}'.format(a, b, a % b))    # 나머지
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 7 + 2 = 9
# # 7 - 2 = 5
# # 7 * 2 = 14
# # 7 ** 2 = 49
# # 7 / 2 = 3.5
# # 7 // 2 = 3
# # 7 % 2 = 1


# # 복합 대입 연산자
# # ex) a가 10에서 시작해서 코드가 진행될수록 값이 변하도록 해보기
# a = 10
# print('a의 값 : {}'.format(a))
#
# a += 5   # a = a + 5
# print('a의 값 : {}'.format(a))
#
# a -= 5   # a = a - 5
# print('a의 값 : {}'.format(a))
#
# a *= 5   # a = a * 5
# print('a의 값 : {}'.format(a))
#
# a /= 5   # a = a / 5
# print('a의 값 : {}'.format(a))  # 결과가 실수형
#
# a %= 5   # a = a % 5
# print('a의 값 : {}'.format(a))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # a의 값 : 10
# # a의 값 : 15
# # a의 값 : 10
# # a의 값 : 50
# # a의 값 : 10.0
# # a의 값 : 0.0


# # 76page)
# piggy_bank = 0  # 저금통
#
# money = 10000
# piggy_bank += money   # piggy_bank = piggy_bank + money
# print('저금통에 용돈 {}원을 넣었습니다.'.format(money))
# print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))
#
# snack = 2000
# piggy_bank -= snack   # piggy_bank = piggy_bank - snack
# print('저금통에서 스낵구입비 {}원을 뺐습니다.'.format(snack))
# print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 저금통에 용돈 10000원을 넣었습니다.
# # 지금 저금통에는 10000원이 있습니다.
# # 저금통에서 스낵구입비 2000원을 뺐습니다.
# # 지금 저금통에는 8000원이 있습니다.


# # 관계 연산자
# # 78page)
# a = 15
# print('{} > 10 : {}'.format(a, a > 10))
# print('{} < 10 : {}'.format(a, a < 10))
# print('{} >= 10 : {}'.format(a, a >= 10))
# print('{} <= 10 : {}'.format(a, a <= 10))
# print('{} == 10 : {}'.format(a, a == 10))
# print('{} != 10 : {}'.format(a, a != 10))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 15 > 10 : True
# # 15 < 10 : False
# # 15 >= 10 : True
# # 15 <= 10 : False
# # 15 == 10 : False
# # 15 != 10 : True


# # 논리 연산자
# # 79page)
# a = 10  # True(참)
# b = 0   # False(거짓)
# print('{} > 0 and {} > 0 : {}'.format(a, b, a > 0 and b > 0))
# print('{} > 0 or {} > 0 : {}'.format(a, b, a > 0 or b > 0))
# print('not {} : {}'.format(a, not a))
# print('not {} : {}'.format(b, not b))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 10 > 0 and 0 > 0 : False
# # 10 > 0 or 0 > 0 : True
# # not 10 : False
# # not 0 : True


# # 비트 연산자
# # 82page)
# a = 10   # 00001010(2진수)
# b = 70   # 01000110
#
# print('a & b : {}'.format(a & b))  # 00000010
# print('a | b : {}'.format(a | b))  # 01001110
# print('a ^ b : {}'.format(a ^ b))  # 01001100
# print('~a : {}'.format(~a))        # 11110101
# print('a << 1 : {}'.format(a << 1)) # 00010100  왼쪽으로 한 칸 이동
# print('a >> 1 : {}'.format(a >> 1)) # 00000101  오른쪽으로 한 칸 이동
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # a & b : 2
# # a | b : 78
# # a ^ b : 76
# # ~a : -11
# # a << 1 : 20
# # a >> 1 : 5


# # 시퀀스 연산자
# # 83page)
# tree = '#'
# space = ' '
# print(space * 4 + tree * 1)
# print(space * 3 + tree * 3)
# print(space * 2 + tree * 5)
# print(space * 1 + tree * 7)
# print(space * 0 + tree * 9)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# #     #
# #    ###
# #   #####
# #  #######
# # #########


# # 멤버쉽 연산자 (in 연산자)
# # ex)
# print('안녕' in '안녕하세요')  # 포함되어 있다
# print('메롱' in '안녕하세요')  # 포함되어 있지 않다
#
# print('안녕' not in '안녕하세요')
# print('메롱' not in '안녕하세요')
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # True
# # False
# # False
# # True


# # 조건 연산자 (삼항 연산자)
# # 84page)
# a = 10
# b = 20
# result = (a - b) if (a >= b) else (b - a)
# print('{}과 {}의 차이는 {}입니다.'.format(a, b, result))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 10과 20의 차이는 10입니다.


# # 섹션 5 : 조건문
# # if
# # ex)
# a = 99
# if a < 100:
#     print('100보다 작군요!')  # 참일 때만 출력
#
# print()
#
# num = int(input('정수를 입력하세요 : '))
# if num > 0:
#     print('양수입니다!')
# if num == 0:
#     print('0입니다!')
# if num < 0:
#     print('음수입니다!')
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 100보다 작군요!
# #
# # 정수를 입력하세요 : 0
# # 0입니다!


# # if-else
# # 95page)
# age = int(input('몇 살입니까? >>> '))
# if age >= 20:
#     print('성인')  # 참일 경우
# else:
#     print('미성년자')  # 거짓일 경우
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day05_240524.py
# # 몇 살입니까? >>> 19
# # 미성년자


# ########################################################
# # input문제)
# # 1) 정수 변수 2개를 만들어 숫자를 입력받는다. input함수
# # 아래의 출력결과처럼 나오게 해보자.
# # [화면실행결과]
# # 첫번째 정수는? 13
# # 두번째 정수는? 5
# # 나눗셈의 몫은 2 나머지는 3입니다.
# a = int(input('첫번째 정수는? '))
# b = int(input('두번째 정수는? '))
# print('나눗셈의 몫은 {} 나머지는 {}입니다.'.format(a // b, a % b))

# 스터디룸에 input 문제 올려두겠으니 풀어볼것!
# http://www.koreastudyroom.com/




