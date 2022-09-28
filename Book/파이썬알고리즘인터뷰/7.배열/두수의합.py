'''
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

:param nums: [2, 7, 11, 15]
:param target: 9
:return : [0, 1]
'''

def solution(nums, target):
    '''
    브루트 포스, 일반적인 완전탐색 방법으로 구현
    '''
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def use_in(nums, target):
    '''
    모든 조합을 비교하지 않고 타겟에서 값을 뺀 값이 존재하는지 in으로 탐색
    같은 시간 복잡도라도 in연산자가 더 가볍고 빠르다
    '''
    for i, n in enumerate(nums):
        temp_target = target - n
        comp_idx = i + 1

        if temp_target in nums[comp_idx:]:
            # return [nums.index(n), nums[i+1:].index(temp_target)+(i+1)]
            return [i, nums.index(temp_target)]

print(use_in([2, 7, 11, 15], 9))
