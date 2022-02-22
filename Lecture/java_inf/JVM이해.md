- ### JVM(java virtual machine)
    - 바이트 코드를 실행하는 표준, 특정 벤더가 구현한 구현체이다  
        - 벤더 : 오라클, 아마존, Azul,..
    - 바이트 코드를 OS에 특화된 코드로 변환후 실행
        - javap -c 클래스파일
            - 클래스 파일의 바이트 코드를 출력한다
        - 특정 OS에 종속적이다

- ### JRE(java runtime environment)
    - JVM+라이브러리
    - JIT 컴파일러
        - 바이트 코드를 네이티드 코드로 컴파일해서 성능을 향상 시킨다
            - (compile)source code -> javac -> byte code -> (runtime) JIT -> native code
            - 메서드 호출시에 활성화 되서 컴파일한다
            - 데이터분석, 레지스터 할당에 의한 메모리 액세스 감소 등 최적화를 수행한다

        - JIT이 컴파일한 메소드가 자주 호출되지 않으면 바이트 코드보다 더 느려질 수있다
            - JIT의 컴파일 시간이 실행시간에 포함되기 때문
        
        - 실행순서
            - Inlining
                - 작은 메서드 트리를 호출자 트리에 병합
            - Local optimizations
                - 코드의 작은 부분을 분석, 최적화
            - Control flow optimizations
                - 코드의 흐름제어를 분석, 최적화
            - Global optimizations 
                - 메서드 전체를 초기화 
            - Native code generation
        - https://aboullaite.me/understanding-jit-compiler-just-in-time-compiler/

    - JVM 기반으로 동작하는 프로그래밍 언어
        - 클로저, 그루비, JRuby, Jython, Kotlin, Scala, ...
    

    - jlink : java9부터 생긴 모듈시스템으로 사용자 JRE를 만들수 있다

- ### JDK(java development kit)
    - JRE + 개발툴
    - java11 부터 JRE만 따로 제공하지는 않는다

- ### java 
    - 언어, JDK의 자바 컴파일러(javac)를 이용해서 바이트코드(.class)로 컴파일 할 수 있다
    - JDK는 java언어에 의존하지 않는 독립적인 프로그램이다

- 오라클의 Oracle JDK 11 버전부터 상용으로 사용할 때 유료

## JVM 구조
- ### 클래스로더
    - .class 에서 바이트코드를 읽고 메모리에 저장
    - 로딩, 링크(래퍼런스연결), 초기화(static값 초기화, 할당)

- ### 메모리
    - 메서드 영역(클래스 정보, 공유자원)
    - 힙 영역(객체정보, 공유자원)
    - Run-Time Constant Pool(상수정보, 공유자원)
        - 메서드 영역 안에 생성된다
        - 클래스,인터페이스가 생성되면 JVM에 의해 생성된다
        - 상수값들을 상수풀에 저장한다
    - 스택 영역(메소드 호출, 스택 프레임 쌓는다)
        - 쓰레드 마다 생성된다
    - PC(프로그램 카운터)레지스터 : 각 쓰레드마다 현재 실행할 스택 프레임의 주소를 저장
    - 네이티브 메소드 스택
        - 쓰레드 마다 생성된다
    
- ### 실행엔진
    - 인터프리터 : 바이트 코드를 한줄씩 실행
    - JIT컴파일러 : 반복되는 코드를 네이티브 코드로 컴파일
    - GC : 객체를 정리

- ### JNI(Java Native Interface)
    - C, C++, 어셈블리로 작성된 함수를 사용할 수 있게 해준다
    - Native 키워드로 메서드 호출
        - 네이티브 메서드 라이브러리에서 호출


## 클래스로더
- 클래스로더 종류
    - Bootstrap 
        - 신뢰할 수 있는 클래스를 로드할 수 있게 한다
        - 최상위 우선순위를 가진 클래스 로더
        - C, C++과 같은 네이티브 언어로 구현(java에서 확인할 수없다)
    - Extension(Platform)
        - Bootstrap의 자식
        - 확장경로, 지정된 기타 디렉토리에 있는 클래스를 로드한다
        - sun.misc.Launcher$ExtClassLoader 클래스로 구현
    - Application
        - Extension의 자식
        - 어플리케이션 클래스 경로에서 클래스를 로드한다
            - 작성된 코드의 클래스를 로드한다
        - java.class.path에 매핑된 환경변수를 사용한다
        - sun.misc.Launcher$AppClassLoader 클래스에 의해 Java로 구현 
    
    - 클래스 로더로 클래스를 찾지 못하면 예외가 발생한다
- 로딩 
    - 클래스 로더가 .class파일을 읽고 바이너리 데이터를 메소드 영역에 저장
    - 저장하는 데이터
        - FQCN(패키지, 풀패키지경로, 클래스이름)
        - class or interface or enum
        - 메소드와 변수
    - 로딩 후 class 객체생성, 힙 영역에 저장

- 링크
    - Verify : .class 파일 형식이 유효한지 체크한다 
    - Prepare : 클래스 변수와 기본값에 필요한 메모리 준비 
    - Resolve(optional) : 심볼릭 메모리 레퍼런스를 메소드 영역에 있는 실제 레퍼런스로 교체한다
        - 심볼릭 메모리 레퍼런스 : 객체가 참조하는 값을 실제가 아니라 논리적으로 저장한 것 

- 초기화
    - static 변수의 값을 할당한다(static블럭을 실행한다)
