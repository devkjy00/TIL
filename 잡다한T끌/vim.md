

##### vim 열기
- vim -o3 : 3개의 분리된 vim창을 연다
- vim +%s/A/B/g 파일명: 해당 파일에서 입력한 모든글자를 바꾼다, A -> B


##### vim 중지
- <ctrl>z : vim을 중지시키고 터미널로 나간다
- fg : 중지시킨 vim 활성화
- 중지시킨 vim은 중첩가능 




##### 입력(표준모드)
- a, A : 커서 다음칸, 줄 마지막칸
- i, I : 커서 위치, 줄의 맨 앞
- o, O : 다음줄 추가, 이전줄 추가
- s, S : 커서 한글자 지우기, 한줄 지우기
- 명령 실행후에 입력

##### 이동(표준모드)
- H : 커서를 화면 맨위로
- M : 커서를 화면 중앙으로 
- L : 커서를 화면 맨 아래로
- z<enter> : 현재 줄을 맨위로 이동
- z. : 현재줄을 중앙으로 이동
- z- : 맨아래로 이동
- <enter> : 다음줄의 첫글자
- - : 다음줄의 마지막 글자
- ^ : 현재줄의 첫글자
- $ : 현재줄의 마지막 글자
- [n]G : 문서의 [n]번째 행으로 이동
- <ctrl>+u,d : 화면반을 위, 아래로 스크롤(b, f는 화면전체스크롤)
    
##### 삭제(표준모드)
- dw : 한 단어
- d0 : 줄 처음부터 커서 까지
- D : 커서부터 줄 끝까지
-[n] dd : 커서 줄, 아래로 [n]개의 줄 

##### 문자열찾기(명령 라인)
- /[문자열], ?[문자열] : 문자열 정,역방향검색
- n, N : 다음문자열, 이전문자열

#### 문자열 바꾸기(명령 라인)
- g : 한 줄에 매칭되는 것 전부, 없으면 각 줄에 한번씩만
- c : 매칭된 문자열 바꿀지 확인
- :[범위]/[찾을문자열]/바꿀문자열/[줄범위]
- :[범위]/[정규식]/''/''/''
- 범위
	- :s/a/b  현재 줄 하나
	- :s/a/b/g  현재 줄 모두
	- :10,20s  10~20번째 줄
	- :%s 	문서 전체
	

##### vim 열기
- vim -o3 : 3개의 분리된 vim창을 연다
- vim +%s/A/B/g 파일명 : 해당 파일에서 입력한 모든글자를 바꾼다, A -> B
- vim -p 파일명 파일명 : 탭을 여러개 생성

##### vim 중지
- <ctrl>z : vim을 중지시키고 터미널로 나간다
- fg : 중지시킨 vim 활성화
- 중지시킨 vim은 중첩가능 

##### vim buffer, window, tabs
> What is a buffer?
A buffer is an in-memory space where you can write and edit some text. When you open a file in Vim, the data is bound to a buffer. When you open 3 files in Vim, you have 3 buffers.
- :buffers, :files, :ls 		-> 현재 버퍼 확인가능
- :bnext, :bprevious, :buffer [n] 	-> 앞, 뒤, n번째 버퍼로 이동
- :bdelete, :qall(qall!, wqall) 	->  [n] 버퍼 닫기, quit-all버퍼전부 닫기
- window 
	- :split [파일명]/<ctrl>w+v  	-> 윈도우 위,아래 분할 (vsplit/<ctrl>w+s:왼,오분할)
	- <ctrl>w+h,j,k,l 		-> 윈도우 이동 왼,아,위,오(+c:윈도우닫기)

> tabs
- :tabnew [파일명] 		-> 새 탭 열기
- :tabclose, next, previous, last, first
- gt, gT 			-> 앞 탭, 뒷 탭


