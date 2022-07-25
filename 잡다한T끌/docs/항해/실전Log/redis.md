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

## 참고 자료
- [Spring-Redis Pub/Sub](https://brunch.co.kr/@springboot/374)
- [redis pub/sub 구현](https://zkdlu.github.io/2020-12-29/redis04-spring-boot%EC%97%90%EC%84%9C-pub,sub-%EB%AA%A8%EB%8D%B8-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/)
- [linux에 redis 설치](https://www.psjco.com/26)
- [mac redis 사용](https://wlswoo.tistory.com/44) 
