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



## 스프링 시큐리티 활성화
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

		- exceptionHandling()
			- accessDeniedPage("/..") : 접근 불가 페이지 URL 설정
## 패스워드 암호화
- 회원 등록 시 '비밀번호'는 사용자가 입력한 문자 그대로 DB 에 안 된다, '정보통신망법, 개인정보보호법' 에 의해 비밀번호는 암호화(Encryption)가 의무!!
	- 복호화가 불가능한 '일방향' 암호 알고리즘 사용이 필요
	- 입력받은 패스워드를 암호화 해서 비교

- 구현
 	```java
	// 스프링 시큐리티에서 '권고'하고 있는 'BCrypt 해시함수'를 사용
	@Bean
    public BCryptPasswordEncoder encodePassword() {
		return new BCryptPasswordEncoder();
	}

	// 패스워드 암호화
	String password = passwordEncoder.encode(requestDto.getPassword());
	```



## 로그인, 로그아웃 구현
- 스프링 시큐리티는 사용자의 Request가 Controller에 전달되기 전에 인증/인가를 확인하고 실패하면 Error Response를 사용자에게 보낸다
	- clien <-> Spring Security -> Controller(client에게 직접 응답) <-> Service

- 로그인 처리
	1. "post /user/login" 으로 로그인 요청
		- 로그인 시도 URL은 WebSecurityConfig 클래스에서 관리(.loginProcessingUrl("/user/login"))
	2. 인증관리자(Authentication Manager)가 Service 객체에게 id 전달
	3. DB에서 id로 찾은 세부정보로 생성한 객체를 인증관리자에게 전달
	4. id와 암호화된 password를 비교해서 인증

- 로그아웃 처리
	1. "get /user/logout" 으로 로그아웃 요청
	2. 서버 세션에 저장된 로그인 사용자 정보 삭제	

- 로그인 구현
	```java
	//
	// 허용할 것들을 설정
	//
	// 모든 요청은 인증
	.anyRequest().authenticated()
	.and()
		.formLogin()
		.loginPage("/user/login")   // get 로그인 View 제공 url
        .loginProcessingUrl("/user/login")  // post 로그인 처리 url
        .defaultSuccessUrl("/")     // 인증 성공 url
        .failureUrl("/user/login?error")    // 인증 실패 url
        .permitAll()
    .and()
        // 로그아웃 기능 허용
		.logout()
	 	.logoutUrl("/user/logout") // 로그아웃 처리 url
	 	.permitAll();
	```

- 회원 정보 조회해서 인증관리자에게 전달
	```java
	@Service
	public class UserDetailsServiceImpl implements UserDetailsService {

		private final UserRepository userRepository;

		@Autowired
		public UserDetailsServiceImpl(UserRepository userRepository) {
			this.userRepository = userRepository;
		}

		public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
			User user = userRepository.findByUsername(username)
					.orElseThrow(() -> new UsernameNotFoundException("Can't find " + username));

			return new UserDetailsImpl(user);
		}
	}
	```

- 회원 정보를 저장할 객체 구현 
	```java
	public class UserDetailsImpl implements UserDetails {

		private final User user;

		public UserDetailsImpl(User user) {
			this.user = user;
		}

		public User getUser() {
			return user;
		}

		@Override
		public String getPassword() {
			return user.getPassword();
		}

		@Override
		public String getUsername() {
			return user.getUsername();
		}

		@Override
		public boolean isAccountNonExpired() {
			return true;
		}

		@Override
		public boolean isAccountNonLocked() {
			return true;
		}

		@Override
		public boolean isCredentialsNonExpired() {
			return true;
		}

		@Override
		public boolean isEnabled() {
			return true;
		}

		@Override
		public Collection<? extends GrantedAuthority> getAuthorities() {
			return Collections.emptyList();
		}
	}
	```
	- @AuthenticationPrincipal 어노테이션으로 주입할 객체, UserDetails를 implements


## 권한 설정
- 스프링 시큐리티에 권한(Authority) 설정방법
	- 인증 관리자가 정보를 전달하는 회원ServiceImpl을 통해서 권한 설정
	- 권한을 1개 이상 설정 가능
	- 권한 이름 규칙 : ROLE_ 로 시작해야 한다("ROLE_ADMIN")
	```java
	public class UserDetailsImpl implements UserDetails {
		// ...

		@Override
		public Collection<? extends GrantedAuthority> getAuthorities() {
			SimpleGrantedAuthority adminAuthority = new SimpleGrantedAuthority("ROLE_ADMIN");
			Collection<GrantedAuthority> authorities = new ArrayList<>();
			authorities.add(adminAuthority);

			return authorities;
		}
	}
	```
	- GrantedAuthority
	- SimpleGrantedAuthority
	- 권한 명을 Enum 으로 정의 해서 테이블에 저장하고 사용하는 것이 좋다
	- @Secured("권한 명")으로 API요청을 특정 권한만 가능하도록 제한할 수 있다

	
## OAuth
- 회원가입을 하지 않고 다른 웹사이트에 있는 자신의 정보에 대한 접근 권한을 부여하는 접근 위임을 위한 개방형 표준으로 HTTP 기반의 보안 프로토콜이다


## JWT(Json Web Token)
- JWT 장/단점
    -  장점
        - 동시 접속자가 많을 때 서버 측 부하 낮춤
        - Client, Sever 가 다른 도메인을 사용할 때
            - 예) 카카오 OAuth2 로그인 시 JWT Token 사용
            
    -  단점
        - 구현의 복잡도 증가
        - JWT 에 담는 내용이 커질 수록 네트워크 비용 증가 (클라이언트 → 서버)
        - 기생성된 JWT 를 일부만 만료시킬 방법이 없음
        - Secret key 유출 시 JWT 조작 가능

- JWT 구조
	- JWT 는 누구나 평문으로 복호화 가능
	- 하지만 Secret Key 가 없으면 JWT 수정 불가능
		- 결국 JWT 는 **Read only 데이터**
	
- 주요 클래스
	- JWTAuthFilter : API요청 Header에 전달되는 JWT 유효성 인증
		- 모든 API 에 대해 JWTAuthFilter 가 JWT 확인
		- 로그인 전 허용이 필요한 API 는 예외처리 필요 ⇒ FilterSkipMatcher
    		-  ex) 로그인 폼 페이지, 로그인 처리, css 파일 등
	
	- FormLoginFilter : 회원 폼 로그인 요청 시 username / password 인증
		- 인증에 성공시 응답에 JWT 포함
		- Authorization: BEARER "JWT문자열"  과 같이 헤더에 넣어서 전달할 수 있다

- JWT 로그인 적용인증 처리 (Filter)
    - Filter 는 Client 의 API 요청이 Controller 에 전달되기 전, 사전처리를 하는 영역
    - 즉, Controller 에 도달하기 전에 인증 처리를 하기 위해 사용
    1. **FormLoginFilter** : 회원 폼 로그인 요청 시 username / password 인증
        1. **POST "/user/login"** API 에 대해서만 동작 필요
            1. "GET /user/login" 가 처리되지 않게 하기 위해 API 주소 변경
                1. "GET /user/login" → "GET /user/loginView"
        2. Client 로부터 username, password 를 전달받아 인증 수행
        3. 인증 성공 시
            1. FormLoginSuccessHandler 통해 JWT 생성
            2. 이후 Client 에서는 모든 API 응답 Header 에 JWT 를 포함하여 인증
            
    2. **JWTAuthFilter** : API 요청 Header 에 전달되는 JWT 유효성 인증



