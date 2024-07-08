# Machine_Learning-Movie_Recommendation_System

The goal is to make a movie recommendation system using machine learning.
The system takes a movie input that a user has watched and then finds similar movies to recommend. 

In this program I have used a shord dummy dataset of a bunch of movies and an user-input example.

Libraries Used:
- Pandas (for reading the .csv file)
- sklearn (for implementing CountVectorizler and cosine_similarity)

After reading the dataset, we select some movie features that are important for the application such as: keywords, cast, genres, director.
Based on those features we have a set of the movie index and the features.

Using CountVectorizer we then make a matrix of that keeps track on how many times a "word"(feature) has appeared per movie.

For this ceartain scenario it is best fit to use Cosine Similarities, when we treat each movie with its features as a vector and find how much a movie is similar to others based on angular distance. The math behind this is shown in the image below:

![image](https://github.com/JonKuqi/Machine-Learning---Movie-Recommendation-System/assets/116517705/207830f6-be31-47e2-bc0e-245680007c62)

After finding similarities we take the user input ex: "Avatar" and put all the similar movies in a list in descending order.
![image](https://github.com/JonKuqi/Machine-Learning---Movie-Recommendation-System/assets/116517705/726541c6-c9ad-48bd-bbfc-3151370c54a3)

Avatar has cosine similarity with itself equal to 1 so, as to be expected it is first. In a real world application we would exclude the same movie for appearing in recommendations.

