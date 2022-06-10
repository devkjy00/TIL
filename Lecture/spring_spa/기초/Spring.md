## 개념
- 3계층 : 책임을 분리로 결합을 느슨하게 해서 유연성과 확장성을 가지게 한다
	- Controller : 가장 바깥쪽, 요청을 받아서 Service에 요청하고 반환값으로 응답
	- Service : 중요한 로직을 처리, DB와 통신한다
		- 생성자에 해당 객체의 repository를 준다
		- 서비스에 꼭 필요한 변수는 final로 지정해서 스프링에 알려준다
	- Repository :  가장 안쪽, DB와의 통신을 처리
		- DB Update는 Service에서 처리한다 -> 조회해서 변경후 다시 COMMIT

- DTO(Data Transfer Object)
	- 테이블에 사용할 객체로 데이터를 바로 입력 받는 것 보다 DTO객체를 따로 만들어서 객체로 옮기는 것이 안전하다
	- 각 레이어간에 Entity를 직접 사용하면 안되고 DTO를 사용해서 데이터를 주고받아야 한다
	- 같은 repository라도 POST 데이터가 다르면 각각 DTO를 정의해 준다

- REST
	- 주소는 명사, 요청은 동사로 의도를 명확히하는 방식
		- 명사는 복수형으로 작성
	- POST, GET, PUT, DELETE



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




