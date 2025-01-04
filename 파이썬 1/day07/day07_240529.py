# # <if과제>
# # 한 점을 구성하는 (x, y) 좌표를 입력받고, 이 점이 (50, 40), (50, 80),
# # (100, 40), (100, 80)을 꼭짓점으로 갖는 사각형 안에 있는지
# # 판별하는 프로그램을 작성하시오.
# # (선 위에 점이 있는 것은 포함하지 않는 것으로 한다.)
# # [화면실행결과]
# # x좌표를 입력하시오 : 60
# # y좌표를 입력하시오 : 100
# # 사각형 안에 없습니다.
# x = int(input('x좌표를 입력하시오 : '))
# y = int(input('y좌표를 입력하시오 : '))
# if 50 < x < 100 and 40 < y < 80:
#     print('사각형 안에 있습니다.')
# else:
#     print('사각형 안에 없습니다.')


# # # 섹션 7 : 반복문
# # # for
# #
# #     반복 횟수가 정해져 있을 때 사용
# #
# #     <형식>
# #     for 변수명 in 리스트명:
# #         반복할 코드
# #
# #     for 변수명 in range(횟수):  # 시작값이 0
# #         반복할 코드 --> 횟수만큼 실행
# #
# #     for 변수명 in range(시작값, 끝값+1):
# #         반복할 코드
# #
# #     for 변수명 in range(시작값, 끝값+1, 증감값):
# #         반복할 코드
# #
# #     for _ in range(횟수): # 반복할 변수를 생략가능(횟수만 반복하고 싶을때)
# #         반복할 코드
#
# # 시퀀스(순서가 있는 자료형)와 for문
#
# # for와 리스트
# for n in [1, 2, 3]:
#     print(n)
#
# print()
#
# string = ['가위', '바위', '보']
# for item in string:
#     print(item)
#
# print('-------------------')
#
# # for와 문자열
# for ch in 'Hello':
#     print(ch)
#
# print('-------------------')
#
# # for와 튜플
# four_seasons = ('Spring', 'Summer', 'Autumn', 'Winter')
# for season in four_seasons:
#     print(season)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day07_240529.py
# # 1
# # 2
# # 3
# #
# # 가위
# # 바위
# # 보
# # -------------------
# # H
# # e
# # l
# # l
# # o
# # -------------------
# # Spring
# # Summer
# # Autumn
# # Winter


# # 120page)
# pwd = input('비밀번호를 입력하세요 >>> ')
#
# ch_count = 0   # 문자 개수
# num_count = 0  # 숫자 개수
#
# for ch in pwd:  # 글자 개수만큼 반복
#     if ch.isalpha():  # ch가 문자라면
#         ch_count += 1  # 문자 개수 변수를 1 증가시킨다
#     elif ch.isnumeric():  # ch가 숫자라면
#         num_count += 1  # 숫자 개수 변수를 1 증가시킨다
#
# if ch_count > 0 and num_count > 0:  # 각각 개수가 0보다 크다면
#     print('가능한 비밀번호입니다.')
# else:
#     print('불가능한 비밀번호입니다.')
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day07_240529.py
# # 비밀번호를 입력하세요 >>> 가나다123
# # 가능한 비밀번호입니다.


