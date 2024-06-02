CREATE TABLE
    ingredients (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        price NUMERIC NOT NULL
    );

CREATE TABLE
    donuts (
        id INTEGER PRIMARY KEY,
        name UNIQUE NOT NULL,
        gluten INTEGER NOT NULL,
        price NUMERIC NOT NULL
    );

CREATE TABLE
    made_with (
        donut_id INTEGER,
        ingredient_id INTEGER,
        FOREIGN KEY (donut_id) REFERENCES donuts (id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredients (id),
        UNIQUE(donut_id, ingredient_id)
    );

CREATE TABLE
    order_headers (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        TIMESTAMP NUMERIC NOT NULL DEFAULT CURRENT_TIME,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    );

CREATE TABLE
    order_details (
        order_id INTEGER,
        donut_id INTEGER,
        qty INTEGER DEFAULT 1,
        FOREIGN KEY (order_id) REFERENCES orders (id),
        FOREIGN KEY (donut_id) REFERENCES donuts (id)
    );

CREATE TABLE
    customers (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT
    );
