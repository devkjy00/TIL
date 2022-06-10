## Authentication(인증), Authorization(인가)
- 인증 : 사용자 신원을 확인(로그인)
- 인가 : 사용자 권한을 확인(접근 권한)


## 쿠키와 세션
- HTTP는 Stateless -> 상태를 저장하지 않아서 사용자를 구별하지 못한다
	- HTTP 상태 정보를 쿠키나 세션에 저장해서 유지한다

- 쿠키
	- 클라이언트 정보를 저장하는 데이터 파일로 웹 브라우저에 저장된다
	- 구성요소 : Name(pk), Value(값), Domain(쿠기가 저장된 도메인), Path(쿠키가 사용되는 경로), Expires(만료기한)
	- 만료 기한 :  브라우저를 종료해도 만료기한 전까지 유지된다
	- 용량 : 크롬기준, 도메인 당 180개, 쿠키 당 4KB
	- 보안 
		- 클라이언트에서 쿠키 정보를 쉽게 변경가능
		- 쿠키를 훔쳐가거나 삭제당하기 쉽다
	
- 세션
	- 서버에서 클라이언트 상태를 유지하기 위해 사용하는 데이터
	- 클라이언트에게 유일한 세션ID를 부여하고 세션ID와 함께 필요한 정보를 서버에 저장
	- 세션 쿠키 : 세션 ID는 쿠키값으로 저장되어서 사용된다
	- 만료 기한 : 브라우저 종료, 로그아웃, 서버의 유지기간 초과시 만료
	- 용량 : 세션 저장소 크기 
	- 보안
		- 서버에 저장해서 비교적 안전하다



## 스프링 시큐리티
- Dependency 추가를 해줘야 한다
	- implementation 'org.springframework.boot:spring-boot-starter-security'

- 스프링 시큐리티 활성화
	``` java
	@Configuration
	public class SecurityConfiguration {

		@Bean
		public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {

			http.authorizeHttpRequests((authz) -> authz
					.anyRequest().authenticated())
				.httpBasic(withDefaults());
			return http.build();
		}
	}

	```
	- HttpSecurity
		- [HttpSecurity, WebSecurity의 차이](https://velog.io/@gkdud583/HttpSecurity-WebSecurity%EC%9D%98-%EC%B0%A8%EC%9D%B4)
