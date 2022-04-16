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

## Date, Time

- Instant는 기계용 시간을 표현, 메소드 처리시간에 사용된다
- Period 
    - .between : 두 LocalDate객체 간의 day차이를 연산

- Duration  
    - .between : 두 Instant객체 간의 차이를 연산

## CompletableFuture
- 자바 Concurrent 프로그래밍
    - Thread 상속 
    - Thread 생성자의 매개변수로 Runnable이나 람다식 사용

- Executors
    - 고수준 Concurrency 프로그래밍
        - 쓰레드를 만들고 관리하는 작업을 애플리케이션에서 분리해서 Executors에 위임

    - Executors가 하는 일
        - 쓰레드 만들기: 애플리케이션이 사용할 쓰레드 풀을 만들어 관리한다.
            - execute(Runnable)
        - 쓰레드 관리: 쓰레드 생명 주기를 관리한다.
        - 작업처리 및 실행: 쓰레드로 실행할 작업을 제공할 수있는 API를 제공한다.

    - ExecutorService 
        - Executor 상속 받은 인터페이스, 구현체로 손쉽게 멀티 프로세서를 활용할 수 있게끔 도와준다
        - Callable동시실행, Executor를 종료 기능을 제공한다.
        - ExecutorService로 작업 실행하기
            ```java
            // Runnable으로 구현, 스레드 하나 생성
            ExecutorService es = Executors.newSingleThreadExecutor();
            es.excute(new Runnable(){ 
                @override
                void run(){

                }
            })
            // 람다식으로 구현, 2개의 스레드로 구현
            ExecutorService es = Executors.newFixedThreadPool(2);

            // 2개의 스레드로 여러번 실행해도 모두 처리된다
            // 스레드가 모두 실행중이면 다른 작업은 Bloking Queue에서 대기한다
            es.submit(() -> {});
            es.submit(() -> {});
            es.submit(() -> {});
            es.submit(() -> {});


            es.shutdown();
            ```
        - ExecutorService로 멈추기
            - executorService.shutdown(); // 처리중인 작업 기다렸다가 종료
            - executorService.shutdownNow(); // 당장 종료 Fork/Join 프레임워크

    - ScheduledExecutorService 
        - ExecutorService를 상속 받은 인터페이스, 특정 시간 이후 또는 주기적으로 작업을 실행할 수 있다 
        ```java
        ScheduledExecutorService ses = Executors.newSingleThreadScheduledExecutor();
        // (작업, 시작시간, 대기시간, 단위)
        ses.scheduleAtFixedRate(()->{System.out.println("Hello");}, 2, 2, TimeUnit.SECONDS);
        ```

- Callable과 Future Callable
    - Callable : Runnable과 유사하지만 작업의 결과를 받을 수 있다.
    - Future
        - 비동기적인 작업의 현재 상태를 조회하거나 결과를 가져올 수 있다.
        - https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html

        - get() : 결과를 가져오기 
            ```java
            ExecutorService es = Executors.newSingleThreadExecutor();

            Callable<String> hello = () -> {
                Thread.sleep(2000L);
                return "Hello";
            };
            // Callable을 처리하는 쓰레드는 값을 반환할 수 있다
            // submit은 Future를 반환한다
            Future<String> submit = es.submit(hello);

            submit.get();
            ```
            - 블록킹 콜이다.
            - 타임아웃(최대한으로 기다릴 시간)을 설정할 수 있다.

        - isDone() : 작업 상태 확인하기 
            - 완료 했으면 true 아니면 false를 리턴한다.

        - cancel() : 작업 취소하기 
            - 취소 했으면 true 못했으면 false를 리턴한다.
            - parameter로 true를 전달하면 현재 진행중인 쓰레드를 interrupt하고 그러지 않으면 현재 진행중인 작업이 끝날때까지 기다린다 
        - invokeAll() : 여러 작업 동시에 실행하기 
            ```java
            List<Future<String>> futures = es.invokeAll(Arrays.asList(hello, hello, hello));

            for(Future<String> f : futures){
                System.out.println(f.get());
            }
            ```
            - 동시에 실행한 작업중에 제일 오래 걸리는 작업만큼 시간이 걸린다
        - invokeAny() : 여러 작업 중에 하나라도 먼저 응답이 오면 끝내기 
            ```java
            String s = futures = es.invokeAny(Arrays.asList(hello, hello, hello));
            System.out.println(s);
            ```
            - 동시에 실행한 작업중에 제일 짧게 걸리는 작업만큼 시간이 걸린다
            - 블록킹 콜이다    


