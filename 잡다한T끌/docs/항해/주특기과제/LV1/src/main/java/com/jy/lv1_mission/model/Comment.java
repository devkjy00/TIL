package com.jy.lv1_mission.model;

import com.jy.lv1_mission.dto.CommentDto;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.Objects;

@Entity
@Getter
@NoArgsConstructor
public class Comment extends TimeStamped implements Comparable<Comment>{

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(nullable = false)
    private long boardId;

    @Column(nullable = false)
    private String content;

    public Comment(CommentDto requestDto){
        this.boardId = requestDto.getBoardId();
        this.content = requestDto.getContent();
    }

    public Comment update(CommentDto requestDto){
        String content = requestDto.getContent();

        this.content = Objects.nonNull(content) ? content : this.content;
        return this;
    }

    @Override
    public int compareTo(Comment o) {
        return this.getStartTime().compareTo(o.getStartTime());
    }
}