# # for와 range()
# for i in range(10):  # 10번 반복, i 변수의 초깃값 0
#     print(f'{i}번째 문장입니다!')  # 0~9
#
# print()
#
# for i in range(1, 11):  # 10번 반복, i 변수의 초깃값 1, 끝값 10
#     print(f'{i}번째 문장입니다!')  # 1~10
#
# print()
#
# for i in range(1, 11, 2):  # 홀수만 출력, 증감값 2
#     print(f'{i}번째 문장입니다!')  # 1,3,5,7,9
#
# print()
#
# for i in range(10, 0, -1):  # 10부터 1까지 1씩 감소
#     print(f'{i}번째 문장입니다!')  # 10~1
#
# print()
#
# for i in reversed(range(10)):  # reversed : 반전(반대로)
#     print(f'{i}번째 문장입니다!')  # 9~0
#
# print()
#
# count = int(input('반복할 횟수를 입력하세요 (1부터 시작) : '))
# for i in range(1, count+1):
#     print(f'{i}번째 문장입니다!')
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day07_240529.py
# # 0번째 문장입니다!
# # 1번째 문장입니다!
# # 2번째 문장입니다!
# # 3번째 문장입니다!
# # 4번째 문장입니다!
# # 5번째 문장입니다!
# # 6번째 문장입니다!
# # 7번째 문장입니다!
# # 8번째 문장입니다!
# # 9번째 문장입니다!
# #
# # 1번째 문장입니다!
# # 2번째 문장입니다!
# # 3번째 문장입니다!
# # 4번째 문장입니다!
# # 5번째 문장입니다!
# # 6번째 문장입니다!
# # 7번째 문장입니다!
# # 8번째 문장입니다!
# # 9번째 문장입니다!
# # 10번째 문장입니다!
# #
# # 1번째 문장입니다!
# # 3번째 문장입니다!
# # 5번째 문장입니다!
# # 7번째 문장입니다!
# # 9번째 문장입니다!
# #
# # 10번째 문장입니다!
# # 9번째 문장입니다!
# # 8번째 문장입니다!
# # 7번째 문장입니다!
# # 6번째 문장입니다!
# # 5번째 문장입니다!
# # 4번째 문장입니다!
# # 3번째 문장입니다!
# # 2번째 문장입니다!
# # 1번째 문장입니다!
# #
# # 9번째 문장입니다!
# # 8번째 문장입니다!
# # 7번째 문장입니다!
# # 6번째 문장입니다!
# # 5번째 문장입니다!
# # 4번째 문장입니다!
# # 3번째 문장입니다!
# # 2번째 문장입니다!
# # 1번째 문장입니다!
# # 0번째 문장입니다!
# #
# # 반복할 횟수를 입력하세요 (1부터 시작) : 16
# # 1번째 문장입니다!
# # 2번째 문장입니다!
# # 3번째 문장입니다!
# # 4번째 문장입니다!
# # 5번째 문장입니다!
# # 6번째 문장입니다!
# # 7번째 문장입니다!
# # 8번째 문장입니다!
# # 9번째 문장입니다!
# # 10번째 문장입니다!
# # 11번째 문장입니다!
# # 12번째 문장입니다!
# # 13번째 문장입니다!
# # 14번째 문장입니다!
# # 15번째 문장입니다!
# # 16번째 문장입니다!


# # ex) 1부터 100까지 수 중 3의 배수, 5의 배수, 3과 5의 공배수
# for i in range(1, 101):  # 초깃값 1, 끝값 100, 증감값 1(생략)
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i}:3과 5의 공배수')
#     elif i % 3 == 0:
#         print(f'{i}:3의 배수')
#     elif i % 5 == 0:
#         print(f'{i}:5의 배수')
#     else:
#         print(i)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day07_240529.py
# # 1
# # 2
# # 3:3의 배수
# # 4
# # 5:5의 배수
# # 6:3의 배수
# # 7
# # 8
# # 9:3의 배수
# # 10:5의 배수
# # 11
# # 12:3의 배수
# # 13
# # 14
# # 15:3과 5의 공배수
# # 16
# # 17
# # 18:3의 배수
# # 19
# # 20:5의 배수
# # 21:3의 배수
# # 22
# # 23
# # 24:3의 배수
# # 25:5의 배수
# # 26
# # 27:3의 배수
# # 28
# # 29
# # 30:3과 5의 공배수
# # 31
# # 32
# # 33:3의 배수
# # 34
# # 35:5의 배수
# # 36:3의 배수
# # 37
# # 38
# # 39:3의 배수
# # 40:5의 배수
# # 41
# # 42:3의 배수
# # 43
# # 44
# # 45:3과 5의 공배수
# # 46
# # 47
# # 48:3의 배수
# # 49
# # 50:5의 배수
# # 51:3의 배수
# # 52
# # 53
# # 54:3의 배수
# # 55:5의 배수
# # 56
# # 57:3의 배수
# # 58
# # 59
# # 60:3과 5의 공배수
# # 61
# # 62
# # 63:3의 배수
# # 64
# # 65:5의 배수
# # 66:3의 배수
# # 67
# # 68
# # 69:3의 배수
# # 70:5의 배수
# # 71
# # 72:3의 배수
# # 73
# # 74
# # 75:3과 5의 공배수
# # 76
# # 77
# # 78:3의 배수
# # 79
# # 80:5의 배수
# # 81:3의 배수
# # 82
# # 83
# # 84:3의 배수
# # 85:5의 배수
# # 86
# # 87:3의 배수
# # 88
# # 89
# # 90:3과 5의 공배수
# # 91
# # 92
# # 93:3의 배수
# # 94
# # 95:5의 배수
# # 96:3의 배수
# # 97
# # 98
# # 99:3의 배수
# # 100:5의 배수


# # 125page)
# dan = int(input('출력할 구구단을 입력하세요 >>> '))
# for n in range(1, 10):  # 1~9
#     print('{} x {} = {}'.format(dan, n, dan * n))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day07_240529.py
# # 출력할 구구단을 입력하세요 >>> 9
# # 9 x 1 = 9
# # 9 x 2 = 18
# # 9 x 3 = 27
# # 9 x 4 = 36
# # 9 x 5 = 45
# # 9 x 6 = 54
# # 9 x 7 = 63
# # 9 x 8 = 72
# # 9 x 9 = 81


