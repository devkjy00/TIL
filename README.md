# TIL

<h2> 항해 99 </h2>
<details>
    <summary> 2일차</summary>
- 오류
	- client = MongoClient('mongodb://3.34.44.93', 27017, username="anwjsrlrhwkd", password="spa0000")
    - 여기에 넣어야 할 IP값을 모르겠다, DB IP인거 같은데
	- client = MongoClient('내AWS아이피', 27017, username="아이디", password="비밀번호")
	- 원래는 인증오류가 뜨는데 AWS  IP로 바꾸면 타임아웃 오류가 뜬다

	-> AWS에서 27017 포트 인바운드 규칙을 추가했다
	-> AWS에 mongodb를 실행시켜주지 않아서 생긴 문제
	-> 1주차 강의를 건너뛰어서 생긴 문제……
	- 또 다른 문제로 이어진다(robo3t)

	-> 팀원과 공유해서 이야기 해본 결과 기존의 사용하던 방법으로 DB를 연결해서 해결했다
		- Linux에 설치한 mongodb를 쓰지 않고 클라우드에 연결해서 사용

	-  강의자료가 혼동을 주는 점이 조금 아쉽다

- TIL 정리
	- <a href="https://github.com/southoftheriver/TIL/blob/master/Lecture/%EC%9B%B9%EA%B0%9C%EB%B0%9C%ED%94%8C%EB%9F%AC%EC%8A%A4_spa/project02/%EC%9A%94%EC%95%BD.md">정리</a>
	- <a href="https://github.com/southoftheriver/TIL/blob/master/Lecture/%EC%9B%B9%EA%B0%9C%EB%B0%9C%ED%94%8C%EB%9F%AC%EC%8A%A4_spa/project04/%EC%9A%94%EC%95%BD.md">..</a>


</details>
<details>
    <summary> 3일차</summary>
- 구현할 시간이 부족해서 TIL정리할 시간도 없이 정신없이 프로젝트를 만들고 있다... 

- 참고한 자료
    - <a href="https://living-only-today.tistory.com/107">라디오 버튼</a>
    - <a href="https://www.fun25.co.kr/blog/python-remove-html-tag/?page=8"> html 태그 삭제</a>
    - <a href="https://webisfree.com/2018-11-01/python-jinja-template%EC%97%90%EC%84%9C-%EC%A3%BC%EC%84%9D-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95">jinja2 주석</a>
    - <a href="https://codingapple.com/forums/topic/%EB%AA%BD%EA%B3%A0db-%EC%A0%91%EC%86%8D%EC%9D%B4-%EC%9E%90%EA%BE%B8-%EC%8B%A4%ED%8C%A8%ED%95%A9%EB%8B%88%EB%8B%A4/">mongodb 인증오류 </a>

</details>
<details>
    <summary> 4일차</summary>

- 오늘은 각자 구현한 코드를 merge해서 완성된 프로젝트로 배포해야 한다

- 웹 미니 프로젝트 느낀점
    - 클라이언트와 서버의 통신이 생각보다 간단하지 않다
    - 클라이언트에서 보내준 자료들이 로직에 큰 영향을 미치게 된다, 이로 인해 캡슐화가 깨질 가능성이 있을 꺼 같다
        - 데이터의 흐름에 대해서 파악하고 그에 따른 구현이 필요하다
        - 로직을 프론트에서 구현할지 백엔드에서 구현할지 에대한 기준은?
        - URI 설계가 중요하다, 일종의 인터페이스 역할을 하는 것 같다
	
	> REST API를 적용한 구현의 필요성을 더 크게 느낀 것 같다

- 참고자료
    - <a href="http://daplus.net/mongodb-mongo-%EC%BD%98%EC%86%94%EC%97%90%EC%84%9C-objectid%EB%A1%9C-%EA%B0%9D%EC%B2%B4%EB%A5%BC-%EC%96%B4%EB%96%BB%EA%B2%8C-%EA%B2%80%EC%83%89%ED%95%A9%EB%8B%88%EA%B9%8C/">.</a>
    - <a href="https://ssamko.tistory.com/38">..</a>
    - <a href="https://velog.io/@leyuri/TIL-input-%EC%97%90%EC%84%9C-%EC%9E%85%EB%A0%A5-%EA%B8%80%EC%9E%90%EC%88%98-%EC%A0%9C%ED%95%9C%ED%95%98%EB%8A%94-2%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95">...</a>


- 매니저님 QnA
    - 데이터베이스에서 정렬하는게 제일 빠르다
    - 프론트에 구현할지 백 엔드에 구현할지의 기준은 성능

</details>
