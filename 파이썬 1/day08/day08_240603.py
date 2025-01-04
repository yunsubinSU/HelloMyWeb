# # 비시퀀스와 for문
#
# # for와 세트
# for item in {'가위', '바위', '보'}:
#     print(item)  # 순서는 랜덤으로 나온다
#
# print('-------------')
#
# # for와 딕셔너리
# person = {
#     'name':'에밀리',
#     'age':20
# }
#
# for item1 in person:
#     print(item1)  # 키(key)가 출력
#
# print('-------------')
#
# for item2 in person:
#     print(person[item2])  # 값(value) 출력
#
# print('-------------')
#
# for item3 in person:
#     print(person.get(item3))  # 값(value) 출력
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 보
# # 가위
# # 바위
# # -------------
# # name
# # age
# # -------------
# # 에밀리
# # 20
# # -------------
# # 에밀리
# # 20


# # 128page)
# eng_dict = {
#     'sun':'태양',
#     'moon':'달',
#     'star':'별',
#     'space':'우주'
# }
# for word in eng_dict:
#     print('{}의 뜻 : {}'.format(word, eng_dict.get(word)))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # sun의 뜻 : 태양
# # moon의 뜻 : 달
# # star의 뜻 : 별
# # space의 뜻 : 우주


# # 섹션 8 : 기타 제어문
#
# # break
# # ex) 0부터 99까지 출력
# i = 0
# while True:  # 무한 반복
#     print(i, end=' ')  # i 출력
#     i += 1  # i = i + 1
#     if i == 100:  # i가 100이 되면
#         break     # 제어 흐름을 빠져나온다(반복문을 종료)
# #
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99


# # 136page)
# while True:
#     city = input('대한민국의 수도는 어디인가요?? >>> ')
#     if city == '서울' or city == 'seoul' or city == 'SEOUL':
#         print('정답입니다!')
#         break  # 반복문을 종료
#     else:
#         print('오답입니다! 다시 시도하세요.')
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 대한민국의 수도는 어디인가요?? >>> 대구
# # 오답입니다! 다시 시도하세요.
# # 대한민국의 수도는 어디인가요?? >>> 광주
# # 오답입니다! 다시 시도하세요.
# # 대한민국의 수도는 어디인가요?? >>> 부산
# # 오답입니다! 다시 시도하세요.
# # 대한민국의 수도는 어디인가요?? >>> 서울
# # 정답입니다!


# # 137page)
# hobbies = []
# while True:
#     hobby = input('취미를 입력하세요 (종료는 그냥 엔터) >>> ')
#     if hobby == '':  # 아무것도 입력되지 않으면
#         print('입력된 취미가 모두 저장되었습니다.')
#         break
#     else:
#         hobbies.append(hobby) # hobby변수에 담긴 값을 리스트에 추가
#
# print(hobbies)  # 반복문이 모두 끝난 후에 실행
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 취미를 입력하세요 (종료는 그냥 엔터) >>> 독서
# # 취미를 입력하세요 (종료는 그냥 엔터) >>> 운동
# # 취미를 입력하세요 (종료는 그냥 엔터) >>> 놀기
# # 취미를 입력하세요 (종료는 그냥 엔터) >>> 잠자기
# # 취미를 입력하세요 (종료는 그냥 엔터) >>>
# # 입력된 취미가 모두 저장되었습니다.
# # ['독서', '운동', '놀기', '잠자기']


# # ex) 반복문을 이용한 커피자판기 프로그램
# coffee = 3
# while True:
#     money = int(input('돈을 넣어주세요 : '))
#     if money == 300:  # 커피값이 300원이라고 가정했을 경우
#         print('커피 나왔습니다!')
#         coffee -= 1   # coffee = coffee - 1
#         print(f'남은 커피의 양은 {coffee}개입니다.')
#     elif money > 300:
#         print(f'거스름돈 {money-300}원을 주고 커피도 줍니다!')
#         coffee -= 1
#         print(f'남은 커피의 양은 {coffee}개입니다.')
#     else:
#         print(f'{money}원을 다시 돌려주고 커피는 주지 않습니다!')
#         print(f'남은 커피의 양은 {coffee}개입니다.')
#
#     if coffee == 0:
#         print('커피가 다 떨어졌습니다. 판매를 중지합니다!')
#         break
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 돈을 넣어주세요 : 300
# # 커피 나왔습니다!
# # 남은 커피의 양은 2개입니다.
# # 돈을 넣어주세요 : 500
# # 거스름돈 200원을 주고 커피도 줍니다!
# # 남은 커피의 양은 1개입니다.
# # 돈을 넣어주세요 : 200
# # 200원을 다시 돌려주고 커피는 주지 않습니다!
# # 남은 커피의 양은 1개입니다.
# # 돈을 넣어주세요 : 1000
# # 거스름돈 700원을 주고 커피도 줍니다!
# # 남은 커피의 양은 0개입니다.
# # 커피가 다 떨어졌습니다. 판매를 중지합니다!


# # continue
# # ex) 0~10 사이의 수 중에서 홀수만 출력
# a = 0
# while a < 10:
#     a += 1  # a = a + 1
#     if a % 2 == 0:  # 짝수라면
#         continue
#     print(a) # 홀수만 출력
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 1
# # 3
# # 5
# # 7
# # 9


