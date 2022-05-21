'''
https://leetcode.com/problems/subsets/

모든 부분 집합을 리턴하라

:param nums: [1, 2, 3]
:return: [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
'''


def solution(nums):
    result = []
    result.append([])

    def dfs(nums, set_list):
        for i, num in enumerate(nums):
            added_set = set_list + [num]
            result.append(added_set)
            dfs(nums[i+1:], added_set)
            pass

    dfs(nums, [])
    return result

def answer(nums):
    '''
    슬라이싱한 리스트를 넘기지 않고 인덱스만 변경해서 같은 전역리스트로 for문을 돌렸다
    '''
    result = []
    def dfs(index, path):
        result.append(path)
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result



print(solution([1, 2, 3]))