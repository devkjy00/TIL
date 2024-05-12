## 오해
1. 양방향 매핑보다 단방향 매핑이 더 좋다?
- 단방향 매핑과 영속성 전이(cascade)를 사용해서 연관객체를 insert하면 insert문 후에 FK를 넣기위한 update문이 각 연관객체마다 추가로 생성되는 문제 발생
    - 양방향 매핑 후 영속성 전이로 insert하면 update문을 없엘 수 있다

- 객체 그래프 탐색 관점에서는 보통 단방향으로 충분하다 


## 새로 배움
```java
@Entity
public class Member{
    @Id
    @Column(name = "member_id")
    private Long memberId;

    private String name;

    @OneToMany(cascade = CascadeType.ALL, mappedBy = "member")
    private List<MemberDetail> details;
}


@Entity
public class MemberDetail{
    // Entity의 복합키 설정
    @EmbeddedId
    private PK pk;

    @ManyToOne
    @MapsId("memberId") // FK를 PK로 지정할 때 사용하는 어노테이션
    private Member member;


    @Embeddable
    public static class PK implements Serializable{
        @Column(name = "member_id")
        private Long memberId;

        private String type;
    }
}
```
- [@MapsId](https://developer-ping9.tistory.com/296)
