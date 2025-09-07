# Book Recommender - User Input Version

def recommend_books(genre):
    # Step 1: Different genre ke liye books ka dictionary
    book_data = {
        "fantasy": [
            "Harry Potter - J.K. Rowling",
            "The Hobbit - J.R.R. Tolkien",
            "Percy Jackson - Rick Riordan"
        ],
        "romance": [
            "Pride and Prejudice - Jane Austen",
            "The Fault in Our Stars - John Green",
            "Me Before You - Jojo Moyes"
        ],
        "classic": [
            "To Kill a Mockingbird - Harper Lee",
            "1984 - George Orwell",
            "Moby-Dick - Herman Melville"
        ],
        "mystery": [
            "Sherlock Holmes - Arthur Conan Doyle",
            "Gone Girl - Gillian Flynn",
            "The Girl with the Dragon Tattoo - Stieg Larsson"
        ]
    }
    
    # Step 2: Agar genre dictionary me hai to recommend karo
    if genre in book_data:
        print(f"\n📚 Recommended {genre.title()} Books for You:")
        for book in book_data[genre]:
            print(f"- {book}")
    else:
        print("\n❌ Sorry, we don't have recommendations for this genre yet.")


if __name__ == "__main__":
    # Step 3: User se input lo
    print("Welcome to Book Recommender!")
    print("Available genres: fantasy, romance, classic, mystery")
    user_choice = input("Enter a genre you like: ").lower()
    
    # Step 4: Function call
    recommend_books(user_choice)
