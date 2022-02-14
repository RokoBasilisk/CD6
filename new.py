import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def standardize(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row

def get_similar_movies(movie_name, user_rating):
    print(movie_name, user_rating)
    similar_score = item_similarity_df[movie_name] * (user_rating - 2.5)
    print(similar_score)
    similar_score = similar_score.sort_values(ascending = False)
    return similar_score

ratings = pd.read_csv('./datasets/ratings.csv')
movies = pd.read_csv('./datasets/movies.csv')

ratings = pd.merge(movies, ratings).drop(['genres', 'timestamp'], axis=1)
user_ratings = ratings.pivot_table(index=['userId'], columns=['title'], values='rating')
user_ratings = user_ratings.dropna(thresh=10, axis=1).fillna(0)

# print(user_ratings.head())

item_similarity_df = user_ratings.corr(method='pearson')
# print(item_similarity_df.head(50))
random_user = [("Toy Story (1995)", 5), ("22 Jump Street (2014)", 2), ("21 Jump Street (2012)", 1), ("Fast and the Furious, The (2001)", 5)]
similar_movies = pd.DataFrame()

for movie, rating in random_user:
    similar_movies = similar_movies.append(get_similar_movies(movie, rating), ignore_index=True)

print(similar_movies.sum().sort_values(ascending = False))