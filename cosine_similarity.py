#Finding Theta in two vectors

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


#Two sentences
text = ["London Paris London", "Paris Paris London"]

#Counting Vectorizor - Class for counting words in a matrix
cv = CountVectorizer()

#Method for transformin text into word count
countMatrix = cv.fit_transform(text)

print(countMatrix.toarray())

#Find the cosines similarity

similarityScore = cosine_similarity(countMatrix)

print(similarityScore)


