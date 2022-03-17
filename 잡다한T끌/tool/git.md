### config
- 속성값 저장
	- git config --globla <속성값> <저장할 값>


- 로그인 정보 저장
	- credential.helper <저장할 값>
	- cache --timeout=<int> : 입력한 초단위 시간만큼 저장
	- store	: 반영구적으로 저장

- 이메일을 지정해줘야 커밋이 잔디밭에 기록된다!!!



### .gitignore
- no .a files
	- *.a

- but do track lib.a, even though you're ignoring .a files above
	- !lib.a

- only ignore the TODO file in the current directory, not subdir/TODO
	- /TODO

- ignore all files in the build/ directory
	- build/

- ignore doc/notes.txt, but not doc/server/arch.txt
	- doc/*.txt

- ignore all .pdf files in the doc/ directory
	- doc/**/*.pdf