- CompletableFuture
    - 자바에서 비동기(Asynchronous) 프로그래밍을 가능케하는 인터페이스.

    - Future로는 하기 어렵던 작업들
        - Future를 외부에서 완료 시킬 수 없다. 취소하거나, get()에 타임아웃을 설정할 수는 있다.
        - 블로킹 코드(get())를 사용하지 않고서는 작업이 끝났을 때 콜백을 실행할 수 없다.
        - 여러 Future를 조합할 수 없다, 예) Event 정보 가져온 다음 Event에 참석하는 회원 목록
        가져오기
        - 예외 처리용 API를 제공하지 않는다.

    - CompletableFuture
        - Implements Futurem, ​CompletionStage
        ```java
		// complete cf의 기본값을 정하고 get에서 작업이 완료되지 않았으면 기본값을 반환
		CompletableFuture<String> cf = new CompletableFuture<>();
		cf.complete("value");
		System.out.println(cf.get());

		CompletableFuture<String> cf2 = CompletableFuture.completedFuture("value");
		System.out.println(cf2.get());
        ```


    - 비동기로 작업 실행하기
        - 리턴값이 없는 경우: runAsync()
            ```java
            CompletableFuture<Void> cf = CompletableFuture.runAsync(() -> {
                System.out.println("Hello");
            });
            cf.get();
            ```
        - 리턴값이 있는 경우: supplyAsync()
            ```java
            CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> {
                return "Hello";
            });
            System.out.println(cf.get());
            ```
        - 원하는 Executor(쓰레드풀)를 사용해서 실행할 수도 있다. (기본은 ForkJoinPool.commonPool())

    - 콜백 제공하기
        - thenApply(Function): 리턴값을 받아서 다른 값으로 바꾸는 콜백
            ```java
            CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> {
                return "Hello";
            }).thenApply((s) -> {
                return s.toUpperCase();
            });
            System.out.println(cf.get());
            ```
        - thenAccept(Consumer): 리턴값을 또 다른 작업을 처리하는 콜백 (리턴없이)
            ```java
            CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> {
                return "Hello";
            }).thenAccept((s) -> {
                System.out.println(s.toUpperCase());
            });
            cf.get();
            ```
        - thenRun(Runnable): 리턴값 받지 않고 다른 작업을 처리하는 콜백
        - 콜백 자체를 또다른 쓰레드에서 실행할 수 있다.

    - 조합하기
        - thenCompose(): 두 작업이 서로 이어서 실행하도록 조합
            ```java
            class A{
                public static void main(String[] args) throws Exception {
                    CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> {
                        return "Hello";
                    });
                    CompletableFuture<String> future = cf.thenCompose(A::compose);
                    System.out.println(future.get());
                }
                static CompletableFuture<String> compose(String msg){
                    return CompletableFuture.supplyAsync(() -> {
                        return msg + " composed";
                    });
                }
            } 
            ```
        - thenCombine(): 두 작업을 독립적으로 실행하고 둘 다 종료 했을 때 콜백 실행
        - allOf(): 여러 작업을 모두 실행하고 모든 작업 결과에 콜백 실행
        - anyOf():여러작업중에가장빨리끝난하나의결과에콜백실행
    - 예외처리
        - exeptionally(Function) 
        - handle(BiFunction)