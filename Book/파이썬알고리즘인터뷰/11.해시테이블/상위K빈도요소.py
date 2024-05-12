'''
https://leetcode.com/problems/top-k-frequent-elements/

상위 K번 이상 등장하는 요소를 추출하라

:param nums: [1, 1, 1, 2, 2, 3]
:param k: 2
:return: [1, 2]
'''
import collections
import heapq


def solution(nums, k):
    table = sorted(
        [(k, v) for k, v in collections.Counter(nums).items()]
        , key=lambda element: element[1], reverse=True)

    return [table[i][0] for i, _ in enumerate(range(k))]


def answer_heap(nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []

    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk

def answer_pythonic(nums, k):
    '''
    zip함수와 언패킹의 조화....
    -> [k, v]를 [k, k..], [v, v..]
    '''
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


print(answer_pythonic([1, 1, 1, 2, 2, 3], 2))

