# 맥 아파치 설정
- 아파치 활성화
    - sudo apachectl start
        - stop, restart 
    - http://localhost/ 또는 http://127.0.0.1 (IPAddress)로 접속
    - It works! 가 뜨면 활성화 된것
        - DocumentRoot 지정된 폴더인 Library/WebServer/Documents 디렉토리에 있는 index.html.en 파일
    - 8080포트는 두번째 설치된 웹서버에 접속한다
- userdir 활성화
    1. /private/etc/apache2/extra 디렉토리의 httpd-userdir.conf 파일을 편집
    2. userdir.conf 파일에서 '# Include /private/etc/apache2/users/*.conf' ,'LoadModule userdir_module libexec/apache2/mod_userdir.so' 부분의 주석처리(# )를 삭제
    3. 사용자 폴더에 접근 권한 주기

- DocumentRoot 수정
    1. /private/etc/apache2/extra 디렉토리의 httpd-userdir.conf 파일을 편집
    2. DocumentRoot: The directory out of which you will serve your 부분의 주석 삭제
    3. DocumentRoot "/Users/{User Name}/www"
        <Directory "/Users/{User Name}/www"> 경로 바꾸기

# http
- Hyper Text Transfer Protocol
- http:// 는 웹서버를 통해서 파일을 읽는다
- file:// 는 웹서버 없이 경로의 파일을 읽는다

- 403 Forbidden error
    - URL에 엑세스 할 수 있는 권한이 없을 때 발생하는 오류