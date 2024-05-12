'''
386p

n명의 성적을 분실
n명의 성적을 비교한 결과만 가지고 있다
비교한 결과를 가지고 순위를 정하라



플로이드 워셜로 특정 노드가 모든 노드와 연결 가능하면 순위를 정할 수 있다
'''

n, m = 6, 6
INF = int(1e9)
datas = [[1, 5],
         [3, 4],
         [4, 2],
         [4, 6],
         [5, 2],
         [5, 4]]

dist = [[INF] * (n + 1) for _ in range(n + 1)]

for idx in range(1, n + 1):
    dist[idx][idx] = 0

for a, b in datas:
    dist[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

result = 0
for cur in range(1, n + 1):
    cnt = 0
    # 현재 노드(cur)를 기준으로,
    # 다른 노드(node)로 갈 방법이 있는지 센다.
    for node in range(1, n + 1):
        if dist[cur][node] != INF or dist[node][cur] != INF:
            cnt += 1
    # 모든 노드에 대해 갈 수 있다면 순위를 아는 것.
    if cnt == n:
        result += 1
print(result)

