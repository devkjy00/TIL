# 최소비용 신장트리 알고리즘.
# 간선의 가중치를 오름차순으로 정렬
# 하나씩 싸이클확인, 없으면 신장트리에 포함
# 완성된 신장트리의 모든 가중치의 합(최소비용)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = 7, 9
# v, e = map(int, input().split())

parent = [0] * (v + 1)

edges = [(29, 1, 2),
        (75, 5, 1),
        (35, 2, 3), 
        (34, 2, 6), 
        (7, 3, 4),
        (23, 4, 6), 
        (13, 4, 7), 
        (53, 5, 6),
        (25, 6, 7)]
result = 0
#for _ in range(e):
#    a, b, cost = map(int, input().split())
#    edges.append((cost, a, b))

for i in range(1, v+1):
    parent[i] = i

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)

   
