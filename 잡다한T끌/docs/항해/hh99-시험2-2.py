'''
https://programmers.co.kr/learn/courses/30/lessons/43165



:param numbers: [1, 1, 1, 1, 1]
:param target: 3
:return: 5
'''


def solution(numbers, target):
    result = [0]
    def dfs(num, idx):
        if idx == len(numbers):
            if num == target:
               result[0] += 1
               return
            else:
                return
        dfs(num + numbers[idx], idx+1)
        dfs(num - numbers[idx], idx+1)


    dfs(0, 0)
    return result[0]

assert solution([1, 1, 1, 1, 1], 3) == 5
assert solution([4, 1, 2, 1], 4) == 2
