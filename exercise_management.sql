CREATE DATABASE exercise_management;
USE exercise_management;

-- 사용자 테이블
CREATE TABLE Users (
    Users_id VARCHAR(50) PRIMARY KEY,
    email VARCHAR(100),
    name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 인증 테이블
CREATE TABLE Authentication (
    User_id VARCHAR(50) PRIMARY KEY,
    Password_hash VARCHAR(255) NOT NULL,
    FOREIGN KEY (User_id) REFERENCES Users(Users_id)
);

-- 식단 기록 테이블
CREATE TABLE Dietrecords (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    diet_id VARCHAR(100),
    diet_much VARCHAR(50),
    diet_cal INT,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(Users_id)
);

-- 운동 기록 테이블
CREATE TABLE Exerciserecords (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    Users_id VARCHAR(50),
    exercise_id VARCHAR(100),
    exercise_cal INT,
    exercise_time INT,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Users_id) REFERENCES Users(Users_id)
);