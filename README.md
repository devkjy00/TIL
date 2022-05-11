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
	- https://github.com/southoftheriver/TIL/blob/master/Lecture/%EC%9B%B9%EA%B0%9C%EB%B0%9C%ED%94%8C%EB%9F%AC%EC%8A%A4_spa/project01/%EC%9A%94%EC%95%BD.md
	- https://github.com/southoftheriver/TIL/blob/master/Lecture/%EC%9B%B9%EA%B0%9C%EB%B0%9C%ED%94%8C%EB%9F%AC%EC%8A%A4_spa/project02/%EC%9A%94%EC%95%BD.md
	- https://github.com/southoftheriver/TIL/blob/master/Lecture/%EC%9B%B9%EA%B0%9C%EB%B0%9C%ED%94%8C%EB%9F%AC%EC%8A%A4_spa/project04/%EC%9A%94%EC%95%BD.md


</details>
<details>
    <summary> 3일차</summary>
- 구현할 시간이 부족해서 TIL정리할 시간도 없이 정신없이 프로젝트를 만들고 있다... 

- 참고한 자료
    - 라디오버튼 : https://living-only-today.tistory.com/107
    - html 태그 삭제 : https://www.fun25.co.kr/blog/python-remove-html-tag/?page=8
    - jinja2 주석 : https://webisfree.com/2018-11-01/python-jinja-template%EC%97%90%EC%84%9C-%EC%A3%BC%EC%84%9D-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95
    - mongodb 인증오류 : https://codingapple.com/forums/topic/%EB%AA%BD%EA%B3%A0db-%EC%A0%91%EC%86%8D%EC%9D%B4-%EC%9E%90%EA%BE%B8-%EC%8B%A4%ED%8C%A8%ED%95%A9%EB%8B%88%EB%8B%A4/

</details>
