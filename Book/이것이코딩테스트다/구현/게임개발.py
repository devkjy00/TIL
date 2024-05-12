import time

column, row = map(int, input().split())
x, y, way = map(int, input().split())
land = [input().split() for _ in range(column)]

start_time: float = time.time()

move = [-1, 0], [0, -1], [1, 0], [0, 1]
no_way = 0
land[x][y] = '2'
count = 1

while True:
    way = (way + 1) % 4
    i, j = move[way]
    if 0 <= x+i < column and 0 <= y+j < row:
        if land[x+i][y+j] == '0':
            x += i
            y += j
            land[x][y] = '2'
            no_way = 0
            count += 1
            print(f'이동, land[{x}][{y}]를 2로 표시')

        else:
            no_way += 1
            print(f'land[{x+i}][{y+j}]는 바다이거나 가본 지역')
    else:
        no_way += 1
        print(f'land[{x+i}][{y+j}]는 지도밖')
    if no_way == 4:
        i, j = move[(way+2) % 4]
        if 0 <= x + i < column and 0 <= y + j < row and land[x + i][y + j] == '2':
            x += i
            y += j
            no_way = 0
            print("뒤로한칸")
        else:
            break
for i in land:
    print(i)
print(count)

end_time: float = time.time()
print(f"time: {end_time - start_time:.5f}")

# 답안 예시
# 비슷한 방법, 문제를 더 정확하게 읽고 파악하자
