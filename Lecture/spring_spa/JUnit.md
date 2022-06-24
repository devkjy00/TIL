## 개념
JUnit: 자바 프로그래밍 언어용 단위 테스트 프레임워크

- given - when - then
- Edge 케이스 : 입력가능한 모든 케이스를 고려해야 한다
	- 값이 null이거나 사용할 수 없는 범위의 값인, 빈 문자열, 빈 이미지등의  경우 독단적 결정보다는 관련 담당자들과 협의 진행후 결정하는 것이 좋다
	

## 어노테이션
- @Test : 테스트할 메서드임을 명시
- @Disabled : @Test를 무시한다
- @DisplayName("...") : 지정된 테스트 명으로 표시할 것을 명시
- @BeforeEach : 모든 테스트 메서드가 수행되기 이전마다 한번씩 실행하는 메서드 명시
- @BeforeAll : 모든 테스트 메서드 이전에 한번만 수행되는 메서드임을 명시
- @AfterAll, @AfterEach


## Mock 객체 
- Controller, Service, Repository는 서로 연결되있어서 분리해서 테스트 해야 한다
	- 가짜 객체를 주입해서 분리할 수 있다
	- 동일한 클래스명, 함수명을 사용

- Mokito 라이브러리
	- @InjectMocks : Mock객체를 주입할 클래스임을 명시(테스트할 클래스)
	- @Mock : 주입할 객체임을 명시
		- when().thenReturn()으로 mock객체의 반환값을 정할 수 있다
