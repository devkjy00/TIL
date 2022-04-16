
# git 명령어
- commit 
    - -am 'msg' : '변경'된 파일만 모두 추가/커밋
    - --amend : 커밋된 메시지를 수정할 수 있다
    - -v : 커밋 메시지 작성 파일에서 커밋된 부분들을 확인할 수 있다(commit과 diff확인을 동시에 하는것)

- switch 브랜치명 : 브랜치 교체

- add
    - -a : 모든 변경사항 추가
    - 파일명 : 해당 파일만 추가
    - -p --patch : 부분별로 변경된 코드를 vim으로 출력하고 옵션을 선택한다 
        - 같은 파일의 변경사항도 따로 추가할 수 있다

- fetch : 원격 저장소의 최신 커밋을 로컬로 가져오고 적용은 하지 않는다
    - fetch한 후에 checkout하면 변경사항을 적용 전에 확인할 수 있다
    
- push
    - -u : push할 원격 브랜치를 설정

- pull : 원격 저장소의 최신 커밋을 로컬로 가져와 merge 또는 rebase

- reset 
    - --hard : 수정사항 완전히 삭제
    - --mixed : (기본값) repository에서 working directory로 이동(커밋을 되돌리고 파일보존)
    - --soft : repository에서 staging area로 이동(커밋을 스테이징상태로 변경)
    - HEAD : ~,^로 이전 커밋을 삭제 가능

- rebase
    - -i 수정할 커밋의 이전log : log 이후의 커밋들을 수정할 수 있다(기본값:바로전 커밋)
        - p, pick : 그대로 두기
        - r, reword : 커밋 메시지 변경
        - e, edit : 수정을 위해 정지
            - 설정한 log의 변경사항이 커밋된 상태로 돌아가서 커밋을 수정할 수 있다
            - rebase --continue 로 다시 돌아올수 있다
        - d, drop : 커밋 삭제
        - s, squash : 이전 커밋에 합치기

- restore 파일명
    - 파일을 이전 커밋으로 되돌린다
    - --staged 파일명 : 스테이징된 파일을 Working 영역으로 되돌린다

- checkout 
    - HEAD : 브랜치의 헤드를 뒤로 이동, 이전 버전으로 파일 되돌리기
        - 원래의 브랜치에서 갈라진 익명의 브랜치를 만들어서 버전을 이동한다
            - 이전의 브랜치로 돌아가 이전커밋에서 새로운 분기를 할 수 있다
        - ^, ~ : 커밋을 한단계 뒤로(중복가능)
        - -: HEAD없이 입력, 이동을 한단계 되돌리기
        - (커밋해시) : 지정된 커밋으로 이동
    - 원격저장소명/브랜치명 : 해당 브랜치의 최신 커밋으로 이동

- git rm, mv
    - 삭제, 이동된 파일의 변경이 바로 스테이징에 추가 된다

- help : 명령어 설명
    - git 명령어 -h : 해당 명령어 설명
    - git help 명령어 : 명령어 설명에 대한 페이지열기

- config (--global)
    - --globla : 전역값에 대한 명령
        - core.autocrif (윈도우:true/맥:input): 줄바꿈 호환 문제 해결
            - 윈도우와 맥 사이에 줄바꿈을 다르게 인식해서 생기는 오류를 방지 
        - push.default current : 로컬과 동일한 브랜치명으로 push
        - init.defaultBranch 브랜치명 : 기본 브랜치명
        - alias.별칭 명령어 : git 명령어를 별칭으로 설정
        
    - --list : git 설정값 출력
        - 속성 설정값 : 속성을 설정값으로 변경, 속성만 쓰면 출력
    
    - -e : git설정 파일 vim으로 열기
    
- stash : 변경사항을 stash공간으로 옮기고 현재 버전에서 없앤다
    - pop : stash한 변경사항을 다시 가져와서 적용시키고 stash를 삭제한다
    - -p : 변경된 부분별로 옵션을 선택할 수 있다
    - -m "메시지" : stash 메시지와 함께 적용
    - list : stash된 변경사항과 stash번호, 메시지를 출력
    - apply stash@{stash번호} : 해당 stash 변경사항만 다시 적용한다
        - apply해도 list에 남아있어서 지워줘야 한다
    - drop stash@{stash번호} : 해당 stash 변경사항을 삭제
    - branch 브랜치명 : 해당 브랜치명으로 stash에 내용을 pop한다
    - clear : stash 내용 지우기


    


## git 이해
- Snapshot 방식을 사용한다
    - 매 버전마다 모든 파일을 저장한다
        - 델타 방식 : 매 버전마다 변경된 파일만 저장한다

    - 커밋이 매우 많아졌을 때 원하는 버전만 알고있으면 쉽게 관리할 수 있다
        - 델타 방식은 버전을 계산해서 관리해야 한다

- 분산 버전 관리를 사용한다
    - 원격 저장소에 의존적이지 않다
    - 로컬에서 작업할 수 있고 push, pull로 동기화 할 수 있다

- 커밋 메세지 컨밴션
    - 일반적인 작성 방식
        ```
        type: subject

        body (optional)
        ...
        ...
        ...

        footer (optional)
        ```
    
    - type
        - feat : 새로운 기능
        - fix : 버그 수정
        - docs : 문서 수정
        - style : 공백, 세미콜론등 스타일 수정
        - refactor : 리팩토링
        - perf : 성능 개선
        - test : 테스트 추가
        - chore : 빌드과정 또는 보조 기능 수정
    
    - Subject : 커밋 작업 내용 간략히 설명
    - Body : 필요시 자세한 설명
    - Footer 
        - 특정 이슈에 대한 해결 작업일 때
        - Breaking Point 가 있을때

    - git 이모티콘 사이트 : https://gitmoji.dev/


- 용어 
    - HEAD : 현재 속한 브랜치의 가장 최신 커밋, 현재 파일의 시점
        - reset이나 checkout등에 사용
 