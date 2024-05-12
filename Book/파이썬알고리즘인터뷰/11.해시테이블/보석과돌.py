'''
https://leetcode.com/problems/jewels-and-stones/

J는 보석, S는 소유한 돌, S에는 보석이 몇 개 있는지 찾아라, 대소문자 구분

:param jewels: "aA"
:param stones: "aAAbbbb"
'''
import collections

def solution(jewels, stones):
    table = collections.defaultdict(int)
    for s in stones:
        table[s] += 1

    count = [num for stone, num in table.items()
                if stone in jewels]
    return sum(count)


def answer(jewels, stones):
    '''
    Counter를 사용해서 계산 생략
    비교없이 jewels를 key로 사용해서 값 더하기
    '''
    table = collections.Counter(stones)
    count = 0

    for char in jewels:
        count += table[char]

def answer_line_1(J, S):
    '''
    sum()에 bool리스트를 넣으면 True 값의 개수를 구한다
    '''
    return sum(s in J for s in S)


print(solution("aA", "aAAbbbb"))