import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
##################################################

##Step 1: Read CSV File

#using pandas
df = pd.read_csv('movie_dataset.csv')
#  print(df.columns)

##Step 2: Select Features

features = ['keywords', 'cast', 'genres', 'director'] #In base of this atrributes

##Step 3: Create a column in DF which combines all selected features


for feature in features:
	df[feature] = df[feature].fillna('') #empty String -> truns NaN and float into string
def combine_features(row):
	return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']


df["combine_features"] = df.apply(combine_features, axis=1) #each row not columns

#print(df['combine_features'].head())

##Step 4: Create count matrix from this new combined column

cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combine_features"])


##Step 5: Compute the Cosine Similarity based on the count_matrix

cosine_sim = cosine_similarity(count_matrix)


movie_user_likes = "Avatar" #taken form the user

#We want to return index of movies in descending order


## Step 6: Get index of this movie from its title

#For keepig indexes we make a list of tuples (index, similarity_score)
#Then we sort on descending order

movie_index = get_index_from_title(movie_user_likes)


#enumerate = > gets tuple on index of list and value
similar_movies = list(enumerate(cosine_sim[movie_index]))

## Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_movies = sorted(similar_movies, key = lambda x:x[1], reverse=True) #sord by x[1], descending

## Step 8: Print titles of first 50 movies

i = 1
print("Movies: ")
for movie in sorted_similar_movies:
	print(i, sep="", end = "")
	print(".",get_title_from_index(movie[0]))
	i += 1
	if i > 50:
		break
