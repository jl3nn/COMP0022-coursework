import os
import pandas as pd

# Set up data directories
additional_dir = "additional/"
movielens_dir = "movielens/"
personality_dir = "personality/"
processed_dir = "processed/"

# Ensure the processed data directory exists
os.makedirs(processed_dir, exist_ok=True)

# Load data
images_df = pd.read_csv(f"{additional_dir}images.csv")
links_df = pd.read_csv(f"{movielens_dir}links.csv", dtype={"tmdbId": "str"})
movies_df = pd.read_csv(f"{movielens_dir}movies.csv")
ratings_df = pd.read_csv(f"{movielens_dir}ratings.csv")
tags_df = pd.read_csv(f"{movielens_dir}tags.csv")
imdb_df = pd.read_csv(f"{additional_dir}imdb_data.csv")


# Normalize movies with links data
movies_df = (
    movies_df.merge(links_df, on="movieId", how="left")
    .merge(images_df, left_on="movieId", right_on="item_id", how="left")
    .drop(columns=["item_id"])
)

# Extract year and clean title
movies_df["year"] = movies_df["title"].str.extract(r"(\d{4})")[
    0].astype("Int64")
movies_df["title"] = movies_df["title"].str.replace(
    r" \(\d{4}\)", "", regex=True)

# Convert imdb_id in movies_df to the same format as in imdb_df
movies_df.rename(columns={'imdbId': 'imdb_id'}, inplace=True)
movies_df['imdb_id'] = movies_df['imdb_id'].apply(lambda x: f"tt{x:07}")

# Filter imdb_df to only include movies present in movies_df
imdb_df = imdb_df[imdb_df['imdb_id'].isin(movies_df['imdb_id'])]

# Create genre table and movie-genre association
exploded_genres = movies_df["genres"].str.split("|").explode()
exploded_genres = exploded_genres[exploded_genres != "(no genres listed)"]

genres_df = pd.DataFrame(exploded_genres.unique(), columns=["genre"])
genres_df["genreId"] = genres_df.index + 1

temp_df = movies_df.assign(
    genres=movies_df["genres"].str.split("|")).explode("genres")
temp_df = temp_df[temp_df["genres"] != "(no genres listed)"]

movie_genres_df = temp_df.merge(
    genres_df, left_on="genres", right_on="genre", how="left"
)[["movieId", "genreId"]]

# Drop redundant genres column from movies_df
movies_df.drop(columns=["genres"], inplace=True)

# Convert timestamps in ratings and tags
ratings_df["timestamp"] = pd.to_datetime(ratings_df["timestamp"], unit="s")
tags_df["timestamp"] = pd.to_datetime(tags_df["timestamp"], unit="s")

# Extract unique user IDs
users_df = (
    pd.concat([ratings_df["userId"], tags_df["userId"]]
              ).drop_duplicates().to_frame()
)


# Link data
imdb_movie_mapping = movies_df[['movieId', 'imdb_id']]
# Merge this mapping with imdb_df to get movieId alongside actors and directors
imdb_df = imdb_df.merge(imdb_movie_mapping, on='imdb_id', how='inner')


# Add IMDB actor data and assign unique IDs
actors_df = pd.DataFrame(imdb_df['actors'].str.split(',').explode(
).dropna().unique(), columns=['name']).reset_index(drop=False)
actors_df.rename(columns={'index': 'actor_id'}, inplace=True)


# Add IMDB director data
directors_df = pd.DataFrame(imdb_df['directors'].str.split(
    ',').explode().dropna().unique(), columns=['name']).reset_index(drop=False)
directors_df.rename(columns={'index': 'director_id'}, inplace=True)


# Create mapping dictionaries for actors and directors
actor_name_to_id_map = actors_df.set_index('name')['actor_id'].to_dict()
director_name_to_id_map = directors_df.set_index(
    'name')['director_id'].to_dict()

# Function to map names to IDs with error handling for unmapped names


def map_names_to_ids(names, mapping_dict):
    return [mapping_dict[name] for name in names if name in mapping_dict]


# Split actors and directors, map their names to IDs, and explode
imdb_df['actor_ids'] = imdb_df['actors'].str.split(',').apply(
    lambda x: map_names_to_ids(x, actor_name_to_id_map))
imdb_df['director_ids'] = imdb_df['directors'].str.split(',').apply(
    lambda x: map_names_to_ids(x, director_name_to_id_map))

# Explode actor_ids and director_ids into rows, keeping movieId for linkage
movie_actors_df = imdb_df.explode(
    'actor_ids')[['movieId', 'actor_ids']].dropna(subset=['actor_ids'])
movie_directors_df = imdb_df.explode(
    'director_ids')[['movieId', 'director_ids']].dropna(subset=['director_ids'])

# Ensure 'movieId', 'actor_ids', and 'director_ids' are integers for database compatibility
movie_actors_df['movieId'] = movie_actors_df['movieId'].astype(int)
movie_actors_df['actor_ids'] = movie_actors_df['actor_ids'].astype(int)
movie_directors_df['movieId'] = movie_directors_df['movieId'].astype(int)
movie_directors_df['director_ids'] = movie_directors_df['director_ids'].astype(
    int)


# Save processed data
movies_df.to_csv(f"{processed_dir}movies.csv", index=False)
ratings_df.to_csv(f"{processed_dir}ratings.csv", index=False)
tags_df.to_csv(f"{processed_dir}tags.csv", index=False)
users_df.to_csv(f"{processed_dir}users.csv", index=False)
genres_df.to_csv(f"{processed_dir}genres.csv", index=False)
movie_genres_df.to_csv(f"{processed_dir}movies_genres.csv", index=False)
actors_df.to_csv(f"{processed_dir}actors.csv", index=False)
movie_actors_df.to_csv(
    f"{processed_dir}movies_actors.csv", index=False)
directors_df.to_csv(f"{processed_dir}directors.csv", index=False)
movie_directors_df.to_csv(
    f"{processed_dir}movies_directors.csv", index=False)
