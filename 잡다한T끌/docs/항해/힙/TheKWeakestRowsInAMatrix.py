'''
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/


:param mat: [[1,1,0,0,0],
             [1,1,1,1,0],
             [1,0,0,0,0],
             [1,1,0,0,0],
             [1,1,1,1,1]]

:param k: 3

:return: [2, 0, 3]

'''
import heapq


def solution(mat, k):
     '''
     값을 더한다 -> 정렬해서 k만큼만 인덱스를 출력한다
     '''
     heap = []
     for idx, element in enumerate(mat):
          heapq.heappush(heap, (sum(element), idx))

     return [heapq.heappop(heap)[1] for _ in range(k)]



print(solution([[1,1,0,0,0],
             [1,1,1,1,0],
             [1,0,0,0,0],
             [1,1,0,0,0],
             [1,1,1,1,1]], 3))