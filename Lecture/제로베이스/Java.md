## 11.Deep Dive Into JVM
- JVM 모듈 구성
    - Class Loader
        - Loading : 클래스 파일을 JVM에 로드
            - Bootstrap Class Loader : 가장 필수가 되는 라이브러리들을 로드(rt.jar 등)
            - Extension Class Loader : 차순위 라이브러리들을 로드($JAVAHOME/jre/lib/ext/`*`.jar)
            - Application Class Loader : 개발자가 작성한 클래스 파일을 로드(classpath에 위치)
            - 상위로더가 먼저 작동 찾기 실패시 요청을 하위로더에게 넘긴다

        - Linking : 클래스 파일을 검증하고 기본값으로 초기화 
            - Verification : 클래스 파일이 올바른 지에 대한 검증
            - Preparation : 클래스와 인터페이스 등에 필요한 static field 메모리 할당 및 기본값 초기화
            - Resolution : Symbolic Reference 값을 Method Area의 Direct Reference값으로 변환

        - Initialization : 클래스 파일으로 static 변수등을 초기
            - 앞의 과정이 끝나면 파일을 읽고 지정한 값으로 초기화
            - 멀티 쓰레드 동작으로 동시성이 고려되어야 한다


    - Execution Engine
        - Interpreter 방식 : 바이트코드를 한줄씩 해석/실행, 초기방식으로 느리다

        - JIT(Just-In-Time) 컴파일러 방식 : Interpreter를 사용하다가 컴파일 임계치를 넘어가면 실행된다
            - 실제 실행하는 시점에 각 OS에 맞는 Native Code로 변환하여 속도 향상
            - 실행 마다 컴파일한 코드를 캐싱

    - Runtime Data Area : JVM이 할당받은 메모리 공간
        - Method Area : static 변수, 메소드 데이터등 Class 메타데이터를 저장
            - JVM에 하나만 존재, JVM의 구동과 종료가 생명주기이다

        - Heap : 인스턴스, 배열등을 저장
            - 모든 Java Stack 영역에서 참조, Thread간 공유 된다

        - Java Stack : Java의 메소드가 호출 될 때 사용되는 공간
            - 변수, 오퍼레이션, reference등의 정보 저장

        - PC Register : Thread별로 동시에 동작할 수 있도록 메모리 주소를 저장하는 공간
            - 현재 실행되는 JVM 명령어의 주소를 가리키는 역할으로 명령어의 순서를 결정
        
        - Native Method Stack : 시스템 자원을 사용하거나 c/c++ 코드를 사용할때 호출 되는 영역


- Garbage Collection(GC)
    - Heap 영역의 참조되지 않는 객체들을 메모리 해제하는 과정
        - Minor GC : Young Generation(Eden, S0, S1) 영역에서 실행하는 GC
            1. Eden 영역이 차면 발생, 사용되지 않는 객체는 메모리 해제되고 남은 데이터는 S 영역으로 이동
                - 두개의 Survivor 영역중 한 영역은 반드시 비어있어야 함
            2. Promotion : S 영역에 오랫동안 있던 데이터를 Tenured 영역으로 이동 

        - Major GC : Old Generation(Tenured)영역에서 실행하는 GC
            - Promotion된 객체가 많아져 메모리가 부족하게 되면 발생
            - 일반적으로 Minor GC보다 오래 걸리고 길어지면 치명적인 영향을 줄수 있다
    
    - Reachability : 객체가 GC의 대상인지 확인하는 것
    - Stop-the-world : GC를 수행하기 위해 JVM이 애플리케이션 실행을 멈추는 것
        - 동작중인 모든 쓰레드를 멈추고 JVM 쓰레드만 동작한다

    
    - 기본 알고리즘(Stop the world시에 동작)
        - Mark & Swap
            - Mark phase : Root Set으로부터 참조되는 객체(mark)을 Marking한다
            - Sweep phase : Mark가 없는 객체는 메모리 해제 
            - 문제점 : Fragmentation 발생
                - 메모리 해제후에 정리되지 않아서 메모리 공간이 조각나게 된다

        - Mark & Compact
            - Compact Phase : Fragmentation을 해결, 메모리를 해제후에 정리한다

    - 여럭다지 GC 방식
        - Serial GC : 앱 스레드1 -> Stop the world 스레드1 -> 앱 스레드1
            - 주로 싱글스레드에서 사용

        - Parallel GC : 앱 스레드N -> Stop the world 스레드n -> 앱 스레드N
            - 멀티 스레드로 동작

        - CMS GC : 앱 스레드N -> Stop the world 스레드N (Initial Mark) -> 앱 스레드N (Marking/Pre-Cleaning) -> Stop the world 스레드N (Remark) -> 앱 스레드N (Sweep/Reset)
            - Stop the world의 발생을 최소화 해서 최적화
            - 3번의 마킹 과정후 앱스레드 동작중에 메모리를 해제 한다

        - G1 GC : Heap의 영역을 Region단위로 관리, 단위별로 GC를 동작시킨다
            - Stop the world가 가장 짧다
