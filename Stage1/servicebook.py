import bookrepo

def get_all_books():
    return bookrepo.get_all_books()

# print(get_all_boeoks())

def create_book(title, author, publisher, genre):
    return bookrepo.create_book(title, author, publisher, genre)

# print(create_book("Atomic Habits", "James Clear", "Penguin", "Self-Help"))   # it will print True

def get_book(book_id):
    return bookrepo.get_book(book_id)

print(get_book(1))
