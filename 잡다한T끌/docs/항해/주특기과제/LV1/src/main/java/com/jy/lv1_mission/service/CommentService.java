package com.jy.lv1_mission.service;

import com.jy.lv1_mission.dto.CommentDto;
import com.jy.lv1_mission.model.Comment;
import com.jy.lv1_mission.repository.CommentRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;

@Service
@RequiredArgsConstructor
public class CommentService {

    private final CommentRepository commentRepository;


    public List<Comment> findComments(long boardId){
        List<Comment> commentList = commentRepository.findByBoardId(boardId);
        Collections.sort(commentList);
        return commentList;
    }

    public Comment createComment(CommentDto requestDto){
        Comment comment = new Comment(requestDto);
        commentRepository.save(comment);
        return comment;
    }

    public Comment updateComment(long id, CommentDto requestDto){
        Comment comment = commentRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("잘못된 id"));

        comment.update(requestDto);
        commentRepository.save(comment);
        return comment;
    }

    public long deleteComment(long id){
        commentRepository.deleteById(id);
        return id;
    }
}
