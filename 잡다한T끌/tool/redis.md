# REDIS
- Messaging: 중간 시스템을 통해서 발신자에서 수신자로 데이터를 전송하는 포괄적 용어
    - 서버와 클라이어트의 느슨한 연결
    - 수신자를 확장하기 쉽다
    - 마이크로서비스 아키텍처에 적합하다
    - Message Queuing: Point-to-Point Channel 방식으로 한 수신자만 메시지를 수신
    - Messaging Pub/Sub: 모든 수신자에게 메시지를 전송한다

- Redis Pub/Sub
    - 메시지가 저장되지 않고 전송된 후에 삭제 된다
    - 수신자가 메시지를 받는 것을 보장하지 않아서 별도의 구현이 필요할 수 있다

- *Spring stomp의 Message broker로 redis를 적용해서 구독과 발신을 관리할 수 있다*

- 레디스 락
    - 레디스는 아토믹을 보장
    - 일명 '따닥'을 백엔드에서 처리할 때 레디스로 값을 저장해서 같은값이 있으면 생성하지 않도록 만들수 있다
    - 분산락으로 여러 서버가 같은 작업을 동시에 하는 경우 레디스와 통신해서 하나의 서버에서만 실행되도록 할 수 있다

## 참고 자료
- [Spring-Redis Pub/Sub](https://brunch.co.kr/@springboot/374)
- [redis pub/sub 구현](https://daddyprogrammer.org/post/4731/spring-websocket-chatting-server-redis-pub-sub/)
- [ubuntu에 redis 설치](https://hayden-archive.tistory.com/429) 
- [linux에 redis설정](https://server-talk.tistory.com/472) 
- [mac redis 사용](https://wlswoo.tistory.com/44) 
- [redis 설정](https://moss.tistory.com/entry/Redis-%EC%84%9C%EB%B2%84-%EC%84%A4%EC%A0%95-%EC%A0%95%EB%A6%AC) 
- [Spring boot redis 2가지 방법](https://wildeveloperetrain.tistory.com/32)
- [Spring stomp에 redis 적용](https://thdwngus2.tistory.com/100)
- [RedisTemplate docs](https://docs.spring.io/spring-data/redis/docs/current/api/org/springframework/data/redis/core/RedisTemplate.html)
- [SimpMessageHeaderAccessor vs StompHeaderAccessor](https://stackoverflow.com/questions/46138831/what-is-the-major-difference-between-simpmessageheaderaccessor-vs-stompheaderacc)
- [redis @id](https://stackoverflow.com/questions/53286528/autoincrement-with-long-in-redis-using-spring-data-repository)
