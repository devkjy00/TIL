# N개의 음식, 1부터 N까지의 음식번호
# 음식 섭취 1초 후 다음음식 먹기
# 회전판은 번호가 증가하는 순서대로 음식을 제공
# 각 음식을 모두 먹는데 필요한 시간 food_times
# k초에 몇번 음식을 먹을 지 반환, 없으면 -1반환

# 효율성이 중요한 문제는 순서대로 하나씩 연산하면 안된다
# 규칙성을 찾아서 동일한 연산을 한번에 처리해야 요구되는 성능을 얻을수 있다
import time

def my_solution(food_times, k):

    return

# 답안
# 음식 시간을 빼서 실제로 구현하지 않고 순서만 찾았다
# 규칙을 찾아서 한번에 연산처리
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

start = time.time()
for i in range(100000):
    solution([8, 6, 4,5,7,8,6,45,3,4,5,67,8,3,1], 73)
end = time.time()
print(f"{end-start:.5f}")