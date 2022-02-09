# 움직이는 뱀, 길이는 1
# 사과를 먹으면 길어진다
# 벽, 자기자신 에 부딪히면 게임 끝
# N * N 정사각 보드, 끝에는 벽
# 맨 위 맨 좌측에서 시작, 오른쪽으로 이동, 매초 이동 
# 1. 몸 길이를 늘려 머리를 다음칸에 위치
# 2. 사과가 있으면 꼬리를 그대로 둔다
# 3. 사과가 없으면 꼬리가 위치한칸을 비운다

# 사과의 위치와 뱀의 이동경로가 주어질 때 몇초에 끝나는지 반환

# 보드의 크기 (2 <= N <= 100)
# 사과의 개수 (0 <= K <= 100)
# 사과의 위치 (행, 열)
# 뱀의 방향 전환 횟수(1 <= L <= 100)
# 뱀의 방향 전환(X초 후에 C방향(L,D)으로 회전)

from collections import deque

n = 10
k = 5
apple = [1, 5], [1, 3], [1, 2], [1, 6], [1, 7]
l = 4
move = [8, "D"], [10, "D"], [11, "D"], [13, "L"]

# 보드 초기화, 사과의 위치를 1로표시
board = [[0] * (n+1) for _ in range(n+1)]
for x, y in apple:
    board[x][y] = 1

# 움직임 연산
move_x_y = (0, 1), (1, 0), (0, -1), (-1, 0)
direction = 0
# 방향전환을 시간을 각 행동의 인터벌로 변환
for i in range(l-1, 0, -1):
    move[i][0] -= move[i-1][0]

# 뱀을 que를 사용해서 표현
q = deque()
q.append((1, 1))
# 머리 위치
head_x = 1
head_y = 1
# 뱀을 2로 표기
board[1][1] = 2
# 살아있는 시간
alive_time = 0 
# 종료상태
game_over = False

for i, way in move:
    for _ in range(i):
        head_x += move_x_y[direction][0]
        head_y += move_x_y[direction][1]

        if 1 <= head_x <= n and 1 <= head_y <= n:
            if board[head_x][head_y] != 2:  
                if board[head_x][head_y] != 1:
                    tail_x, tail_y = q.popleft()
                    board[tail_x][tail_y] = 0

                board[head_x][head_y] = 2
                q.append((head_x, head_y))
                alive_time += 1
            else:
                game_over = True
                break
        else:
            game_over = True
            break

        # for _ in range(i)

    if game_over:
        break

    direction += 1 if way == "D" else 3 
    direction %= 4

print(alive_time+1)

