n = int(input())

x = n//3

for i in range(x+1):
    temp = n
    result = i
    temp -= 3*i
    if temp % 5 == 0:
        result += temp//5 
        break
    if temp:
        result = -1
print(result)
