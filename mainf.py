from sklearn.neighbors import NearestNeighbors
from Preprocess import *

n = NearestNeighbors(n_neighbors=6, algorithm='ball_tree').fit(anime_features)
distances, indices = n.kneighbors(anime_features)
