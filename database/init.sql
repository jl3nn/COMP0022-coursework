CREATE TABLE movies (
    movie_id INT,
    title VARCHAR(255) NOT NULL,
    year INT,
    imdb_id VARCHAR(255), 
    tmdb_id VARCHAR(255),
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
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE
);

CREATE TABLE tags (
    tag_id INT,
    tag VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY(tag_id)
);

CREATE TABLE movies_users_tags(
    movie_id INT,
    user_id INT, 
    tag_id INT,
    timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY(movie_id, user_id, tag_id), 
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
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
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY(genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);

CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE movies_actors (
    movie_id INT NOT NULL,
    actor_id INT NOT NULL,
    PRIMARY KEY(movie_id, actor_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY(actor_id) REFERENCES actors(actor_id) ON DELETE CASCADE
);

CREATE TABLE directors (
    director_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);


CREATE TABLE movies_directors (
    movie_id INT NOT NULL,
    director_id INT NOT NULL,
    PRIMARY KEY(movie_id, director_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY(director_id) REFERENCES directors(director_id) ON DELETE CASCADE
);


COPY movies (movie_id, title, imdb_id, tmdb_id, image_url, year) FROM '/docker-entrypoint-initdb.d/movies.csv' DELIMITER ',' CSV HEADER;
COPY users (user_id) FROM '/docker-entrypoint-initdb.d/users.csv' DELIMITER ',' CSV HEADER;
COPY ratings (user_id, movie_id, rating, timestamp) FROM '/docker-entrypoint-initdb.d/ratings.csv' DELIMITER ',' CSV HEADER;
COPY tags (tag, tag_id) FROM '/docker-entrypoint-initdb.d/tags.csv' DELIMITER ',' CSV HEADER;
COPY movies_users_tags (movie_id, user_id, tag_id, timestamp) FROM '/docker-entrypoint-initdb.d/movies_users_tags.csv' DELIMITER ',' CSV HEADER;
COPY genres (genre, genre_id) FROM '/docker-entrypoint-initdb.d/genres.csv' DELIMITER ',' CSV HEADER;
COPY movies_genres (movie_id, genre_id) FROM '/docker-entrypoint-initdb.d/movies_genres.csv' DELIMITER ',' CSV HEADER;
COPY actors(actor_id, name) FROM '/docker-entrypoint-initdb.d/actors.csv' DELIMITER ',' CSV HEADER;
COPY directors(director_id, name) FROM '/docker-entrypoint-initdb.d/directors.csv' DELIMITER ',' CSV HEADER;
COPY movies_actors (movie_id, actor_id) FROM '/docker-entrypoint-initdb.d/movies_actors.csv' DELIMITER ',' CSV HEADER;
COPY movies_directors (movie_id, director_id) FROM '/docker-entrypoint-initdb.d/movies_directors.csv' DELIMITER ',' CSV HEADER;

DELETE FROM movies WHERE movie_id IN (SELECT movie_id FROM movies WHERE
        movie_id NOT IN (SELECT movie_id FROM ratings) OR
        movie_id NOT IN (SELECT movie_id FROM movies_genres) OR
        movie_id NOT IN (SELECT movie_id FROM movies_actors) OR
        movie_id NOT IN (SELECT movie_id FROM movies_directors)
);
