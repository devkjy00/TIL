## 웹 소켓 개념
- 양 방향 통신 : 클라이언트와 서버가 서로 원할 때 데이터 전송 가능
- 실시간 네트워킹 : 연속된 데이터를 빠르게 노출 시키는 데 사용된다
- 웹 소켓을 지원하는 브라우저의 경우 웹 소켓 프로토콜을 지원한다
 
- 예전 기술
    - polling : 일정 주기로 계속 서버에 요청을 보내는 방법
        - 불필요한 요청을 생성, 애매한 실시간성
    - long polling : 서버에 요청을 보내고 이벤트가 생겨서 응답이 올때까지 대기, 응답을 받으면 끊고 다시 재요청
        - 한번에 많은 데이터를 받으면 polling과 같다
    - streaming : 서버에 요청을 보내고 연결이 끈기지 않은 상태에서 계속 응답을 받음
        - 클라이언트에서 서버로 데이터 송신이 어렵다

    - 모두 HTTP통신 이기 때문에 요청, 응답에 Header가 불필요하게 크다


- 웹 소켓의 한계
    - 문자열을 주고 받는 것만 가능하다
    - 문자열 해독은 온전히 어플리케이션이 담당하고 형식이 정해져있지 않아서 쉽지않다
        - -> sub-protocols를 사용해서 주고 받는 메시지의 형태를 약속하는 경우가 많다

    - 웹 소켓을 지원하지 않는 브라우저의 버전이 있을 수 있다
        - SockJS, Socket.io를 사용해서 소켓을 사용하는 것같은 환경을 구성할 수 있다
        - webSocket을 지원하지 않으면 streaming, 그것도 안되면 polling을 사용
## 연결 과정
- 핸드쉐이킹 : http(80)이나 https(443)으로 GET 요청을 보낸다
    - *request Header*
        - Host : 웹 소켓 서버의 주소
        - Upgrade : websocket 
            - 현재 프로토콜에서 업그레이드시킬 프로토콜(http -> ws)
        - Connection : Upgrade옵션
            - Upgrade 필드가 헤더에 있을 경우 반드시 작성해야함
        - Sec-WebSocket-Key : 길이가 16비트인 임의의 수를 base64로 인코딩한 값
            - 클라이언트와 서버의 인증 키
        - Origin : 클라이언트 주소
        - Sec-WebSocket-Protocol : chat, superchat...
            - 클라이언트에서 요청하는 서브 프로토콜, 순서로 우선순위 부여
        - Sec-WebSocket-Version : ...
            - 서버에서 여러 프로토콜 혹은 프로토콜 버전을 나눌때 사용하는 정보
    
    - *response Header*
        - 101, Switching Protocols 
            - 연결이 성공했을 때 http 상태 코드
        - Upgrade : websocket 
        - Connection : Upgrade옵션
        - Sec-WebSocket-Accept : Sec-WebSocket-Key값을 처리한 값
            - 클라이언트에서 처리한 값과 일치하지 않으면 연결 x

- 핸드쉐이킹 완료 후 통신 : ws(80)이나 wss(443)으로 프로토콜 변경
    - Message : 여러 frame이 모여서 구성하는 하나의 논리적 메시지
    - frame : 통신에서 가장 작은 단위의 데이터
        - 작은 헤더와 payload로 구성
    
    - UTF-8 인코딩으로 0x00 (전송할 데이터, UTF-8 payload) 0xff 와 같은 형태로 전송
        - 텍스트와 바이너리만 전송할 수 있다

## WebSocketConfiurer로 구현
```java

@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {

    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(new SocketTextHandler(), "/..")
            // 직접 구현한 핸들러 클래스
            // 웹 소켓 연결 주소
            .setAllowedOrigins("*") // cors 설정
            .withSockJS(); // SockJS 설정
}

public class SocketTextHandler extends TextSocketHandler {
    // binary핸들러도 있다
    
    private final Set<WebSocketSession> sessions = ConcurrentHashMap.newKeySet();

    @Override
    public void afterConnectionEstablished(WebSocketSession session){
        sessions.add(session); // 웹 소켓 커넥션 정보를 Collection으로 관리
    }

    @Override
    protected void hanbleTextMessage(WebSocketSession session, TextMessage message) throws Exception{
        String payload = message.getPayload();
        JSONObject jsonObject = new JSONObject(payload);

        for (WebSocketSession s : sessions){
            s.sendMessage(new TextMessage("Hi" + jsonObject.get("user") + "! How may I help you?"));
        }
    }

    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throw Exception {
        session.remove(session) // 커넥션이 끊어지면 삭제
    }
}

```

## STOMP(Simple Test Oriented Message Protocol)
- 채팅 통신을 하기위한 형식을 정의
- HTTP와 유사하게 간단한 방식으로 정의되서 해석하기 편한 프로토콜
    - 메시지 브로커를 이용해서 쉽게 메시지를 주고받을 수 있게 한다
    - 메시지 브로커 : 발신자의 메시지를 수신자에게 전달하는 어떤 것
- 일반적으로 웹소켓 위에서 사용되는 서브 프로토콜


- 명령, 헤더, 바디로 구성되어있다
    ```
    COMMAND 
    header1:value1
    header2:value2

    BodyBodyBody^@
    ```
    - COMMAND : CONNECT, SEND, SUBSCRIBE, DISCONNECT...
    - 헤더와 바디는 빈라인으로 구분, 바디의 끝은 null

- STOMP 장점
    - 하위 프로토콜 혹은 컨벤션을 따로 정의할 필요가 없다
    - 연결 주소마다 Handler 클래스를 정의할 필요없이 Controller로 구현할 수 있다
    - 외부 Messaging Queue를 사용할 수 있다(RabbitMQ, redis..)
    - Spring security를 사용할 수 있다

## WebSocketMessageBrokerConfigurer로 구현
```java

@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry){
        // prefix가 붙은 메시지를 발행시 브로커가 처리
        registry.enableSimpleBroker("/queue", "/topic"); // 내장 브로커 사용
        // queue는 1:1 일 때 topic 1:N 일 때 관습적으로 사용되는 prefix이다

        // 메시지 핸들러(controller)로 라우팅되는 prefix
        registry.setApplicationDestinationPrefixes("/app");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        // 웹 소켓 연결 주소 
        registry.addEndpoint("/gs-guide-websocket")
            .setAllowedOrigins("*")
            .withSockJS();
    }
}


// Handler
@Controller
public class GreetingController {

    @MessageMapping("/hello") // "/app/hello"로 오는 요청 처리
    @SendTo("/topic/greeting") // message를 처리해서 반환할 경로
    public Greeting greeting(HelloMessage message) throws Exception {
        return new Greeting("hello" + HtmlUtils.htmlEscape(message.getName()))

    }
}

```






## 참고자료
- [테코톡 아론](https://www.youtube.com/watch?v=rvss-_t6gzg)
- [web socket](https://dev-gorany.tistory.com/3)
- [ConcurrentHashMap](https://devlog-wjdrbs96.tistory.com/269)
