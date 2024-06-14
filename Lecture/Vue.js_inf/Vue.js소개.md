## MVVM 모델에서의 Vue
- MVVM 패턴의 뷰모델 레이어에 해당하는 화면단 라이브러리
	- view(DOM) <-> {ViewModel} <-> Model(js)
	- ViewModel은 DOM Listeners, DataBindings를 수행

## Reactivity
```html
<script>
	var div = document.querySelector("#app");
	var viewModel= {};

	// 즉시 실행 함수
	(function() {

		function init() {
			// (대상 객체, 객체의 속성, { 정의할 내용})
			Object.defineProperty(viewModel, 'str', {
				get: function() {
					console.log('접근');
					// viewModel.str
					// '접근'
				},
				set: function(val) {
					console.log('할당', val);
					// viewModel.str = 10 
					// '할당 10'
					render(val)
					// 새로운 값을 할당할 때마다 해당 값을 출력할 수 있다(Reactivity)
				}
			});
		}

		function render(value) {
				div.innerHTML = value;
		}

		init();

	})();
</script>
```
- Object.difineProperty() : 객체 속성을 재정의하는 함수
- 즉시 실행 함수 : Self-Excution Anonymous Function라는 디자인 패턴
	```
	var result = (function () {
		var name = "Barry";
		return name;
	})();
	// 즉시 결과를 생성한다.
	result; // "Barry"
	```
	- 첫번째 괄호() 안의 익명함수 
		- 로컬 영역으로 외부에서 접근하는 것을 막는다
	- 즉시 실행 함수를 생성하는 괄호() 
		- 자바스크립트 엔진이 함수를 바로 해석,실행하도록 명령하는 괄호


## 인스턴스 소개
```html
	<div id="app">
		<!-- ... -->
	</div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    // var options = 
    var vm = new Vue({
      el: '#app',
      data: {
        message: 'hi'
      },
      methods: {

      },
      created: function() {

      }
    });
  </script>
```
