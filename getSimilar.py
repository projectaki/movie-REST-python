from datetime import datetime
import pandas as pd
import json
import numpy as np
import pickle
import sys
from sklearn.feature_extraction.text import CountVectorizer
from numpy import dot
from numpy.linalg import norm

def fast_cosine(a,b):
    return dot(a, b)/(norm(a)*norm(b))

def get_index_from_movie_id(movie_id, df):
        return df[df["id"] == int(movie_id)].index[0]

def findSimilar(movie_id):
    try:
        with open ('movies', 'rb') as fp:
            movies = pickle.load(fp)
            
            movie_df = pd.DataFrame(movies, columns =[ 'id', "original_title","overview"])

        with open ('transformedOverview', 'rb') as fp:
            transformed_overview = pickle.load(fp)
            
        vectorizer = CountVectorizer().fit_transform(transformed_overview)
        vectors = vectorizer.toarray()

        test_query = vectors[get_index_from_movie_id(movie_id, movie_df)]

        cosines = []

        for i,item in enumerate(vectors):
            cosines.append([fast_cosine(test_query, item), i])

        sorted_cosines = sorted(cosines, reverse=True)

        results = []

        for i in range(1,15):
            results.append({"id": movie_df["id"][sorted_cosines[i][1]]})

        for item in results:
            item["id"] = int(item["id"])

        response = json.dumps(results)

        return response
    except:
        return "No such id"
    