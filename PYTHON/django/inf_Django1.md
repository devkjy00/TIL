# Django 
설치
- pip install django==(버젼)

초기셋업(디렉토리에 파일자동생성)
- 터미널에서 생성을 원하는 디렉토리로 이동
- django-admin startproject 파일명
- 파일명으로 생성된 디렉토리는 프로젝트디렉토리를 담고있는 단순한 컨테이너 이다

django-admin 
- 작업을 관리하기위한 커멘드라인 유틸리티이다

생성된 파일

- ```manage.py```
    - 장고프로젝트 파일에 자동으로 생성된다
    - django-admin 와 비슷한 일을 한다
    - setting.py 파일을 가리키도록 DJANGO_SETTINGS_MODULE 의 환경변수를 설정한다

- 생성된 디렉토리
    - 실제 프로젝트의 파이썬 패키지이다.
    - 디렉토리명이 임포트할 때 쓰임

- ```__init__.py```
    - 아무것도 들어 있지 않은 빈 파일, 파이썬에게 현재 디렉터리가 파이썬 패키지임을 알려준다

- ```settings.py```
    - 장고프로젝트의 셋팅과 설정이 포함된 파일

- ```urls.py```
    - 장고프로젝트안의 URL을 선언하는 곳, 장고 사이트의 컨텐츠 목록이다

- ```wsgi.py```
    - WSGI프로토콜을 사용하는 웹서버가 프로젝트의 페이지를 보여주기 위해 가장먼저 사용하는 파일

웹 서버 실행
- 생성된 디렉토리로 이동
- python ```manage.py``` runserver 
    - 장고 개발용 웹 서버를 실행한다
    - 개발용 서버이기 때문에 실무개발에서 사용하면 안된다
    - runserver명령어는 디폴트로 8000번 포트의 내부IP에 웹서버를 실행한다

- python manage.py runserver 8080
    - 8080 포트에 서버를 실행한다

- IP변경
    - 포트번호와 함께 피라미터 입력
    - python manage.py runserver 0.0.0.0:8000
        - 모든 퍼블릭 IP의 8000번 포트에서 서버를 실행할 수 있다
        - 같은 네트워크 상의 다른 사람들에게 자랑할 수 있음

### Django 앱 만들기
앱은 python path의 어디에나 존재할 수 있다

- 디렉토리 생성
    - python manage.py startapp polls
        - polls 라는 이름의 디렉터리 생성
    
- 뷰 만들기
    - 생성된 디렉토리의 views.py 파일을 열고 코드를 입력
        ```py
        from django.http import HttpResponse

        def index(request):
            return HttpResponse("Hello, world. You're at the polls index.")
        ```
        - 가장 간단한 장고 뷰이다

- URL에 맵핑하기
    - 디렉터리 안에 URLconf를 만들기 위해서 urls.py 파일을 생성
        ```py
        from django.conf.urls import url
        from . import views

        urlpatterns = [
            url(r'^$', views.index, name='index')
        ]
        ```

- URLconf가 생성된 urls 모듈을 보도록 한다
    ```py
    from django.contrib import admin
    from django.urls import path
    from django.conf.urls import include, url

    urlpatterns = [
        url(r'^polls/', include('polls.urls')),
        # include(): 다른 URL패턴을 포함시킬때 사용한다
        # admin.site.urls만 제외
        path('admin/', admin.site.urls),
    ]
    ```
    - include()함수는 루트 URLconf가 다른 URLconf를 참조하도록 해준다
    - $/^ 이러한 문자는 문자열을 수정한다
    - 그리고 include 함수가 지정한 URLconf로 보내진다

- 앱은 자신의 URLconf인 polls/urls.py 안에 자신만의 URL을 가지고 있기 때문에 관리자가 원하는 root path로 설정할 수 있다