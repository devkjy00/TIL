## Javascript on the browser
- Document 객체 :  DOM 구조를 기반으로 동작,  웹 페이지의 요소를 선택/생성/변경하거나 스타일을 조작할 수 있다
    - document.title : 페이지 제목
    - document.body : html 바디
    - *document.querySelector("...")* : css 셀렉터를 그대로 사용
        - *document.querySelectorAll("...")*

    > html 태그는 객체이고 모두 DOM에 속해있다, Document로 모두 접근할 수 있다


- Events : HTML 요소에 발생하는 동작들로 listener를 등록해서 처리할 수 있다
    ```js
    function handler() {
        console.log("title was clicked");
        }
    title.addEventListener("click", handler);
    ```
    - click, cancel, error, scroll, select, show, wheel, copy, cut, paste, blur, focus, focusin, focusout......
    - 해당 엘리먼트에 적용가능한 이벤트는 .dir로 모두 확인할 수 있다

- window : 브라우저 창(window)을 나타내는 전역 객체
    - 창 조작, 이벤트리스너, 타이버, 페이지 이동, 크기/위치, 스크롤 등등을 조작

> css는 js로 정의하는 것을 지양해야한다



## 구현 

- .preventDefault : event에 대한 브라우저의 기본동작을 막는다
    - eventlistner의 첫 매개변수로 event에 대한 값이 전달된다
    - form안에 input은 submit하면 페이지가 새로고침된다
        ```js
        function onSubmit(event) {
            event.preventDefault();     // 브라우저의 기본동작을 막는다
            }
        ```

    - a태그에 사용하면 기본동작인 페이지이동을 막을 수 있다

- display:none : css 값으로 html요소를 가려준다
    ```css
    .hidden {
        display: none
        }
    ```
    ```js
    function onSubmit(event) {
        event.preventDefault();
        ...
        loginForm.classList.add("hidden")
        }
    ```
    - classList.remove("...")
    
