'''
https://www.acmicpc.net/problem/9095

정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다.
합을 나타낼 때는 수를 1개 이상 사용해야 한다
'''
def solution(n):
    basic_nums = [1, 2, 3]
    count = [0]
    def dfs(num):
        if not n:
            return
        for i in basic_nums:
            if num+i == n:
                count[0] += 1
            elif num+i < n:
                dfs(num+i)
    dfs(0)
    return count[0]

print(solution(8))