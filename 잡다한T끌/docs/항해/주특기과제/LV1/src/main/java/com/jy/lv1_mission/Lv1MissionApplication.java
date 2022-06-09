package com.jy.lv1_mission;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

import javax.persistence.EntityListeners;

@SpringBootApplication
@EnableJpaAuditing
public class Lv1MissionApplication {

    public static void main(String[] args) {
        SpringApplication.run(Lv1MissionApplication.class, args);
    }

}
