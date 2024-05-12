# n가지 화폐, 개수를 최소한으로 이용
# 사용개수에 제한 없음, 순서가 상관없음
# 떨어지지 않을 때 -1 반환

n, m = 3, 97 
coin = [2, 3, 5]

# n, m = map(int, input().split())
# coin = list(map(int,input().split()))

coin.sort()
d = [10001] * (m+1) 
d[0] = 0

for k in coin:
    for i in range(k, m+1):
        print(f"d[{i}] = min(d[{i}], d[{i}-{k}]+1)")
        d[i] = min(d[i], d[i-k]+1 ) 
        print("------>", d[i])
print(d[m])

# 이전의 값들을 사용
