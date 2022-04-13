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

- Comparator 대신 함수형 인터페이스 사용
    - Arrays.sort(A, (x, y)->x-y);
    - Arrays.sort(B, String::compareToIgnoreCase);
        - 인스턴스 메서드로 인자가 String타입인 경우
    
## 인터페이스의 변화
- 기본 메서드(default method)
    - 기본 메소드는 구현체가 모르게 추가된 기능으로 그만큼 리스크가 있다.
        - 컴파일 에러는 아니지만 구현체에 따라 런타임 에러가 발생할 수 있다.
        - 반드시 문서화 할 것. (@implSpec 자바독 태그 사용)

    - Object에 정의된 기본 메서드는 재정의(오버라이딩) 할 수 없다
    - 기본메서드를 가진 인터페이스를 구현한 인터페이스에서 기본메서드를 추상메서드로 다시 정의할 수 있다
    - 같은 기본메서드를 가진 인터페이스 여러개를 하나의 클래스에 구현하면 메서드 충돌로 컴파일 에러 발생
        - 충돌할 경우 직접 오버라이딩 해야 한다
    
- 스태틱 메서드
    - 해당 타입 관련 헬퍼 또는 유틸리티 메소드를 제공할 때 인터페이스에 스태틱 메소드를 제공할 수 있다

- iterable의 기본 메서드
    - forEach()
    - spliterator() : Spliterator를 반환
        - .trySplit() : 이터레이터를 반으로 분할해서 반만 반환, 원래의 객체도 반으로 분할된다
        - .tryAdance() : Consumer를 실행

- Comparator의 기본 메소드 및 스태틱 메소드
    - reversed()
    - thenComparing()
    - static reverseOrder() / naturalOrder()
    - static nullsFirst() / nullsLast()
    - static comparing()

- 기본, 스태틱 메서드의 이점
    - 추상클래스가 없이 인터페이스만으로도 구현된 메서드를 더 간단하게 상속할 수 있다

## Stream
- 종료 연산을 먼저 처리하고나서 그 다음에 중간 연산이 실행된다
- 스트림의 paralleStream으로 간단하게 병렬처리를 할 수 있다

- fillter에서 not 연산 구현
    - .filter(Predicate.not(Objects::isNull));
    - .filter(i -> !i.isNull());

- flatMap으로 이터러블의 차원을 낮춰서 내부의 객체타입을 사용할 수 있다
- iterate(람다식)으로 무한한 스트림을 만들 수 있다
    - limit으로 제한가능

## Optional
- if(obj==null) 과 같은 형식은 좋지 않다
- 값을 제대로 리턴할 수 없는 경우 대책
    - 예외를 던진다
        - 리소스를 많이 사용한다, 비즈니스 로직을 처리하기에 좋지 않은 방법
    
    - null을 반환한다
        - 항상 조건문으로 null을 체크해야 한다

    - Optional을 반환한다
        - null이거나 아닌 객체를 Optional에 넣어서 nullPointerException을 방지할 수 있다

- Optional은 메소드의 리턴값으로만 사용하는 것이 좋다
    - 다른 방법은 null을 관리하는 Optional에 의미가 없다

- Collection, Map, Stream, Array, Optional은  Optional로 감싸면 안된다
- 기본형은 기본형을 감싸는 OptionalInt를 사용

- API
    - 생성 : of, ofNullable, empty
    - 메서드 : isPresent, isEmpty, get, ifPresent, orElse, orElseGet, orElseThrow, filter, map, flatMap