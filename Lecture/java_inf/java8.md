## 함수형 인터페이스와 람다 표현식
- 함수형 인터페이스(Funcional Interface) 
    - SAM(Single Abstract Method) 인터페이스
    - @FuncationInterface 애노테이션을 가지는 인터페이스

- 자바에서 함수형 프로그래밍
    - 고차 함수(Higher-Order Function) : 매개변수, 리턴 값으로 사용할 수 있다
    - 순수 함수(Pure function) : 사이드 이팩트가 없고 상태가 없다(함수 밖의 값을 사용/변경하지 않는다)
    - 불변성

- 변수 캡쳐
    - effective final : 익명 클래스 구현체 또는 람다에서 참조하는 변수를 final로 만든다
        - 변경되는 변수는 effective final이 될수 없다
    - 로컬 변수 캡처 : final, effective final인 경우만 참조가능
    - 쉐도잉 : 같은 이름의 내부, 외부변수는 내부변수가 외부변수를 가린다
        - 내부/익명 클래스는 내부 스코프를 가져서 쉐도잉이 가능하다
        - 람다식은 따로 스코프를 가지지 않고 선언된 로컬과 같은 스코프를 가진다