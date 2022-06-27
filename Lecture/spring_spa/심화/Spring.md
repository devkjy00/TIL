## Servlet GET 요청 처리
```java
@WebServlet(urlPatterns = "/api/search")
public class ItemSearchServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // 1. API Request 의 파라미터 값에서 검색어 추출 -> query 변수
        String query = request.getParameter("query");

        // 2. 네이버 쇼핑 API 호출에 필요한 Header, Body 정리
        RestTemplate rest = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.add("X-Naver-Client-Id", "zdqMoIkFaK8uKvC2oNY2");
        headers.add("X-Naver-Client-Secret", "LiZfsgtuD5");
        String body = "";
        HttpEntity<String> requestEntity = new HttpEntity<>(body, headers);

        // 3. 네이버 쇼핑 API 호출 결과 -> naverApiResponseJson (JSON 형태)
        ResponseEntity<String> responseEntity = rest.exchange("https://openapi.naver.com/v1/search/shop.json?query=" + query, HttpMethod.GET, requestEntity, String.class);
        String naverApiResponseJson = responseEntity.getBody();

        // 4. naverApiResponseJson (JSON 형태) -> itemDtoList (자바 객체 형태)
        //  - naverApiResponseJson 에서 우리가 사용할 데이터만 추출 -> List<ItemDto> 객체로 변환
        ObjectMapper objectMapper = new ObjectMapper()
                .configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
        JsonNode itemsNode = objectMapper.readTree(naverApiResponseJson).get("items");
        List<ItemDto> itemDtoList = objectMapper
                .readerFor(new TypeReference<List<ItemDto>>() {})
                .readValue(itemsNode);

        // 5. API Response 보내기
        //  5.1) response 의 header 설정
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");
        //  5.2) response 의 body 설정
        PrintWriter out = response.getWriter();
        //     - itemDtoList (자바 객체 형태) -> itemDtoListJson (JSON 형태)
        String itemDtoListJson = objectMapper.writeValueAsString(itemDtoList);
        out.print(itemDtoListJson);
        out.flush();
    }
}


@ServletComponentScan // @WebServlet 어노테이션이 동작하게 함
@SpringBootApplication
public class SpringcoreApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringcoreApplication.class, args);
    }
}
```

## Controller의 이점
- Servlet과 비교
    - HTTP request, response 처리를 매번 작성해야하는 중복 코드 생략가능
        - @RequesetParam, @ResponseBody등의 어노테이션을 명시하면 스프링이 알아서 처리해준다
    
    - API마다 클래스 파일을 만들 필요가 없다
        - 유사한 성격의 API를 메서드에 Mapping해서 하나의 Controller 클래스로 관리한다
    

## MVC(Model - View - Controller)
- SSR(Server Side Rendering)의 경우
    - 정적 웹페이지 
        1. Controller에서 Model로 받아서 처리
        2. View(정적 HTML)로 응답한다
    - 동적 웹페이지 
        1. Controller에서 Model로 받아서 처리
        2. Template engine에게 View(동적 HTML), Model(정보)를 전달
        3. Template engine(Thymeleaf)이 View에 Model을 적용해서 동적 웹페이지 생성
        4. View(동적 HTML)로 응답한다
    
## HTTP 메시지
- 메시지 구조
    - 시작줄
        - 요청(start line) : 요청타입/ 프로토콜/버전
        - 응답(status line) : 프로토콜/버전 상태코드/ 상태텍스트

    - 헤더(headers)
        - Content type으로 HTML이나 AJAX임을 명시
        - 응답 : Location 속성에 Redirect할 페이지 URL을 명시
    - 본문(body)
        - 요청 : POST(~/name=k&age=20)
        - 응답 : HTML이나 JSON

- https://developer.mozilla.org/ko/docs/Web/HTTP/Messages 


## DI(Dependency Injection)의 이해
- 강한 결합의 문제  
    - 각 Controller클래스에서 Service를 또 각 Sevice클래스에서 Repository를 직접 생성할 경우
    - Repository 생성자의 매개변수가 변하면 Controller에서 값을 줘서 Service를 통해 전달하기 때문에 모든 클래스가 변경되어야 한다

- 강한 결합 해결방법, IoC(Inversion of Control, 제어역전)
    - 객체생성의 제어를 역전, 생성을 완료하고 생성된 상태로 다른 객체에게 전달한다 -> 다른 클래스에 생성 변경사항이 영향을 미치지 않는다
        - ***DI(Dependency Injection, 의존성 주입) : 완성된 필요한 객체를 그냥 가져다 사용하는 것***
    - 객체를 딱 1번만 생성해서 모든 곳에서 재사용(싱글톤)
    ```java
    public class 
    Repository repository = new repository();
    
    public class Service{
        private final Repository repository;
        public Service(Repository repository){
            this.repository = repository;
        }
    }
    Service service = new Service(repository);
    ```


## 스프링 IoC 컨테이너, Bean
- 스프링이 관리하는 객체(Bean)를 모아둔 컨테이너
- Bean 등록
    - @Component를 클래스에 명시
        - 해당 클래스의 객체를 생성해서 스프링 IoC 컨테이너에 저장한다
        - @ComponentScan에 설정된 packages위치에 속해야 한다
            - @SpringBootApplication 에 의해 default 설정이 되있다
    
    - @Bean을 생성자 메서드에 명시
        - 명시된 함수를 호출, 반환 값을 IoC에 저장
            - 함수명으로 저장된다

