CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    cash NUMERIC NOT NULL DEFAULT 10000.00
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE UNIQUE INDEX username ON users (username);
CREATE TABLE symbols (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    symbol TEXT NOT NULL
);
CREATE TABLE histories (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER,
    transacted DATETIME NOT NULL,
    symbol_id TEXT NOT NULL,
    price NUMERIC NOT NULL,
    shares INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (symbol_id) REFERENCES symbols(id)
);
CREATE TABLE portfolios (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER,
    symbol_id TEXT NOT NULL,
    shares INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (symbol_id) REFERENCES symbols(id)
)