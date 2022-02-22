# 데코레이터(Decorator)
## 장점
1. 중복 제거, 간결한 코드, 공통 함수 작성
2. 로깅, 프레임 워크, 유효성 체크 -> 공통함수
    - 성능체크하는 함수를 하나 만들어서 각 함수마다 데코레이터로 체크할 수 있다
3. 조합해서 사용 용이

## 단점
1. 가독성 감소가능
2. 특정 기능에만 한정된 함수는 단일 함수로 작성이 유리
3. 디버깅 불편

데코레이터 예제
```py

import time


def perf_clock(func):

    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()

        # 인자값으로 받은 함수 실행
        result = func(*args)

        # 함수 종료 시간
        et = time.perf_counter()

        # 실행 함수명
        name = func.__name__

        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)

        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))

        return result

    return perf_clocked

# 데코레이터 미사용
def a(x):
    for i in range(0, x):
        print(i)


# 테스트할 함수를 인수로 대입해서 식별자에 할당
deco = perf_clock(a)
# 식별자를 호출할 때 주는 인수값이 테스트함수에 전달됨
deco(10)


# 데코레이터 사용
@perf_clock  # perf_clock(b)와 같다
def b(x):
    for i in range(0, x):
        print(i)

# 원래 함수를 실행하면 
# 데코레이터도 같이 실행된다
b(100)

# 데코레이터가 훨씬 직관적이고 간단하다
# 데코레이터가 감싼 함수들의 값을 기록할 수도 있고
# 프레임 워크로 사용하거나 테스트,분석같은 것도 할수있다
# 데코레이터안에서 실행된 함수를 스택으로 쌓아서 
# 그 값들은 다시 순차적으로 불러올쑤도 있겠다
```