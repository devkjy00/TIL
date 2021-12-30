

x, y = list(input())

x, y = ord(x), int(y)
pattern = [2, -1], [2, 1], [-2, -1], [-2, 1], [1, -2], [1, 2], [-1, -2], [-1, 2]
count = 0

for i, j in pattern:
    if 97 <= x + i <= 104 and 1 <= y + j <= 8:
        count += 1

print(count)


# 답안 예시
# 같은 방법이지만 좀더 명시적으로 썻다


