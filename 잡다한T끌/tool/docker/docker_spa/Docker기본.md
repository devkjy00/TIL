### Docker
- 도커는 프로그램 실행환경을 쉽게 구현시켜주는 플랫폼
	- 서버 운영에서 인프라 관리와 어플리케이션 작성을 분리하게 해준다
	- 서버에서 간단한 이미지를 가지고 실행만 시킨다
	
- 가상화 기술(VMware, VirtualBox)
	- 하이퍼바이저를 거쳐서 성능의 손실이 발생
	- 완벽한 OS를 생성하지만 크기가 크고 성능 손실이 있다

- 도커
	- 자체 기능으로 프로세스 단위의 격리환경을 만들어서 성능 손실이 거의 없다
	- host OS의 kernel을 공유해서 사용, 성능 손실이 거의 없다
### Docker 구성요소
- docker image & container
	- image : 어플리케이션에 필요한 모든 것이 생성 되어있는 파일
	- container : image를 실행시킨 것, 독립성 보장을 위해 네트워크나 저장소가 분리

- registry : image를 저장하는 공간
- dockerd : docker API requests를 받아서 docker object(image, container등)을 관리
- client : docker를 사용하기 위한 cli

