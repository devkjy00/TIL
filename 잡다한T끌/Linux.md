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


