## 스프링 프레임워크 설정
- 프로젝트 구조
    ```
    - main
        - java
        - resource
            - appConfig.xml
            - webAppConfig.xml
        - webapp
            - web.xml
    ```
    - web.xml : 웹 애플리케이션 환경설정 파일, 스프링 구동을 위한 설정이 대부분
    - webAppConfig.xml : 스프링 웹 관련 환경설정 파일, 스프링 MVC설정과 웹 계층을 담당
        - `<mvc:annotation-driven>` : MVC 기능 활성화
        - `<context:component-scan>` : basePackages를 포함한 하위 패키지를 검색해서 빈 등록
        - `<bean>` : 스프링 빈을 등록한다
    - appConfig.xml : 스프링 애플리케이션 관련 환경설정 파일, 비즈니스 로직, 도메인 계층, 서비스 계층, 데이터 저장 계층을 담당
        - `<tx:annotation-driven/>` : 스프링의 어노테이션 기반 트랜잭션 관리자(@Transactional)를 활성화한다
        - bean 등록
            - 데이터베이스에 접근할 dataSource를 등록한다
        - JPA
            - JPA를 사용하려면 LocalConatainerEntityManagerFactoryBean을 스프링 빈으로 등록해야 한다
                - persistenceUnitName : 영속성 유닛 이름을 지정
                - packagesToScan : @Entity가 붙은 클래스를 검색할 시작점 지정
                - jpaVendorAdapter : 사용할 JPA벤더(하이버네이트)를 지정
            - 트랜잭션 관리자를 등록한다(JPA는 ort.springframework.orm.jpa.JpaTransactionManager를 사용)
            - @Repository에서 JPA예외를 AOP가 처리하도록 하는 빈등록(org.springframework.dao.annotation.PersistenceExceptionTranslationPostProcessor)





