# 알파벳 대문자와 숫자로만 구성된 문자열
# 알파벳을 오름차순으로 정렬하고 그뒤에 모든 숫자를 합한 값을 출력


st = "K1KA5CB7"
s_list = []
num = 0

for s in st:
    if s.isdigit():
        num += int(s)
    else:
        s_list.append(s)
        
s_list.sort()

print("".join(s_list)+str(num))