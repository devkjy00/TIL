## query DSL
- 사용 이유
    1. 정적 타입을 사용해서 컴파일 시점에서 쿼리문의 오류, 오타를 발견할 수 있다
    2. 동적인 쿼리를 작성할 수 있다
    3. 메서드 추출을 통해 제약조건등을 재사용할 수 있다

- 단점
    1. Gradle와 intellij 버전에 따라 설정이 다르다

### 개념
- Q-class, Q-타입 : @Entity 클래스마다 생성되는 클래스
    - 쿼리 작성시에 사용되서 Type-safe하게 작성할 수 있다
    - Gradle 설정을 통해 소스코드에서 Q-클래스를 import해서 사용

- JPA의 EntityManager



### 구현
- 예시
    ```java
    void queryDsl_findPostsByMyCriteria_Three() {
        EntityManager entityManager = testEntityManager.getEntityManager();

        JPAQuery<Post> query = new JPAQuery<>(entityManager);
        QPost qPost = new QPost("p");

        List<Post> posts = query.from(qPost)
            .where(qPost.content.contains("hi")
                .and(qPost.comments.size().gt(0))
            ).orderBy(qPost.id.desc())
            .fetch();
    }
    ```