# # ex) 중첩 for문을 사용한 구구단 만들기
# for i in range(2, 10):  # 단(2~9)
#     print('----{}단----'.format(i))  # 단 제목
#     for k in range(1, 10):  # 곱해지는 수(1~9)
#         print('{} x {} = {}'.format(i, k, i * k))
#     print()  # 단 끝난 후 빈 줄 추가
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day07_240529.py
# # ----2단----
# # 2 x 1 = 2
# # 2 x 2 = 4
# # 2 x 3 = 6
# # 2 x 4 = 8
# # 2 x 5 = 10
# # 2 x 6 = 12
# # 2 x 7 = 14
# # 2 x 8 = 16
# # 2 x 9 = 18
# #
# # ----3단----
# # 3 x 1 = 3
# # 3 x 2 = 6
# # 3 x 3 = 9
# # 3 x 4 = 12
# # 3 x 5 = 15
# # 3 x 6 = 18
# # 3 x 7 = 21
# # 3 x 8 = 24
# # 3 x 9 = 27
# #
# # ----4단----
# # 4 x 1 = 4
# # 4 x 2 = 8
# # 4 x 3 = 12
# # 4 x 4 = 16
# # 4 x 5 = 20
# # 4 x 6 = 24
# # 4 x 7 = 28
# # 4 x 8 = 32
# # 4 x 9 = 36
# #
# # ----5단----
# # 5 x 1 = 5
# # 5 x 2 = 10
# # 5 x 3 = 15
# # 5 x 4 = 20
# # 5 x 5 = 25
# # 5 x 6 = 30
# # 5 x 7 = 35
# # 5 x 8 = 40
# # 5 x 9 = 45
# #
# # ----6단----
# # 6 x 1 = 6
# # 6 x 2 = 12
# # 6 x 3 = 18
# # 6 x 4 = 24
# # 6 x 5 = 30
# # 6 x 6 = 36
# # 6 x 7 = 42
# # 6 x 8 = 48
# # 6 x 9 = 54
# #
# # ----7단----
# # 7 x 1 = 7
# # 7 x 2 = 14
# # 7 x 3 = 21
# # 7 x 4 = 28
# # 7 x 5 = 35
# # 7 x 6 = 42
# # 7 x 7 = 49
# # 7 x 8 = 56
# # 7 x 9 = 63
# #
# # ----8단----
# # 8 x 1 = 8
# # 8 x 2 = 16
# # 8 x 3 = 24
# # 8 x 4 = 32
# # 8 x 5 = 40
# # 8 x 6 = 48
# # 8 x 7 = 56
# # 8 x 8 = 64
# # 8 x 9 = 72
# #
# # ----9단----
# # 9 x 1 = 9
# # 9 x 2 = 18
# # 9 x 3 = 27
# # 9 x 4 = 36
# # 9 x 5 = 45
# # 9 x 6 = 54
# # 9 x 7 = 63
# # 9 x 8 = 72
# # 9 x 9 = 81


# # ex) 중첩 for문을 이용한 별찍기
# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()
#
# print()
#
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
#
# print()
#
# for i in range(5): # 0 1 2
#     for j in range(5):  # 0 1 2
#         if i > j:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(5):  # 0 1 2 3 4
#     for j in range(i+1): # 1번반복, 2번반복, 3번반복, 4번반복, 5번반복
#         print('*', end='')
#     print()
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day07_240529.py
# # *****
# # *****
# # *****
# # *****
# # *****
# #
# # *
# #  *
# #   *
# #    *
# #     *
# #
# # *****
# #  ****
# #   ***
# #    **
# #     *
# # *
# # **
# # ***
# # ****
# # *****


# ##############################################
# # 반복문 문제)
# # 문제1) for를 이용해서 1~5까지의 숫자들을 차례대로 출력하기
# # (range함수 사용)
# # [화면실행결과]
# # 1 2 3 4 5
# for i in range(1, 6):
#     print(i, end=' ')

# # 문제2) for문을 이용하여 1부터 10까지의 합을 구하시오.
# # [화면실행결과]
# # 1부터 10까지의 합 : 55
# # 힌트 : 합계를 담을 변수를 먼저 만들어서 초기화하고 진행하기, range사용
# total = 0  # 합계
# for i in range(1, 11):
#     total += i   # total = total + i
# print('1부터 10까지 합 : {}'.format(total))

# # 문제3) for문을 이용하여 1부터 키보드로 입력한 값까지의 합계구하기
# # [화면실행결과]
# # 값을 입력하시오 : 123
# # 1부터 123까지의 합계 : 7626
# num = int(input('값을 입력하시오 : '))
# total = 0
# for i in range(1, num+1):
#     total += i  # total = total + i
# print('1부터 {}까지의 합계 : {}'.format(num, total))







