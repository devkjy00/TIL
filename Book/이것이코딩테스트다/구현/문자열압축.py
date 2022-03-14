"""
반복되는 문자열을 압축
aaabb -> 3a2b
abab -> 2ab
문자열을 분리할수 있는 모든 경우중 가장 짧은 경우 찾기
"""

st = "aaaabbabbabb" 
answer = len(st)

for step in range(1, len(st)//2+1): 
    # 3//2=1 -> 1*2=2 -> 오류, 3//2+1=2 -> 2*2=4 -> OK
    compressed = ""
    prev = st[0:step]
    count = 1

    for j in range(step, len(st), step):
        # n길이 만큼 문자열참조후 n만큼 인덱스 증가 -> 문자열전체를 겹치지않게 참조
        # 이전 문자와 비교 
        if prev == st[j:j+step]:
            count += 1  
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = st[j:j+step]
            count = 1
        
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))
print(answer)