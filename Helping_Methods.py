from mainf import *
from Preprocess import *


def get_index_from_name(name):
    return anime[anime['name'] == name].index.tolist()[0]


all_anime = list(anime.name.values)


def get_id_from_partial_name(partial):
    for name in all_anime:
        if partial in name:
            print(name, all_anime.index(name))


def get_similar(q=None, id=None):
    if id:
        for id in indices[id][1:]:
            print(anime.ix[id]['name'])
    if q:
        found_id = get_index_from_name(q)
        for id in indices[found_id][1:]:
            print(anime.ix[id]['name'])


print(get_similar(q='Doraemon'))
