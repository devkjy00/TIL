# 높이 H를 각 떡의 길이에서 뺀 나머지들의 합(M)을 원하는 값으로 만들기 위한 높이 H를 구해야한다

# n, m = map(int, input().split())
# dduk = map(int, input().split())
n, m = 4, 6
dduk = [19, 15, 10, 17]

h = max(dduk)

while True:
    h -= 1
    cutted = 0
    for i in dduk:
        cutted += i - h if i > h else 0

    if cutted >= m:
        break
print(h)








# 답안 예다
# 파라메트릭 서치유형의 문제(최적화 문제를 결정 문제로 바꾸어서 해결)
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문다
# 예 : 범위 내에서 조건을 만족하는 가장 큰값을 찾으라는 최적화 문제는 이진 참색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있다
# 가장 긴 떡의 길이를 리스트길이로 보고 이진 탐색을 했다

start = 0
end = max(dduk)

result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in dduk:
        total += i - mid if i > mid else 0
    
    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)