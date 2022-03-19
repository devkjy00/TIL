"""
0~9로 이루어진 문자열 S
숫자 사이에 x, + 연산자를 대입해서 가장 큰 수를 구하는 프로그램
모든 연산은 왼쪽부터 순서대로

-> 피연산자중 하나라도 1이하이면 더하기, 두 수가 모두 2이상인 경우는 곱하기
:param : "02984"
:return: 576
"""


s = "567"

def mySolution(st: str):
    # result = 0
    result = int(str[0]) # 1-1. 첫번째 수를 대입
    # for s in st:
    for s in st[1:]: # 1-2. 첫번째 수는 건너뛰기
        s = int(s)
        # if result==0: -> 1. 조건문보다 초기값 대입
        #     result = s
        #     continue
        if result>1 and s>1:
            result *= s
        else:
            result += s
    
    print(result)
        
            


mySolution(s)

    