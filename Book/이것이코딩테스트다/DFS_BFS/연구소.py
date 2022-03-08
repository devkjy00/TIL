"""
N*M의 직사각형
0과 1그리고 2로 이루어진 행렬
2와 인접한 0은 모두 2를 값으로 가지게 된다
값이 0인 자리 3개를 1로 바꿔서 
2로 변하는 0의 개수를 최소한으로 만들어라

-> 완전탐색을 해서 조건에 맞는 상황에 재귀함수를 호출
재귀함수 흐름제어에 대한 깊은 이해
"""
n, m = 7, 7
data = [[2,0,0,0,1,1,0],
            [0,0,1,0,1,2,0],
            [0,1,1,0,1,0,0],
            [0,1,0,0,0,0,0],
            [0,0,0,0,0,1,1],
            [0,1,0,0,0,0,0],
            [0,1,0,0,0,0,0]]
temp = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
        
# 깊이우선탐색, 재귀함수로 2와 인접한 0 모두 2로 만들기
def virus(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 0의 개수를 세는 메서드
def get_score():
    count = 0
    for line in temp:
        count += line.count(0)
    return count

# 깊이우선 탐색을 이용해서 울타리 설치후 안전영역 계산
def dfs(count):
    global result
    
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())        
        return


    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                # 특정조건을 만들어서 함수를 
                # 호출하고 다시 그전으로 복구
                data[i][j] = 0
                count -= 1