CREATE TABLE movies (
    movieId INT,
    title VARCHAR(255) NOT NULL,
    genres VARCHAR(255) NOT NULL,
    imdbId INT, 
    tmdbId INT,
    PRIMARY KEY (movieId)
);

CREATE TABLE ratings (
    userId INT,
    movieId INT,
    rating FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY(userId, movieId),
    FOREIGN KEY(movieId) REFERENCES movies(movieId)
);

CREATE TABLE tags (
    tagId SERIAL,
    userId INT NOT NULL,
    movieId INT NOT NULL,
    tag VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    PRIMARY KEY(tagId),
    FOREIGN KEY(movieId) REFERENCES movies(movieId)
);

COPY movies (movieId, title, genres, imdbId, tmdbId) FROM '/docker-entrypoint-initdb.d/movies.csv' DELIMITER ',' CSV HEADER;
COPY ratings (userId, movieId, rating, timestamp) FROM '/docker-entrypoint-initdb.d/ratings.csv' DELIMITER ',' CSV HEADER;
COPY tags (userId, movieId, tag, timestamp) FROM '/docker-entrypoint-initdb.d/tags.csv' DELIMITER ',' CSV HEADER;