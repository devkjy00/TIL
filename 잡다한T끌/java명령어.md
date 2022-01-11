- javac, java 

- javac -d (컴파일,저장)
    - javac -d [바이트 코드 파일 저장 위치] [소스 경로/*.java]
    - javac -d bin src/com/test/.*java

- java -c (실행)
    - java -c [바이트 코드 파일 저장 위치] [패키지 이름 ... 클래스 이름]
    - java -c bin com.test.Hello

http://sjava.net/2008/02/java-%EB%AA%85%EB%A0%B9%EC%96%B4%EC%9D%98-%EC%98%B5%EC%85%98-%EC%A0%95%EB%A6%AC/