# 0번 부터  N번까지의 번호
# N+1 개의 팀이 존재한다 

# n, m = map(int, input().split())

from logging import root


def find_root(root_table, x):
    if root_table[x] != x:
        root_table[x] = find_root(root_table, root_table[x])
    return root_table[x]

def union_root(root_table, x, y):
    x = find_root(root_table,x)
    y = find_root(root_table,y)
    if x > y:
        root_table[x] = y
    else:
        root_table[y] = x
    
n, m = 7,8

team = (0, 1, 3), (1, 1, 7), (0, 7, 6), (1, 7, 1), (0, 3, 7), (0, 4, 2), (0, 1, 1), (1, 1, 1)
root_table = [i for i in range(m)]


for type, a, b in team:
    if type == 0:
        union_root(root_table, a, b)
    elif type == 1:
        if find_root(root_table, a) == find_root(root_table, b):
            print("YES")
        else:
            print("NO")
        

    

