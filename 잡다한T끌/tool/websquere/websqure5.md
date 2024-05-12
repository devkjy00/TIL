- W-Pack을 활용해서 XML파일을 JS파일로 변환한다

## 변화 과정
- websqure 5 
	- datacollection
	- gridview

- sp4 : scope, ifame -> wframe
	- wframe : 서버사이드로 html을 만들어서 제공
	- iframe은 각 iframe마다 별도로 설정파일 필요(css...) wframe은 완성된 형태의 태그로 html을작성해주기 때문에 관리가 편하다

- sp5 : wpack으로 xml을 html로 파싱
	- wpack은 github에서 관리

## WebSquare5 소스 구조
- XML내부에 HTML포함
- 헤더에 MODEL레이어를 정의
	- dataCollection : 통신 시점의 데이터를 주고 받을 때 사용(dto)
	- workflowCollection
	- submission : 어떤 함수를 호출할지, 통신 환경(동기/비동기), 데이터 형식등을 정의
		- 헤더값, 요청 url, dataCollection으로 데이터 매핑해주는 기능

- WRM 폴더 : 일반적으로 많이 사용되는 부분들을 제공
	- 로그인 관리, 메뉴 등록등



