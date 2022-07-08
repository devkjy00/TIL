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

- JPA의 EntityManager를 매개변수로 JPAQueryFactory를 생성해서 



### 구현
    
    
### 참고자료
- [Query DSL 설정](https://nomoreft.tistory.com/m/25)
- [우아콘2020 QUERY DSL](https://www.youtube.com/watch?v=zMAX7g6rO_Y)
    - 엔티티를 save할 때 연관관계인 엔티티에 ID값만 들어가 있으면 조인관계가 만들어진다
    - 조건이 복잡한 쿼리문의 경우 id값만 가져와서 id값을 조건으로 다시 쿼리문을 작성(서브쿼리처럼)하면 성능을 최적화할 
- [우아한 형제들 Query DSL 사용법](https://github.com/Youngerjesus/Querydsl)
- [QueryDsl 을 사용한 쿼리 튜닝과 N+1 해결](https://velog.io/@recordsbeat/QueryDsl-%EA%B3%BC-JPA-Repository-%EC%82%AC%EC%9A%A9%EC%B2%98)
- [에디블로그](https://jessyt.tistory.com/category/Develop/spring-data)
    - @Id 필드 값이 있는 Entity를 save하면 값을 가져와서 변경됬는지 검사하고 저장한다(sql문 2번 실행) -> 1차 캐시로 값을 변경하고 @Transaction하면 1번만 실행
- [JPAQuery<T> 와 JPAQueryFactory 차이](https://www.inflearn.com/questions/37565)
- [BooleanBuilder, BooleanExpression](https://whitekeyboard.tistory.com/306)
