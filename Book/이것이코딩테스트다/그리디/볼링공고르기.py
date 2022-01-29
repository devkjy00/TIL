# 사람 A, B 서로다른 무게의 볼링공을 고른다
# N개의 볼링공, 무게가 적혀있다
# 볼링공의 무게 1~M 
# 두 사람 A, B가 공을 고르는 경우의 수 구하기
from collections import deque
import time

n, m = 8, 5
data = [1, 5, 4, 3, 2, 4, 5, 2] 

start = time.time()
ball_kg = deque(data)

result = 0 
 
for _ in range(n):
    kg = ball_kg.pop()
    case = len(ball_kg) - ball_kg.count(kg)  
    result += case


print(result)
end = time.time()
print(f"{end - start:.8f} sec")

# 답안
# 더 빠르다

start = time.time()
# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)
end = time.time()
print(f"{end - start:.8f} sec")

