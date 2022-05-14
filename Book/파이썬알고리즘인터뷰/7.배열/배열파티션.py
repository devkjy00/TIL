'''
https://leetcode.com/problems/array-partition-i/

n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

:param nums: [1, 4, 3, 2]
:return: 4
'''

import heapq
from pprint import pprint

def solution(nums):
    '''
    heap에 넣어서 순서대로 빼서 함수에 넣는다
    뒤에서 부터 2개씩 읽어와야겠다
    368 ms	17.3 MB
    '''

    arr = []
    num = 0
    [heapq.heappush(arr, -i) for i in nums]

    while len(arr) >= 2:
        num += min(-heapq.heappop(arr), -heapq.heappop(arr))

    return num

def answer(nums):
    '''
    정렬된 리스트에서 min()로 더 큰 값을 구했을 때 짝수 번째 값이 선택되는 규칙을 찾아서 적용했다
    290 ms	16.9 MB
    '''
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i%2 == 0:
            sum += n

    return sum

print(answer([1,4,3,2]))