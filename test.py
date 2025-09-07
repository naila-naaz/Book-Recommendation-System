# test.py

from recommender import recommend_books   # apne recommender.py se function import karo

# Ek sample book name do (dataset me jo ho)
book_name = "Harry Potter"

print(f"Testing recommendation system for: {book_name}\n")
recommendations = recommend_books(book_name)

# Output print karo
if recommendations:
    print("Recommended Books:")
    for book in recommendations:
        print("-", book)
else:
    print("No recommendations found. Check dataset or function.")
