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