## day27
- ***Redis Pub/Sub***

레디스로 Messaging을 결정하고 구현에 들어갔다<br>
간단하게 스프링에 redis코드를 구현하고 나서 redis를 서버에<br>
설치하고 커맨드라인에서 통신을 시도했는데 계속해서 연결에 실패했다<br>
알고보니 ec2보안 그룹에서 포트허용설정을 해주지 않아서 안됬었다<br>

## day28
- ***Spring-redis***

하루종일 스프링으로 redis의 Pub/Sub을 구현하는 방법을 구글링하면서<br>
내가 원하는 정보를 찾아해맷다.. 이상적인 자료를 찾기가 너무 힘들었는데<br>
같이 공부하는 분의 도움을 받아서 구현 이해도를 높일 수 있었다<br>
결국에는 공식문서가 가장 도움이 되는 것 같다.. 중요한 클래스를 찾아서<br>
메서드를 확인하는게 가장 정확하고 빠른 길인듯 한다..<br>

## day29
- ***변경사항, redis***

redis를 적용하려고 했던 이유가 서버가 바뀌어도 실시간 처리가 유지되도록 하기 위해서<br>
였다.. 그런데 redis pub/sub은 서버끼리 실시간 통신을 하는 방식으로 사용되는 경우가<br>
많은 것 같다(구글링에서는) 그래서 클라이언트에서 redis로 바로 연결을 하던지<br>
아니면 메시지 브로커 없이  세션 정보를 redis에 저장해서 캐쉬로 사용하는<br>
방법이 있을 꺼 같은데<br>
처음 생각했던 방향과 많이 다른 것 같아서 일단 redis를 빼고 구현에 들어갔다<br>
기존에 있는 Stomp 로직에 redis를 메시지 브로커로 끼워넣는 방식을 생각했는데<br>
현재로써는 길이 보이지가 않는다..<br>

## day32
- ***CRUD, redis 활용방안***

추가 기능인 워크스페이스 기능 구현에 들어가면서 CRUD기능을 구현했다<br>
이번엔 cascade와 batch size를 설정해서 더 간단하고 빠르게 구현해보았다<br>
값을 생성하거나 가져올때 훨씬 편하게 가져올 수 있게 된듯 하다<br>
그리고 팀원들의 접속 상태를 redis에 저장해서 처음 들어온 팀원이 바로<br>
다른 팀원들의 접속 상태를 전달받도록 구현하기로 했다<br>
그리고 이제 발표까지 얼마 안 남았다 발표자로써 열심히 준비해보자<br>

