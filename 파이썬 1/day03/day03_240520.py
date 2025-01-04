# #################################################
# # 문제1) 날짜와 시간이 출력되게 만들기
# # [화면실행결과]
# # 2020/10/31 11:43:59
# # 힌트 --> print함수의 sep, end사용
# print(2020, 10, 31, sep='/', end=' ')
# print(11, 43, 59, sep=':')

# #########################################################
# # 문제2) 화면실행결과를 참고하여 문자열 인덱싱으로 한 글자씩 출력해보자.
# # string = 'PYTHON'
# # [화면실행결과]
# # P
# # Y
# # H
# # N
# string = 'PYTHON'
# print(string[0])
# print(string[1])
# print(string[3])
# print(string[-1])

# # 문제3) 문자열 슬라이싱으로 화면실행결과와 같도록 출력해보자.
# # mystr = 'GOOD NIGHT'
# # [화면실행결과]
# # OO
# # GH
# #  NIGHT
# mystr = 'GOOD NIGHT'
# print(mystr[1:3])
# print(mystr[7:9])
# print(mystr[4:])
# #########################################################
# # 문제4) 과일이름을 요소로 하는 값이 3개인 리스트 a를 생성해라(과일이름 3개)
# a = ['사과', '복숭아', '포도']
# print(a)
#
# # 문제5) 음식이름을 요소로 하는 값이 3개인 리스트 b를 생성해라(음식이름 3개)
# b = ['김치', '불고기', '비빔밥']
# print(b)
#
# # 문제6) 위 두 개의 리스트를 하나로 합친 리스트 c를 생성해라 (---->풀지 말기!)
#
#
# # 문제7) 리스트 a에서 마지막 과일을 다른 과일로 대체해라
# a[2] = '바나나'
# print(a)


# # 리스트 연산자 --> +, *
# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
#
# print(list_a)
# print(list_b)
#
# list_c = list_a + list_b  # 하나의 리스트로 합쳐진다(이어진다)
# print(list_c)
#
# list_d = list_a * 3  # 3번 반복
# print(list_d)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day03_240520.py
# # [1, 2, 3]
# # [4, 5, 6]
# # [1, 2, 3, 4, 5, 6]
# # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# # 리스트의 요소(값) 추가 : append, insert
# list1 = [1, 2, 3]
# print('list1 :', list1)
#
# list1.append(4)  # 맨 뒤에 정수 4를 삽입
# print('list1 :', list1)
#
# list1.append(100)
# print('list1 :', list1)
#
# list1.insert(1, 50)  # 1번 인덱스 자리에 정수 50을 삽입
# print('list1 :', list1)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day03_240520.py
# # list1 : [1, 2, 3]
# # list1 : [1, 2, 3, 4]
# # list1 : [1, 2, 3, 4, 100]
# # list1 : [1, 50, 2, 3, 4, 100]


# # 리스트의 요소(값) 제거 - 인덱스 번호로 삭제 : pop, del
# list2 = [0, 1, 2, 3, 4, 5]
# print('list2 :', list2)
#
# del list2[1]  # 1번 인덱스 자료(값)를 삭제
# print('list2 :', list2)
#
# list2.pop(2)  # 2번 인덱스 자료(값)를 삭제
# print('list2 :', list2)
#
# list2.pop()   # 맨 마지막 자료를 삭제
# print('list2 :', list2)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day03_240520.py
# # list2 : [0, 1, 2, 3, 4, 5]
# # list2 : [0, 2, 3, 4, 5]
# # list2 : [0, 2, 4, 5]
# # list2 : [0, 2, 4]


# # 튜플 - 읽기 전용 리스트
# t1 = (1, 2, 3)
# print('튜플 t1 :', t1)
#
# t2 = 1, 2, 3   # 괄호를 생략할 수 있다!
# print('튜플 t2 :', t2)
#
# t3 = tuple([100, 3.14, 'hello'])
# print('튜플 t3 :', t3)
# print(type(t3))
#
# t4 = (100)   # 튜플이 아님!  변수로 인식!
# print('변수 t4 :', t4)
# print(type(t4))
#
# t5 = (100,)  # t5 = 100,
# print('튜플 t5 :', t5)
# print(type(t5))
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day03_240520.py
# # 튜플 t1 : (1, 2, 3)
# # 튜플 t2 : (1, 2, 3)
# # 튜플 t3 : (100, 3.14, 'hello')
# # <class 'tuple'>
# # 변수 t4 : 100
# # <class 'int'>
# # 튜플 t5 : (100,)
# # <class 'tuple'>


