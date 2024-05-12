## ec2에 code deploy agent를 다운받아 설치하는 과정에서 ruby2.x 버전을 설치할 수 없어서 deploy 설치 안됨
- 현재 ec2의 ubuntu 버전 22.04 LTS
	- ubuntu 버전 별로 ruby를 설치하는 방법이 다르다

- [Ubuntu 22.04에 CodeDeploy설치법](https://ssue95.tistory.com/31)
	```bash
	#!/bin/bash
	# Ubuntu 22.04에서의 CodeDeploy 설치
	sudo apt-get update
	sudo apt-get install ruby-full ruby-webrick wget -y
	cd /tmp

	wget wget https://aws-codedeploy-ap-northeast-2.s3.amazonaws.com/releases/codedeploy-agent_1.3.2-1902_all.deb
	#가장 최신버전의 CodeDeploy를 찾아서 설치했으나, 원하는 버전이 있다면 해당 버전으로 설치해도 무방함

	mkdir codedeploy-agent_1.3.2-1902_ubuntu22 #폴더명은 자율
	dpkg-deb -R codedeploy-agent_1.3.2-1902_all.deb codedeploy-agent_1.3.2-1902_ubuntu22
	sed 's/Depends:.*/Depends:ruby3.0/' -i ./codedeploy-agent_1.3.2-1902_ubuntu22/DEBIAN/control
	dpkg-deb -b codedeploy-agent_1.3.2-1902_ubuntu22/
	sudo dpkg -i codedeploy-agent_1.3.2-1902_ubuntu22.deb
	systemctl list-units --type=service | grep codedeploy

	sudo service codedeploy-agent status
	```


