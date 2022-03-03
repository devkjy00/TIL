'''
N명의 모험가
공포도 X이면 X명이상과 동행해야 한다
만들수 있는 그룹의 최대값 
모든 모험가가 떠날 필요는 없음

->공포도가 제일 낮은 순서로 그룹분할
'''
import heapq

n = 5
fear = [2, 3, 1, 2, 2, 5, 3, 2, 3 ,5, 4, 6, 5, 7, 4, 5]
q = []

def solution():
    for i in fear:
        heapq.heappush(q, i)

    group = []
    person = 0
    print("N :",  fear)
    while q:
        limit = heapq.heappop(q)
        group.append(limit)  
        if len(group) == limit:
            print(group)
            group.clear()
            
        
