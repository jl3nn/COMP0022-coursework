import pandas as pd
import os

# Ensure the processed data directory exists
processed_data_dir = "processed/"
os.makedirs(processed_data_dir, exist_ok=True)

# Load data
movies_df = pd.read_csv("movies.csv")
links_df = pd.read_csv("links.csv", dtype={"tmdbId": "str"})
images_df = pd.read_csv("image_assets.csv")
ratings_df = pd.read_csv("ratings.csv")
tags_df = pd.read_csv("tags.csv")

# Normalize movies with links data
movies_df = (
    movies_df.merge(links_df, on="movieId", how="left")
    .merge(images_df, left_on="movieId", right_on="item_id", how="left")
    .drop(columns=["item_id"])
)

# Extract year, clean title
movies_df["year"] = movies_df["title"].str.extract(r"(\d{4})")[0].astype('Int64')
movies_df["title"] = movies_df["title"].str.replace(r" \(\d{4}\)", "", regex=True)

# Create genre table and movie-genre association
exploded_genres = movies_df["genres"].str.split("|").explode()
exploded_genres = exploded_genres[exploded_genres != "(no genres listed)"]

genres_df = pd.DataFrame(exploded_genres.unique(), columns=["genre"])
genres_df["genreId"] = genres_df.index + 1

temp_df = movies_df.assign(genres=movies_df["genres"].str.split("|")).explode("genres")
temp_df = temp_df[temp_df["genres"] != "(no genres listed)"]

movie_genres_df = temp_df.merge(
    genres_df, left_on="genres", right_on="genre", how="left"
)[["movieId", "genreId"]]

# Drop genres column from movies_df as it's now redundant
movies_df.drop(columns=["genres"], inplace=True)

# Convert timestamps in ratings and tags
ratings_df["timestamp"] = pd.to_datetime(ratings_df["timestamp"], unit="s")
tags_df["timestamp"] = pd.to_datetime(tags_df["timestamp"], unit="s")

# Extract unique user IDs
users_df = (
    pd.concat([ratings_df["userId"], tags_df["userId"]]).drop_duplicates().to_frame()
)

# Save processed data
movies_df.to_csv(f"{processed_data_dir}movies.csv", index=False)
ratings_df.to_csv(f"{processed_data_dir}ratings.csv", index=False)
tags_df.to_csv(f"{processed_data_dir}tags.csv", index=False)
users_df.to_csv(f"{processed_data_dir}users.csv", index=False)
genres_df.to_csv(f"{processed_data_dir}genres.csv", index=False)
movie_genres_df.to_csv(f"{processed_data_dir}movies_genres.csv", index=False)
