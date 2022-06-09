package com.jy.lv1_mission.service;

import com.jy.lv1_mission.dto.NoticeBoardDto;
import com.jy.lv1_mission.model.NoticeBoard;
import com.jy.lv1_mission.repository.NoticeBoardRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class NoticeBoardService {


    private final NoticeBoardRepository noticeBoardRepository;


    @Transactional
    public NoticeBoard createPost(NoticeBoardDto requestDto){
        NoticeBoard noticeBoard = new NoticeBoard(requestDto);
        noticeBoardRepository.save(noticeBoard);
        return noticeBoard;
    }


    public List<NoticeBoard> findPosts(){
       return noticeBoardRepository.findAll();
    }


    public List<String> findTitles(){
        List<String> titles = new ArrayList<>();
        List<NoticeBoard> noticeBoards = noticeBoardRepository.findAll();

        for (NoticeBoard nb : noticeBoards){
            titles.add(nb.getTitle());
        }
        return titles;
    }


    @Transactional
    public NoticeBoard updatePost(long id, NoticeBoardDto requestDto){
        NoticeBoard noticeBoard = noticeBoardRepository
                .findById(id)
                .orElseThrow(() -> new IllegalArgumentException("잘못된 id"));

        noticeBoard.update(requestDto);
        noticeBoardRepository.save(noticeBoard);
        return noticeBoard;
    }


    @Transactional
    public long deletePost(long id){
        noticeBoardRepository.deleteById(id);
        return id;
    }
}
