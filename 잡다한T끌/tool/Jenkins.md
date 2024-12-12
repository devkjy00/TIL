## 설치
```
1. Jenkins 저장소의 GPG 키를 추가
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/jenkins.gpg >/dev/null

2. Jenkins 저장소를 시스템에 추가
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

3. 패키지 목록 업데이트
apt-get update

4. 설치
sudo apt-get install jenkins

5. systmectl로 서비스 시작, 8080포트로 접속
6. 로그인 시 키 필요
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

- Docker 이미지 
```Dockerfile
FROM ubuntu:latest

# Update package lists and install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget gnupg openjdk-11-jdk

# Add Jenkins repository and key
RUN wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | gpg --dearmor | tee /etc/apt/trusted.gpg.d/jenkins.gpg >/dev/null && \
    echo "deb http://pkg.jenkins.io/debian-stable binary/" > /etc/apt/sources.list.d/jenkins.list

# Install Jenkins
RUN apt-get update && \
    apt-get install -y jenkins

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# Expose Jenkins default port
EXPOSE 8080

# Run Jenkins
CMD ["java", "-jar", "/usr/share/jenkins/jenkins.war"]
```

## 설정
- git credential 추가
    - Dashboard > Jenkins 관리 > Credentials > System > Global credentials (unrestricted)
