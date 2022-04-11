 강의자료 : https://teamsparta.notion.site/1-da6d8595945d4b868e5fcfa933c56011

## html
- h1 태그는 구글 검색 엔진을 통해 검색된다
- 이모티콘 모음
  - https://kr.piliapp.com/facebook-symbols/

## css
- 백그라운드 이미지 설정
    ```html
    <style>
    background-image: url("https://www.ancient-origins.net/sites/default/files/field/image/Agesilaus-II-cover.jpg");
    background-size: cover; /* 이미지 적절한 크기로 맞추기 */
    background-position: center; /* 이미지 가운데 맞추기 */
    </style>
    ```

- 폰트를 검색, 코드를 가져올수 있다
  - https://fonts.google.com/?subset=korean
    
- bootstrap : 미리 정의된 CSS를 제공, 간단하게 스타일을 적용할 수 있다
  - https://getbootstrap.com/docs/5.0/components/buttons/

- 텍스트를 정 가운데로 정렬
  ```html
  <style>
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  </style>
  ```
  
- 모바일 처리하기
  ```css
  width: 95%; 
  max-width: 500px;
  ```
  
## javascript
- 구글 chrome의 Console을 통해 대화형으로 코드를 작성할 수 있다
- html파일을 위에서 부터 읽어서 script에 정의된 명령은 페이지를 열면 바로 실행된다
- JQuery : HTML요소를 조작하는 라이브러리
  - https://www.w3schools.com/jquery/jquery_get_started.asp
  - 요소의 id를 통해서 요소를 식별하고 동작한다
    - $('#id명')
      - .val('문자열') : 해당 태그에 값 입력
      - .val() : 해당 태그의 값 반환
      - .hide() : 태그 숨기기
      - .show() : 태그 보이기
      - .append(`태그`) : (`)백틱으로 작성된 태그를 HTML로 변환, 태그에 추가
        ```js
        let title = "title"
        let a = `<h1>제목 : ${title}</h1>`
        $('#id').append(a)
        ```
        - ${}를 사용해서 문자열에 변수를 추가 할 수 있다
        - **태그에 CSS클래스를 적용 시켜서 동적으로 스타일을 적용시킬 수 있다**
      - .empty() : 태그 내용 지우기
      - .attr("속성명", 값) : 태그 속성 변경
      - .text("문자열") : 태그 텍스트 변경
  

- Ajax 비동기로 XML, JSON 파일을 다룬다
  - Rest API를 사용해서 JSON파일을 다룬다
    - URI를 통해서 자원에 접근한다
    
  - 기본 골격
    ```js
    $.ajax({
    type: "GET",
    url: "여기에URL을입력",
    data: {},
    success: function(response){
    console.log(response)
    }
    })
    ``` 
    - JSON 인덱싱 할 때는 무조건 복사하기
  
  - 로딩 후 호출
    ```js
    $(document).ready(function(){
    $.ajax({...})
    });
    ```