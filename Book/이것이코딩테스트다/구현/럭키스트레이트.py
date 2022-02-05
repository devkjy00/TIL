# 정수 N
# 자릿수를 기준으로 N을 반으로 나누어 
# 왼쪽 부분의 각 자릿수의 합과 
# 오른쪽 부분의 각 자릿수의 합이 같으면 
# LUCKY출력 아니면 READY
import time

n = "7575"

start = time.time()

idx = len(n)//2

front_num = sum(map(int, n[:idx]))
back_num = sum(map(int, n[idx:]))

if front_num == back_num:
    print("LUCKY")
else:
    print("READY")

end = time.time()
print(f"{end-start:.5f} sec")

# 답안
# 더 빠르다
start = time.time()
length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length//2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else: 
    print("READY")
end = time.time()
print(f"{end-start:.5f} sec")