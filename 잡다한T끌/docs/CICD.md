# CICD
## 개념
- github actions 구성요소
	- Workflow : 레포지토리에 추가할 수 있는 일련의 자동화된 커맨드의 집합
		- 하나 이상의 Job으로 구성
		- push, PR, 시간등 다양한 event에 의해 실행
		- .github/workflows 디렉토리에 YAML파일로 저장
	
	- Event : push, pr, commit 등을 트리거로 workflow를 실행
	- Job : 동일한 Runner에서 실행되는 여러 Step(테스트, 빌드 등)
		- 의존관계를 설정해서 순서 설정 가능
	
	- Step : 커맨드로 실행할 수 있는 각각의 Task를 의미

	- Action : Job을 만들기 위한 Step을 결합한 독립적 커맨드, 생성된 Action을 불러와 사용가능

	- Runner : Github Actions Workflow 내에 있는 Job을 실행시키기 위한 애플리케이션
		- 가상 환경에서 실행가능



## 참고자료
- [github actions 구성요소, cicd](https://ji5485.github.io/post/2021-06-06/build-ci-cd-pipeline-using-github-actions/)
- [spring boot&gradle cicd 1~4](https://stalker5217.netlify.app/devops/github-action-aws-ci-cd-1/)
- [AWS CodeDeploy 그룹 생성, 역할 에러](https://velog.io/@16fekim/AWS-CodeDeploy-%EA%B7%B8%EB%A3%B9-%EC%83%9D%EC%84%B1-%EC%97%AD%ED%95%A0-%EC%97%90%EB%9F%AC)
- [code deploy 실행오류, log보기 ](https://sarc.io/index.php/aws/1327)
- [code deploy appspec 오류 해결](https://stackoverflow.com/questions/53103139/the-codedeploy-agent-did-not-find-an-appspec-file-within-the-unpacked-revision-d)
	- zip 파일을 폴더안에 생성하면 안된다	
		```zsh
		폴더안에 압축하면 안된다
		run: zip -r ./$PROJECT_NAME.zip ./deploy

		run: zip -r ./$PROJECT_NAME.zip .
		```
- [aws 설정](https://velog.io/@hwany/AWS-EC2-CodeDeploy-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0) 
- [github 파일 암호화](https://kimmj.github.io/git/git-secret/)
- [git-secret-reveal on github actions](https://stackoverflow.com/questions/65385671/git-secret-reveal-failed-on-github-actions)
