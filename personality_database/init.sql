CREATE TABLE users (
    user_id VARCHAR(255),
    openness VARCHAR(255), 
    agreeableness VARCHAR(255), 
    emotional_stability VARCHAR(255), 
    conscientiousness VARCHAR(255), 
    extraversion VARCHAR(255), 
    assigned_metric VARCHAR(255), 
    assigned_condition VARCHAR(255),
    PRIMARY KEY (user_id)
);

CREATE TABLE movies (
    movie_id INT,
    title VARCHAR(255) NOT NULL,
    PRIMARY KEY (movie_id)
);

CREATE TABLE ratings (
    user_id VARCHAR(255) NOT NULL,
    movie_id INT NOT NULL,
    rating VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id, movie_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id), 
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

CREATE TABLE genres (
    genre_id INT,
    genre VARCHAR(255) NOT NULL,
    PRIMARY KEY (genre_id)
);

CREATE TABLE movie_genre(
    genre_id INT NOT NULL,
    movie_id INT NOT NULL,
    PRIMARY KEY (genre_id, movie_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);

COPY users(user_id, openness, agreeableness, emotional_stability, conscientiousness, extraversion, assigned_metric, assigned_condition)
FROM '/docker-entrypoint-initdb.d/users.csv' DELIMITER ',' CSV HEADER;

COPY movies(movie_id, title)
FROM '/docker-entrypoint-initdb.d/movies.csv' DELIMITER ',' CSV HEADER;

COPY genres(genre, genre_id)
FROM '/docker-entrypoint-initdb.d/genres.csv' DELIMITER ',' CSV HEADER;

COPY movie_genre(movie_id, genre_id)
FROM '/docker-entrypoint-initdb.d/genre_movie.csv' DELIMITER ',' CSV HEADER;

COPY ratings(user_id, movie_id, rating)
FROM '/docker-entrypoint-initdb.d/ratings.csv' DELIMITER ',' CSV HEADER;
