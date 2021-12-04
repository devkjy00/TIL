# 리스트의 반을 선택할 때 중복되지 않은 숫자를 가장많이 갖는 갯수
nums = [3, 3, 3, 2, 2, 4]

if (max := len(set(nums))) < (rimit := len(nums) / 2):
    print(max)
else:
    print(rimit)

# min(max, rimit)으로 더 간단하게 표현할 수 있다
