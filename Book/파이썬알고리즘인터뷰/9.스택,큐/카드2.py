'''
https://www.acmicpc.net/problem/2164

백준, 카드2
1부터 N까지 순서대로 정렬된 카드
한장만 남을 때까지 위에서부터 한장 버리고 한장 마지막에 다시 넣고 반복

:param input: 6
:return: 4
'''

import collections, sys
input = sys.stdin.readline

def solution():
    cards = collections.deque(range(int(input()), 0, -1))

    while len(cards) > 1:
        cards.pop()
        cards.appendleft(cards.pop())

    print(cards.pop())
solution()