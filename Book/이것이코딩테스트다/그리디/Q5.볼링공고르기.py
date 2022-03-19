"""
사람 A, B 서로다른 무게의 볼링공을 고른다
N개의 볼링공, 볼링공의 무게 1~M 
같은 무게의 공도 다른 공으로 간주
두 사람 A, B가 공을 고르는 경우의 수 구하기

-> 서로 다른 무게 선택 -> 동시 선택가능 경우의 수 = 공 개수 - 무게가 같은 공 개수
-> 같은 무게의 공이 여러개 -> 특정 무게에서 경우의 수 = 같은 무게의 공 개수 * 다른 무게의 공 개수
:param N : 8
:param M : 5
:param ball : [1, 5, 4, 3, 2, 4, 5, 2]  
:return : 25
"""

n, m = 8, 5
ball = [1, 5, 4, 3, 2, 4, 5, 2] 

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in ball:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)

