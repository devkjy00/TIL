'''
https://www.acmicpc.net/problem/2606

N개의 컴퓨터가 무작위로 서로 연결되어 있다, 바이러스는 연결된 컴퓨터를 모두 감염시킨다
1번 컴퓨터가 감염됬을 때 감염시킨 컴퓨터 수를 구하라



30840 KB, 76ms

'''

















def solution(pc_qty, link):
    '''
    :param pc_qty: 7
    :param link: [1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]
    :return: 4
    '''

    # 감염됬는지, 안됬는지를 확인하기 위해 값을 저장하자
    #   -> bool 리스트를 컴퓨터 개수+1 생성(0번째 컴퓨터는 없다)
    infection_table = [False] * (pc_qty + 1)
    #  0  1  2  3  4  5  6  7 - index
    # [F, F, F, F, F, F, F, F]
















    # 컴퓨터 연결구조를 2차원 리스트로 표현
    #   -> 인덱스를 활용한 구현을 할 수 있게 된다

    # 무방향 그래프
    #   -> 연결된 양쪽에서 서로에게 갈 수 있다
    #   -> 양 쪽 컴퓨터에 모두 연결정보를 넣어준다

    pc_link_table = [[] for _ in range(pc_qty + 1)]
    for i, j in link:
        pc_link_table[i].append(j)
        pc_link_table[j].append(i)

    # link : [1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]
    # pc_link_table[0] : []
    # pc_link_table[1] : [2, 5]
    # pc_link_table[2] : [1, 3, 5]
    # pc_link_table[3] : [2]
    # pc_link_table[4] : [7]
    # pc_link_table[5] : [1, 6, 2]
    # pc_link_table[6] : [5]
    # pc_link_table[7] : [4]













    # DFS(깊이우선탐색)
    #   -> 미로에서 막다른 벽이 나올때까지 일단 달린다
    #   -> 벽이 나오면 왔던 길을 돌아가다가 갈림길이 나오면 안가본 길로 다시 달린다

    # DFS(깊이우선탐색)을 구현하기 위해 재귀함수로 작성
    #   -> 재귀함수는 일단 끝까지 달린다

    def infect(pc_idx):
        infection_table[pc_idx] = True                  # 현재 침투한 컴퓨터를 감염시키고
        for linked_pc_idx in pc_link_table[pc_idx]:     # 연결된 컴퓨터들을 살펴서
            if not infection_table[linked_pc_idx]:      # 감염되지 않았으면
                infect(linked_pc_idx)                   # 바이러스를 전파하겠다...

    infect(1) # 1번 컴퓨터부터 감염

    # infection_table
    #  0  1  2  3  4  5  6  7 - index
    # [F, T, T, T, F, T, T, F]
















    # 감염된 pc의 수를 계산
    #   -> sum으로 True를 센다, 1번 pc는 빼기
    return sum(infection_table)-1
    # 4

















# 값 입력받기
# pc_qty = int(input())
# link = []
# for i in range(int(input())):
#     link.append(list(map(int, input().split())))

print(solution(7, [[1, 2], [1, 5], [2, 3], [4, 7], [5, 6], [5, 2]]))
