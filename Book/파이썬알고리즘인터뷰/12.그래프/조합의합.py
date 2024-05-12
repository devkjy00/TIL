'''
https://leetcode.com/problems/combination-sum/

숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능하다

:param candidates: [2, 3, 6, 7]
:param target: 7
:return: [[7], [2, 2, 3]]
'''


def solution(candidates, target):

    result = []
    def dfs(candidates, num_sum, target):
        for idx, num in enumerate(candidates):
            if sum(num_sum)+num > target:
                continue
            param_num = num_sum[:]
            param_num.append(num)

            if sum(num_sum)+num < target:
                dfs(candidates[idx:], param_num, target)
            else:
                result.append(param_num)
            pass

    dfs(candidates, [], target)
    print(result)

def answer(candidates, target):
    '''
    값을 더하는 방식이 아니라 target값에서 빼는 방식으로 더 효율적인 방식이다
    '''
    result = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])




solution([2,3,5], 8)