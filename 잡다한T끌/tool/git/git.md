
### 레포지토리 가져와서 다른곳에 저장하기 시나리오
1. `git clone --bare https://github.com/sinanuozdemir/quick-start-guide-to-llms.git`: 이 명령어는 원격 GitHub 저장소인 "https://github.com/sinanuozdemir/quick-start-guide-to-llms.git"를 복제합니다. `--bare` 옵션은 작업 디렉토리를 생성하지 않고 저장소를 클론합니다. 이는 주로 다른 저장소로 푸시하기 전에 작업을 수행하는 데 사용됩니다.
    
2. `cd quick-start-guide-to-llms`: 이 명령어는 새로 생성된 로컬 저장소 디렉토리로 이동합니다. 이 디렉토리는 이전 단계에서 복제한 GitHub 저장소의 클론입니다.
    
3. `git push --mirror git@github.com:kimwooglae/quick-start-guide-to-llms.git`: 이 명령어는 로컬 저장소의 모든 브랜치와 태그를 목적지 저장소로 푸시합니다. `--mirror` 옵션은 원본 저장소의 모든 내용을 복사하여 대상 저장소에 동기화합니다. 이 경우, `git@github.com:kimwooglae/quick-start-guide-to-llms.git`는 푸시 대상의 URL입니다.


- git 한글 깨짐
	- git config --global core.quotepath false

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
