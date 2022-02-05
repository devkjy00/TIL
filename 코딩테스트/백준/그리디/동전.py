# n, money = map(int, input().split())
# coins = [int(input()) for _ in range(n)]

n, money = 10, 1
coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

coins.sort(reverse=True)

count = 0
for coin in coins:
    if money < coin:
        continue
    
    count += money//coin
    money %= coin
print(count)
    





