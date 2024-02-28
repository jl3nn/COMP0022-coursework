import os
import pandas as pd


def ensure_directory_exists(directory):
    """Ensure the specified directory exists."""
    os.makedirs(directory, exist_ok=True)


def load_csv(directory, filename, *args, **kwargs):
    """Load a CSV file from the specified directory."""
    return pd.read_csv(f"{directory}{filename}", *args, **kwargs)


def normalize_movies_with_links(movies_df, links_df, images_df):
    """Normalize movies with links data."""
    return (
        movies_df.merge(links_df, on="movieId", how="left")
        .merge(images_df, left_on="movieId", right_on="item_id", how="left")
        .drop(columns=["item_id"])
    )


def process_movies_df(movies_df):
    """Extract year, clean title, and convert imdb_id format in movies_df."""
    movies_df["year"] = movies_df["title"].str.extract(r"(\d{4})")[
        0].astype("Int64")
    movies_df["title"] = movies_df["title"].str.replace(
        r" \(\d{4}\)", "", regex=True)
    movies_df.rename(columns={"imdbId": "imdb_id"}, inplace=True)
    movies_df["imdb_id"] = movies_df["imdb_id"].apply(lambda x: f"tt{x:07}")


def process_and_normalise_tags(tags_df, movies_df, users_df):
    """Extract tags, normalize the relation with movies and users."""

    normalized_tags_df = pd.DataFrame(tags_df['tag'].unique(), columns=['tag'])
    normalized_tags_df['tagId'] = normalized_tags_df.index + 1

    tags_with_ids_df = tags_df.merge(
        movies_df, left_on='movieId', right_on='movieId', how='left')
    tags_with_ids_df = tags_with_ids_df.merge(
        users_df, left_on='userId', right_on='userId', how='left')

    tags_with_ids_df = tags_with_ids_df.merge(
        normalized_tags_df, on='tag', how='left')

    movies_users_tags_df = tags_with_ids_df[[
        'movieId', 'userId', 'tagId', 'timestamp']]

    return normalized_tags_df, movies_users_tags_df


def create_genre_tables(movies_df):
    """Create genre table and movie-genre association."""
    exploded_genres = movies_df["genres"].str.split("|").explode()
    exploded_genres = exploded_genres[exploded_genres != "(no genres listed)"]
    genres_df = pd.DataFrame(exploded_genres.unique(), columns=["genre"])
    genres_df["genreId"] = genres_df.index + 1
    temp_df = movies_df.assign(genres=movies_df["genres"].str.split("|")).explode(
        "genres"
    )
    temp_df = temp_df[temp_df["genres"] != "(no genres listed)"]
    movie_genres_df = temp_df.merge(
        genres_df, left_on="genres", right_on="genre", how="left"
    )[["movieId", "genreId"]]
    return genres_df, movie_genres_df


def map_names_to_ids(names, mapping_dict):
    """Function to map names to IDs with error handling for unmapped names."""
    return [mapping_dict.get(name) for name in names if name in mapping_dict]


def process_imdb_df(imdb_df, movies_df):
    """Process IMDb data frame to include movieId and map actor/director names to IDs."""
    # Filter imdb_df to only include movies present in movies_df
    imdb_df = imdb_df[imdb_df["imdb_id"].isin(movies_df["imdb_id"])]
    # Link data
    imdb_movie_mapping = movies_df[["movieId", "imdb_id"]]
    # Merge this mapping with imdb_df to get movieId alongside actors and directors
    imdb_df = imdb_df.merge(imdb_movie_mapping, on="imdb_id", how="inner")
    return imdb_df


def process_actor_director_data(imdb_df):
    """Process actor and director data, creating unique IDs and mapping."""
    actors_df = pd.DataFrame(
        imdb_df["actors"].str.split(",").explode().dropna().unique(), columns=["name"]
    ).reset_index(drop=False)
    actors_df.rename(columns={"index": "actor_id"}, inplace=True)
    directors_df = pd.DataFrame(
        imdb_df["directors"].str.split(",").explode().dropna().unique(),
        columns=["name"],
    ).reset_index(drop=False)
    directors_df.rename(columns={"index": "director_id"}, inplace=True)
    return actors_df, directors_df


def save_dataframes(base_dir, **dfs):
    """Save provided dataframes to CSV files in the processed directory."""
    for name, df in dfs.items():
        df.to_csv(f"{base_dir}{name}.csv", index=False)


