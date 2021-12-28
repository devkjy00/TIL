import time

# N이 1 이 될 때까지 반복
# 1을 빼거나 K로 떨어지는 경우 나누는 최소의 횟수
start_time: float = time.time()

n, k = map(int, input().split())
result = (n % k)
while n != 1:
    n = int(n/k)
    result += 1
    if n < k:
        result += n-1
        break
    else:
        result += (n % k)
        n -= (n % k)
    print(n)
print(result)

end_time: float = time.time()
print(f"time: {end_time - start_time:.5f}")

# 답안 예시
# 내 답안과 거의 동일 하다고 보여진다


