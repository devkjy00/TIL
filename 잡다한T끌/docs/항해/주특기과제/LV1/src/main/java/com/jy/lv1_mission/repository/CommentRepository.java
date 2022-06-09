package com.jy.lv1_mission.repository;

import com.jy.lv1_mission.model.Comment;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface CommentRepository extends JpaRepository<Comment, Long> {
    public List<Comment> findByBoardId(long id);
}
