INF = int(1e9)
n, m = 4, 7
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

info = (1,2,4), (1,4,6), (2,1,3), (2,3,7), (3,1,5), (3,4,4), (4,3,2)
for a, b, c in info:
    graph[a][b] = c

for k in range(1, n+1):             # 지나가는 노드 K 일때
    for a in range(1, n+1):         # 시작노드 a
        for b in range(1, n+1):     # 끝노드 b
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for line in graph[1:]:
    for num in line[1:]:
        if num == INF:
            print("INFINITY", end=" ")
        else: 
            print(num, end=" ")
    print()