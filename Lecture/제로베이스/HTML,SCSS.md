### Block vs Inline
- Block : 한줄에 하나씩
- Inline : 한줄에 여러개, 요소 사이에 여백이 생긴다

### HTML Emmet : HTML 자동완성 플러그인
https://docs.emmet.io/cheat-sheet/
- 셀렉터 형식으로 작성후 tab
- 자식(하위)요소 : > 
	- div>ul>li
- 형제 요소 : +
	- div+p+bq
- 올라가기 : ^
	- div+div>p>span+em
- 반복하기 : *
	- ul>li*5
- 그룹화 : ()
	- div>(header>ul>li*2>a)+footer>p
- 클래스 : .
	- div.container
- 아이디 : #
	- div#header
- 속성: [attr]
	- a[title="hello world"]
- 넘버링 : $
  - ul>li.item$*5


### CSS 속성 작성 팁
- 레이아웃을 먼저 잡고 순서대로 작성한다
	1. box-sizing: border-box | content-box
		- border, content를 기준으로 width, height를 잡는다
	2. position: relative | absolute | fixed | sticky
		- 자기자신 | 부모 | 브라우저(고정) | 브라우저(스크롤시변화) 를 기준으로 top, left, right, bottom을 잡는다
	3. display: flex | block | inline | inline-block | none
		- flex : 한줄에 여러개, 공간이 충분하지 않으면 한줄에 하나씩
		- block : 한줄에 하나씩
		- inline : 한줄에 여러개, 요소 사이에 여백이 생긴다
		- inline-block : 한줄에 여러개, 공간이 충분하지 않으면 한줄에 하나씩
		- none : 화면에서 사라진다	
	4. margin: 100px
	5. padding: 100px
	6. width: 100px
	7. height: 100px
	8. border: 1px solid #000
	9. background: #fff
	10. font-size: 16px
	11. font-weight: 300(thin) | 400(normal) | 500(medium) | 700(bold) | 900 (extra bold)
	12. color: #000
	13. text-align: center | left | right
	14. overflow: auto | scroll | hidden
		- auto : 내용이 넘치면 스크롤이 생긴다
		- scroll : 내용이 넘치지 않아도 스크롤이 생긴다
		- hidden : 내용이 넘치면 잘린다
	15. z-index: 1
		- z-index가 높을수록 위에 보인다
	
### CSS 선택자
- 기본 선택자
	- 전체 선택자 : *
		- 성능 저하 가능
	- 그룹 선택자 : h1, h2, h3, ...
	- 클래스 선택자 : .class
	- 아이디 선택자 : #id
	- 속성 선택자 : [type="text"..]

- 결합자
	- 자손 결합자 : .parent .child
	- 자식 결합자 : .parent > .child
	- 인접 형제 결합자 : .prev + .next
	- 일반 형제 결합자 : .prev ~ .next

- 가상 클래스 선택자 : a:hover, a:active, a:focus, a:disabled, a:checked, a:first-child, a:last-child, a:nth-child(2) 
- 가상 요소 선택자 : ::before, ::after, ::placeholder


### 단축 속성
- padding: padding-top padding-right padding-bottom padding-left
	- padding: 10px 20px 30px 40px;
- margin: margin-top margin-right margin-bottom margin-left
	- margin: 10px 20px 30px 40px;
	- margin: 10px auto
		- 가운데 정렬
- border: border-width border-style border-color
	- border: 1px solid #000;
- border-radius: border-top-left-radius border-top-right-radius border-bottom-right-radius border-bottom-left-radius
	- border-radius: 10px 20px 30px 40px;


### CSS Emmet : CSS 자동완성 플러그인
https://docs.emmet.io/cheat-sheet/
- mt10 -> margin-top: 10px;
- pb10 -> padding-bottom: 10px;
- w100 -> width: 100px;
- h100p -> height: 100%;
- bd -> border: 1px solid #000;
- bgc -> background-color: #fff;
- fsz10 -> font-size: 10px;
- fw700 -> font-weight: 700;
- c#ddd -> color: #ddd;
- z10 -> z-index: 10;


### Sass, Scss

- Scss 예시
	```scss
	a {
		&:hover {
			color: #000;
		}
	}
	```
	- 계층 구조를 활용해서 중복되는 코드를 줄일 수 있다


- Sass 패턴 : 로직에 따라서 파일을 분리해서 작성
	- base/ : 기본 스타일
		- _reset.scss : 초기화
		- _typography.scss : 타이포그래피
	- components/ 
	- layout/ 
	- pages/
	- themes/ 
	- abstracts/
		- _variables.scss : 변수
		- _functions.scss : 함수
		- _mixins.scss : 믹스인
	- vendors/ : 외부 라이브러리
	> main.scss 에서 위 파일들을 @import로 불러온다

- Scss 문법
	```scss
	// _variables.scss : 다른 파일에서 사용할 변수를 선언한다
	$color: #000;
	$size: 10px;

	@function calc($size) {
		@return $size * 2;
	}

	// _mixins.scss : 다른 파일에서 사용할 믹스인을 선언한다, 매개변수도 가능
	@mixin ellipsis($size: 100px) {
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
		width: calc($size);
	}

	p {
		width: 300px;
		@include ellipsis();
	}

	```

