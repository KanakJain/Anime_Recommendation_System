import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

anime = pd.read_csv('anime.csv')

# _________________________________________________________________________________________________
# There are a lot of data with unknown episodes
# Movies genre were given 1 episode
# OVA --> 2
anime.loc[(anime['genre'] == 'Movie') & (anime['episodes'] == 'Unknown'), 'episodes'] = '1'
anime.loc[(anime['genre'] == 'OVA') & (anime['episodes'] == 'Unknown'), 'episodes'] = '1'
# Animes with unknown episodes were given median of the episodes
anime['episodes'] = anime['episodes'].map(lambda x: np.nan if x == 'Unknown' else x)
anime['episodes'].fillna(anime['episodes'].median(), inplace=True)
# __________________________________________________________________________________________________

# Changing Type to Categorical Values
anime['type'] = pd.get_dummies(anime['type'])
anime['rating'] = anime['rating'].astype(float)
anime['rating'].fillna(anime['rating'].median(), inplace=True)
anime['members'] = anime['members'].astype(float)
anime_features = pd.concat([anime["genre"].str.get_dummies(sep=","),pd.get_dummies(anime[["type"]]),anime[["rating"]],anime[["members"]],anime["episodes"]], axis=1)
Scalar = MinMaxScaler()
anime_features = Scalar.fit_transform(anime_features)
