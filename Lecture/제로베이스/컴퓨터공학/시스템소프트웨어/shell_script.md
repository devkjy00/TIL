### 기본
- .sh 확장자
- '#!/bin/bash'로 시작
    - # : 주석
- 파일은 실행 권한을 가지고 있어야 한다
    - chmod 700 a.sh

### 변수
```sh
#!/bin/bash
abc="abc"
def="def"

echo $abc $def

# 배열
arr=("a" "b" "c")
filelist=( $(ls) ) # 명령의 결과를 리스트로 생성

echo $arr   # 첫 데이터 출력
echo ${arr[*]}   # 모든 데이터 출력
echo ${#arr[@]}  # 배열 크기 출력

```

- 사전에 정의된 변수
```
 $$ : 쉘의 프로세스 번호
 $0 : 쉘스크립트 이름
 $1 ~ $9 : 명령줄 인수
 $* : 모든 명령줄 인수리스트
 $# : 인수의 개수
 $? : 최근 실행한 명령어의 종료 값
 0 (성공), 1 ~ 125 (에러)
 126 (파일이 실행가능하지 않음)
 128 ~ 255 (시그널 발생)
```

### 조건문
```sh
#!/bin/bash

# 숫자 계산
num=`expr \( 3 \* 5 \) / 4 + 7`
# (, ), * 앞에는 \를 붙인다
# 숫자, 변수, 기호 사이는 공백

# 숫자 계산
echo '1+2' | bc


# 조건문
if [ $num != 1 ]
then
    echo $num
else
    echo 'no'
fi
```
- 조건
    - ==, !=, -eq, -ne : 값이 일치하는지
    - -z : 문자가 null이면 참
    - -n : 문자가 null이 아니면 참
    - -it : less then
    - -le : less or equal
    - -gt : greater then
    - -ge : greater or equal

- 파일 검사
    - -e 파일명 # 존재하면 참
    - -d ...    # 디렉토리면 참
    - -h ...    # 심볼릭 링크파일이면 참
    - -f ...    # 일반파일이면 참
    - -r ...    # 읽기 가능이면 참
    - -s ...    # 크기가 0이 아니면 참
    - -u ...    # set-user-id가 설정되면 참
    - -w ...    # 쓰기 가능 상태이면 참
    - -x ...    # 실행 가능 상태이면 참

### 반복문
```
for 변수 in 변수1 변수2 ...
do 
    명령문
done

while [조건문]
do 
    명령문
done
```
```sh
for file in $(ls)
do 
    echo $file
done
```

- *tar*
    - 리눅스에서는 여러 파일을 한 파일로 묶은 것을 archive라고한다
    - 리눅스 파일 압축 단계
        - archive로 만든다(.tar)
        - gzip 프로그램을 사용해서 압축(.tar.gz)
    
    - 압축 명령어는 tar를 사용하되, 옵션을 사용해서 gzip기능 사용 

    

### 예제
- ping
    ```sh
    #!/bin/bash
    ping -c 1 192.168.0.1 1> /dev/null
    if [ $? == 0 ]
    then
        echo "게이트웨이 핑 성공"
    else
        echo "게이트웨이 핑 실패"
    fi
    ```
    - 0(표준입력), 1(표준출력), 2(표준에러)
        - 1> /dev/null : 표준 출력 내용을 버린다
    - -c 1 : 1번만 ping을 보낸다
