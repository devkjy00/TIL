# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 경우의 수
import sys
n = int(sys.stdin.readline().rstrip())

d = [0] * (n+3)

d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n]%10007)
