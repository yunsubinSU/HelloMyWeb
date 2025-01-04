# # 숫자 내장 함수
# # abs() : 절대값
# print(abs(10))
# print(abs(-10))
# print('------------')
#
# # divmod() : 몫과 나머지
# print(divmod(10, 3))  # 결과는 튜플형식
# d, m = divmod(10, 3)
# print(d)
# print(m)
# print('------------')
#
# # max() : 최댓값
# print(max(1, 2))
# li = [10, 8, 4, 6, 2]
# print(max(li))
# print('------------')
#
# # min() : 최솟값
# print(min(1, 10))
# print(min(li))
# print('------------')
#
# # pow() : 거듭제곱 ( ** 연산자 )
# print(pow(10, 2))  # 10을 두 번 곱하다
# print(pow(10, 3))
# print(pow(10, -2))
# print('------------')
#
# # round() : 반올림
# print(round(1.5))  # 일의 자리까지
# print(round(1.4))
# print(round(1.55, 1))  # 소수 첫째자리까지
# print('------------')
#
# # sum() : 합계
# li = [1, 2, 3, 4, 5]
# print(sum(li))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day09_240605.py
# # 10
# # 10
# # ------------
# # (3, 1)
# # 3
# # 1
# # ------------
# # 2
# # 10
# # ------------
# # 1
# # 2
# # ------------
# # 100
# # 1000
# # 0.01
# # ------------
# # 2
# # 1
# # 1.6
# # ------------
# # 15


# # 153page)
# money = 10000
# price = 3000  # 빵 1개의 가격
# result = divmod(money, price)
# print(result)
# print('빵을 {}개 사고 {}원이 남았습니다.'.format(result[0], result[1]))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day09_240605.py
# # (3, 1000)
# # 빵을 3개 사고 1000원이 남았습니다.


# # # 시퀀스 내장 함수
# #
# # # enumerate()
# #
# #     <형식>
# #     for 인덱스번호, 값 in enumerate(리스트명):
# #         수행할 코드
#
# # ex)
# li = [10, 20, 30]
# for i in li:
#     print(i)  # 리스트의 값(요소)만 출력
#
# print()
#
# for item in enumerate(li):
#     print(item)  # 튜플로 묶어져서 나온다
# for index, value in enumerate(li):
#     print(f'{index}번째 : {value}')
#
# print()
#
# for i, v in enumerate(li, start=1): # 인덱스 시작 번호를 1로 정함
#     print(f'{i}번째 : {v}')
#
# print('----------------')
#
# # len() : 길이 (항목 수)
# li = ['a', 'b', 'c', 'd']
# print(len(li))
#
# ch = 'Hello'
# print(len(ch))
#
# d = {'a':'apple', 'b':'banana'}
# print(len(d))
#
# print(len(range(10)))  # 0~9:10개
# print(len(range(1, 10)))  # 1~9:9개
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day09_240605.py
# # 10
# # 20
# # 30
# #
# # (0, 10)
# # (1, 20)
# # (2, 30)
# # 0번째 : 10
# # 1번째 : 20
# # 2번째 : 30
# #
# # 1번째 : 10
# # 2번째 : 20
# # 3번째 : 30
# # ----------------
# # 4
# # 5
# # 2
# # 10
# # 9


# # ex) 총점과 평균구하기
# score = [70, 60, 55, 75, 95]  # 학생 점수 리스트
# total = 0  # 총점을 0으로 초기화
#
# for i, v in enumerate(score, start=1):
#     print(f'{i}번째 학생 점수 : {v}')
#     total += v
#
# print(f'총점 : {total}')
# avg = total / len(score)  # 리스트 개수로 나누어 평균구한다
# print(f'평균 : {avg}')
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day09_240605.py
# # 1번째 학생 점수 : 70
# # 2번째 학생 점수 : 60
# # 3번째 학생 점수 : 55
# # 4번째 학생 점수 : 75
# # 5번째 학생 점수 : 95
# # 총점 : 355
# # 평균 : 71.0


# # sorted() : 정렬
# my_list = [6, 3, 1, 2, 5, 4]
# sorted_list = sorted(my_list)  # 정렬된 새로운 리스트 생성, 원본은 그대로
# reverse_list = sorted(my_list, reverse=True)
# print(f'원본 : {my_list}')
# print(f'정렬 후 (오름차순) : {sorted_list}')
# print(f'정렬 후 (내림차순) : {reverse_list}')
# print('---------------------------')
#
# # zip() : 튜플로 묶기
# names = ['james', 'emily', 'amanda']
# scores = [60, 70, 80]
# for student in zip(names, scores):
#     print(student)
#
# for name, score in zip(names, scores):
#     print(f'{name}의 점수는 {score}점입니다.')
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day09_240605.py
# # 원본 : [6, 3, 1, 2, 5, 4]
# # 정렬 후 (오름차순) : [1, 2, 3, 4, 5, 6]
# # 정렬 후 (내림차순) : [6, 5, 4, 3, 2, 1]
# # ---------------------------
# # ('james', 60)
# # ('emily', 70)
# # ('amanda', 80)
# # james의 점수는 60점입니다.
# # emily의 점수는 70점입니다.
# # amanda의 점수는 80점입니다.


