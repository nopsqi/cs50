SHOW DATABASES;

CREATE DATABASE linkedin;

USE linkedin;

CREATE TABLE
    users (
        id INT AUTO_INCREMENT,
        first_name VARCHAR(16) NOT NULL,
        last_name VARCHAR(16),
        username VARCHAR(15) NOT NULL UNIQUE,
        password VARCHAR(128) NOT NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE
    schools (
        id INT AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        type ENUM ('Primary', 'Secondary', 'Higher Education') NOT NULL,
        YEAR YEAR NOT NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE
    companies (
        id INT AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        industry ENUM ('Technology', 'Education', 'Business') NOT NULL,
        location VARCHAR(100) NOT NULL,
        PRIMARY KEY (id)
    );

CREATE TABLE
    follows (
        id INT AUTO_INCREMENT,
        user_id INT NOT NULL,
        follow_user_id INT NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (USER) REFERENCES users (id),
        FOREIGN KEY (follow) REFERENCES users (id),
        UNIQUE (USER, follow)
    );

CREATE TABLE
    attends (
        id INT AUTO_INCREMENT,
        user_id INT NOT NULL,
        school_id INT NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE CHECK (end_date > start_date),
        degree VARCHAR(5),
        PRIMARY KEY (id),
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (school_id) REFERENCES schools (id),
        UNIQUE (user_id, school_id)
    );

CREATE TABLE
    works (
        id INT AUTO_INCREMENT,
        user_id INT NOT NULL,
        company_id INT NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE,
        PRIMARY KEY (id),
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (company_id) REFERENCES companies (id)
    );
