'''
https://leetcode.com/problems/binary-search/submissions/

:param num: [-1,0,3,5,9,12]
:param target: 9
:return: 4
'''
import bisect


def answer(nums, target):
    low_idx = 0
    high_idx = len(nums)-1
    while low_idx <= high_idx:
        binary_idx = (low_idx + high_idx) // 2
        print(binary_idx, low_idx, high_idx)
        if nums[binary_idx] < target:
            low_idx = binary_idx + 1  # 똑같은 수를 검사하지 않도록 이전의 위치는 뺀다
            print("high")
        elif nums[binary_idx] > target:
            high_idx = binary_idx - 1 # 똑같은 수를 검사하지 않도록 이전의 위치는 뺀다
        else:
            return binary_idx

    return -1

assert answer([-1,0,3,5,9,12], 9) == 4
assert answer([2, 5], 5) == 0


def bisect_use(nums, target):
    '''
    bisect 모듈에서는 탐색으로 값을 찾지 못하면 해당 값이 있어야 할 위치를 반환한다
    '''
    idx = bisect.bisect_left(nums, target)  # 중복되는 값의 가장 왼쪽
    idx = bisect.bisect_right(nums, target) # 중복되는 값의 가장 왼쪽

