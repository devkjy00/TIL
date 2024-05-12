import time
from collections import deque

# n, m = map(int, input().split())
# ices = [list(map(int, input().split())) for _ in range(n)]
n, m = 4, 4
ice = [[0, 1, 0, 0],
       [1, 0, 1, 0],
       [0, 1, 0, 1],
       [0, 1, 1, 0]]

start_time: float = time.time()

que = deque()
count = 0
for x in range(n):
    for y in range(m):

        print(x, y)
        if ice[x][y] == 0:
            ice[x][y] = 1
            count += 1
            que.append([x, y])
            while True:
                print(que)
                i, j = que.popleft()
                if i + 1 <= n - 1:
                    if ice[i + 1][j] == 0:
                        que.append([i + 1, j])
                        ice[i + 1][j] = 1
                if j + 1 <= m - 1:
                    if ice[i][j + 1] == 0:
                        que.append([i, j + 1])
                        ice[i][j + 1] = 1
                if not que:
                    break

print(count)

end_time: float = time.time()
print(f"time: {end_time - start_time:.5f}")

# 답안 예시
# DFS로 구현했다, 재귀함수로 간결하게

def dfs(x, y):
    # 유효값 범위
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if ice[x][y] == 0:
        ice[x][y] = 1

        # 매개변수 증감 정의
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    # 스택이 끝나면 False 반환
    return False

# 2중 for문으로 함수 호출