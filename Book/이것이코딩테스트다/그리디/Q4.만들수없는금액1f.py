"""
N개의 동전으로 만들수 없는 금액(떨어지지않는 값)의 최소값 구하기

-> 시작비교 값 1, 정렬된 동전을 비교후 더한다, 비교값보다 더 값이큰 동전이 나오면 최소값
:param N: 5
:param coin: [3,2,1,1,9]
:return : 8
"""
n = 5
coins = [3,2,1,1,9]

def my_solution():
    coins.sort()
    target = 1
    for x in coins:
        if target<x:
            break
        target += x

my_solution()
        




