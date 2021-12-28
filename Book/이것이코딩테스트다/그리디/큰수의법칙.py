'''
문제풀이 
- 반복되는 수열에 대해서 파악해야 한다 -> {6,6,6,5}가 반복
- 반복되는 수열의 길이 -> (k+1)
- m // (k+1) 이 반복 횟수가 된다
- 반복횟수에 k를 곱하면 다시 가장 큰수가 등장하는 횟수가 된다
- m이 딱 떨어지지 않으면 나머지 만큼 큰수를 추가로 더해준다
- 그래서 int(M/(k+1)) * K + M % (K+1) dl 가장 큰수를 더하는 횟수가 된다

반복되는 수열을 반복하지 않고 한번에 연산하는 것
- 반복되는 값 파악
- 반복 횟수, 그외의 경우등을 파악
'''






# 첫 풀이
# 1. 가장 큰수를 K번 더하고 M-K 하기
# 가장 큰 수가 몇번 중복되는지 체크하고 더 더하기
# 2. 가장 큰 수를 배열에서 빼고 그 다음 큰수를 더하고 M-k 반복
import time

start_time: float = time.time()
n, m, k = 5, 1000000, 3
num_list = [2, 4, 5, 4, 6]

max_num = 0
temp1 = max(num_list)
if num_list.count(temp1) > 1:
    max_num = temp1 * m
    m = 0
num_list.remove(temp1)
temp2 = max(num_list)
while m:
    max_num += temp1 * k
    m -= k
    if m < k:
        k = m
    if m >= 1:
        max_num += temp2
        m -= 1
print(max_num)

end_time: float = time.time()

print(f"time: {end_time - start_time:.5f}")




# 책에 나온 답안 예시

start_time: float = time.time()

n, m, k = 5, 1000000, 3
num_list = [2, 4, 5, 4, 6]

num_list.sort()
first = num_list[n - 1]
second = num_list[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/ (k+1)) * k
count += m % (k - 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m-count) * second # 두번째 큰 수 더하기

print(result)

end_time: float = time.time()

print(f"time: {end_time - start_time:.5f}")




