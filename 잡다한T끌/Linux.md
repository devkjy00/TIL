## 기본명령어
- man 명령어	: 명령어 매뉴얼보기
- pwd 	: 현재 디렉토리
- ls 	: 현재 디렉토리 파일보기
	- -a	숨겨진폴더 보기
	- -l 	관련정보같이 보기
		- d(dir),-(file),l(link)
		- wrx(접근권한)
		- 사용자 그룹
		- 수정날짜
	- -i 	inode 번호를 출력

- cd	: 이동
	- /  	    가장상위디렉토리
	- /폴더명   폴더로 이동
	- ..	    상위폴더로 이동
	- ../폴더명 상위의 폴더명으로이동
	- ~/ 	    home 위치기준

  
- mkdir : 폴더 생성
- touch : 파일 생성
- rm	: 삭제
	- -f    파일삭제
	- -r	폴더도 삭제가능

- mv 	: 소스이동
	- mv file1 file2  파일명바꾸기
	- mv file2 ./dir2/. 위치바꾸기

- cp	: 복사하기
	- -r 	디렉토리 복사
	- cp file1 ./dir2/file2 복사해서경로에 저장
	 
### 파일 출력
- cat 	: 파일 출력
	- cat 파일명 | more 	모두출력
	- cat 파일명 > 파일명  파일복사
	- cat 파일명 >> 파일명 파일뒤에 붙여넣기
	- 명령어에서 명령어로 데이터를 보내는 방식
		- | : 파이프라인
		- > : 꺽쇠(Redirection)

- head	: 10라인만 출력
- tail 	: 끝에서 10라인만출력
	- -f 파일명 	: 라인이추가되면 바로 추가된라인 출력
		- 로그데이터를 쉽게 확인할 수 있다

### less 텍스트뷰어
- less 파일명
	- vi는 파일전체를 메모리에 올리는 것에 비해 less는 화면에 출력되는 내용만 메모리에 올려서 무거운 파일도 가볍게 확인하고 자원낭비를 막을 수있다

### tar 압축
- tar cvfz target.tar.gz 파일명 파일명 ...
	- tar를 사용해 gz로 압축
	- * 로 폴더의 모든 파일압축
	- c(create),z(gzip)

- tar xvfz 파일명	
	- 압축해제
	- x(extract)


### grep 문자열검색
- grep 문자열 파일이름
	- grep abc *.txt
	- 문자열을 포함한 파일을 찾아준다

- -H	어떤파일인지 출력
- -w	정확히 일치하는 문자열만검색

### 접근권한
- chmod	: 접근 권한설정
	- wrxwrx--x 771 ,user/group/other
		- wrx를 이진법으로 표현
		- write, read, execute
	- chmod 764 a.txt  -> wrxwr-w--
	- chmod g+w a.txt  -> group에 write권한을 +한다(-하면삭제)

### link
- link
	- 컴퓨터의 방식으로 저장한 자료를 inode로 link해서 사용자에게 보여주는 방식(저장된 자료를 다른위치에서 참조하는 방식)
	- 자료는 참조횟수(link파일개수)만큼 Ref값을 가진다  
		- Ref값이 0일때만 삭제가능
	- Hard Link
		- Ref에 1을 더해주고 Link파일을 하나더 생성 같은 원본 파일을 참조한다(포인터)
		- Hard Link파일이 하나라도 있으면 원본은 삭제되지 않는다, 파일만 가능
		- ln source target 	하드링크 생성(원본소스, 만들소스명)

	- Soft(Symbolic) Link
		- 바로가기기능
		- Link 파일을 참조하는 Link파일을 만드는 방식, 파일,폴더 모두가능
		- ln -s source target 	소프트링크 생성(원본소스, 만들소스명)

### sudo
- root계정은 ip설정, 네트워크작업, 웹서버, 인증서설치, rebooting등의 작업을 하기위한 수퍼관리자이다

- sudo명령어로 root계정의 권한을 사용한다

- root권한부여(root계정을진행)
	- vi /etc/sudoers
	- 계정이름 ALL=(ALL:ALL) NOPASSWD:ALL

### which 명령어의 위치찾기
- which python3

### top 모니터링
- o <> 입력된 기준으로 정렬

### ping 네트워크 모니터
- ping google.com
	- google.com 네트워크 연결정보를 모니터링 할 수 있다
	- time= 은 레이턴시로 값이 적을 수록 인터넷이 빠른것

- nslookup google.com
	- 구글의 ip주소를 알려준다

### kill 
- sudo kill -9 process.id

- ps -ef | grep 파일명
	- 첫번째 수가 process.id이다


