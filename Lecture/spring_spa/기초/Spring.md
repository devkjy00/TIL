## 개념
- 3계층 : 책임을 분리로 결합을 느슨하게 해서 유연성과 확장성을 가지게 한다
	- Controller : 가장 바깥쪽, 요청/응답을 처리
	- Service : 중간, 중요한 로직을 처리
		- 생성자에 해당 객체의 repository를 준다
		- 서비스에 꼭 필요한 변수는 final로 지정해서 스프링에 알려준다
	- Repository :  가장 안쪽, DB와의 통신을 처리
		- DB Update는 Service에서 처리한다

- DTO(Data Transfer Object)
	- 테이블에 사용할 객체로 데이터를 바로 입력 받는 것 보다 DTO객체를 따로 만들어서 객체로 옮기는 것이 안전하다
	- 각 레이어간에 Entity를 직접 사용하면 안되고 DTO를 사용해서 데이터를 주고받아야 한다
	- 같은 repository라도 POST 데이터가 다르면 각각 DTO를 정의해 준다

- REST
	- 주소는 명사, 요청은 동사로 의도를 명확히하는 방식
		- 명사는 복수형으로 작성
	- POST, GET, PUT, DELETE



## 어노테이션
- org.springframework.stereotype
	- @Service : 로직을 담당하는 클래스임을 명시

- org.springframework.web.bind.annotation
	- @RestController : 요청에 JSON을 리턴하는 클래스임을 명시
	- @Controller : 요청에 HTML, CSS등을 주고받는 클래스임을 명시
	- @GetMapping("uri") : 지정된 주소로 온 GET(조회) 요청을 처리하는 메서드임을 명시
	- @PostMapping("uri") : 지정된 주소로 온 POST(삽입) 요청을 처리하는 메서드임을 명시
	- @PutMapping("uri") : 지정된 주소로 온 PUT(수정) 요청을 처리하는 메서드임을 명시

	- @RequestBody : POST요청의 body를 저장할 변수임을 명시
	- @RequestParam : URI의 쿼리를 문자열로 저장할 변수임을 명시
	- @PathVariable : URI에서 지정한 값을 받을 변수임을 명시, 같은 이름이어야 한다
	- @Scheduled : 주기적인 작업을 처리할 Scheduler클래스임을 명시한다
		- ~Applicatino 클래스에 @EnableScheduling을 추가해서 스케줄러사용을 명시
		- 속성 : cron, fixedDelay, fixedDelayString, fixedRate, fixedRateString, initialDelay, initialDelayString, zone
		- https://jeong-pro.tistory.com/186

- javax.transactional
	- @Transactional : 메서드에 SQL쿼리가 일어나는 것을 명시


- javax.persistence
	- @Entity : 클래스가 테이블임을 명시
	- @Id : 변수를 primary key로 사용하겠다고 명시
	- @GeneratedValue
		- (strategy = GenerationType.AUTO) : 변수가 자동증가 되도록 명시
	
	- @Column : 변수가 컬럼 값임을 명시
		- (nullable = false) : 반드시 값이 존재해야함을 명시
	
	- @MappedSuperclass : 테이블에 공통정보를 가진 부모클래스로 매핑되도록 명시
		- Etity 종류에 상관없이 공통으로 가져야하는 정보(생성시간, 수정시간등)를 공통 클래스로 추출하고 이를 상속하는 방식으로 구현할 때 사용된다
		- https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=adamdoha&logNo=222139716154

	- @EntityListeners(Listener클래스.class) : 엔티티의 변화를 감지하고 데이블의 데이터를 조작하는 일을 한다
		- (AuditingEntityListener.class) : JPA에서 제공
			-  ~Application.java파일에 @EnableJpaAuditing annotation을 추가해줘야한다
			- LocalDateTime변수에 @CreatedDate, @LastModifiedDate등을 붙여서 업데이트할 변수 명시
		- https://velog.io/@seongwon97/Spring-Boot-Entity-Listener


- lombok : 필수적으로 필요한 메서드/생성자등을 자동으로 생성해주는 라이브러리
	- intellij의 플러그인을 설치해서 사용
	- @Getter and @Setter
	- @FieldNameConstants
	- @ToString
	- @EqualsAndHashCode
	- @AllArgsConstructor, @RequiredArgsConstructor and @NoArgsConstructor
	- @Log, @Log4j, @Log4j2, @Slf4j, @XSlf4j, @CommonsLog, @JBossLog, @Flogger, @CustomLog
	- @Data
	- @Builder
	- @SuperBuilder
	- @Singular
	- @Delegate
	- @Value
	- @Accessors
	- @Wither
	- @With
	- @SneakyThrows
	- @val
	- @var
	- experimental @var
	- @UtilityClass

## JPA
- Domain(DB의 테이블 기능)
- Repository(DB의 SQL 기능)
- ***JpaRepository***
	- 이 클래스를 상속한 인터페이스를 이용해서 개체가 DB와 통신한다
		- 각 테이블(개체)마다 생성해줘야 한다
		- 제네릭에 엔티티이름,pk값 타입을 명시해야 한다

	- 메서드
		- void save(entity)
		- List<entity> findAll() 
			- findById
		- void deleteAll()



## application.properties
- h2 db 설정
	```
	spring.h2.console.enabled=true
	spring.datasource.url=jdbc:h2:mem:testdb;MODE=MYSQL
	spring.jpa.show-sql=true # sql문이 보이도록 설정
	```

## Spring API 요청 예제
```java
RestTemplate rest = new RestTemplate();
HttpHeaders headers = new HttpHeaders();
headers.add("X-Naver-Client-Id", "coSd7QD9SiS6WMyg3bx2");
headers.add("X-Naver-Client-Secret", "gm90HNggug");
String body = "";

HttpEntity<String> requestEntity = new HttpEntity<String>(body, headers);
ResponseEntity<String> responseEntity = rest.exchange("https://openapi.naver.com/v1/search/shop.json?query=기타", HttpMethod.GET, requestEntity, String.class);
HttpStatus httpStatus = responseEntity.getStatusCode();
int status = httpStatus.value();
String response = responseEntity.getBody();
System.out.println("Response status: " + status);
System.out.println(response);
```
- org.springframework.web.client
	- .RestTemplate() : https://velog.io/@soosungp33/%EC%8A%A4%ED%94%84%EB%A7%81-RestTemplate-%EC%A0%95%EB%A6%AC%EC%9A%94%EC%B2%AD-%ED%95%A8
		- exchange(url, API방식, HttpEntity) : ResponseEntity를 반환한다

	
- org.springframework.http
	- .HttpHeaders() : 헤더 객체
		- add(name, value)
	- .HttpEntity(String, HttpHeaders) : body정보 문자열과 header정보로 생성
	- .ResponseEntity() 
		- getStatusCode() : HttpStatus 반환
		- getBody() : 응답받은 body 문자열 반환

	- .HttpStatus() 
		- value() : 상태 코드(int) 반환

- json.org (JSON In Java 라이브러리)
	- JSONObject(json문자열) : 문자열 정보를 json으로 바꿔서 JSONObject 객체 반환
		- getJSONArray("키값") : 해당 키의 값들을 가진 JSONArray 객체 반환
		- getString("키값") : 해당 키의 값을 String으로 반환
		- getInt("키값") : 해당 키의 값을 Int로 반환

	- JSONArray : JSON 배열
		- get(idx) : 특정 idx를 반환, 형 변환이 필요하다
		- getJSONObject(idx) : 특정 idx를 반환




