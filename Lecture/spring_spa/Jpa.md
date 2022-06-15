## 개념
- ORM(Object-Relational Mapping)
	- 개발자가 SQL작성이 아닌 비즈니스 로직 개발에 집중하게 해준다

- JPA(Java Persistence API) : 자바 ORM기술에 대한 표준 명세
- Hibernate : JPA를 구현한 사실상 표준, 스프링 부트에서 기본으로 사용된다

## 영속성 컨텍스트
- JPA
	- 객체 - ORM, 영속성 컨텍스트 매니저(entity context manager) - DB

- 영속성 컨택스트 매니저는 객체와 DB의 소통을 효율적으로 관리한다
	
- 영속성 컨텍스트 캐시
	- 1차 캐시
		1. Entity 저장 시 {Id: Entity} 값을 영속성 컨텍스트에 1차 캐시한다
			- 삭제시에 영속성 컨텍스트 1차캐시에서도 삭제된다
		2. 조회 시에 Id로 캐시를 확인해서 있으면 가져오고 없으면 DB 쿼리해서 다시 캐시
		- 장점 	
			- DB조회 횟수를 줄인다
			- DB row 1개 당 객체 1개가 사용되는 것을 보장(객체 동일성 보장)
				- DB튜플이 자바 객체로 여러개 생성되면 어떤 객체를 저장할 지 알 수 없다 -> DB와 같은 원칙을 적용

- Entity 업데이트 주의 사항
	```java
	public User updateUserFail() {
		// 회원 "user1" 객체 추가
		User user = new User("user1", "뷔", "콜라");
		// 회원 "user1" 객체를 영속화 
		User savedUser = userRepository.save(user);

		// 회원의 nickname 변경
		savedUser.setNickname("얼굴천재");
		// 회원의 favoriteFood 변경
		savedUser.setFavoriteFood("버거킹");
		// -> DB가 아닌 1차 캐시의 객체를 변경한다

		// 회원 "user1" 을 조회
		User foundUser = userRepository.findById("user1").orElse(null);
		// 중요!) foundUser 는 DB 값이 아닌 1차 캐시에서 가져오는 값
		assert(foundUser == savedUser);             
	}
	```
	- @Transactional을 메서드에 선언해서 Dirty check업데이트 해줄 수 있다

## JPA 연관관계
- Entity 클래스의 필드위에 연관관계 어노테이션을 명시
- @OneToMany, @ManyToOne, @OneToOne, @ManyToMany
- @JoinColumn(name = "외래키", nullable = false)
	- 외래키를 지정해서 연관관계를 정의한다



## Spring Data JPA
- 스프링에서 JPA를 Wrapping해서 필수적으로 쓰는 반복적 코드들을 Spring Data JPA가 대신 작성 해준다
	- Repository 인터페이스만 작성하면 스프링이 알아서 구현해준다

- 기본 메서드
	- save()
	- findAll(), findBy{컬럼명}()
	- findBy{컬럼명}Containing() : 매개변수 값이 포함된 튜플을 찾는다
	- findAll{컬럼명}Between() : 값의 범위가 매개변수x 부터 y에 포함된 튜플을 찾는다
	- count()
	- delete()

- [Spring Data JPA](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#jpa.query-methods)


## 페이징, 정렬
- 페이지네이션(Pagination), 페이징(Paging) 구현
	```java
	// Controller
	@GetMapping("/api/products")
    public Page<Product> getProducts(
            @RequestParam("page") int page,
            @RequestParam("size") int size,
            @RequestParam("sortBy") String sortBy,
            @RequestParam("isAsc") boolean isAsc,
            @AuthenticationPrincipal UserDetailsImpl userDetails
    ) {
        Long userId = userDetails.getUser().getId();
        page = page - 1;
        return productService.getProducts(userId, page, size, sortBy, isAsc);
	
	// Service
    public Page<Product> getProducts(Long userId, int page, int size, String sortBy, boolean isAsc) {
        Sort.Direction direction = isAsc ? Sort.Direction.ASC : Sort.Direction.DESC;
        Sort sort = Sort.by(direction, sortBy);
        Pageable pageable = PageRequest.of(page, size, sort);

        return productRepository.findAllByUserId(userId, pageable);
    }
