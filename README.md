# Project: Movie Recommender System Using Machine Learning!

<img src="demo/6.jpeg" alt="workflow" width="70%">

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

# Types of Recommendation System :

### 1 ) Content Based :

- Content-based systems, which use characteristic information and takes item attriubutes into consideration .

- Twitter , Youtube .

- Which music you are listening , what singer are you watching . Form embeddings for the features .
	
- User specific actions or similar items reccomendation .
	
- It will create a vector of it .
	
- These systems make recommendations using a user's item and profile features. They hypothesize that if a user was interested in an item in the past, they will once again be interested in it in the future
	
- One issue that arises is making obvious recommendations because of excessive specialization (user A is only interested in categories B, C, and D, and the system is not able to recommend items outside those categories, even though they could be interesting to them).

### 2 ) Collaborative Based :
		
- Collaborative filtering systems, which are based on user-item interactions.
	
- Clusters of users with same ratings , similar users .
	
- Book recommendation , so use cluster mechanism .
	
- We take only one parameter , ratings or comments .
	
- In short, collaborative filtering systems are based on the assumption that if a user likes item A and another user likes the same item A as well as another item, item B, the first user could also be interested in the second item . 
	
- Issues are :

	- User-Item nXn matrix , so computationally expensive .

	- Only famous items will get reccomended .

	- New items might not get reccomended at all .   

### 3 ) Hybrid Based :
	
- Hybrid systems, which combine both types of information with the aim of avoiding problems that are generated when working with just one kind.

- Combination of both and used now a days .

- Uses : word2vec , embedding .           

# About this project:

# Movie Recommender System

The Movie Recommender System project aims to provide personalized movie recommendations to users based on the content of movies. By analyzing movie attributes such as genres, keywords, cast, and crew, this system helps users discover movies that are similar to the ones they enjoy.

## Problem Statement

The goal of the Movie Recommender System project is to develop an intelligent recommendation engine that suggests movies to users based on their preferences. This system leverages the content of movies, including genres, keywords, and cast, to provide accurate and relevant movie suggestions.


# Demo:

<img src="demo/1.png" alt="workflow" width="70%">

<img src="demo/2.png" alt="workflow" width="70%">

<img src="demo/3.png" alt="workflow" width="70%">


### Dataset has been used:

* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## Dataset Description

The dataset used for this project includes a collection of movies, each described by various attributes such as genres, keywords, cast, crew, and overview. The relevant columns for recommendation are 'movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', and 'crew'. The following preprocessing steps were applied to the dataset:

- Selection of Important Columns
- Handling Null Values
- Elimination of Duplicate Entries
- Text Preprocessing:
  - Removing Spaces
  - Converting Text to Lowercase
  - Combining Text Columns into One (tags)

## Architecture of the Project

The project follows these steps:

### 1. Data Preprocessing

- Selecting relevant columns
- Handling missing values and duplicates
- Preprocessing text data

### 2. Text Vectorization

- Converting text data into numerical vectors using techniques like TF-IDF (Term Frequency-Inverse Document Frequency)

### 3. Cosine Similarity

- Calculating the cosine similarity between vectors to measure the similarity between movies
- Ensuring similarity despite variations in word forms (e.g., "love" and "loved")

### 4. Model Building

- Creating a recommendation model using the cosine similarity scores

### 5. Web Application

- Developing a user-friendly web application using Streamlit
- Input: Movie title
- Output: Recommended movies based on content similarity

# Concept used to build the model.pkl file : cosine_similarity

1 . Cosine Similarity is a metric that allows you to measure the similarity of the documents.

2 . In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

3 . Finally, Once we have vectors, We can call cosine_similarity() by passing both vectors. It will calculate the cosine similarity between these two.

4 . It will be a value between [0,1]. If it is 0 then both vectors are complete different. But in the place of that if it is 1, It will be completely similar.

## Usage

1. Prepare or obtain the movie dataset with relevant columns.
2. Execute the Data Preprocessing steps to clean and preprocess the dataset.
3. Perform Text Vectorization to convert movie attributes into numerical vectors.
4. Calculate Cosine Similarity scores between movie vectors.
5. Build the recommendation model and save it in a pickle format.
6. Run the web application using Streamlit to receive movie recommendations based on user input.




