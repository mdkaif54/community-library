import psycopg2

def get_connection():
    return psycopg2.connect(
        database = "library2",
        host = "localhost",
        user = "postgres",
        password = "post"
    )


def get_all_books():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM History"
        )
        rows = cursor.fetchall()
        return rows

    except Exception as e:
        print(f"Error: {Exception}")
        return []
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



def create_book(title, author, publisher, genre):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
                INSERT INTO History(title, author, publisher, genre) 
                VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (title, author, publisher, genre))
        conn.commit()
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return []
    
    finally:
        cursor.close()
        conn.close()


def get_book(book_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
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
        if conn:
            conn.close()

