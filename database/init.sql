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
    user_id INT,
    PRIMARY KEY (user_id)
);

CREATE TABLE ratings (
    user_id INT,
    movie_id INT,
    rating FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY(user_id, movie_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);

CREATE TABLE tags (
    tag_id SERIAL,
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    tag VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY(tag_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);

CREATE TABLE genres (
    genre_id INT,
    genre VARCHAR(255) NOT NULL,
    PRIMARY KEY(genre_id)
);

CREATE TABLE movies_genres (
    movie_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY(movie_id, genre_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY(genre_id) REFERENCES genres(genre_id)
);


COPY movies (movie_id, title, genres, imdb_id, tmdb_id, image_url) FROM '/docker-entrypoint-initdb.d/movies.csv' DELIMITER ',' CSV HEADER;
COPY users (user_id) FROM '/docker-entrypoint-initdb.d/users.csv' DELIMITER ',' CSV HEADER;
COPY ratings (user_id, movie_id, rating, timestamp) FROM '/docker-entrypoint-initdb.d/ratings.csv' DELIMITER ',' CSV HEADER;
COPY tags (user_id, movie_id, tag, timestamp) FROM '/docker-entrypoint-initdb.d/tags.csv' DELIMITER ',' CSV HEADER;
COPY genres (genre_id, genre) FROM '/docker-entrypoint-initdb.d/genres.csv' DELIMITER ',' CSV HEADER;
COPY movies_genres (movie_id, genre_id) FROM '/docker-entrypoint-initdb.d/movies_genres.csv' DELIMITER ',' CSV HEADER;