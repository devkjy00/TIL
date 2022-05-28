# 부품 N개, 각 부품에는 고유한 번호
# M개 종류의 부품을 구매
# M개 종류의 부품이 모두 있는지 확인
import bisect

n = 5
component = [8, 3, 7, 9, 2]

m = 3
buy = [5, 7, 9]


def solution(component, buy):
    component.sort()
    for i in buy:
        result = bisect.bisect_left(component, i)
        if component[result] == i:
            print("yes")
        else:
            print("no")



solution(component, buy)