def explode_and_map_ids(imdb_df, mapping_df, id_column_name, new_column_name):
    """Explode and map actor or director names to IDs, keeping movieId for linkage."""
    mapping_dict = mapping_df.set_index("name")[id_column_name].to_dict()
    imdb_df[new_column_name] = (
        imdb_df[id_column_name.replace("_id", "s")]
        .str.split(",")
        .apply(lambda x: map_names_to_ids(x, mapping_dict))
    )
    return imdb_df.explode(new_column_name)[["movieId", new_column_name]].dropna(
        subset=[new_column_name]
    )

def prep_personality_data(data: pd.DataFrame, movies: pd.DataFrame, ratings: pd.DataFrame) -> tuple:
    users = data[['userid', 'openness', 'agreeableness', 'emotional_stability', 'conscientiousness', 'extraversion', 'assigned_metric', 'assigned_condition']]
    valid_movie_ids = movies['movieId'].unique()
    valid_ratings = ratings.loc[ratings['movieId'].isin(valid_movie_ids)]
    movies_df = movies.loc[movies['movieId'].isin(valid_ratings['movieId'].unique())]

    ratings_df = valid_ratings.loc[valid_ratings['userId'].isin(users['userid'].unique())]
    users_df = users.loc[users['userid'].isin(ratings_df['userId'].unique())]
    users_df = users_df.rename(columns={'userid': 'user_id'})

    genres = movies_df['genres'].str.split('|', expand=True).stack().reset_index(level=-1, drop=True)
    genres_df = pd.DataFrame(genres.unique(), columns=['genre'])

    genres_df['genre_id'] = range(1, len(genres_df) + 1)
    genre_to_id = genres_df.set_index('genre')['genre_id'].to_dict()
    genres = genres.map(genre_to_id)

    genre_movie_df = pd.DataFrame({
        'movie_id': genres.index.get_level_values(0),
        'genre_id': genres.values
    })
    genre_movie_df.reset_index(drop=True, inplace=True)

    movies_df = movies_df.drop('genres', axis=1).rename(columns={'movieId': 'movie_id'})
    ratings_df = ratings_df.drop('timestamp', axis=1).rename(columns={'userId': 'user_id', 'movieId': 'movie_id'})

    return users_df, movies_df, genres_df, genre_movie_df, ratings_df


def main():
    base_dirs = {
        "additional": "additional/",
        "movielens": "movielens/",
        "processed": "processed/",
    }

    # Ensure the processed data directory exists
    ensure_directory_exists(base_dirs["processed"])

    # Load data
    images_df = load_csv(base_dirs["additional"], "images.csv")
    links_df = load_csv(base_dirs["movielens"],
                        "links.csv", dtype={"tmdbId": "str"})
    movies_df = load_csv(base_dirs["movielens"], "movies.csv")
    ratings_df = load_csv(base_dirs["movielens"], "ratings.csv")
    tags_df = load_csv(base_dirs["movielens"], "tags.csv")
    imdb_df = load_csv(base_dirs["additional"], "imdb.csv")

    # Process data
    movies_df = normalize_movies_with_links(movies_df, links_df, images_df)
    process_movies_df(movies_df)
    genres_df, movie_genres_df = create_genre_tables(movies_df)
    movies_df.drop(columns=["genres"], inplace=True)
    ratings_df["timestamp"] = pd.to_datetime(ratings_df["timestamp"], unit="s")
    tags_df["timestamp"] = pd.to_datetime(tags_df["timestamp"], unit="s")
    users_df = (
        pd.concat([ratings_df["userId"], tags_df["userId"]])
        .drop_duplicates()
        .to_frame()
    )
    tags_df, movies_users_tags_df = process_and_normalise_tags(
        tags_df, movies_df, users_df)
    imdb_df = process_imdb_df(imdb_df, movies_df)
    actors_df, directors_df = process_actor_director_data(imdb_df)

    # Explode and map actor and director IDs
    movie_actors_df = explode_and_map_ids(
        imdb_df, actors_df, "actor_id", "actor_ids")
    movie_directors_df = explode_and_map_ids(
        imdb_df, directors_df, "director_id", "director_ids"
    )

    save_dataframes(
        base_dirs["processed"],
        movies=movies_df,
        ratings=ratings_df,
        tags=tags_df,
        movies_users_tags=movies_users_tags_df,
        users=users_df,
        genres=genres_df,
        movies_genres=movie_genres_df,
        actors=actors_df,
        directors=directors_df,
        movies_actors=movie_actors_df,
        movies_directors=movie_directors_df,
    )


if __name__ == "__main__":
    main()