# # 159page)
# months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# for month, day in enumerate(months):
#     print('{}월={}일'.format(month+1, day))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day09_240605.py
# # 1월=31일
# # 2월=28일
# # 3월=31일
# # 4월=30일
# # 5월=31일
# # 6월=30일
# # 7월=31일
# # 8월=31일
# # 9월=30일
# # 10월=31일
# # 11월=30일
# # 12월=31일


# 섹션 10 : 메소드

# # 문자열 메소드
# # .count() : 특정 문자열의 개수
# s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
# print(s.count('기린'))
#
# a = 'best of best'
# print(a.count('best'))
# print(a.count('best', 5))  # 5번 인덱스부터 시작
# print(a.count('best', -7))
# print('----------')
#
# # .find(), .index() : 특정 문자열의 위치 반환
# b = 'apple'
# print(b.find('p'))  # 해당 인덱스 번호
# print(b.rfind('p')) # 오른쪽에서부터 제일 먼저 나오는 p의 인덱스 번호
# print(b.find('z'))  # 없는 경우 -1
#
# print(a.find('best'))
# print(a.find('best', 5))  # 지정한 인덱스부터 검색
#
# print(b.index('p'))
# print(b.index('z'))  # 없는 경우 에러 발생
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day09_240605.py
# # 4
# # 2
# # 1
# # 1
# # ----------
# # 1
# # 2
# # -1
# # 0
# # 8
# # 1
# # Traceback (most recent call last):
# #   File "C:\Python_저녁\day09_240605.py", line 237, in <module>
# #     print(b.index('z'))
# #           ^^^^^^^^^^^^
# # ValueError: substring not found


# # .upper(), .lower(), .capitalize() : 대소문자 변환 메소드
# s = 'BEST of best'
# print(s.upper())  # 대문자로 변환
# print(s.lower())  # 소문자로 변환
# print(s.capitalize())  # 첫 글자만 대문자
# print('----------------------')
#
# # .join() : 합치기
# a = '-'.join('python')
# print(a)
#
# b = '+'.join(['a', 'b', 'c'])
# print(b)
#
# c = ''.join(['x', 'y', 'z'])
# print(c)
#
# d = ''.join({'a':'apple', 'b':'banana'})
# print(d)  # key만 사용
# print('----------------------')
#
# # .split() : 나누기 (리스트 형식으로 결과가 나옴)
# a = 'Life is too short'
# print(a.split())  # 공백을 기준으로 분리
#
# b = '010-1234-5678'
# print(b.split('-'))  # -을 기준으로 분리
#
# c = '제임스,25,남,서울'
# print(c.split(','))  # ,를 기준으로 분리
# print('----------------------')
#
# # .replace() : 바꾸기
# print(a.replace('Life', 'Leg'))
#
# print(b.replace('-', ''))
# print('----------------------')
#
# # .strip() : 불필요한 문자열 제거
# a = '     apple   '
# print(a)
# print(len(a))
#
# b = a.lstrip()  # 왼쪽 공백 제거, rstrip() : 오른쪽 공백 제거
# print(b)
# print(len(b))
#
# c = '<head<'
# d = c.strip('<')  # 양쪽 < 문자 제거
# print(d)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day09_240605.py
# # BEST OF BEST
# # best of best
# # Best of best
# # ----------------------
# # p-y-t-h-o-n
# # a+b+c
# # xyz
# # ab
# # ----------------------
# # ['Life', 'is', 'too', 'short']
# # ['010', '1234', '5678']
# # ['제임스', '25', '남', '서울']
# # ----------------------
# # Leg is too short
# # 01012345678
# # ----------------------
# #      apple
# # 13
# # apple
# # 8
# # head


# # 리스트 메소드
# # .extend() : 확장 (여러개 추가)
# my_list = ['apple', 'banana']
# my_list.extend(['cherry', 'mango'])
# print(my_list)  # 원본 수정됨
# print('----------------------------')
#
# # .remove() : 특정 값을 제거
# my_list.remove('mango')
# print(my_list)
#
# my_list.remove('banana')
# print(my_list)
# print('----------------------------')
#
# # .clear() : 모든 값을 제거
# my_list.clear()
# print(my_list)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day09_240605.py
# # ['apple', 'banana', 'cherry', 'mango']
# # ----------------------------
# # ['apple', 'banana', 'cherry']
# # ['apple', 'cherry']
# # ----------------------------
# # []



