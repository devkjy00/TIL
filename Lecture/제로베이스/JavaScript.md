### 변수 범위
- var : 함수 스코프
- let, const : 블럭 스코프

### JS DOC
```js
/**
 * @param {number} a 첫번째 숫자
 * @param {number} b 두번째 숫자
 * @returns {number} 두 숫자의 합
 */
function sum(a, b) {
	return a + b;
}
```

### use strict : 조용히 무시되던 에러들을 throwing 해준다
- ES5에서 도입
- var 사용시 전역 변수로 선언되는 것을 방지
- 함수 호출시 this가 undefined로 바인딩 되는 것을 방지
- 객체에 같은 이름의 프로퍼티를 중복 선언할 수 없도록 함
- 함수의 매개변수 이름 중복을 방지

### 객체 생성
- 객체 생성
	```js
	const person = {
		name: 'Lee',
		sayHello() {
			console.log(`Hello! My name is ${this.name}.`);
		}
	};
	```



