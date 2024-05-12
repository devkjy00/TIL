"""
N개의 오름차순 정렬된 원소
x가 등장하는 횟수를 O(logN)시간복잡도로 구하라
"""

from bisect import bisect_left, bisect_right


_, x = 7, 2
nums = [1, 1, 2, 2, 2, 2, 3]


def mysolution(x: int, nums: list[int]) -> int:
    return bisect_right(nums, x)-bisect_left(nums, x)


result = mysolution(x, nums)
if result == 0:
    print(-1)
else:
    print(result)