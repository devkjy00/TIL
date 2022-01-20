# d(51) = 51 + 5 + 1 = 57
# 57의 생성자는 51
# 생성자가 없는 수는 셀프넘버라고 한다
# 10000까지의셀프넘버 구하기

def d(num: int)->int:
    result = num
    x = 0

    len_num = len(str(num))

    for _ in range(len_num):
        x = num%10
        num //= 10
        result += x

    return result

n = 10000

self_num = [True] * (n+1)
self_num[0] = False

for i in range(1, n):
    if (idx := d(i)) > n:
        break
    self_num[idx] = False

for idx, b in enumerate(self_num):
    if b:
        print(idx)

