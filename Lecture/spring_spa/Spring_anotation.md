## 어노테이션
- org.springframework.context.annotation
	- @Configuration : 설정파일을 만들기 위한 애노테이션 or Bean을 등록하기 위한 애노테이션


- org.springframework.stereotype
	- @Service : 로직을 담당하는 클래스임을 명시

- org.springframework.web.bind.annotation
	- @RestController : 요청에 JSON을 리턴하는 클래스임을 명시
	- @Controller : 요청에 HTML, CSS등을 주고받는 클래스임을 명시
	- https://m.blog.naver.com/cmh348/221912870674
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
	
- org.springframework.beans.factory.annotation
	- @Autowired : 생성자, setter, 필드에 사용할 수 있다
		- [@Autowired란 무엇인가](https://devlog-wjdrbs96.tistory.com/166)

- javax.transactional
	- @Transactional : 메서드에 SQL쿼리가 일어나는 것을 명시

- javax.persistence
	- @Entity : 클래스가 테이블임을 명시
	- @Id : 변수를 primary key로 사용하겠다고 명시
	- @GeneratedValue
		- (strategy = GenerationType.AUTO) : 변수가 자동증가 되도록 명시
	
	- @Column : 변수가 컬럼 값임을 명시
		- nullable = false : 반드시 값이 존재해야함을 명시
		- unique = true : 중복 값을 허용하지 않는다
	
	- @Transactional : 메서드가 트랜잭션임을 명시
		- Dirty check, 메서드가 끝나면 변경된 부분을 알아서 업데이트 해준다

	- @MappedSuperclass : 테이블에 공통정보를 가진 추상클래스로 매핑되도록 명시
		- Etity 종류에 상관없이 공통으로 가져야하는 정보(생성시간, 수정시간등)를 공통 클래스로 추출하고 이를 상속하는 방식으로 구현할 때 사용된다
		- LocalDateTime변수에 @CreatedDate, @LastModifiedDate등을 붙여서 업데이트할 변수 명시
		- https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=adamdoha&logNo=222139716154

	- @EntityListeners(Listener클래스.class) : 엔티티의 변화를 감지하고 데이블의 데이터를 조작하는 일을 한다
		- (AuditingEntityListener.class) : JPA에서 제공
		-  ~Application.java파일에 @EnableJpaAuditing annotation을 추가해줘야한다
		- https://velog.io/@seongwon97/Spring-Boot-Entity-Listener

- org.springframework.security
	- .core.annotation
		- @AuthenticationPrincipal : 시큐리티에서 인증된 회원 정보 객체를 주입할 것을 명시, 매개변수에 작성할 수 있다

	- .access.annotation
		- @Secured("ROLE_...") : 지정된 권한을 가진 요청만 허용하도록 Controller의 메서드에 명시

	- .config.annotation.web.configuration
		- @EnableWebSecurity : WebSecurityConfigurerAdapter를 구현한 클래스에 명시해서 시큐리티 활성화
	
	- .config.annotation.method.configuration
		- @EnableGlobalMethodSecurity  
			- securedEnabled = true : @Secured 어노테이션을 활성화할 것을 명시

- javax.annotation
	- @Resource : @Autowired와 같은 역할, 빈의 이름을 사용해서 주입할 빈 객체를 찾기 때문에, @Resource 어노테이션의 값으로 빈 객체의 이름을 지정
		- 필드나 메서드에만 적용할 수 있다
		- Autowired와 차이점은 타입과 이름 중 무엇을 먼저 사용하느냐에 대한 것이다

- org.hibernate.annotations
	- @ColumnDefault(value = "...") : 데이터베이스에서 테이블을 생성할 때 디폴트 값을 지정하도록 명시
	- @DynaminInsert : 튜플 INSERT 할 때 null인 필드는 빼고 INSERT 한다
	- @DynaminUpdate : 튜플 값 UPDATE 할 때 null인 필드는 그대로 두고 UPDATE한다

- lombok : 필수적으로 필요한 메서드/생성자등을 자동으로 생성해주는 라이브러리
