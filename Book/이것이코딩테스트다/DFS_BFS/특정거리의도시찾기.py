# 1~N의 도시, M개의 단방향 도로
# 도로의 거리는 1
# 도시 X로 부터 출발
# 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램
# 없으면-1을 출력

n, m, k, x = 4, 4, 1, 1 
roads = [1, 2], [1, 3], [2, 3], [2, 4] 

min_way = [1e9] * (n+1)
linked_city = [[] for _ in range(n+1)]
for a, b in roads:
    linked_city[a].append(b)

q = []
q.append((linked_city[x], x))
min_way[x] = 0

while q:
    linked_way, pre_city = q.pop()
    for i in linked_way:
        min_way[i] = min(min_way[i], min_way[pre_city]+1) 
        q.append((linked_city[i], i))

if k in min_way:
    [print(i) for i in range(1, n+1) if min_way[i] == k]
else:
    print(-1)
