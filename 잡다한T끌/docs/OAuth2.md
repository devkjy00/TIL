# OAuth2
## 개념
- OAuth : Access Token을 발급 받기 위한 일련의 과정들을 인터페이스로 정의해둔 것

- 용어
    - Client : 구현된 서버
    - Resource Owner : 유저
    - Authorization Server : 소셜 로그인 인증 서버
    - Resource Server : 소셜 로그인 API 서버

- 방식
    - Authorization Code Grand 
        1. 권한 부여 코드 요청 -> 유저 로그인 -> 권한 부여 코드 응답
        2. 권한 코드로 Access Token 요청 -> 응답
        3. Token으로 API(유저정보) 호출 
    
    - Implicit Grant 
        1. 권한 부여 코드 요청 -> 유저 로그인 -> Access Token 응답
        2. 권한 서버로 토큰 인증 요청(Validation) -> 응답
        3. Token으로 API(유저정보) 호출 

    - Resource Owner Password Credential Grant
        1. ID, PW로 로그인 -> 클라이언트가 권한 서버로 요청 -> Access Token 응답
        2. Token으로 API(유저정보) 호출
    
    - Client Credentials Grant 
        1. 클라이언트 없이 리소스 주인이 권한서버로 Token 요청 -> Access Token 응답
        2. Token으로 API(유저정보) 호출
    


- Spring OAuth2 순서
    1. 사용자가 소셜 로그인을 정상적으로 완료

    2. AbstractAuthenticationProcessingFilter에서 OAuth2 로그인 과정을 호출
        - UsernamePasswordAuthenticationFilter와 OAuth2LoginAuthenticationFilter가 상속해서 구현한다

    3. Resource Server에서 넘겨주는 정보를 토대로 OAuth2LoginAuthenticationFilter의 attemptAuthentication()에서 인증 과정을 수행

    4. attemptAuthentication() 처리 과정에서 OAuth2AuthenticationToken을 생성하기 위해 OAuth2LoginAuthenticationProvider의 authenticate()를 호출

    5. authenticate() 처리 과정에서 OAuth2User를 생성하기 위해 OAuth2UserService의 loadUser()를 호출

    6. OAuth2UserService의 기본 구현체는 DefaultOAuth2UserService이지만, 커스텀한 OAuth2User를 반환하도록 구현하고 싶었으므로 직접 구현한 CustomOAuth2UserService의 loadUser()가 호출됨



## 구현
- application.yml 파일 설정
    ``` yml
    spring:
        security:
            oauth2:
                client:
                    registration:
                        google:
                            client-id: # 발급 받은 client-id #
                            client-secret: # 발급 받은 client-secret #
                            scope: # 필요한 권한 #
                        kakao:
                            client-id: # 발급 받은 client-id #
                            client-secret: # 발급 받은 client-secret #
                            scope: # 필요한 권한 #
                            redirect-uri: "{baseUrl}/{action}/oauth2/code/{registrationId}"
                            authorization-grant-type: authorization_code
                            client-name: kakao
                            client-authentication-method: POST

                    provider:
                        kakao:
                            authorization-uri: https://kauth.kakao.com/oauth/authorize
                            token-uri: https://kauth.kakao.com/oauth/token
                            user-info-uri: https://kapi.kakao.com/v2/user/me
                            user-name-attribute: id
    ```

## 참고자료
- [Spring Security 와 OAuth 2.0 와 JWT 의 콜라보](https://velog.io/@tmdgh0221/Spring-Security-%EC%99%80-OAuth-2.0-%EC%99%80-JWT-%EC%9D%98-%EC%BD%9C%EB%9D%BC%EB%B3%B4)
- [OAuth2.0 구현을 위해 알아야 할 것들](https://developer88.tistory.com/372)
- [OAuth2 인증 방식](https://cheese10yun.github.io/oauth2/)
- [카카오 로그인 1](https://sudo-minz.tistory.com/77)
- [카카오 로그인 2](https://sudo-minz.tistory.com/78?category=1012147)
- [Team-Delight](https://github.com/Team-Delight/Delight-Server)
