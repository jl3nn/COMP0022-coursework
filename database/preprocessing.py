import pandas as pd
import os

processed_dir = 'processed/'
if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

# 1. Normalise the data by merging movies with their links on the 'movieId' column
movies_df = pd.read_csv(f"movies.csv")
links_df = pd.read_csv(f"links.csv", dtype={'tmdbId': 'str'})

merged_df = pd.merge(movies_df, links_df, on='movieId')

merged_df.to_csv(f'{processed_dir}movies.csv', index=False)

# 2. Convert the unix timestamp to a datetime object
ratings_df = pd.read_csv(f"ratings.csv")
tags_df = pd.read_csv(f"tags.csv")

ratings_df['timestamp'] = pd.to_datetime(ratings_df['timestamp'], unit='s')
tags_df['timestamp'] = pd.to_datetime(tags_df['timestamp'], unit='s')

ratings_df.to_csv(f'{processed_dir}ratings.csv', index=False)
tags_df.to_csv(f'{processed_dir}tags.csv', index=False)