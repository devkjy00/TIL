'''
https://leetcode.com/problems/reconstruct-itinerary/

[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라
여러 일정이 있는 경우 사전 어휘 순으로 방문한다

:param tickets: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
:return: ["JFK", "MUC", "LHR", "SFO", "SJC"]
'''
import collections


def solution(tickets):
    '''
    사전순으로 선택해야 하기 때문에 미리 정렬하고 시작
    참조값이 아니라 재귀함수의 각 메모리
    스택마다 다른 메모리를 사용해야만 제대로된 반환값을 만든다
        -> return dfs() -> 경로를 한가지 경우만 찾는 오류
        -> append(dfs())로 수정 -> for문이 돌때마다 append된다
        -> if not tickets 에서 return 대신 append 사용
    '''
    tickets.sort()
    trevel_line = []

    def dfs(result, tickets):
        if not tickets: # tickets를 모두 사용했다면 일정이 다이어진것
            trevel_line.append(result)
            return
        for idx, ticket in enumerate(tickets):
            if ticket[0] == result[-1]: # 티켓의 출발지와 일정의 마지막 비교
                 # 같으면 티켓의 도착지를 더해서 반환
                dfs(result+[ticket[1]], tickets[:idx]+tickets[idx+1:]) # 확인한 티켓은 뺀다


    dfs(["JFK"], tickets)
    return trevel_line[0]

from pprint import  pprint
def answer(tickets):
    '''
    해쉬 테이블을 사용해서 비교 하지 않고 키 값으로 바로 찾는다 ->  중복된 티켓을 쓸수 없는 건 어떻게 해결?
        -> 사전에 저장된 리스트는 정렬되어 있어서 순서대로 pop(0)하면 된다

    사전순으로 이으면 무조건 이어진다 !? -> 고려하지 못한 부분
    '''
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    pprint(dict(graph))
    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
        print(route)

    dfs('JFK')
    return route[::-1]


print(answer([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
