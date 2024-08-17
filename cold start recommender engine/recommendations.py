import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_courses():
    return pd.read_csv('courses.csv')

def recommend_courses(user_interest, skill_level):
    courses_df = load_courses()

    # Filter courses by skill level
    filtered_courses = courses_df[courses_df['skill-level'].str.lower() == skill_level.lower()]

    # Calculate similarity between user interest and course tags
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(filtered_courses['tags'])

    interest_vector = tfidf.transform([user_interest])
    similarity_scores = cosine_similarity(interest_vector, tfidf_matrix)

    # Get top 5 course indices
    course_indices = similarity_scores.argsort().flatten()[-5:]
    
    return filtered_courses.iloc[course_indices]
