CREATE DATABASE comp0022;

CREATE TABLE movies (
    movieId INT,
    title VARCHAR(255),
    genres VARCHAR(255),
    PRIMARY KEY (movieId)
);

CREATE TABLE ratings (
    userId INT,
    movieId INT,
    rating FLOAT,
    timestamp INT,
    PRIMARY KEY (userId, movieId),
    FOREIGN KEY (userId) REFERENCES movies(userId),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);

CREATE TABLE tags (
    userId INT,
    movieId INT,
    tag VARCHAR(255),
    timestamp INT,
    PRIMARY KEY (userId, movieId),
    FOREIGN KEY (userId) REFERENCES movies(userId),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);

CREATE TABLE links (
    movieId INT,
    imdbId VARCHAR(20),
    tmdbId INT,
    PRIMARY KEY (movieId),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);

COPY ratings FROM '/docker-entrypoint-initdb.d/ratings.csv' DELIMITER ',' CSV HEADER;
COPY tags FROM '/docker-entrypoint-initdb.d/tags.csv' DELIMITER ',' CSV HEADER;
COPY movies FROM '/docker-entrypoint-initdb.d/movies.csv' DELIMITER ',' CSV HEADER;
COPY links FROM '/docker-entrypoint-initdb.d/links.csv' DELIMITER ',' CSV HEADER;