CREATE TABLE Character (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    image VARCHAR(255),
    range VARCHAR(50),
    base_atk INTEGER,
    base_def INTEGER,
    max_atk INTEGER,
    max_def INTEGER,
    acc INTEGER,
    eva INTEGER
);
