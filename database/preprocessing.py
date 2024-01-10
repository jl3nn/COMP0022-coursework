import pandas as pd
import os

processed_data_dir = 'processed/'
if not os.path.exists(processed_data_dir):
    os.makedirs(processed_data_dir)

# 1. Normalise the data by merging movies with their links on the 'movieId' column
movies_df = pd.read_csv(f"movies.csv")
links_df = pd.read_csv(f"links.csv", dtype={'tmdbId': 'str'})

merged_df = pd.merge(movies_df, links_df, on='movieId', how='left')

# 2. Add movie image links 
images_df = pd.read_csv(f"image_assets.csv")

merged_df = pd.merge(merged_df, images_df, left_on='movieId', right_on='item_id', how='left')
merged_df.drop(columns=['item_id'], inplace=True)

merged_df.to_csv(f'{processed_data_dir}movies.csv', index=False)

# 3. Convert the unix timestamp to a datetime object
ratings_df = pd.read_csv(f"ratings.csv")
tags_df = pd.read_csv(f"tags.csv")

ratings_df['timestamp'] = pd.to_datetime(ratings_df['timestamp'], unit='s')
tags_df['timestamp'] = pd.to_datetime(tags_df['timestamp'], unit='s')

ratings_df.to_csv(f'{processed_data_dir}ratings.csv', index=False)
tags_df.to_csv(f'{processed_data_dir}tags.csv', index=False)

# 4. Create a new table with the predicted rating for each movie
original_data = pd.read_csv('personality-data.csv', delimiter=', ', engine='python')
users_data = original_data[['userid', 'openness', 'agreeableness', 'emotional_stability',
                             'conscientiousness', 'extraversion', 'assigned_metric',
                             'assigned_condition', 'is_personalized', 'enjoy_watching']].copy()
users_data.to_csv(f'{processed_data_dir}users.csv', index=False)

dfs = []
for i in range(1, 13):
    dfs.append(original_data[['userid', f'movie_{i}', f'predicted_rating_{i}']].rename(columns={f'movie_{i}': 'movie', f'predicted_rating_{i}': 'predicted_rating'}))
predicted_ratings_df = pd.concat(dfs, ignore_index=True)
predicted_ratings_df.to_csv(f'{processed_data_dir}predicted_ratings.csv', index=False)
