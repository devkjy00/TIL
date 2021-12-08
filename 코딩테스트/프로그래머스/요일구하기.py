# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.
import datetime


def solution(a, b):
    answer = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    idx = datetime.date(2016, a, b).weekday()
    return answer[idx]


# 테스트
a, b = 5, 24
result = "TUE"

assert result == solution(a, b)

# 함수를 쓰지 않는 방법
# 매 월별로 시작 요일을 리스트로 정의해서
# 날짜를 더하고 나머지를 구해서 요일을 반환할 수 있다
