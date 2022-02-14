import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
def standardize(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row

def get_similar_movies(movie_name, user_rating):
    similar_score = item_similarity_df[movie_name] * (user_rating - 2.5)
    similar_score = similar_score.sort_values(ascending = False)
    return similar_score

ratings = pd.read_csv("./datasets/toy_dataset.csv", index_col=0)
ratings = ratings.fillna(0)

ratings_std = ratings.apply(standardize)

item_similarity = cosine_similarity(ratings_std.T)
item_similarity_df = pd.DataFrame(item_similarity, index=ratings.columns, columns=ratings.columns)
# print(item_similarity_df)
# print(get_similar_movies("action1", 2))

action_lover = [("action1", 5), ("romantic1", 1), ("romantic3", 1)]
similar_movies = pd.DataFrame()

for movie,rating in action_lover:
    print(movie, rating)
    similar_movies = similar_movies.append(get_similar_movies(movie, rating), ignore_index=True)

print(similar_movies)