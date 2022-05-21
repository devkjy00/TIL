'''
https://www.acmicpc.net/problem/9663

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

:param n: 8
:return: 92

'''
from pprint import pprint
import copy


def solution(n):
    '''
    백트래킹을 이용한 풀이
    n번 반복하는 for문,
    -> if문으로 놓을 수 있는 위치를 찾기위해 좌표생성 필요
    -> 만약 이전의 좌표보다 x가 한칸 위/아래인 경우는 놓을 수 없다
        -> [0][0] 이면 [1][0], [1][1]에 둘수 없다
        -> [0][2] 이면
    -> 참조가 아닌 값을 복사하도록 .. -> 값 복사가 제대로 안되고 있는 것 같다 ->  값을 바꾸기 전에 복사
    -> 시간 초과로 실

    - 재귀함수로 돌릴 데이터를 최소화해야 한다
    '''
    result = [0]

    def dfs(table, idx):
        if idx == n:
            result[0] += 1
            return
        for i in range(n):
            if table[i][idx]:       # 퀸을 놓을 수 있으면
                # 각 for문은 변경되지 않은 값이 필요하기 때문에 값 복사...
                copied_table = copy.deepcopy(table)
                num = 0
                for j in range(idx, n): # 그 뒤로 퀸이 갈수 있는 자리를 모두 체크
                    copied_table[i][j] = False
                    if i+num < n:
                        copied_table[i+num][j] = False
                    if i-num >= 0:
                        copied_table[i-num][j] = False
                    num += 1
                # pprint(copied_table)
                dfs(copied_table, idx+1)


    dfs([[True]*n for _ in range(n)], 0)
    print(result[0])



solution(8)



