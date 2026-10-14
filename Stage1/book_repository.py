import psycopg2

def get_connection():
    return psycopg2.connect(
        database = "library2",
        host = "localhost",
        user = "postgres",
        password = "post"
    )


def get_all_books():
    db_connection = None
    cursor = None
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()
        cursor.execute(
            "SELECT * FROM History;"
        )
        rows = cursor.fetchall()
        return rows

    except Exception as e:
        print(f"Error: {Exception}")
        return []
    
    finally:
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()


def create_book(title, author, publisher, genre):
    db_connection = None
    cursor = None
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()
        query = """
                INSERT INTO History(title, author, publisher, genre) 
                VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (title, author, publisher, genre))
        db_connection.commit()
        return True
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        db_connection.close()


def get_book(book_id):
    db_connection = None
    cursor = None
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()
        cursor.execute(
            "SELECT * FROM History WHERE id = %s;",
            (book_id,)
        )
        book = cursor.fetchone()
        return book

    except Exception as e:
        print(f"error: {e}")

    finally:
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()


def update_book(book_id, title, author, publisher, genre):
    db_connection = None
    cursor = None
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()
        parameters = (title, author, publisher, genre, book_id)
        cursor.execute(
            """UPDATE History
               SET title = %s, author = %s, publisher = %s, genre = %s
               WHERE id = %s;""",
               parameters
        )
        if cursor.rowcount == 0:
            print(f"Update failed: Book ID{book_id} does not exist.")
            return False
        db_connection.commit()
        print(f"Book ID {book_id} updated successfully.")
        return True
   
    except Exception as e:
        print(f"error: {e}")
        if db_connection:
            db_connection.rollback()
        return False

    finally:
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()


def delete_book(book_id):
    db_connection = None
    cursor = None
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()
        cursor.execute(
            "DELETE FROM History WHERE id = %s;",
            (book_id,)
        )
        if cursor.rowcount == 0:
            print(f"No book foun with ID:{book_id}")
            return False

        db_connection.commit()
        print(f"Book with ID:{book_id} Deleted successfully")
        return True

    except Exception as e:
        print(f"error: {e}")
        if db_connection:
            db_connection.rollback()
        return False

    finally:
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()