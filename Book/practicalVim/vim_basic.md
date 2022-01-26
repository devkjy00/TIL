### 표기법
- <C-r>0	: Ctrl과 r을 동시에 누르고 나서 0을 누른다
- f{}		: f를 누른 다음에 문자 입력가능
- m{a-zA-Z}	: m을 누른 다음 영문 입력가능

### 명령행 모드 사용
- : 	: Ex명령을 실행하는 명령행모드
- /		: 정방향검색을 위한 명령행모드
- ?		: 역방향검색을 위한 명령행모드

### 검색에 일치하는 본문 강조
- /{검색어}<CR>

### Vim Factory Settings
- $ vim -u NONE -N
	- -u NONE은 vimrc 파일을 사용하지 않고 실행된다, 기존의 모든 설정과 플러그인을 제외한 채 동작한다
	- -N 플래그는 nocompatible설정을 활성화 하는 기능으로 vi호환 모드로 전환되지 않도록 방지한다

### Vim 스크립트
- Vim에 새로운 기능을 추가하거나 수정하는데 사용된다
- 이 언어는 그 자체로 완벽한 스크립트 언어로 동작한다
- Vim스크립트는 따로 실행하지 않아도 Vim에서 언제든 사용할 수 있다

### 선택 기능
- Vim 기능 중 일부는 컴파일 과정에서 제외할 수 있다
- --with-features=tiny 설정을 사용해서 Vim을 빌드했다면 아주 핵심적인 기능을 제외하고는 모두 비활성화 상태로 제공한다
	- small, normal, big, huge로 설정할 수 있다
	- :h +feature-list로 플래그가 제공하는 기능목록을 확인할 수 있다

- :version 명령으로 어떤 기능이 포함되어 있는지 확인할 수 있다

- GUI(그래픽사용자인터페이스), TUI(터미널환경)
	- GUI기반 vim은 GVim, MacVim이 있다




#### vim 열기
- vim -o3 : 3개의 분리된 vim창을 연다
- vim +%s/A/B/g 파일명: 해당 파일에서 입력한 모든글자를 바꾼다, A -> B
- 파일 불러 오기           :e 파일명        (Tab키로 자동 완성 사용 가능)
- 새 빈 파일 만들기        :new             (Ctrl+wn)
- 새 이름으로 파일 작성    :e 새파일이름


#### vim 중지
- <ctrl>z : vim을 중지시키고 터미널로 나간다
- fg : 중지시킨 vim 활성화
- 중지시킨 vim은 중첩가능 




#### 입력(표준모드)
- a, A : 커서 다음칸, 줄 마지막칸
- i, I : 커서 위치, 줄의 맨 앞
- o, O : 다음줄 추가, 이전줄 추가
- s, S : 커서 한글자 지우기, 한줄 지우기
- 명령 실행후에 입력

#### 이동(표준모드)
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
    
#### 삭제(표준모드)
- dw : 한 단어
- d0 : 줄 처음부터 커서 까지
- D : 커서부터 줄 끝까지
-[n] dd : 커서 줄, 아래로 [n]개의 줄 

#### 문자열찾기(명령 라인)
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

#### 한번에 문자넣기, 삭제(visual)
- 한번에 주석처리: 블럭처리 -> :'<,'>norm i//(앞에 해당글자 추가)
- 한번에 주석해제: 블럭처리 -> :'<,'>norm 2x (앞에서2글자삭제)

#### 한번에 tab 하기 (visual)
- 블럭처리하고 <, >  
 
#### vim buffer, window, tabs
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


#### 키 맵핑
- map(recursive), noremap(non-recursive)
	- recursive일경우 맵핑된 키가 또 다른 키를 맵핑할 경우 마지막 루트의 키를 입력하게 된다

- <leader>
	- 기본적으로 '/'를 가리킨다(<leader>a -> /a)
	- let mapleader="," 로 설정하면 ','로 바뀐다: 

- 모드별로 설정할 수 있다
	- map : Normal, Visual, Operator-pending 
	- nmap : Normal
	- vmap : Visual

- <, >를 사용해서 키를 맵핑
	- CR(엔터), C(ctrl), A(alt), S(shift) 

- http://jaeheeship.github.io/console/2013/11/15/vimrc-configuration.html
