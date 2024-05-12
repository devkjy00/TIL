'''
https://www.acmicpc.net/problem/1966

중요도에 따른 인쇄순서

'''
import collections, sys
input = sys.stdin.readline
for _ in range(int(input())):
    length, order = map(int, input().split())
    print_que = [(val, idx) for idx, val in enumerate(map(int, input().split()))]
    print_que = collections.deque(print_que)


    print(print_que[order][1])




