# 선수 강의를 먼저 들어야 한다
# 총 N개의 강의, 동시에 여러 강의 수강 가능 
# 각 강의는 시간이 정해져 있다
# N개의 강의 정보, 각 강의를 수강하기 위한 최소시간 구하기

# 1 <= N <= 500
# time, pre_course = 강의시간, 선수강의 번호
from collections import deque 

# n = int(input())
# course_info = map(int, input(),split())
n = 5
course_info = [10, -1], [10, 1, -1], [4, 1, -1], [4, 3, -1], [3, 3, -1]

course_list = [[] for _ in range(n+1)]
# 리스트 형태로 저장
time = [0] * (n+1)
for i in range(1, n+1):
    info = course_info[i-1]
    if info[1] > 0:
        course_list[info[1]].append(i)
    time[i]= info[0]
table = [0] * (n+1)

# 진입차수 테이블 
for i in course_list: 
    for j in i:
        table[j] += 1

q = deque()
for i in range(1, n+1):
    if table[i] == 0: 
        q.append(i)

di = [0] * (n+1)
while q:
    i = q.popleft()
    di[i] += time[i] 

    for j in course_list[i]:
        di[j] += di[i]
        table[j] -= 1
        if table[j] == 0:
            q.append(j)
    
print(di)


# 답안
# 진입차수가 복수인 경우를 고려했다

from collections import deque
import copy


v = 5
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

course_info = [10, -1], [10, 1, -1], [4, 1, -1], [4, 3, -1], [3, 3, -1]
for i in range(1, v+1):
    time[i] = course_info[i-1][0]
    for x in course_info[i-1][1:-1]:
        indegree[i] += 1
        graph[x].append(i)
    
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            # 진입차수가 복수인 경우를 고려
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()



