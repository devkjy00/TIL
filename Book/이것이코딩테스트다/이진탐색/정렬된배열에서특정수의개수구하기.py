"""
N개의 오름차순 정렬된 원소
x가 등장하는 횟수를 O(logN)시간복잡도로 구하라
"""

from bisect import bisect_left, bisect_right 


_, x = 7, 2
nums = [1, 1, 2, 2, 2, 2, 3]


def mysolution(x: int, nums: list[int]) -> int:
    a = bisect_right(nums, x)
    b = bisect_left(nums, x)
    return a-b


def 이진검색직접구현(x, nums):
    n = len(nums)
    if(a := first(nums, x, 0 , n-1)==None):
        return 0
    # b = last(nums, x, 0, n-1)
    # return b - a + 1

def first(array, target, start, end):
    pass
    
    
result = mysolution(x, nums)
print(result)