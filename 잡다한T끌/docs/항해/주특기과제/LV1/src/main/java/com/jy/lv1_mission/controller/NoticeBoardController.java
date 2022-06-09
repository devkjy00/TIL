package com.jy.lv1_mission.controller;

import com.jy.lv1_mission.dto.NoticeBoardDto;
import com.jy.lv1_mission.model.NoticeBoard;
import com.jy.lv1_mission.service.NoticeBoardService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class NoticeBoardController {

    private final NoticeBoardService noticeBoardService;


    @GetMapping("/notice-boards")
    public List<NoticeBoard> findPosts(){
        return noticeBoardService.findPosts();
    }


    @GetMapping("/notice-boards-title")
    public List<String> findTitles(){
        return noticeBoardService.findTitles();
    }


    @PostMapping("/notice-boards")
    public NoticeBoard createPost(@RequestBody NoticeBoardDto requestDto){
        return noticeBoardService.createPost(requestDto);
    }


    @PutMapping("notice-boards/{id}")
    public NoticeBoard updatePost(@PathVariable long id, @RequestBody NoticeBoardDto requestDto){
        return noticeBoardService.updatePost(id, requestDto);
    }


    @DeleteMapping("notice-boards/{id}")
    public long deletePost(@PathVariable long id){
        return noticeBoardService.deletePost(id);
    }
}
