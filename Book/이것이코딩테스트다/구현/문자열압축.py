# 반복되는 문자열을 압축
# aaabb -> 3a2b
# abab -> 2ab
# 문자열을 분리할수 있는 모든 경우중 가장 짧은 경우 찾기

s = "aaaabbabbabb" 
answer = len(s)

for step in range(1, len(s)//2+1):
    compressed = ""
    prev = s[0:step]
    count = 1

    for j in range(step, len(s), step):
        if prev == s[j:j+step]:
            count += 1  
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j:j+step]
            count = 1
        
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))
print(answer)