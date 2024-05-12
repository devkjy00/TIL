'''
https://programmers.co.kr/learn/courses/30/lessons/42577

전화번호부에 있는 번호중, 한 번호가 다른 번호의 접두어인 경우를 확인
있으면 False 없으면 True 반환

:param phone_book: ["119", "97674223", "1195524421"]
:return: False
'''


def solution_timeover(phone_book):
    '''
    주어진 매개 변수를 중복을 비교
        - 짧은 전화번호가 앞에 나오기 쉽다 -> 문자열 길이로 정렬하자
        - 문자열의 접두어인 경우만 비교 -> str.startswith()
    '''
    phone_book.sort(key=lambda x: len(x))

    for i, tel in enumerate(phone_book):
        for j, tel_compare in enumerate(phone_book):
            if i == j:
                continue
            if tel_compare.startswith(tel):
                return False

    return True

def solution(phone_book):
    '''
    for 문을 한번만 돌도록 구현해야 한다 -> 인덱스를 활용해서 구현(투포인터)
    비슷한 값이 옆에 있도록 하자 -> 문자열값으로 정렬
    '''
    phone_book.sort()

    for i, tel in enumerate(phone_book):
        if i == len(phone_book)-1:
            break
        if phone_book[i+1].startswith(tel):
            return False
    return True
# solution(["119", "97674223", "1195524421"])
