import time

# 각 행들의 가장 작은 수 중에서 가장 높은 수 뽑기
start_time: float = time.time()

x, y = [2, 4]
_list = [7, 3, 1, 8], [3, 3, 3, 4]
temp = 0
for i in _list:
    if (num := min(i)) > temp:
        temp = num

print(temp)

end_time: float = time.time()

print(f"time: {end_time - start_time:.5f}")

# 답안 예시

start_time: float = time.time()

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))  # 입력 받고 바로 처리
    min_value = min(data)
    result = max(result, min_value)  # max(x, y)로 값을 비교 할 수 있다

print(result)
end_time: float = time.time()
print(f"time: {end_time - start_time:.5f}")
