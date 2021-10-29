# 클로저(Closure)
## 네임 스페이스(Name Space)

- 특정한 하나의 이름이 통용될 수 있는 범위를 제한해서 다른 범위의 네임이라면 같은 이름이 다른 객체를 참조할 수 있도록 만든것
- 네임 스페이스 구현
    - 파이썬 사전으로 구현된다
    - 모든 네임은 문자열로 되어있고, 유효한 범위에서의 실제 객체를 가리키며 이름과 객체 사이의 맵핑은 가변적이다
    - 새로운 이름이 실행 시간에 추가되거나 삭제 될 수도 있다.
    ```py
    globals() # 전역범위의 네임과 값을 사전형으로 반환
    locals() # 호출된 함수,메소드범위의 네임과 값을 사전형으로 반환
    ```
    - 새도우잉 구현
        1. 호출된 범위에서 로컬 변수명을 찾는다
        2. 상위 네임스페이스에서 이름을 찾는다, 중첩된 함수일 경우 이름이 발견 될 때 까지 상위로 올라가서 전역 네임스페이스를 찾는다
        3. 내장된 네임스페이스에서 이름을 찾는다
        4. 이 과정에서 최초로 발견된 이름을 사용, 발견되지 않았다면 NameError예외가 발생한다

https://soooprmx.com/python-namespace-and-variable-scope/

> 새도우잉(Shadowing),(네임 마스킹)
- 특정 스코프 내에서 선언된 이름이 외부 스코프와 중첩되는 것
- 중복된 이름이 발견되면 로컬값이 우선적으로 참조되고 전역값은 참조되지 않는다
- 새도우잉은 "읽기"시점에만 적용된다, 전역변수를 로컬 네임 스페이스에서 "수정"하는 건 가변형 일 때 가능하다

> global, nonlocal
- global : 전역변수로 선언된 이름을 사용한다는 뜻
- nonlocal : 상위 스코프의 이름을 사용한다는 뜻
#
## 클로저(Closure)
- 참조가 끝난 값을 기억하는 기능
    - 외부에서 호출된 함수의 변수값, 상태(래퍼런스) 복사 후 저장 -> 나중에 접근(엑세스) 가능
- 클로저 사용이유
    - 서버 프로그래밍 -> 동시성(Concurrency)제어 -> 메모리 공간에 여러 자원이 접속 -> 교착 상태(Dead Lock)
- 클로저는 immutable(read only)이다,함수형 프로그래밍
- 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점을 가진다
- 클로저의 예
    ```py
    def a():
        # 자유 변수(Free variable)
        # 클로저 영역
        # 함수가 종료되어도 변경된 값이 저장됨
        y = []

        def b(x):
            y.append(x)
        return b
    # 함수 b의 관점에서 a는 nonlocal 범위이다
    
    # a()를 호출, b함수를 변수에 할당한다
    closure = a()

    # b()를 호출 하는 것과 같다
    closure(10)
    closure(13)
    # b의 상위 네임스페이스인 y값이 계속 누적저장 된다
    # 함수는 종료 되지만 자유영역에 값이 저장된다

    # 클로저 영역에 저장된 값을 반환한다
    print(closure.__code__.co_freevars)
    print(closure.__closure__[0].cell_contents)


    ```
- 클래스를 활용한 예
    ```py
    class Averager():
        def __init__(self) -> None:
            self._series = []

        # 함수처럼 인스턴스를 호출하도록 선언
        def __call__(self, v):
            self._series.append(v)
            print(f'inner >> {self._series}/{len(self._series)}')
            return sum(self._series) / len(self._series)
    
    # init을 실행한다
    aver = Averager()
    
    # ()는 호출을 의미, __call__ 메서드를 실행한다
    print(aver(10))
    print(aver(20))
    # 값이 계속해서 누적된다
    ```

- 잘못된 클로저 사용
    ```py
    def closure_ex():
        a = 0
        b = 0
        
        def sum(x):
            a += 1
            b += x
            return total / cnt
        return sum
    avg = closure_ex():
    avg(2)
    # 오류 발생 : nonlocal변수를 참조하지 못하고 local변수 a,b로 값을 인식하기 때문에 오류가 발생한다
    # 해결법 : nonlocal a,b 를 선언해서 자유 변수의 값을 참조하도록 만든다
    ```