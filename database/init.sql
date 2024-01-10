CREATE TABLE movies (
    movieId INT,
    title VARCHAR(255) NOT NULL,
    genres VARCHAR(255) NOT NULL,
    imdbId INT, 
    tmdbId INT,
    imageUrl VARCHAR(255),
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

CREATE TABLE users (
    userid VARCHAR(255),
    openness FLOAT,
    agreeableness FLOAT,
    emotional_stability FLOAT,
    conscientiousness FLOAT,
    extraversion FLOAT,
    assigned_metric VARCHAR(50),
    assigned_condition VARCHAR(50),
    is_personalized FLOAT,
    enjoy_watching FLOAT
);

CREATE TABLE predicted_ratings (
    userid VARCHAR(255),
    movie INT,
    predicted_rating FLOAT
);


COPY movies (movieId, title, genres, imdbId, tmdbId, imageUrl) FROM '/docker-entrypoint-initdb.d/movies.csv' DELIMITER ',' CSV HEADER;
COPY ratings (userId, movieId, rating, timestamp) FROM '/docker-entrypoint-initdb.d/ratings.csv' DELIMITER ',' CSV HEADER;
COPY tags (userId, movieId, tag, timestamp) FROM '/docker-entrypoint-initdb.d/tags.csv' DELIMITER ',' CSV HEADER;
COPY users (userid, openness, agreeableness, emotional_stability, conscientiousness, extraversion, assigned_metric, assigned_condition, is_personalized, enjoy_watching) FROM '/docker-entrypoint-initdb.d/users.csv' DELIMITER ',' CSV HEADER;
COPY predicted_ratings (userid, movie, predicted_rating) FROM '/docker-entrypoint-initdb.d/predicted_ratings.csv' DELIMITER ',' CSV HEADER;