# # 리스트와 튜플의 차이점
#
#     리스트는 [], 튜플은 ()
#     리스트는 그 값의 추가, 수정, 삭제 가능
#     튜플은 그 값을 바꿀 수 없다
#
# # 리스트와 튜플의 공통점
#
#     연산 가능(덧셈, 곱셈)
#     인덱싱, 슬라이싱 가능(시퀀스 자료형 - 순서가 있는 자료형)


# # 세트 (집합)
# s1 = {1, 2, 3}
# print('세트 s1 :', s1)
# print(type(s1))
#
# # 값 1개 추가하기 - add
# s1.add(4)  # 무조건 맨 뒤에 추가(순서가 없기 때문에)
# print('세트 s1 :', s1)
#
# # 값 여러개 추가하기 - update
# s1.update([5, 6, 7])
# print('세트 s1 :', s1)
#
# # 특정 값을 제거하기 - remove
# s1.remove(3)  # 값 3을 지워라
# print('세트 s1 :', s1)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day03_240520.py
# # 세트 s1 : {1, 2, 3}
# # <class 'set'>
# # 세트 s1 : {1, 2, 3, 4}
# # 세트 s1 : {1, 2, 3, 4, 5, 6, 7}
# # 세트 s1 : {1, 2, 4, 5, 6, 7}


# # 딕셔너리
# dic = {}  # 빈 딕셔너리
# print(type(dic))
#
# s2 = set() # 빈 세트
# print(s2)
# print(type(s2))
#
# dic = {'name':'홍길동', 'birthday':'0720'}
# print('딕셔너리 dic :', dic)
#
# # 특정 값을 출력할 때
# print(dic['name'])  # 값(홍길동)이 출력
# a = dic['birthday'] # 0720이 변수 a에 담긴다
# print(a)
#
# # 딕셔너리 값을 수정할 때
# dic['name'] = '푸바오'
# print('딕셔너리 dic :', dic)
#
# # 딕셔너리 쌍을 추가할 때
# dic['address'] = '용인'  # 해당하는 키가 없으면 추가됨
# print('딕셔너리 dic :', dic)
#
# # 딕셔너리 쌍을 삭제할 때 - del
# del dic['address']   # address에 해당하는 키와 값을 삭제
# print('딕셔너리 dic :', dic)
#
# # key 리스트 만들기 - keys
# print(dic.keys()) # 키 부분만 따로 모은 것
# li = list(dic.keys())
# print(li)
# print(type(li))
#
# # 값(value) 리스트 만들기 - values
# print(dic.values())
#
# # items 함수를 이용해서 쌍을 얻기
# print(dic.items())  # 쌍이 튜플형식으로 묶인다
# li = list(dic.items())
# print(li)
#
# # 키와 값을 모두 지우기
# dic.clear()
# print('딕셔너리 dic :', dic)
#
# # C:\Python_저녁\.venv\Scripts\python.exe C:\Python_저녁\day03_240520.py
# # <class 'dict'>
# # set()
# # <class 'set'>
# # 딕셔너리 dic : {'name': '홍길동', 'birthday': '0720'}
# # 홍길동
# # 0720
# # 딕셔너리 dic : {'name': '푸바오', 'birthday': '0720'}
# # 딕셔너리 dic : {'name': '푸바오', 'birthday': '0720', 'address': '용인'}
# # 딕셔너리 dic : {'name': '푸바오', 'birthday': '0720'}
# # dict_keys(['name', 'birthday'])
# # ['name', 'birthday']
# # <class 'list'>
# # dict_values(['푸바오', '0720'])
# # dict_items([('name', '푸바오'), ('birthday', '0720')])
# # [('name', '푸바오'), ('birthday', '0720')]
# # 딕셔너리 dic : {}




