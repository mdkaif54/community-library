import psycopg2

def get_connection():
    return psycopg2.connect(
        database = "library2",
        host = "localhost",
        user = "postgres",
        password = "post"
    )


def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM History"
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

