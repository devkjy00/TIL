import time, sys, string
from pprint import pprint



start = time.time()

#코드#

import sys
# com_len = int(sys.stdin.readline()[:-1])
# node_len = int(sys.stdin.readline()[:-1])
# inputs = [list(map(int,(sys.stdin.readline()[:-1]).split(" "))) for _ in range(node_len)]
com_len = 7
inputs = [1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]

from collections import defaultdict as dfd
input_dict = dfd(list)
for i in inputs:
    input_dict[i[0]] += [i[1]]
    input_dict[i[1]] += [i[0]]

print(input_dict)

def dfs(cur,list_gam):
    if cur in list_gam:
        return

    list_gam.append(cur)
    for i in input_dict[cur]:
        dfs(i,list_gam)

gam_com = []
dfs(1,gam_com)

print(gam_com)

print(len(gam_com)-1)
#####

print("실행 시간 : {0:.6f}".format(time.time()-start) )