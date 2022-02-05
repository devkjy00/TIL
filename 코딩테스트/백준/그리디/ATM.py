# ATM 앞에 N명의 사람이 줄을 서있다
# 각 사람마다 특정 시간(값)을 사용
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값

n = 5
time = [3, 1, 4, 3, 2]
# n = int(input())
# time = list(map(int, input().split()))

time.sort()
num = 0
result = []  

for x in time:
    num += x 
    result.append(num)

print(sum(result))

# 정렬해서 순서대로 더하기