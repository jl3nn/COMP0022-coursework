CREATE TABLE #bla (
    # bla
);

COPY bla FROM '/docker-entrypoint-initdb.d/data.csv' WITH CSV HEADER;
