## MVC & MTV
- MVC 패턴을 사용해서 더 큰 프로젝트를 효과적으로 다룰 수 있다
    - Model : 안전하게 데이터를 저장
    - View : 데이터를 유저에게 적절한 형태로 보여준다
    - Control, Template : 사용자의 입력과 이벤트에 반응하여 Model과 View를 업데이트

## Django 개념
- MVC의 흐름
    - user(입력) -> controller(요청) -> model(데이터) ->
    -> controller(요청) -> view(데이터출력) -> user

- Django 흐름
    - Web(URL입력) -> URL Dispatcher(URL분석) -> View(필요한데이터요청) -> Model(데이터베이스에 접근) -> DataBase(데이터전송) -> Model(데이터수집) -> View(데이터가공) -> Template(UI생성) -> Web
- 더 자세하게
    - WEB -> wsgi.py 
    - -> (request) urls.py 
    - -> (view)[views.py <-> form.py(UI관리)] 
    - -> [models.py <-> MANAGERS(SQL언어역할) <-> DATABASE(sqlite, mysql)] 
    - -> view.py 
    - -> (template) example.html 
    - -> (responce) wsgi.py -> WEB

> wsgi (Web Server Gateway Interface)
- 다양한 웹 서버와 장고를 적절하게 결합

## Project와 App
- 프로젝트 생성
    - 생성 디렉토리로 이동
    - django-admin startproject tutorial

- app 생성
    - ./manage.py startapp community

## settings.py
- 프로젝트 환경 설정 파일
    - DEBUG 
        - 개발중 코드를 디버그 할 수 있다
        - 배포 할 때는 false로 해야 한다
    
    - INSTALLED_APPS
        - pip로 설치한 앱, 사용자 app 추가
    
    - MIDDELWARE_CLASSES
        - 요청과 응답 사이에서 인증, 보안과 관련된 기능
    
    - TEMPLATES
        - template관련 설정, html, 변수 등을 다룬다

    - DATABASES
        - 다양한 데이터베이스 엔진과 연결설정
    
    - STATIC_URL
        - 정적 파일의 URL(css, javascript, image 등등)설정 파일

## manage.py
- 프로젝트 관리 명령어파일
- 주요 명령어
    - startapp : 앱 생성
    - runserver : 서버 실행
    - createsuperuser : 관리자 생성
    - makemigrations app : app의 모델 변경 사항 체크
    - migrate : 변경 사항을 DB에 반영
    - shell : 쉘을 통해 데이터확인
    - collectstatic : static파일을 한 곳에 모음