# N 개의 집을 연결하는 M개의 길, 양방향
# 2개의 마을로 분리, 각 마을의 집들 사이에 항상 경로가 존재
# 분리된 마을 사이에 경로는 삭제 가능
# 경로가 있으면 다른 경로는 삭제 가능
# 최소비용으로 만들기

# 구현
# 1. 먼저 모든 노드를 포함한 최소신장트리를 생성
# 2. 그중에 가중치가 가장 큰 간선을 삭제하면 2개로 나뉘게된다

n, m = 7, 12
load = [1, 2, 3], [1, 3, 2], [3, 2, 1], [2, 5, 2], [3, 4, 4], [7, 3, 6], [5, 1, 5], [1, 6, 2], [6, 4, 1], [6, 5, 3], [4, 5, 3], [6, 7, 4]

    
def find_root(table: list, x: int) -> int:
    if table[x] != x:
        table[x] = find_root(table, table[x])
    return table[x]

def union_root(table: list, a: int, b: int):
    a = find_root(table, a)
    b = find_root(table, b)
    if a > b:
        table[a] = b
    else:
        table[b] = a

parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, cost = load[i]    
    edges.append((cost, a, b))

edges.sort()
last = 0

for cost, a, b in edges:
    
    if find_root(parent, a) != find_root(parent, b):
        union_root(parent, a, b)
        result += cost
        last = cost

print(result - last)