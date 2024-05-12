# 방문 판매원 A(1번회사에 위치), 1~N까지의 회사, 일부회사끼리 연결(가중치1), K번 회사 방문후 X번 회사 방문 가장 빠른 이동, X번 회사에 도달할 수 없으면 -1
from ctypes.wintypes import HWINSTA
import heapq

INF = int(1e9)

n, m, x, k = 5, 7, 4, 5
road = (1,2),(1,3),(1,4),(2,4),(3,4),(3,5),(4,5)



# 1 부터 K, K부터 X 최단거리 같은 알고리즘
# K 부터 X를 먼저 구해서 길이 없으면 -1 반환
def di(start, end):
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n + 1)
    start = 1
    q = []

    for i,j in road:
        graph[i].append((j,1))
        
    distance[start] = 0
    for node, dis in graph[start]:
        distance[node] = dis
        heapq.heappush(q, (node, dis)) 
        

    while q:
        node, dis = heapq.heappop(q)

        for i,j in graph[node]:
            if (distance[i] > dis+j):
                distance[i] = dis+j
                heapq.heappush(q, (i,j))
                
    return distance[end] 



if (di(1, k) + di(k, x) >= INF):
    print(-1)
else:
    print(di(1, k) + di(k, x)) # 3


n, m, x, k = 4, 2, 3, 4
road = (1, 3), (2, 4) 

if (di(1, k) + di(k, x) >= INF):
    print(-1)                   # -1
else:
    print(di(1, k) + di(k, x))