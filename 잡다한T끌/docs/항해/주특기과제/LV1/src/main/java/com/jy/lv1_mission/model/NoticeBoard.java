package com.jy.lv1_mission.model;


import com.jy.lv1_mission.dto.NoticeBoardDto;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.List;
import java.util.Objects;

@Entity
@Getter
@NoArgsConstructor
public class NoticeBoard extends TimeStamped{

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(nullable = false)
    private String title;

    @Column(nullable = false)
    private String writer;

    @Column(nullable = false)
    private String content;


    public NoticeBoard(NoticeBoardDto requestDto){
        this.title = requestDto.getTitle();
        this.content = requestDto.getContent();
        this.writer = requestDto.getWriter();
    }

    public NoticeBoard update(NoticeBoardDto requestDto){
        String title = requestDto.getTitle();
        String content = requestDto.getContent();
        String writer = requestDto.getWriter();

        this.title = Objects.nonNull(title) ? title : this.title;
        this.content = Objects.nonNull(content) ? content : this.content;
        this.writer = Objects.nonNull(writer) ? writer : this.writer;

        return this;
    }


}
