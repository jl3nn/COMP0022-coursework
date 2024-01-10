CREATE TABLE movies (
    movie_id INT,
    title VARCHAR(255) NOT NULL,
    genres VARCHAR(255) NOT NULL,
    imdb_id INT, 
    tmdb_id INT,
    image_url VARCHAR(255),
    PRIMARY KEY (movie_id)
);

CREATE TABLE users (
    user_id VARCHAR(255),
    openness FLOAT,
    agreeableness FLOAT,
    emotional_stability FLOAT,
    conscientiousness FLOAT,
    extraversion FLOAT,
    assigned_metric VARCHAR(50),
    assigned_condition VARCHAR(50),
    is_personalized INT,
    enjoy_watching INT, 
    PRIMARY KEY(user_id)
);


CREATE TABLE ratings (
    user_id INT,
    movie_id INT,
    rating FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY(user_id, movie_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);

CREATE TABLE tags (
    tag_id SERIAL,
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    tag VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY(tag_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);


CREATE TABLE predicted_ratings (
    user_id VARCHAR(255),
    movie_id INT,
    predicted_rating FLOAT, 
    PRIMARY KEY(user_id, movie_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);


COPY movies (movie_id, title, genres, imdb_id, tmdb_id, image_url) FROM '/docker-entrypoint-initdb.d/movies.csv' DELIMITER ',' CSV HEADER;
COPY users (user_id, openness, agreeableness, emotional_stability, conscientiousness, extraversion, assigned_metric, assigned_condition, is_personalized, enjoy_watching) FROM '/docker-entrypoint-initdb.d/users.csv' DELIMITER ',' CSV HEADER;
COPY ratings (user_id, movie_id, rating, timestamp) FROM '/docker-entrypoint-initdb.d/ratings.csv' DELIMITER ',' CSV HEADER;
COPY tags (user_id, movie_id, tag, timestamp) FROM '/docker-entrypoint-initdb.d/tags.csv' DELIMITER ',' CSV HEADER;
COPY predicted_ratings (user_id, movie_id, predicted_rating) FROM '/docker-entrypoint-initdb.d/predicted_ratings.csv' DELIMITER ',' CSV HEADER;
