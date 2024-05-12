
# 이동할 수 있는 위치의 인덱스를 도달해야하는 인덱스에서 빼보고 
# 가장 적은 값이 나오는 위치(최단 경로)로 이동
# 이동마다 카운트하기..
n, m = map(int, input().split())
space = [list(input())for _ in range(n)]

# n, m = 5, 6
# space = [['1', '0', '1', '0', '1', '0'],
#         ['1', '1', '1', '1', '1', '1'],
#         ['0', '0', '0', '0', '0', '1'],
#         ['1', '1', '1', '1', '1', '1'],
#         ['1', '1', '1', '1', '1', '1']]


seek = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dfs(x, y, c):
    path = []    

    if x == n-1 and y == m-1:
        return c
        
    for i, j in seek:
        i += x
        j += y
        if (i >= 0 and i <= n-1 and j >= 0 and j <= m-1 
            and space[i][j] == '1'):
                path.append([i, j])
                print(path)
    
    a, b = 0, 0
    for i, j in path:
        if (n - i)+(m - j) < (n - a)+(m - b):
            a = i
            b = j
            print()
    
    c = dfs(a, b, c+1)

    return c

print(dfs(0, 0, 1))

# 답안 예시
# bfs로 구현, while queue:
# 전부 탐색하고 위치마다 가중치를 저장
# 도달해야하는 인덱스의 가중치를 반환

        


