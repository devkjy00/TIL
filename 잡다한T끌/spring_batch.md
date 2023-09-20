## Spring batch 
- 기능
    - 로깅/추적, 트랜잭션 관리, 작업 처리 통계, 작업 재시작, 건너뛰기, 리소스 관리 등 대용량 레코드 처리에 필수적인 기능 제공

- 개념
    - Job : 배치 처리 단위
    - JobInstance : Job의 실행 단위, 인스턴스
    - JobParameter : JobInstance를 구별하는 값
        - String, Double, Long, Date 4가지 형식 지원

    - JobExecution : JobInstance에 대한 실행 정보에 대한 객체
        - 같은 인스턴스 2번 실행시 Execution은 2번 실행된다

    - Step : Job의 배치 처리를 정의하고 순차적인 단계를 캡슐화, 일괄처리 제어정보를 가진다
        - Job은 1개 이상의 Step을 가진다
        
    - StepExcution : Step 실행 정보에 대한 객체
        - read, write, commit, skip 횟수등의 정보들이 저장된다

    - ExecutionContext : Job에서 데이터를 공유할 수 있는 데이터 저장소
        - JobExecutionContext : Commit 시점에 저장된다
        - StepExecutionContext : 실행 사이에 저장된다

    - JobRepository : Job실행시 Execution 정보들을 저장하고 조회하여 사용하게 된다
    
    - ItemReader : Step에서 Item을 읽어오는 인터페이스
    - ItmeWriter : 처리 경과물에 따라 Insert, Update, Queue의 Send등
    - ItemProcessor : Reader에서 읽어온 Item을 데이터 처리하는 역할
