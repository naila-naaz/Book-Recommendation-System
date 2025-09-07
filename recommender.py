# recommender.py
# Simple Book Recommendation System

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Dataset load karo
books = pd.read_csv("books.csv")

# Step 2: Features combine karo (title + author + genre)
books["features"] = books["title"] + " " + books["author"] + " " + books["genre"]

# Step 3: TF-IDF se vector banao
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(books["features"])

# Step 4: Cosine Similarity calculate karo
similarity = cosine_similarity(feature_vectors)

def recommend_book(book_title):
    # Convert user input to lowercase
    book_title = book_title.lower()

    # Find closest match (case-insensitive + partial)
    matches = books[books['title'].str.lower().str.contains(book_title)]

    if matches.empty:
        return ["Book not found in database. Try another."]

    # Use the first matching book
    index = matches.index[0]


    scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommended = []
    for i in sorted_scores[1:6]:
        recommended.append(books.iloc[i[0]]["title"])
    return recommended

# Step 5: User Interaction
print("📚 Welcome to the Book Recommender!")
while True:
    book_name = input("\nEnter a book title (or 'exit' to quit): ")
    if book_name.lower() == "exit":
        print("Goodbye!")
        break

    recommendations = recommend_book(book_name)
    print("✨ Recommended Books:")
    for rec in recommendations:
        print(" -", rec)
