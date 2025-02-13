import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("Data/data.csv")
df = df.drop(columns=["id", "release_date"])


# Normalize numerical features
scaler = StandardScaler()
numeric_features = ['acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness',
                    'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo', 'valence', 'year']
df[numeric_features] = scaler.fit_transform(df[numeric_features])

song_features = df[numeric_features].values

# Function to recommend songs
def recommend_songs(song_name, n_recommendations=5):
    song_name = song_name.lower()
    df['name'] = df['name'].str.lower()

    if song_name not in df['name'].values:
        return "Song not found in the dataset."
    
    song_idx = df[df['name'] == song_name].index[0]
    song_vector = song_features[song_idx].reshape(1, -1)
    similarities = cosine_similarity(song_vector, song_features)[0]
    
    recommended_indices = similarities.argsort()[-(n_recommendations+1):-1][::-1]
    recommended_songs = df.iloc[recommended_indices][['name']]
    return recommended_songs.to_dict()
