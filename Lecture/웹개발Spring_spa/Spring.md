## 개념
- Controller : 가장 바깥쪽, 요청/응답을 처리
- Service : 중간, 중요한 로직을 처리
- Repo :  가장 안쪽, DB와의 통신을 처리
	- Update는 Service에서 처리한다

## 어노테이션
- @RestController : 요청에 JSON을 리턴하는 클래스임을 명시
- @Controller : 요청에 HTML, CSS등을 주고받는 클래스임을 명시
- @GetMapping("uri") : 지정된 주소로 온 GET 요청을 처리하는 메서드임을 명시

- javax.persistence
	- @Entity : 클래스가 테이블임을 명시
	- @Id : 변수를 primary key로 사용하겠다고 명시
	- GeneratedValue
		- (strategy = GenerationType.AUTO) : 변수가 자동증가 되도록 명시
	
	- Column : 변수가 컬럼 값임을 명시
		- (nullable = false) : 반드시 값이 존재해야함을 명시

- lombok
	- @NoArgsConstructor : 클래스의 파라미터가 없는 기본생성자를 대신 생성해준다
	- @AllArgsConstructor : 클래스의 모든 필드 값을 파라미터로 받는 생성자를 대신 생성해준다


## JPA
- Domain(DB의 테이블 기능)
- Repository(DB의 SQL 기능)
- ***JpaRepository***
	- 이 클래스를 상속한 클래스를 이용해서 개체가 DB와 통신한다
		- 각 테이블(개체)마다 생성해줘야 한다
		- 제네릭에 엔티티이름,pk값 타입을 명시해야 한다

	- 메서드
		- void save(entity)
		- List<entity> findAll() 
			- findById



## application.properties
- h2 db 설정
	```
	spring.h2.console.enabled=true
	spring.datasource.url=jdbc:h2:mem:testdb;MODE=MYSQL
	spring.jpa.show-sql=true # sql문이 보이도록 설정
	```
