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



