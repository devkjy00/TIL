'''
https://programmers.co.kr/learn/courses/30/lessons/12985

참가자 n명, n-1과 n번 참가자끼리 게임진행 ->
다음 라운드는 1번 부터 n/2번 까지 배정
참가자 a, b가 몇번째 라운드에서 만나는지 return
'''

def solution(n, a, b):
    player = [False for _ in range(n+1)]
    player[a], player[b] = True, True
    depth, num, interval = 0, 2, 1

    while True:
        depth += 1
        for p in range(1, n, num):
            if player[p] and player[p+interval]:
                return depth
            if player[p] or player[p+interval]:
                player[p] = True

        num *= 2
        interval *= 2

print(solution(8, 4, 7))



