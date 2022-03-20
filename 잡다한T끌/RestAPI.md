Representational State Transfer API 
- 로이 필딩은 웹(HTTP)의 장점을 최대한 활용할 수 있는 아키텍처로써 REST를 발표

- REST 구성
    - 자원(Resource) : URI
        - Uniform Resource Identifier : 웹 기술에서 사용하는 논리적 또는 물리적 리소스를 식별하는 고유한 문자열 시퀀스
    - 행위(Verb) : HTTP 메소드
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