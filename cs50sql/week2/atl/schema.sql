CREATE TABLE
    passengers (
        id INTEGER,
        first_name TEXT NOT NULL,
        last_name TEXT,
        PRIMARY KEY (id)
    );

CREATE TABLE
    airlines (
        id INTEGER,
        name TEXT NOT NULL,
        concourse CHECK (concourse IN ('A', 'B', 'C', 'D', 'E', 'F', 'T')),
        PRIMARY KEY (id)
    );

CREATE TABLE
    airports (
        id INTEGER,
        code TEXT NOT NULL UNIQUE,
        PRIMARY KEY (id)
    );

CREATE TABLE
    flights (
        id INTEGER,
        flight_number INTEGER NOT NULL,
        airline INTEGER,
        from_airport INTEGER,
        to_airport INTEGER,
        depature NUMERIC NOT NULL,
        arrival NUMERIC NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (airline) REFERENCES airlines (id),
        FOREIGN KEY (from_airport) REFERENCES airports (id),
        FOREIGN KEY (to_airport) REFERENCES airports (id)
    );

CREATE TABLE
    checkins (
        id INTEGER,
        passenger_id INTEGER,
        flight_id INTEGER,
        TIMESTAMP NUMERIC CURRENT_TIME,
        PRIMARY KEY (id),
        FOREIGN KEY (passenger_id) REFERENCES passengers (id),
        FOREIGN KEY (flight_id) REFERENCES flight (id)
    );
