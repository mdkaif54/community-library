import bookrepo

def get_all_books():
    bookList = bookrepo.get_all_books()
    for row in bookList:
        print(row)  

get_all_books()