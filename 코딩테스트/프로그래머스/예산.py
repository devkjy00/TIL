d = [1, 3, 2, 5, 4]
budget = 9
a = 0
d.sort()
for idx, num in enumerate(d):
    a += num
    print(num)
    if a > 9:
        print(idx)
        break
