'''
388p

[0][0] 부터 [n-1][n-1]까지 가는 최단 경로

:param n: 3
:param t:   [5, 5, 4],
            [3, 9, 1],
            [3, 2, 7]

:return: 20
'''
import heapq
from pprint import pprint


def solution(n, t):
    q = []
    distance = [[1e9]*n for _ in range(n)]
    distance[0][0] = t[0][0]

    visited = [[False]*n for _ in range(n)]
    direction = (-1, 0), (0, 1), (1, 0), (0, -1)

    heapq.heappush(q, (t[0][0], 0, 0))

    while q:
        *_, x, y = heapq.heappop(q)

        if visited[x][y]:
            continue
        else:
            visited[x][y] = True

        for dir_x, dir_y in direction:

            temp_x = x + dir_x
            temp_y = y + dir_y

            if (0 <= temp_x < n and 0 <= temp_y < n
                and distance[x][y] + t[temp_x][temp_y]
                    < distance[temp_x][temp_y]) : # 배열 범위 확인, 짧은 거리 넣기

                distance[temp_x][temp_y] = distance[x][y] + t[temp_x][temp_y]
                heapq.heappush(q, (distance[temp_x][temp_y], temp_x, temp_y))


        print(x, y)
        [print(i) for i in distance]
        [print(i) for i in visited]

        if x == n-1 and y == n-1:
            break









solution(3, [[5, 5, 4],
            [3, 9, 1],
            [3, 2, 7]]
)

solution(7, [[9, 0, 5, 1, 1, 5, 3],
             [4, 1, 2, 1, 6, 5, 3],
             [0, 7, 6, 1, 6, 8, 5],
             [1, 1, 7, 8, 3, 2, 3],
             [9, 4, 0, 7, 6, 4, 1],
             [5, 8, 3, 2, 4, 8, 3],
             [7, 4, 8, 4, 8, 3, 4]]
         )