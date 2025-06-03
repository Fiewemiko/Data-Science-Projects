#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data that ships with this repository.  When the notebook was
# originally converted to a script it contained an absolute path to the author's
# local machine which causes a FileNotFoundError when run elsewhere.  Use a
# path relative to this file so the script works regardless of where the
# repository lives.
DATA_PATH = os.path.join(os.path.dirname(__file__), "netflix_data.csv")
netflix = pd.read_csv(DATA_PATH)
#get rid of TV shows 
netflix_subset = netflix[netflix['type'] != "TV Show"] 
netflix_movies = netflix_subset[['title','country','genre','release_year',"duration"]]

shorter_movies = netflix_movies[netflix_movies['duration']< 60]

colors = []
for movie in netflix_movies['genre']:
    if movie == 'Children':
        colors.append('yellow')
    elif movie == 'Documentaries':
        colors.append('green')
    elif movie == 'Stand-Up':
        colors.append('blue')
    else:
        colors.append('red')


fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies['release_year'],netflix_movies['duration'],c=colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie duration by Year of Release')