- Bean 사용

    - @Autowired
        - 멤버 변수에 명시 -> 변수가 DI된다
        - 함수에 명시 -> 매개변수가 DI된다
        - 생성자 선언이 1개일때는 생략가능
    
    - @RequiredArgsConstructor을 클래스에 명시
        - final로 선언된 객체가 DI되서 생성자 생략 가능
    
    - ApplicationContext를 통해서 수동으로 가져오기
        ```java
        @Autowired
        public ProductService(ApplicationContext context) {
            // 1.'빈' 이름으로 가져오기
            ProductRepository productRepository = (ProductRepository) context.getBean("productRepository");
            // 2.'빈' 클래스 형식으로 가져오기
            ProductRepository productRepository = context.getBean(ProductRepository.class);
            this.productRepository = productRepository;
        }

        ```

# Spring
- 요구사항 해결에 초점을 맞춘 프레임 워크
    - 비즈니스 로직에 집중할 수 있게 해준다

- Enterprise applications
    - 신뢰성, 서버 안정성, 데이터 관리가 중요


# AOP(Aspect Oriented Programming)
- 비즈니스 로직을 보조하는 부가기능들을 모듈화할 필요하다
    - 핵심 기능마다 부가기능을 넣어줘야 한다면?
        - 중복되는 코드가 계속 늘어난다
        - 핵심 기능 이해를 위해 부가 기능까지 이해 필요
        - 핵심 기능 개수 만큼 부가기능도 수정해줘야 함

    - AOP를 통해 부가기능을 모듈화
        - 핵심기능과 분리해서 부가기능 중심으로 설계, 구현
        - 스프링에서는 어드바이스(부가 기능)와 포인트컷(부가기능 적용위치)를 제공해서 AOP를 구현할 수 있다
            - 포인트 컷 Expression Language
                ```java 
                execution(modifiers-pattern? return-type-pattern declaring-type-pattern? method-name-pattern(param-pattern) throws-pattern?)
                ```
                - ?가 붙은 구몬은 생략 가능
                - modifiers-pattern
                    - **public**, private, *
                - return-type-pattern
                    - void, String, List<String>, *****
                - declaring-type-pattern
                    - 클래스명 (패키지명 필요)
                    - **com.sparta.springcore.controller.*** - controller 패키지의 모든 클래스에 적용
                    - **com.sparta.springcore.controller..** - controller 패키지 및 하위 패키지의 모든 클
                    
                - **method-name-pattern(param-pattern)**
                    - 함수명
                        - **addFolders** : addFolders() 함수에만 적용
                        - **add*** : add 로 시작하는 모든 함수에 적용
                    - 파라미터 패턴 (param-pattern)
                        - **(com.sparta.springcore.dto.FolderRequestDto)** - FolderRequestDto 인수 (arguments) 만 적용
                        - **()** - 인수 없음
                        - **(*)** - 인수 1개 (타입 상관없음)
                        - **(..)** - 인수 0~N개 (타입 상관없음)
                    
    - @Aspect, @Around는 클로져와 같은 방식으로 실행할 핵심 기능 함수를 매개변수로 받아서 별개로 부가 기능을 정의한다
        ```java
        @Aspect
        @Component
        public class UseTimeAop {
            private final ApiUseTimeRepository apiUseTimeRepository;

            public UseTimeAop(ApiUseTimeRepository apiUseTimeRepository) {
                this.apiUseTimeRepository = apiUseTimeRepository;
            }

            @Around("execution(public * com.sparta.springcore.controller..*(..))")
            public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {
                // 측정 시작 시간
                long startTime = System.currentTimeMillis();

                try {
                    // 핵심기능 수행
                    Object output = joinPoint.proceed();
                    return output;
                } finally {
                    // 측정 종료 시간
                    long endTime = System.currentTimeMillis();
                    // 수행시간 = 종료 시간 - 시작 시간
                    long runTime = endTime - startTime;

                    // 로그인 회원이 없는 경우, 수행시간 기록하지 않음
                    Authentication auth = SecurityContextHolder.getContext().getAuthentication();
                    if (auth != null && auth.getPrincipal().getClass() == UserDetailsImpl.class) {
                        // 로그인 회원 정보
                        UserDetailsImpl userDetails = (UserDetailsImpl) auth.getPrincipal();
                        User loginUser = userDetails.getUser();

                        // API 사용시간 및 DB 에 기록
                        ApiUseTime apiUseTime = apiUseTimeRepository.findByUser(loginUser)
                                .orElse(null);
                        if (apiUseTime == null) {
                            // 로그인 회원의 기록이 없으면
                            apiUseTime = new ApiUseTime(loginUser, runTime);
                        } else {
                            // 로그인 회원의 기록이 이미 있으면
                            apiUseTime.addUseTime(runTime);
                        }

                        System.out.println("[API Use Time] Username: " + loginUser.getUsername() + ", Total Time: " + apiUseTime.getTotalTime() + " ms");
                        apiUseTimeRepository.save(apiUseTime);
                    }
                }
            }
        }
        ```

