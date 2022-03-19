"""
0~1로만 이루어진 문자열 S 모든 숫자가 같도록 만들기
1. 전체를 뒤집는다
2. 인접한 같은 숫자만 뒤집는다
둘 다 1회로 계산, 최소횟수를 출력

-> '1', '0'를 구분자로 사용해서 더 짧은 리스트의 길이가 최소횟수
:param : "0001100"
:print : 1

"""
s = "0001100"

part_0 = [i for i in s.split("1") if i]
part_1 = [i for i in s.split("0") if i]

print(min(len(part_0), len(part_1)))
