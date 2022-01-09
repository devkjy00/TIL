# 정수 n를 3, 2로 나누어떨어지면 나누고 아니면 1을 뺀다
# 1이 되는 최소횟수
import sys
n = int(sys.stdin.readline().rstrip())
d = [0] * (n+1)


for i in range(2, n+1):
    d[i] = d[i-1]+1
    if i%2==0:
        d[i] = min(d[i], d[i//2]+1)

    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
print(d[n])
