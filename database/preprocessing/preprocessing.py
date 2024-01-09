import pandas as pd

raw_data_dir = 'raw_data/'
processed_data_dir = 'processed_data/'

# 1. Normalise the data by merging movies with their links on the 'movieId' column
movies_df = pd.read_csv(f"{raw_data_dir}movies.csv")
links_df = pd.read_csv(f"{raw_data_dir}links.csv", dtype={'tmdbId': 'str'})

merged_df = pd.merge(movies_df, links_df, on='movieId')

# 2. Add movie image links 
images_df = pd.read_csv(f"{raw_data_dir}image_assets.csv")
merged_df = pd.merge(merged_df, images_df, left_on='movieId', right_on='item_id')

merged_df.rename(columns={'url': 'imageUrl'}, inplace=True)

merged_df.to_csv(f'{processed_data_dir}movies.csv', index=False)

# 3. Convert the unix timestamp to a datetime object
ratings_df = pd.read_csv(f"{raw_data_dir}ratings.csv")
tags_df = pd.read_csv(f"{raw_data_dir}tags.csv")

ratings_df['timestamp'] = pd.to_datetime(ratings_df['timestamp'], unit='s')
tags_df['timestamp'] = pd.to_datetime(tags_df['timestamp'], unit='s')

ratings_df.to_csv(f'{processed_data_dir}ratings.csv', index=False)
tags_df.to_csv(f'{processed_data_dir}tags.csv', index=False)
