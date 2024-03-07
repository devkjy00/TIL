- docs.docker.com : 도커 매뉴얼

## 용어
- docker hub : 프로그램 저장소의 역할
	- hub.docker.com

- image : 프로그램의 역할
	- docker hub에서 pull해서 다운로드

- container : 프로세스의 역할
	- image를 run해서 container 실행

## 기본명령어
- docker --help : 명령어 출력
- search 이미지명 : 검색
- pull 이미지명 : 이미지 다운로드
- images : 설치된 이미지 정보

- build PATH : 해당 경로에 Dockerfile으로 image를 빌드 한다
	- 프로그램을 업데이트 하려면 항상 새로운 이미지를 빌드해야한다
	- -t 이미지명:태그명 : 사용자 태그를 설정할 수 있다

- run 이미지명 : 컨테이너 생성
	- -p port1:port2 : 1으로 들어오는 포트를 도커의 2번포트로 포워딩
	- -d : 백그라운드에서 실행
	- --name : 지정된 이름으로 컨테이너 생성

	- -p 8080:80 -v [폴더경로] httpd - 호스트의 파일을 컨테이너에서 접근한다 
		- 컨테이너는 종료하면 설정정보가 제거된다, 호스트의 파일을 컨테이너가 사용하도록 하면 수정, 버전관리가 용이

	- 마지막 인자는 컨테이너에 전달할 명령 "/bin/bash"가 기본값 이다

- ps : 실행중인 컨테이너 정보
	- -a : 정지된 컨테이너도 출력

- stop 컨테이너명 : 정지
	- kill 컨테이너명 : 종료
- start 컨테이너명 : 시작 
- restart 컨테이너명 : 재실행

- exec 컨테이너명 명령어 : 컨테이너 내부의 커널에서 명령어 실행
	- exec -it 컨테이너명 /bin/[sh, bash, zsh] : 컨테이너를 지속적연결해서 명령실행
		- -it 는 지속적으로 연결
		- /bin/shell 로 커널 환경 선택
	- exit : 컨테이너환경에서 나가기
	- 컨테이너 환경은 리눅스이고 기본적인 프로그램이 깔려있지않아서 apt, yum 설치를 해야 한다

- logs 컨테이너명 : 로그 정보 출력
	- -f : 로그 지속적으로 출력

- rm 컨테이너명 : 컨테이너 제거(중지된 컨테이너만 가능)
	- --force : 강제 제거
- rmi 이미지명 : 이미지 제거
- attach  컨테이너명 : 컨테이너 접속


## 도커 파일 생성
- DockerFile
	```docker
	FROM python:3.8

	ADD requirements.txt .

	RUN pip install -r requirements.txt

	ADD templates templates

	ADD app.py .

	CMD ["python", "app.py"]
	```
	- FROM : 기본으로 사용할 base image
	- ADD src dst : 파일이나 폴더를 dst 위치에 저장
	- RUN script : script를 실행
	- CMD : docker image를 실행할 때 자동으로 실행되는 커맨드


