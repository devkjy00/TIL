## 요구 사항

- 전체 게시글 목록 조회
- 게시글 작성, 조회, 수정, 삭제
- 댓글 목록 조회
- 댓글 작성, 수정, 삭제

## API

- 게시글 목록 조회 : GET(/notice-boards-list)
- 게시글 조회 : GET(/notice-boards)
- 게시글 작성 : POST(/notice-boards)
- 게시글 수정 : PUT(/notice-boards/{id})
- 게시글 삭제 : DELETE(/notice-boards/{id})
- 댓글 목록 조회 : GET(/comments-list)
- 댓글 작성 : POST(/comments)
- 댓글 수정 : PUT(/comments/{id})
- 댓글 삭제 : DELETE(/comments/{id})

## 클래스 설계

- controller
    - NoticeBoardContrallor : 게시글 관련 요청 처리
    - CommentContrallor : 댓글 관련 요청 처리

- service
    - NoticeBoardService
    - CommentService

- repository
    - NoticeBoardRepository
    - CommentRepository

- model
    - NoticeBoard : 게시글
    - Comment : 댓글

- dto
    - NoticeBoardDto
    - CommentDto

## DB

- NoticeBoard
    - id(pk), title, writer, date, content

- Comment
    - id(pk), boardid(fk), date, content 


