# 부품 N개, 각 부품에는 고유한 번호
# M개 종류의 부품을 구매
# M개 종류의 부품이 모두 있는지 확인

n = 5
component = [3, 5, 4, 2, 1]

m = 3
buy = [5, 4, 1]

component.sort()

# 이진 탐색
for i in buy:
    print(i)
    end = len(component)-1
    start = 0
    while start <= end:
        mid = (start + end)//2
        print("start", start, "mid", mid, "end", end)
        if component[mid] == i:
            print(i,"찾았다")
            break
        elif component[mid] < i:
            start = mid + 1
        else:
            end = mid - 1





