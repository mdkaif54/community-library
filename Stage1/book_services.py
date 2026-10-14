import book_repository

def get_all_books():
    return book_repository.get_all_books()

print(get_all_books())

def create_book(title, author, publisher, genre):
    return book_repository.create_book(title, author, publisher, genre)

# print(create_book("Atomic Habits", "James Clear", "Penguin", "Self-Help"))   # it will print True

def get_book(book_id):
    return book_repository.get_book(book_id)

# print(get_book(1))

def update_book(book_id, title, author, publisher, genre):
    return book_repository.update_book(
        book_id, title, author, publisher, genre
    )

# print(update_book(6, "The Hobbit", "J.R.R. Tolkien", "Allen & Unwin", "Fantasy"))

def delete_book(book_id):
    return book_repository.delete_book(book_id)

# print(delete_book(2))