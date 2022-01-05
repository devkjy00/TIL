# N개의 원소로 구성된 배열 A, B
# 최대 K번 바꿔치기 연산을 수행해서 A의 원소의 합이 최대가 되도록 한다

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split())) 

a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))