# # 139page)
# fruits = ['사과', '감귤']
# count = 3   # 입력해야 할 남은 과일의 수
#
# while count > 0:
#     fruit = input('어떤 과일을 저장할까요? >>> ')
#     if fruit in fruits:  # fruit변수에 있는 값이 fruits리스트에 포함되었나?
#         print('동일한 과일이 있습니다.')
#         continue # 포함되었다면 다시 반복문의 처음(조건)으로 간다
#     fruits.append(fruit) # 포함되지 않았으면 리스트에 추가
#     count -= 1  # 횟수를 1번 줄여준다
#     print('입력이 {}번 남았습니다.'.format(count))
#
# print('5개의 과일은 {}입니다.'.format(fruits))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 어떤 과일을 저장할까요? >>> 사과
# # 동일한 과일이 있습니다.
# # 어떤 과일을 저장할까요? >>> 감귤
# # 동일한 과일이 있습니다.
# # 어떤 과일을 저장할까요? >>> 바나나
# # 입력이 2번 남았습니다.
# # 어떤 과일을 저장할까요? >>> 망고
# # 입력이 1번 남았습니다.
# # 어떤 과일을 저장할까요? >>> 바나나
# # 동일한 과일이 있습니다.
# # 어떤 과일을 저장할까요? >>> 포도
# # 입력이 0번 남았습니다.
# # 5개의 과일은 ['사과', '감귤', '바나나', '망고', '포도']입니다.


# # 140page)
# count = 0
# total = 0 # 합계
#
# while count < 5:
#     n = int(input('{}번째 정수를 입력하세요 >>>'.format(count + 1)))
#     if n <= 0:  # 0과 음수는 제외하기 위해 넣은 코드
#         print('0 이하의 정수를 처리할 수 없습니다!')
#         continue
#     total += n
#     count += 1
#
# print('입력된 5개의 양수의 총 합은 {}입니다.'.format(total))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 1번째 정수를 입력하세요 >>>-1
# # 0 이하의 정수를 처리할 수 없습니다!
# # 1번째 정수를 입력하세요 >>>2
# # 2번째 정수를 입력하세요 >>>0
# # 0 이하의 정수를 처리할 수 없습니다!
# # 2번째 정수를 입력하세요 >>>23
# # 3번째 정수를 입력하세요 >>>5
# # 4번째 정수를 입력하세요 >>>-3
# # 0 이하의 정수를 처리할 수 없습니다!
# # 4번째 정수를 입력하세요 >>>5
# # 5번째 정수를 입력하세요 >>>10
# # 입력된 5개의 양수의 총 합은 45입니다.


# # 참고) 리스트 내포 (리스트 컴프리헨션)
# # append 사용
# li = [1, 2, 3]
# num1 = []
# for n in li:
#     num1.append(n * 2)
# print('append 사용 : {}'.format(num1))
#
# # 리스트 내포 사용
# num2 = [n * 2 for n in li]
# print('리스트 내포 사용 : {}'.format(num2))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # append 사용 : [2, 4, 6]
# # 리스트 내포 사용 : [2, 4, 6]


# # 섹션 9 : 내장 함수
#
# # 문자열 내장 함수
# # chr() : 유니코드를 문자로 변환
# print(chr(48))
# print(chr(49))
# print(chr(65))
# print(chr(66))
# print(chr(97))
# print(chr(98))
# print(chr(44032))
# print('---------------')
#
# # ord() : 문자를 유니코드로 변환
# print(ord('A'))
# print(ord('a'))
# print(ord('가'))
# print('---------------')
#
# # eval() : 문자열로 된 값을 계산
# print('100 + 200')
# print(eval('100 + 200'))
# print(eval('min(1,2,3)'))  # min() : 최솟값
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 0
# # 1
# # A
# # B
# # a
# # b
# # 가
# # ---------------
# # 65
# # 97
# # 44032
# # ---------------
# # 100 + 200
# # 300
# # 1


# # 149page)
# expr = input('계산식을 입력하세요 >>> ')
# result = eval(expr)
# print(result)
# print(type(result))
# print(expr + '=' + str(result))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day08_240603.py
# # 계산식을 입력하세요 >>> 1+2+3
# # 6
# # <class 'int'>
# # 1+2+3=6


# ###################################################
# # for문제)
# # 시작값과 끝값, 증감값까지 사용자에게 정수를 입력받아
# # 시작값과 끝값까지의 합계구하기 (for, range()이용)
# # [화면실행결과]
# # 시작값을 입력하시오 : 3
# # 끝값을 입력하시오 : 300
# # 증감값을 입력하시오 : 3
# # 3에서 300까지 3씩 증가시킨 값의 합계 : 15150
# num1 = int(input('시작값을 입력하시오 : '))
# num2 = int(input('끝값을 입력하시오 : '))
# num3 = int(input('증감값을 입력하시오 : '))
# total = 0
# for i in range(num1, num2+1, num3):
#     total += i
# print(f'{num1}에서 {num2}까지 {num3}씩 증가시킨 값의 합계 : {total}')









