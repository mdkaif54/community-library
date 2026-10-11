import psycopg2

conn = psycopg2.connect(database = "library2", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "post",
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS History (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    publisher VARCHAR(100),
    genre VARCHAR(100));
""")

bookData = [
        ("All the Light We Cannot See", "Anthony Doerr", "Scribner", "Historical Fiction / War Literature"),
        ("The Pillars of the Earth", "Ken Follett", "William Morrow & Company ", "Historical Fiction / Epic"),
        ("Pachinko", "Min Jin Lee", "Grand Central Publishing", "Historical Fiction / Family Saga"),
        ("The Kite Runner", "Khaled Hosseini", "Riverhead Books", "Historical Fiction / Modern Literature")    
]
cursor.execute(
    "INSERT INTO History (title, author, publisher, genre) VALUES (%s, %s, %s, %s)",
    bookData          
)

cursor.execute("SELECT * FROM History;")
conn.commit()

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()