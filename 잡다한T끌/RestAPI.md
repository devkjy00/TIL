Representational State Transfer API 
- 로이 필딩은 웹(HTTP)의 장점을 최대한 활용할 수 있는 아키텍처로써 REST를 발표

- REST 구성
    - 자원(Resource) : URI
        - Uniform Resource Identifier : 웹 기술에서 사용하는 논리적 또는 물리적 리소스를 식별하는 고유한 문자열 시퀀스
            - 행위가 아닌 정보의 자원을 표현해야 한다
    - 행위(Verb) : HTTP 메소드(GET, POST, PUT, DELETE)
    - 표현(Representations)

- REST 특징
    - Uniform(유니폼 인터페이스)
        - URI로 지정한 리소스에 대한 조작을 표준화한 인터페이스로 수행하는 아키텍처 스타일
    
    - Stateless(무상태성)
        - REST는 작업을 위한 상태정보를 따로 저장, 관리하지 않는다
    
    - Cacheable(캐시 가능)
        - HTTP의 기존 인프라를 그대로 활용한다
    
    - Self-descriptiveness(자체 표현 구조)
        - REST API 메시지만 보고도 쉽게 이해하는 구조
    
    - Client-Server 구조
        - REST서버는 API제공, 클라이언트는 사용자 인증/컨텍스트등을 관리, 서로 독립적이다
    
    - 계층형 구조
        - REST서버는 다중 계층으로 구성, 보안, 로드밸런싱, 암호화 계층을 추가

- URI설계 시 고려사항
    - 슬래시(/)는 계층관계를 나타내는데 사용, URI마지막 문자로 사용하지 않는다
        - http://abc.com/home/room
    - 하이픈(-)은 URI가독성을 위해 사용, 밑줄(_) 은사용하지 않는다
    - URI경로에는 소문자가 적합
    - 파일 확장자는 URI에 포함시키지 않는다 

- HTTP 응답 상태 코드
    - 200 : 요청을 정상처리
    - 201 : POST를 통한 리소스 생성요청을 정상처리
    - 400 : 요청이 부적절한 경우
    - 401 : 사용자가 인증되지 않은 상태에서 보호된 리소스를 요청한 경우
    - 403 : 응답하고 싶지 않은 리소스를 요청했을때 (404사용 권장)
    - 405 : 요청한 리소스에 사용 불가능한 Method사용
    - 301 : 요청한 리소스에 대한 URI가 변경되었을 때
    - 500 : 서버에 문제가 있을 경우
    