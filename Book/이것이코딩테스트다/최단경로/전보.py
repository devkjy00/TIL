# 
# N개의 도시, 메시지 전송 
# 최대한 많은 도시로 메시지를 전달, 출발 도시에서 모든 간선으로 이동
# 출발 도시에서 모든 도시까지의 가중치중 가장 큰값과 INF가 아닌 거리의 갯수
# 메시지를 받게 될 도시의 개수, 모두 메시지를 받는데 걸리는 시간
import heapq
INF = int(1e9)
n, m, c = 3, 2, 1
info    = (1,2,4), (1,3,2)

graph = [[] for _ in range(n+1)]
for i,j,k in info:
    graph[i].append((j,k))
    
distance = [INF] * (n+1)
q = []

def di(start):

    for i, j in graph[start]:
        distance[i] = j
        heapq.heappush(q, (i,j))
    distance[start] = 0

    while(q):
        city, dis = heapq.heappop(q)

        if distance[city] < dist:
            continue
        
        for i,j in graph[city]:
            if (distance[i] > dis+j):
                distance[i] = dis+j
                heapq.heappush(q, (i, dis+j))
        
di(c)

count = 0
max_time = 0
for i in distance[1:]:
    if (i < INF and i > 0):
        count += 1
        max_time = max(max_time, i)
    
print(count, max_time)
    
            






   
