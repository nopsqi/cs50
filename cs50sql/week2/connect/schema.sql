CREATE TABLE
    users (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT,
        username NOT NULL UNIQUE,
        password TEXT NOT NULL
    );

CREATE TABLE
    schools (
        id INTEGER PRIMARY KEY,
        type TEXT NOT NULL,
        location TEXT NOT NULL,
        YEAR NUMERIC NOT NULL
    );

CREATE TABLE
    companies (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        industry TEXT NOT NULL,
        location NOT NULL
    );

CREATE TABLE
    following (
        id INTEGER PRIMARY KEY,
        user_a INTEGER,
        user_b INTEGER CHECK (user_b != user_a),
        FOREIGN KEY (user_a) REFERENCES users (id),
        FOREIGN KEY (user_b) REFERENCES users (id),
        UNIQUE (user_a, user_b)
    );

CREATE TABLE
    attending (
        user_id INTEGER,
        school_id INTEGER,
        start_date NUMERIC NOT NULL,
        end_date NUMERIC CHECK (end_date > start_date),
        type TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (school_id) REFERENCES schools (id)
    );

CREATE TABLE
    working (
        user_id INTEGER,
        company_id INTEGER,
        start_date NUMERIC NOT NULL,
        end_date NUMERIC CHECK (end_date > start_date),
        title TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (company_id) REFERENCES companies (id)
    );
