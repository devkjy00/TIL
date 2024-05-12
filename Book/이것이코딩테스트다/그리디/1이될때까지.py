"""
N이 1 이 될 때까지 반복
1을 빼거나 K로 떨어지는 경우 나누는 최소의 횟수
"""

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




