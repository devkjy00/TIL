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

- 스프링 시큐리티 활성화, 인증/인가 설정
	``` java
	@Configuration
	@EnableWebSecurity // 스프링 Security 지원을 가능하게 함
	public class WebSecurityConfig extends WebSecurityConfigurerAdapter {
		@Override
		protected void configure(HttpSecurity http) throws Exception {

			http.authorizeRequests()
					.antMatchers("/images/**").permitAll() 	// image 폴더를 login 없이 허용
					.antMatchers("/css/**").permitAll() 	// css 폴더를 login 없이 허용
					.anyRequest().authenticated()			// 어떤 요청이든 인증해야만 응답
					.and()
						// 로그인 요청은 허용
						.formLogin()
						.loginPage("/user/login") 			// 로그인 페이지 설정
						.defaultSuccessUrl("/") 			// 인증 성공하면 반환
						.failureUrl("/user/login?error")	// 인증 실패하면 반환
						.permitAll()
					.and()
						// 로그아웃 기능도 허용
						.logout()
						.permitAll();
		}
	}
	```
	- WebSecurityConfigurerAdapter
		- security 5.7버전 부터 deprecated된다
		- implementation group: 'org.springframework.security', name: 'spring-security-config', version: '5.6.3'
			- 버전을 낮춰서 사용

	- HttpSecurity : 인증, 인가의 세부적인 기능을 설정할 수 있도록 API를 제공해주는 클래스
		- https://catsbi.oopy.io/c0a4f395-24b2-44e5-8eeb-275d19e2a536
		- https://dev-setung.tistory.com/29
		- formLogin() : 로그인 방식에 대해서 설정
		- logout() : 로그아웃 설정
		- rememberMe() : SessionId가 만료되어도 쿠키에 remember-me 값이 유효하면 로그인 유
		- sessionManagement() : 세션을 설정한다
			```java
			http.sessionManagement()
				.maximumSessions(1)                // 최대 허용 가능 세션 수 , -1 : 무제한 로그인 세션 허용
				.maxSessionsPreventsLogin(true)    // true 동시 로그인 차단, false 기존 세션 만료
				.expiredUrl("/expired");           // 세션이 만료된 경우 이동 할 페이지
			```
		- authorizeRequests() : 접근하는 url에 따라 인가를 설정
			- antMatchers("/images/**").permitAll() : image 폴더를 login 없이 허용
			- antMatchers("/css/**").permitAll() : css 폴더를 login 없이 허용
		- csrf()
			- 서버에 요청 시 서버에서 발급해준 토큰을 HTTP 파라미터로 보냄으로써 보안을 강화하는 기능
