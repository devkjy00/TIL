# 1. 거리, 방문 리스트 생성
# 2. 시작노드에서 연결된 모든 간선의 가중치를 거리리스트에 입력
# 3. 가장 가중치가 적은(가까운) 노드부터 방문
# 4. 방문처리후 노드와 연결된 모든 간선의 가중치를 계산해서 더 가까운 거리를 입력
# 5. 모든 노드를 방문할 때 까지 반복

# 간단한 다익스트라 알고리즘
import sys
input = sys.stdin.readline

INF = int(1e9)


n, m    = 4, 7
start   = 1   # 시작노드
graph   = [], [(2, 2), (3, 4), (4, 6)], [(4, 4), (3, 1)], [(2, 1)], [(2, 4)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 연결된 간선중 가중치가 가장 낮은 간선의 인덱스 반환
# def get_smallest_node():

#     min_value = INF
#     index = 0
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
    
#     return index

# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for i in graph[start]:
#         distance[i[0]] = i[1]
    
#     for i in range(n - 1):
#         now = get_smallest_node()
#         print("now = ", now)
#         visited[now] = True

#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost

# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
    
#     else:
#         print(distance[i])


# 개선된 다익스트라 (우선순위 큐)
# 우선순위 큐에 값이 없을 때까지 동작하기때문에 방문값은 필요없다
import heapq

def di(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

   

di(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])