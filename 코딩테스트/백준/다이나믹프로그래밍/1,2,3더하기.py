# 정수 n을 1,2,3 의 합으로 나타내는 경우의 수
# d[i] = d[i-1]+d[i-2]+d[i-3]
import sys

x = int(sys.stdin.readline().rstrip())
case_t = [int(sys.stdin.readline().rstrip()) for _ in range(x)]
n = max(case_t)

d = [0] * (n+3)

d[0] = 1
d[1] = 1
d[2] = 2 

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]+d[i-3]

for i in case_t:
    print(d[i])


