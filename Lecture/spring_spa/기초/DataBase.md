## RDBMS
#### H2
- In-memory DB의 대표주자
- 인 메모리 DB는 서버가 작동하는 동안만 내용을 저장, 멈추면 데이터가 삭제된다
- H2 웹 콘솔 설정
	```
	spring.h2.console.enabled=true
	spring.datasource.url=jdbc:h2:mem:testdb
	```
	- 스프링기본주소/h2-console로 접속하면 콘솔이 뜬다


#### MySQL
- AWS RDS 세팅
	- https://www.notion.so/Spring-5-e1b5ceb6ede84d70b3366f03207e2e8c#8525792f30864e378a87448de90f53ef
	```
	spring.datasource.url=jdbc:mysql://나의엔드포인트:3306/DB명
	spring.datasource.username=나의USERNAME
	spring.datasource.password=나의패스워드
	spring.jpa.hibernate.ddl-auto=update
	```	
