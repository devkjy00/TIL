'''
390p

1~N 번 헛간에 숨는다, 술래는 1번부터 출발
M개의 양방향 통로가 헛간을 연결

1번 헛간에서 최단 거리가 가장 먼 헛간을 찾아라(가중치 없이 간선만 존재)

'''
import heapq

n, m = 6, 7
link = [3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]

graph = [[] for _ in range(n + 1)]
distance = [1e9] * (n + 1)
distance[0] = distance[1] = 0

visited = [[False] for _ in range(n + 1)]

for i, j in link:
    graph[i].append(j)
    graph[j].append(i)

q = []
heapq.heappush(q, (distance[1], 1))

while q:
    num, idx = heapq.heappop(q)

    if visited[idx] == True:
        continue
    visited[idx] = True

    for i in graph[idx]:
        if distance[i] > num + 1:
            distance[i] = num + 1
            heapq.heappush(q, (distance[i], i))




max_num = max(distance)
result_idx = distance.index(max_num)
result_count = distance.count(max_num)
print(result_idx, max_num, result_count)




