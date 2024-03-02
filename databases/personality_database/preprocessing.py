import os
import pandas as pd


def ensure_directory_exists(directory):
    """Ensure the specified directory exists."""
    os.makedirs(directory, exist_ok=True)

def load_csv(directory, filename, *args, **kwargs):
    """Load a CSV file from the specified directory."""
    return pd.read_csv(f"{directory}{filename}", *args, **kwargs)

def save_dataframes(base_dir, **dfs):
    """Save provided dataframes to CSV files in the processed directory."""
    for name, df in dfs.items():
        df.to_csv(f"{base_dir}{name}.csv", index=False)

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

    # genres_df['genre_id'] = range(1, len(genres_df) + 1)
    # genre_to_id = genres_df.set_index('genre')['genre_id'].to_dict()
    # genres = genres.map(genre_to_id)

    # movie_genres_long = movies_df['genres'].str.split('|', expand=True).stack().reset_index(level=0).rename(columns={0: 'genre'})
    # movie_genres_long['genre_id'] = movie_genres_long['genre'].map(genre_to_id)
    # genre_movie_df = movie_genres_long.reset_index(drop=True).rename(columns={'level_0': 'movieId'})
    # genre_movie_df = genre_movie_df[['movieId', 'genre_id']].drop_duplicates()

    exploded_genres = movies_df["genres"].str.split("|").explode()
    exploded_genres = exploded_genres[exploded_genres != "(no genres listed)"]
    genres_df = pd.DataFrame(exploded_genres.unique(), columns=["genre"])
    genres_df["genreId"] = genres_df.index + 1
    temp_df = movies_df.assign(genres=movies_df["genres"].str.split("|")).explode(
        "genres"
    )
    temp_df = temp_df[temp_df["genres"] != "(no genres listed)"]
    genre_movie_df = temp_df.merge(
        genres_df, left_on="genres", right_on="genre", how="left"
    )[["movieId", "genreId"]]

    movies_df = movies_df.drop('genres', axis=1).rename(columns={'movieId': 'movie_id'})
    ratings_df = ratings_df.drop('timestamp', axis=1).rename(columns={'userId': 'user_id', 'movieId': 'movie_id'})
    genre_movie_df = genre_movie_df.rename(columns={'movieId': 'movie_id', 'genreId': 'genre_id'})
    genres_df = genres_df.rename(columns={'genreId': 'genre_id'})

    users_df = users_df.drop_duplicates(subset=['user_id'], keep='last')
    movies_df = movies_df.drop_duplicates(subset=['movie_id'], keep='last')
    genres_df = genres_df.drop_duplicates(subset=['genre_id'], keep='last')
    genre_movie_df = genre_movie_df.drop_duplicates(subset=['movie_id', 'genre_id'], keep='last')
    ratings_df = ratings_df.drop_duplicates(subset=['user_id', 'movie_id'], keep='last')

    return users_df, movies_df, genres_df, genre_movie_df, ratings_df

def main():
    base_dirs = {
        "personality": "personality/",
        "processed": "processed/",
    }
    
    ensure_directory_exists(base_dirs["processed"])

    data = load_csv(base_dirs["personality"], 'data.csv', delimiter=', ')
    ratings = load_csv(base_dirs["personality"], 'ratings.csv', delimiter=', ')
    movies = load_csv(base_dirs["personality"], 'movies.csv')
    users_df, movies_df, genres_df, \
        genre_movie_df, ratings_df = \
            prep_personality_data(data, movies, ratings)

    save_dataframes(
        base_dirs["processed"],
        users=users_df, 
        movies=movies_df, 
        genres=genres_df,
        genre_movie=genre_movie_df, 
        ratings=ratings_df
    )


if __name__ == "__main__":
    main()
